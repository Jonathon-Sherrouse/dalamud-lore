using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace NpcDialogueLinks.Atlas;

/// <summary>Semantic validation for schema v2 (docs/atlas/schema.md). Collects every error rather than stopping at the first.</summary>
internal static class AtlasValidator
{
    public const int MaxIdLength = 64;
    public const int MaxLabelLength = 80;
    public const int MaxSummaryLength = 1200;
    public const int MaxCitationTitleLength = 200;
    public const int MaxUrlLength = 2048;
    public const int MaxPresentations = 512;

    /// <summary>The highest game icon number a portrait may name (the game's icon folders stop below a million).</summary>
    public const uint MaxGameIcon = 999_999;

    /// <summary>The smallest crop, as a fraction of the image's shorter side, so a portrait is never a few stray pixels.</summary>
    public const double MinCropSize = 0.1;
    public const int MaxAliases = 8;
    public const int MaxCitations = 8;
    public const int MaxGameQuestIds = 8;
    public const int MaxCastMembers = 10;
    private const int MaxReportedErrors = 100;

    private static readonly Regex IdPattern = new("^[a-z0-9]+(-[a-z0-9]+)*$", RegexOptions.CultureInvariant);

    private static readonly AtlasContentView[] AllViews = { AtlasContentView.MainStory, AtlasContentView.MainAndOptional };

    public static AtlasLoadResult Build(AtlasFileDto file, AtlasValidationMode mode)
    {
        var errors = new ErrorSink();

        // Bounds first: refuse oversized collections before doing per-record work.
        CheckCount(errors, "$.checkpoints", file.Checkpoints, 1, AtlasLoader.MaxCheckpoints);
        CheckCount(errors, "$.relationshipTypes", file.RelationshipTypes, 1, AtlasLoader.MaxRelationshipTypes);
        CheckCount(errors, "$.entities", file.Entities, 1, AtlasLoader.MaxEntities);
        CheckCount(errors, "$.relationships", file.Relationships ?? new List<AtlasRelationshipDto?>(), 0, AtlasLoader.MaxRelationships);
        CheckCount(errors, "$.arcs", file.Arcs ?? new List<AtlasArcDto?>(), 0, AtlasLoader.MaxArcs);
        if (errors.HasErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var checkpoints = BuildCheckpoints(errors, file.Checkpoints!, out var checkpointPaths);
        CheckGameQuestCoverage(errors, checkpoints, checkpointPaths);
        var types = BuildTypes(errors, file.RelationshipTypes!);
        if (errors.HasStructuralErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var orderById = checkpoints.ToDictionary(c => c.Id, c => c.Order, StringComparer.Ordinal);
        var citationRegistry = new Dictionary<string, (int AvailableAt, AtlasScope Scope, string Path)>(StringComparer.Ordinal);
        var context = new Context(errors, orderById, checkpoints.Count, mode, citationRegistry, checkpoints);

        var entities = BuildEntities(context, file.Entities!);
        if (errors.HasStructuralErrors)
        {
            // Relationship checks depend on a sound entity set.
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var relationships = BuildRelationships(context, file.Relationships ?? new List<AtlasRelationshipDto?>(), types, entities);
        var arcs = errors.HasStructuralErrors
            ? new List<AtlasArc>()
            : BuildArcs(context, file.Arcs ?? new List<AtlasArcDto?>(), types, entities, relationships);
        if (errors.HasErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        return AtlasLoadResult.Ok(new AtlasDataset(checkpoints, types, entities.Values.ToList(), relationships, arcs));
    }

    private sealed record Context(
        ErrorSink Errors,
        IReadOnlyDictionary<string, int> OrderById,
        int CheckpointCount,
        AtlasValidationMode Mode,
        Dictionary<string, (int AvailableAt, AtlasScope Scope, string Path)> CitationRegistry,
        IReadOnlyList<AtlasCheckpoint> Checkpoints);

    private static List<AtlasCheckpoint> BuildCheckpoints(ErrorSink errors, List<AtlasCheckpointDto?> dtos, out List<string> paths)
    {
        var result = new List<AtlasCheckpoint>();
        paths = new List<string>();
        var seen = new HashSet<string>(StringComparer.Ordinal);
        for (var i = 0; i < dtos.Count; i++)
        {
            var path = $"$.checkpoints[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "Checkpoint is null.");
                continue;
            }

            var before = errors.Count;
            var id = RequireId(errors, $"{path}.id", dto.Id);
            var label = RequireText(errors, $"{path}.label", dto.Label, MaxLabelLength);
            var questTitle = dto.QuestTitle is null ? null : RequireText(errors, $"{path}.questTitle", dto.QuestTitle, MaxLabelLength);
            var gameQuestIds = ParseGameQuestIds(errors, $"{path}.gameQuestIds", dto.GameQuestIds);
            if (dto.ContiguousWithPrevious == true && result.Count == 0)
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}.contiguousWithPrevious", "The first checkpoint has no previous step.");
            }

            if (errors.Count != before)
            {
                continue;
            }

            if (!seen.Add(id!))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate checkpoint id.");
                continue;
            }

            paths.Add(path);
            result.Add(new AtlasCheckpoint(id!, label!, result.Count)
            {
                Milestone = dto.Milestone ?? false,
                QuestTitle = questTitle,
                ContiguousWithPrevious = dto.ContiguousWithPrevious ?? false,
                GameQuestIds = gameQuestIds,
            });
        }

        return result;
    }

    private static Dictionary<string, AtlasRelationshipType> BuildTypes(ErrorSink errors, List<AtlasRelationshipTypeDto?> dtos)
    {
        var result = new Dictionary<string, AtlasRelationshipType>(StringComparer.Ordinal);
        for (var i = 0; i < dtos.Count; i++)
        {
            var path = $"$.relationshipTypes[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "Relationship type is null.");
                continue;
            }

            var id = RequireId(errors, $"{path}.id", dto.Id);
            var outgoing = RequireText(errors, $"{path}.outgoingLabel", dto.OutgoingLabel, MaxLabelLength);
            var incoming = RequireText(errors, $"{path}.incomingLabel", dto.IncomingLabel, MaxLabelLength);
            if (dto.Symmetric is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}.symmetric", "symmetric is required.");
            }

            if (id is null || outgoing is null || incoming is null || dto.Symmetric is null)
            {
                continue;
            }

            if (dto.Symmetric.Value && !string.Equals(outgoing, incoming, StringComparison.Ordinal))
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}.incomingLabel", "A symmetric type must use the same label in both directions.");
                continue;
            }

            if (!result.TryAdd(id, new AtlasRelationshipType(id, outgoing, incoming, dto.Symmetric.Value)))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate relationship type id.");
            }
        }

        return result;
    }

    private static Dictionary<string, AtlasEntity> BuildEntities(Context context, List<AtlasEntityDto?> dtos)
    {
        var errors = context.Errors;
        var result = new Dictionary<string, AtlasEntity>(StringComparer.Ordinal);
        for (var i = 0; i < dtos.Count; i++)
        {
            var path = $"$.entities[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "Entity is null.");
                continue;
            }

            var before = errors.Count;
            var id = RequireId(errors, $"{path}.id", dto.Id);
            var category = ParseCategory(errors, $"{path}.category", dto.Category);
            var portrait = dto.Portrait is null ? null : BuildPortrait(context, $"{path}.portrait", dto.Portrait);
            var presentations = new List<AtlasPresentation>();
            if (dto.Presentations is null || dto.Presentations.Count == 0 || dto.Presentations.Count > MaxPresentations)
            {
                errors.Add(AtlasErrorCode.BoundsExceeded, $"{path}.presentations", $"An entity needs 1–{MaxPresentations} presentations.");
            }
            else
            {
                for (var p = 0; p < dto.Presentations.Count; p++)
                {
                    var presentation = BuildPresentation(context, $"{path}.presentations[{p}]", dto.Presentations[p]);
                    if (presentation is not null)
                    {
                        presentations.Add(presentation);
                    }
                }
            }

            if (errors.Count != before)
            {
                continue;
            }

            if (result.ContainsKey(id!))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate entity id.");
                continue;
            }

            var entity = new AtlasEntity(id!, category!.Value, presentations) { Portrait = portrait };
            CheckPresentationOverlap(errors, path, presentations);
            CheckOptionalBoundaries(errors, path, presentations, context.CheckpointCount);
            CheckOptionalPersistence(errors, path, entity, context.CheckpointCount);
            CheckVisibilityContiguous(errors, path, entity, context.CheckpointCount);
            result.Add(entity.Id, entity);
        }

        return result;
    }

    /// <summary>A portrait: a game icon number, a crop inside the image, and its own review (NDL-011).</summary>
    private static AtlasPortrait? BuildPortrait(Context context, string path, AtlasPortraitDto dto)
    {
        var errors = context.Errors;
        var before = errors.Count;
        if ((dto.GameIcon is null) == (dto.Asset is null))
        {
            errors.Add(AtlasErrorCode.InvalidField, path, "A portrait needs exactly one of gameIcon and asset.");
        }

        if (dto.GameIcon is { } icon && (icon == 0 || icon > MaxGameIcon))
        {
            errors.Add(AtlasErrorCode.InvalidField, $"{path}.gameIcon", $"gameIcon must be a game icon number from 1 to {MaxGameIcon}.");
        }

        if (dto.Asset is { } asset && (asset.Length is < 1 or > 100
            || !asset.All(c => c is (>= 'a' and <= 'z') or (>= '0' and <= '9') or '-')))
        {
            errors.Add(AtlasErrorCode.InvalidField, $"{path}.asset", "asset must be a lowercase image key.");
        }

        var crop = dto.Crop;
        if (crop?.X is not { } x || crop.Y is not { } y || crop.Size is not { } size
            || !double.IsFinite(x) || !double.IsFinite(y) || !double.IsFinite(size)
            || x < 0 || x > 1 || y < 0 || y > 1 || size < MinCropSize || size > 1)
        {
            errors.Add(AtlasErrorCode.InvalidField, $"{path}.crop", $"crop needs x and y from 0 to 1 and a size from {MinCropSize} to 1.");
        }

        var review = ParseReview(errors, $"{path}.review", dto.Review, context.Mode);
        return errors.Count != before
            ? null
            : new AtlasPortrait(dto.GameIcon.GetValueOrDefault(), crop!.X!.Value, crop.Y!.Value, crop.Size!.Value, review!.Value) { Asset = dto.Asset };
    }

    private static AtlasPresentation? BuildPresentation(Context context, string path, AtlasPresentationDto? dto)
    {
        var errors = context.Errors;
        if (dto is null)
        {
            errors.Add(AtlasErrorCode.InvalidField, path, "Presentation is null.");
            return null;
        }

        var before = errors.Count;
        var interval = ParseInterval(errors, path, dto.ValidFrom, dto.ValidUntil, context.OrderById);
        var scope = ParseScope(errors, $"{path}.scope", dto.Scope);
        var name = RequireText(errors, $"{path}.name", dto.Name, MaxLabelLength);
        var summary = RequireText(errors, $"{path}.summary", dto.Summary, MaxSummaryLength);
        var review = ParseReview(errors, $"{path}.review", dto.Review, context.Mode);
        var aliases = ParseAliases(errors, $"{path}.aliases", dto.Aliases, name);
        var citations = interval is not null && scope is not null
            ? ParseCitations(context, $"{path}.citations", dto.Citations, interval, scope.Value)
            : null;

        if (errors.Count != before)
        {
            return null;
        }

        return new AtlasPresentation(interval!, scope!.Value, name!, aliases, summary!, citations!, review!.Value);
    }

    private static List<AtlasRelationship> BuildRelationships(
        Context context,
        List<AtlasRelationshipDto?> dtos,
        IReadOnlyDictionary<string, AtlasRelationshipType> types,
        IReadOnlyDictionary<string, AtlasEntity> entities)
    {
        var errors = context.Errors;
        var result = new List<AtlasRelationship>();
        var paths = new List<string>();
        var ids = new HashSet<string>(StringComparer.Ordinal);
        for (var i = 0; i < dtos.Count; i++)
        {
            var path = $"$.relationships[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "Relationship is null.");
                continue;
            }

            var before = errors.Count;
            var id = RequireId(errors, $"{path}.id", dto.Id);
            var source = RequireReference(errors, $"{path}.source", dto.Source, entities);
            var target = RequireReference(errors, $"{path}.target", dto.Target, entities);
            AtlasRelationshipType? type = null;
            var typeId = RequireId(errors, $"{path}.type", dto.Type);
            if (typeId is not null && !types.TryGetValue(typeId, out type))
            {
                errors.Add(AtlasErrorCode.UnknownReference, $"{path}.type", "Unknown relationship type.");
            }

            var interval = ParseInterval(errors, path, dto.ValidFrom, dto.ValidUntil, context.OrderById);
            var scope = ParseScope(errors, $"{path}.scope", dto.Scope);
            var review = ParseReview(errors, $"{path}.review", dto.Review, context.Mode);
            var citations = interval is not null && scope is not null
                ? ParseCitations(context, $"{path}.citations", dto.Citations, interval, scope.Value)
                : null;
            var endCitations = interval is not null && scope is not null
                ? ParseEndCitations(context, $"{path}.endCitations", dto.EndCitations, interval, scope.Value)
                : null;
            if (errors.Count != before)
            {
                continue;
            }

            if (!ids.Add(id!))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate relationship id.");
                continue;
            }

            if (string.Equals(source!.Id, target!.Id, StringComparison.Ordinal))
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "A relationship cannot connect an entity to itself.");
                continue;
            }

            var relationship = new AtlasRelationship(id!, source.Id, type!.Id, target.Id, interval!, scope!.Value, citations!, review!.Value)
            {
                EndCitations = endCitations!,
            };
            CheckEndpointsVisible(errors, path, relationship, source, target, context.CheckpointCount);
            result.Add(relationship);
            paths.Add(path);
        }

        CheckDuplicatePairs(errors, result, paths, types);
        CheckEndingsAreReal(errors, result, paths);
        return result;
    }

    private static void CheckPresentationOverlap(ErrorSink errors, string path, List<AtlasPresentation> presentations)
    {
        for (var a = 0; a < presentations.Count; a++)
        {
            for (var b = a + 1; b < presentations.Count; b++)
            {
                if (presentations[a].Scope == presentations[b].Scope && presentations[a].Interval.Overlaps(presentations[b].Interval))
                {
                    errors.Add(AtlasErrorCode.OverlappingPresentation, $"{path}.presentations[{b}]", $"Overlaps presentation {a} in the same scope.");
                }
            }
        }
    }

    /// <summary>An optional presentation sits inside one main presentation, or only where no main presentation exists.</summary>
    private static void CheckOptionalBoundaries(ErrorSink errors, string path, List<AtlasPresentation> presentations, int checkpointCount)
    {
        for (var o = 0; o < presentations.Count; o++)
        {
            var optional = presentations[o];
            if (optional.Scope != AtlasScope.Optional)
            {
                continue;
            }

            int? coveringMain = null;
            var first = true;
            for (var order = 0; order < checkpointCount; order++)
            {
                if (!optional.Interval.Contains(order))
                {
                    continue;
                }

                var mainIndex = -1;
                for (var m = 0; m < presentations.Count; m++)
                {
                    if (presentations[m].Scope == AtlasScope.Main && presentations[m].Interval.Contains(order))
                    {
                        mainIndex = m;
                        break;
                    }
                }

                if (first)
                {
                    coveringMain = mainIndex;
                    first = false;
                }
                else if (coveringMain != mainIndex)
                {
                    errors.Add(AtlasErrorCode.OptionalSpansMainBoundary, $"{path}.presentations[{o}]", "An optional presentation must sit inside one main presentation, or cover only checkpoints without one.");
                    break;
                }
            }
        }
    }

    /// <summary>Once optional knowledge starts, it covers every later checkpoint where the entity is visible.</summary>
    private static void CheckOptionalPersistence(ErrorSink errors, string path, AtlasEntity entity, int checkpointCount)
    {
        var started = false;
        for (var order = 0; order < checkpointCount; order++)
        {
            var optionalHere = entity.Presentations.Any(p => p.Scope == AtlasScope.Optional && p.Interval.Contains(order));
            if (optionalHere)
            {
                started = true;
                continue;
            }

            if (started && entity.IsVisibleAt(order, AtlasContentView.MainAndOptional))
            {
                errors.Add(AtlasErrorCode.OptionalEndsEarly, path, "Optional presentations must continue while the entity stays visible.");
                return;
            }
        }
    }

    /// <summary>No checkpoint between an entity's first and last visible checkpoint may be missing, in either view.</summary>
    private static void CheckVisibilityContiguous(ErrorSink errors, string path, AtlasEntity entity, int checkpointCount)
    {
        foreach (var view in AllViews)
        {
            var state = 0; // 0 = not yet visible, 1 = in visible run, 2 = run ended
            for (var order = 0; order < checkpointCount; order++)
            {
                var visible = entity.IsVisibleAt(order, view);
                if (visible && state == 2)
                {
                    errors.Add(AtlasErrorCode.VisibilityGap, path, $"The entity disappears and reappears in the {view} view.");
                    break;
                }

                state = visible ? 1 : state == 1 ? 2 : state;
            }
        }
    }

    private static void CheckEndpointsVisible(ErrorSink errors, string path, AtlasRelationship relationship, AtlasEntity source, AtlasEntity target, int checkpointCount)
    {
        foreach (var view in AllViews)
        {
            for (var order = 0; order < checkpointCount; order++)
            {
                if (relationship.IsVisibleAt(order, view) && (!source.IsVisibleAt(order, view) || !target.IsVisibleAt(order, view)))
                {
                    errors.Add(AtlasErrorCode.EndpointNotVisible, path, $"An endpoint is hidden at checkpoint {order} in the {view} view.");
                    return;
                }
            }
        }
    }

    /// <summary>
    /// End evidence shows only on a Changes "ended" row, and Changes diffs by (source, type, target). A record whose
    /// triple carries straight on at its validUntil, in every view where the record was visible, never produces that row,
    /// so its end citations could never be shown. A main ending continued only by optional content still shows in the
    /// main-story view.
    /// </summary>
    private static void CheckEndingsAreReal(ErrorSink errors, List<AtlasRelationship> relationships, List<string> paths)
    {
        for (var a = 0; a < relationships.Count; a++)
        {
            var ending = relationships[a];
            if (ending.EndCitations.Count == 0 || ending.Interval.UntilOrder is not { } until)
            {
                continue;
            }

            var continued = relationships.Any(next =>
                !ReferenceEquals(next, ending)
                && next.SourceId == ending.SourceId && next.TypeId == ending.TypeId && next.TargetId == ending.TargetId
                && next.Interval.Contains(until)
                && (next.Scope == AtlasScope.Main || ending.Scope == AtlasScope.Optional));
            if (continued)
            {
                errors.Add(AtlasErrorCode.EndCitationOutOfRange, $"{paths[a]}.endCitations", "The same relationship continues at validUntil, so it never ends and its end evidence could never be shown.");
            }
        }
    }

    private static void CheckDuplicatePairs(ErrorSink errors, List<AtlasRelationship> relationships, List<string> paths, IReadOnlyDictionary<string, AtlasRelationshipType> types)
    {
        for (var a = 0; a < relationships.Count; a++)
        {
            for (var b = a + 1; b < relationships.Count; b++)
            {
                var x = relationships[a];
                var y = relationships[b];
                if (!string.Equals(x.TypeId, y.TypeId, StringComparison.Ordinal))
                {
                    continue;
                }

                var same = x.SourceId == y.SourceId && x.TargetId == y.TargetId;
                var reversed = x.SourceId == y.TargetId && x.TargetId == y.SourceId;
                if (same && x.Interval.Overlaps(y.Interval))
                {
                    errors.Add(AtlasErrorCode.DuplicateRelationship, paths[b], $"Duplicates {paths[a]} over an overlapping interval.");
                }
                else if (reversed && types[x.TypeId].Symmetric)
                {
                    errors.Add(AtlasErrorCode.ReverseSymmetricDuplicate, paths[b], $"Reverses symmetric relationship {paths[a]}; store it once, in one direction.");
                }
            }
        }
    }

    private static AtlasInterval? ParseInterval(ErrorSink errors, string path, string? from, string? until, IReadOnlyDictionary<string, int> orderById)
    {
        if (from is null || !orderById.TryGetValue(from, out var fromOrder))
        {
            errors.Add(from is null ? AtlasErrorCode.InvalidField : AtlasErrorCode.UnknownReference, $"{path}.validFrom", "validFrom must name a known checkpoint.");
            return null;
        }

        if (until is null)
        {
            return new AtlasInterval(fromOrder, null);
        }

        if (!orderById.TryGetValue(until, out var untilOrder))
        {
            errors.Add(AtlasErrorCode.UnknownReference, $"{path}.validUntil", "validUntil must name a known checkpoint or be null.");
            return null;
        }

        if (untilOrder <= fromOrder)
        {
            errors.Add(AtlasErrorCode.InvalidInterval, $"{path}.validUntil", "validUntil must be later than validFrom.");
            return null;
        }

        return new AtlasInterval(fromOrder, untilOrder);
    }

    private static List<string> ParseAliases(ErrorSink errors, string path, List<string?>? dtos, string? name)
    {
        var aliases = new List<string>();
        if (dtos is null)
        {
            return aliases;
        }

        if (dtos.Count > MaxAliases)
        {
            errors.Add(AtlasErrorCode.BoundsExceeded, path, $"At most {MaxAliases} aliases are allowed.");
            return aliases;
        }

        var seen = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        if (name is not null)
        {
            seen.Add(name);
        }

        for (var a = 0; a < dtos.Count; a++)
        {
            var alias = RequireText(errors, $"{path}[{a}]", dtos[a], MaxLabelLength);
            if (alias is null)
            {
                continue;
            }

            if (!seen.Add(alias))
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}[{a}]", "Aliases must be unique and differ from the name.");
                continue;
            }

            aliases.Add(alias);
        }

        return aliases;
    }

    private static List<AtlasCitation>? ParseCitations(Context context, string path, List<AtlasCitationDto?>? dtos, AtlasInterval recordInterval, AtlasScope recordScope)
    {
        if (dtos is null || dtos.Count == 0 || dtos.Count > MaxCitations)
        {
            context.Errors.Add(AtlasErrorCode.BoundsExceeded, path, $"1–{MaxCitations} citations are required.");
            return null;
        }

        return ParseCitationList(context, path, dtos, recordInterval, recordScope, isEnding: false);
    }

    /// <summary>
    /// Optional ending evidence (schema v2): each source must become available after the record starts and no later
    /// than when it ends, so it can only ever appear once the ending is player knowledge.
    /// </summary>
    private static List<AtlasCitation>? ParseEndCitations(Context context, string path, List<AtlasCitationDto?>? dtos, AtlasInterval recordInterval, AtlasScope recordScope)
    {
        if (dtos is null || dtos.Count == 0)
        {
            return new List<AtlasCitation>();
        }

        if (dtos.Count > MaxCitations)
        {
            context.Errors.Add(AtlasErrorCode.BoundsExceeded, path, $"At most {MaxCitations} end citations are allowed.");
            return null;
        }

        if (recordInterval.UntilOrder is null)
        {
            context.Errors.Add(AtlasErrorCode.EndCitationOutOfRange, path, "Only a relationship with validUntil can cite why it ended.");
            return null;
        }

        // End evidence is shown only in the Changes row at the ending step, so it must end where Changes is offered:
        // never across a slice/milestone boundary, where no surface could ever display it.
        var until = recordInterval.UntilOrder.Value;
        if (context.Checkpoints[until - 1].Milestone != context.Checkpoints[until].Milestone)
        {
            context.Errors.Add(AtlasErrorCode.EndCitationOutOfRange, path, "End citations need an ending step where the Changes lens is offered (not across a slice/milestone boundary).");
            return null;
        }

        return ParseCitationList(context, path, dtos, recordInterval, recordScope, isEnding: true);
    }

    private static List<AtlasCitation>? ParseCitationList(Context context, string path, List<AtlasCitationDto?> dtos, AtlasInterval recordInterval, AtlasScope recordScope, bool isEnding)
    {
        var errors = context.Errors;

        var result = new List<AtlasCitation>();
        var before = errors.Count;
        for (var i = 0; i < dtos.Count; i++)
        {
            var itemPath = $"{path}[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, itemPath, "Citation is null.");
                continue;
            }

            var title = RequireText(errors, $"{itemPath}.title", dto.Title, MaxCitationTitleLength);
            var url = ParseUrl(errors, $"{itemPath}.url", dto.Url);
            var scope = ParseScope(errors, $"{itemPath}.scope", dto.Scope);
            int? availableAt = null;
            if (dto.AvailableAt is null || !context.OrderById.TryGetValue(dto.AvailableAt, out var order))
            {
                errors.Add(dto.AvailableAt is null ? AtlasErrorCode.InvalidField : AtlasErrorCode.UnknownReference, $"{itemPath}.availableAt", "availableAt must name a known checkpoint.");
            }
            else
            {
                availableAt = order;
            }

            if (title is null || scope is null || availableAt is null)
            {
                continue;
            }

            if (isEnding)
            {
                if (availableAt.Value <= recordInterval.FromOrder || availableAt.Value > recordInterval.UntilOrder!.Value)
                {
                    errors.Add(AtlasErrorCode.EndCitationOutOfRange, $"{itemPath}.availableAt", "An end citation must become available after validFrom and no later than validUntil.");
                    continue;
                }
            }
            else if (availableAt.Value > recordInterval.FromOrder)
            {
                errors.Add(AtlasErrorCode.CitationTooNew, $"{itemPath}.availableAt", "A citation must be available at or before its record's validFrom.");
                continue;
            }

            if (recordScope == AtlasScope.Main && scope.Value == AtlasScope.Optional)
            {
                errors.Add(AtlasErrorCode.CitationScopeMismatch, $"{itemPath}.scope", "A main record may cite only main sources.");
                continue;
            }

            if (context.CitationRegistry.TryGetValue(title, out var registered))
            {
                if (registered.AvailableAt != availableAt.Value || registered.Scope != scope.Value)
                {
                    errors.Add(AtlasErrorCode.InconsistentCitation, itemPath, $"Citation title disagrees with {registered.Path} on availableAt or scope.");
                    continue;
                }
            }
            else
            {
                context.CitationRegistry[title] = (availableAt.Value, scope.Value, itemPath);
            }

            if (url is not null || dto.Url is null)
            {
                result.Add(new AtlasCitation(title, url, availableAt.Value, scope.Value));
            }
        }

        return errors.Count == before ? result : null;
    }

    private static Uri? ParseUrl(ErrorSink errors, string path, string? value)
    {
        if (value is null)
        {
            return null;
        }

        if (value.Length > MaxUrlLength
            || !Uri.TryCreate(value, UriKind.Absolute, out var url)
            || (url.Scheme != Uri.UriSchemeHttps && url.Scheme != Uri.UriSchemeHttp)
            || url.UserInfo.Length > 0
            || value.Contains('#'))
        {
            errors.Add(AtlasErrorCode.InvalidField, path, "url must be an absolute http(s) URL without a fragment or user info, or null.");
            return null;
        }

        return url;
    }

    private static AtlasCategory? ParseCategory(ErrorSink errors, string path, string? value)
    {
        switch (value)
        {
            case "character": return AtlasCategory.Character;
            case "organization": return AtlasCategory.Organization;
            case "location": return AtlasCategory.Location;
            case "event": return AtlasCategory.Event;
            default:
                errors.Add(AtlasErrorCode.InvalidField, path, "category must be character, organization, location, or event.");
                return null;
        }
    }

    private static AtlasScope? ParseScope(ErrorSink errors, string path, string? value)
    {
        switch (value)
        {
            case "main": return AtlasScope.Main;
            case "optional": return AtlasScope.Optional;
            default:
                errors.Add(AtlasErrorCode.InvalidField, path, "scope must be main or optional.");
                return null;
        }
    }

    private static AtlasReviewStatus? ParseReview(ErrorSink errors, string path, string? value, AtlasValidationMode mode)
    {
        switch (value)
        {
            case "reviewed":
                return AtlasReviewStatus.Reviewed;
            case "pending":
                if (mode == AtlasValidationMode.Strict)
                {
                    // Reported, but not structural: validation continues so one Strict run lists every unreviewed record.
                    errors.AddReview(path, "Strict validation requires every record to be reviewed.");
                }

                return AtlasReviewStatus.Pending;
            default:
                errors.Add(AtlasErrorCode.InvalidField, path, "review must be pending or reviewed.");
                return null;
        }
    }

    /// <summary>
    /// Follow treats a step as covered when it has game quest ids, so coverage is all-or-none: if any checkpoint has
    /// ids, every checkpoint must, and no id may mark two different steps.
    /// </summary>
    private static void CheckGameQuestCoverage(ErrorSink errors, List<AtlasCheckpoint> checkpoints, List<string> paths)
    {
        if (checkpoints.All(c => c.GameQuestIds.Count == 0))
        {
            return;
        }

        var owner = new Dictionary<int, string>();
        for (var i = 0; i < checkpoints.Count; i++)
        {
            var checkpoint = checkpoints[i];
            if (checkpoint.GameQuestIds.Count == 0)
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{paths[i]}.gameQuestIds", "Once any checkpoint has game quest ids, every checkpoint must.");
                continue;
            }

            foreach (var id in checkpoint.GameQuestIds)
            {
                if (!owner.TryAdd(id, checkpoint.Id))
                {
                    errors.Add(AtlasErrorCode.InvalidField, $"{paths[i]}.gameQuestIds", $"Game quest id {id} already marks checkpoint '{owner[id]}'.");
                }
            }
        }
    }

    private static List<int> ParseGameQuestIds(ErrorSink errors, string path, List<int?>? dtos)
    {
        var ids = new List<int>();
        if (dtos is null)
        {
            return ids;
        }

        if (dtos.Count > MaxGameQuestIds)
        {
            errors.Add(AtlasErrorCode.BoundsExceeded, path, $"At most {MaxGameQuestIds} game quest ids are allowed.");
            return ids;
        }

        for (var i = 0; i < dtos.Count; i++)
        {
            if (dtos[i] is not { } value || value <= 0)
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}[{i}]", "A game quest id must be a positive integer.");
            }
            else if (ids.Contains(value))
            {
                errors.Add(AtlasErrorCode.InvalidField, $"{path}[{i}]", "Duplicate game quest id.");
            }
            else
            {
                ids.Add(value);
            }
        }

        return ids;
    }

    /// <summary>
    /// Arc rules (docs/atlas/v2-plan.md): the entry is a main-scope event that first appears exactly at the arc's
    /// first step and stays visible through its last; membership edges never end, so the cast only grows; at most
    /// <see cref="MaxCastMembers"/> participants at any step; an arc never starts on the first timeline step.
    /// </summary>
    private static List<AtlasArc> BuildArcs(
        Context context,
        List<AtlasArcDto?> dtos,
        IReadOnlyDictionary<string, AtlasRelationshipType> types,
        IReadOnlyDictionary<string, AtlasEntity> entities,
        IReadOnlyList<AtlasRelationship> relationships)
    {
        var errors = context.Errors;
        var result = new List<AtlasArc>();
        if (dtos.Count == 0)
        {
            return result;
        }

        if (!types.TryGetValue(AtlasDataset.ParticipantTypeId, out var participantType))
        {
            errors.Add(AtlasErrorCode.InvalidArc, "$.relationshipTypes", $"Arcs need the '{AtlasDataset.ParticipantTypeId}' relationship type.");
            return result;
        }

        if (participantType.Symmetric)
        {
            // A symmetric membership edge could point from the entry to a member and silently drop them from the cast.
            errors.Add(AtlasErrorCode.InvalidArc, "$.relationshipTypes", $"'{AtlasDataset.ParticipantTypeId}' must not be symmetric.");
            return result;
        }

        var ids = new HashSet<string>(StringComparer.Ordinal);
        var entries = new HashSet<string>(StringComparer.Ordinal);
        for (var i = 0; i < dtos.Count; i++)
        {
            var path = $"$.arcs[{i}]";
            var dto = dtos[i];
            if (dto is null)
            {
                errors.Add(AtlasErrorCode.InvalidField, path, "Arc is null.");
                continue;
            }

            var before = errors.Count;
            var id = RequireId(errors, $"{path}.id", dto.Id);
            var entry = RequireReference(errors, $"{path}.entityId", dto.EntityId, entities);
            int first = -1, last = -1;
            if (dto.FirstStep is null || !context.OrderById.TryGetValue(dto.FirstStep, out first))
            {
                errors.Add(AtlasErrorCode.UnknownReference, $"{path}.firstStep", "firstStep must name a known checkpoint.");
            }

            if (dto.LastStep is null || !context.OrderById.TryGetValue(dto.LastStep, out last))
            {
                errors.Add(AtlasErrorCode.UnknownReference, $"{path}.lastStep", "lastStep must name a known checkpoint.");
            }

            if (errors.Count != before)
            {
                continue;
            }

            if (!ids.Add(id!))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate arc id.");
                continue;
            }

            if (!entries.Add(entry!.Id))
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.entityId", "Each arc needs its own entry entity.");
                continue;
            }

            if (first > last)
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.lastStep", "lastStep must not be earlier than firstStep.");
                continue;
            }

            if (first == 0)
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.firstStep", "An arc cannot start on the first timeline step; a baseline step must come before it.");
                continue;
            }

            if (entry.Category != AtlasCategory.Event)
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.entityId", "An arc entry must be an event entity.");
                continue;
            }

            if (entry.Presentations.Any(p => p.Scope != AtlasScope.Main))
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.entityId", "An arc entry's presentations must all be main scope.");
                continue;
            }

            if (entry.Presentations.Min(p => p.Interval.FromOrder) != first)
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.entityId", "The arc entry's first presentation must start exactly at firstStep.");
                continue;
            }

            if (Enumerable.Range(first, last - first + 1).Any(order => !entry.IsVisibleAt(order, AtlasContentView.MainStory)))
            {
                errors.Add(AtlasErrorCode.InvalidArc, $"{path}.entityId", "The arc entry must stay visible from firstStep through lastStep.");
                continue;
            }

            var members = relationships.Where(r => r.TypeId == AtlasDataset.ParticipantTypeId && r.TargetId == entry.Id).ToList();
            if (members.Any(r => r.Scope != AtlasScope.Main || r.Interval.UntilOrder is not null || r.Interval.FromOrder < first))
            {
                errors.Add(AtlasErrorCode.InvalidArc, path, $"Every '{AtlasDataset.ParticipantTypeId}' edge to the entry must be main scope, start at or after firstStep, and never end.");
                continue;
            }

            var tooLarge = Enumerable.Range(first, last - first + 1)
                .FirstOrDefault(order => members.Where(r => r.Interval.FromOrder <= order).Select(r => r.SourceId).Distinct().Count() > MaxCastMembers, -1);
            if (tooLarge >= 0)
            {
                errors.Add(AtlasErrorCode.CastTooLarge, path, $"The cast exceeds {MaxCastMembers} participants at checkpoint {tooLarge}.");
                continue;
            }

            result.Add(new AtlasArc(id!, entry.Id, first, last, result.Count));
        }

        return result;
    }

    private static AtlasEntity? RequireReference(ErrorSink errors, string path, string? id, IReadOnlyDictionary<string, AtlasEntity> entities)
    {
        var checkedId = RequireId(errors, path, id);
        if (checkedId is null)
        {
            return null;
        }

        if (!entities.TryGetValue(checkedId, out var entity))
        {
            errors.Add(AtlasErrorCode.UnknownReference, path, "Unknown entity.");
            return null;
        }

        return entity;
    }

    private static string? RequireId(ErrorSink errors, string path, string? value)
    {
        if (value is null || value.Length > MaxIdLength || !IdPattern.IsMatch(value))
        {
            errors.Add(AtlasErrorCode.InvalidField, path, $"Expected a lowercase kebab-case id of at most {MaxIdLength} characters.");
            return null;
        }

        return value;
    }

    private static string? RequireText(ErrorSink errors, string path, string? value, int maxLength)
    {
        if (value is null || string.IsNullOrWhiteSpace(value) || value.Length > maxLength || value.Trim().Length != value.Length)
        {
            errors.Add(AtlasErrorCode.InvalidField, path, $"Expected non-empty trimmed text of at most {maxLength} characters.");
            return null;
        }

        return value;
    }

    private static void CheckCount<T>(ErrorSink errors, string path, List<T>? items, int min, int max)
    {
        if (items is null || items.Count < min || items.Count > max)
        {
            errors.Add(AtlasErrorCode.BoundsExceeded, path, $"Expected {min}–{max} items.");
        }
    }

    private sealed class ErrorSink
    {
        private readonly List<AtlasError> errors = new();

        /// <summary>Structural errors only; a record with one is dropped and dependent checks are skipped.</summary>
        public int Count { get; private set; }

        public bool HasStructuralErrors => Count > 0;

        public bool HasErrors => Count > 0 || reviewCount > 0;

        private int reviewCount;

        public void Add(AtlasErrorCode code, string path, string message)
        {
            Count++;
            Record(new AtlasError(code, path, message));
        }

        public void AddReview(string path, string message)
        {
            reviewCount++;
            Record(new AtlasError(AtlasErrorCode.UnreviewedRecord, path, message));
        }

        private void Record(AtlasError error)
        {
            if (errors.Count < MaxReportedErrors)
            {
                errors.Add(error);
            }
        }

        public IReadOnlyList<AtlasError> ToList() => errors.ToArray();
    }
}
