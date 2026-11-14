using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace NpcDialogueLinks.Atlas;

/// <summary>Semantic validation for schema v1 (docs/atlas/schema.md). Collects every error rather than stopping at the first.</summary>
internal static class AtlasValidator
{
    public const int MaxIdLength = 64;
    public const int MaxLabelLength = 80;
    public const int MaxSummaryLength = 1200;
    public const int MaxCitationTitleLength = 200;
    public const int MaxUrlLength = 2048;
    public const int MaxPresentations = 32;
    public const int MaxAliases = 8;
    public const int MaxCitations = 8;
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
        if (errors.HasErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var checkpoints = BuildCheckpoints(errors, file.Checkpoints!);
        var types = BuildTypes(errors, file.RelationshipTypes!);
        if (errors.HasStructuralErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var orderById = checkpoints.ToDictionary(c => c.Id, c => c.Order, StringComparer.Ordinal);
        var citationRegistry = new Dictionary<string, (int AvailableAt, AtlasScope Scope, string Path)>(StringComparer.Ordinal);
        var context = new Context(errors, orderById, checkpoints.Count, mode, citationRegistry);

        var entities = BuildEntities(context, file.Entities!);
        if (errors.HasStructuralErrors)
        {
            // Relationship checks depend on a sound entity set.
            return AtlasLoadResult.Fail(errors.ToList());
        }

        var relationships = BuildRelationships(context, file.Relationships ?? new List<AtlasRelationshipDto?>(), types, entities);
        if (errors.HasErrors)
        {
            return AtlasLoadResult.Fail(errors.ToList());
        }

        return AtlasLoadResult.Ok(new AtlasDataset(checkpoints, types, entities.Values.ToList(), relationships));
    }

    private sealed record Context(
        ErrorSink Errors,
        IReadOnlyDictionary<string, int> OrderById,
        int CheckpointCount,
        AtlasValidationMode Mode,
        Dictionary<string, (int AvailableAt, AtlasScope Scope, string Path)> CitationRegistry);

    private static List<AtlasCheckpoint> BuildCheckpoints(ErrorSink errors, List<AtlasCheckpointDto?> dtos)
    {
        var result = new List<AtlasCheckpoint>();
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

            var id = RequireId(errors, $"{path}.id", dto.Id);
            var label = RequireText(errors, $"{path}.label", dto.Label, MaxLabelLength);
            if (id is null || label is null)
            {
                continue;
            }

            if (!seen.Add(id))
            {
                errors.Add(AtlasErrorCode.DuplicateId, $"{path}.id", "Duplicate checkpoint id.");
                continue;
            }

            result.Add(new AtlasCheckpoint(id, label, result.Count));
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

            var entity = new AtlasEntity(id!, category!.Value, presentations);
            CheckPresentationOverlap(errors, path, presentations);
            CheckOptionalBoundaries(errors, path, presentations, context.CheckpointCount);
            CheckOptionalPersistence(errors, path, entity, context.CheckpointCount);
            CheckVisibilityContiguous(errors, path, entity, context.CheckpointCount);
            result.Add(entity.Id, entity);
        }

        return result;
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

            var relationship = new AtlasRelationship(id!, source.Id, type!.Id, target.Id, interval!, scope!.Value, citations!, review!.Value);
            CheckEndpointsVisible(errors, path, relationship, source, target, context.CheckpointCount);
            result.Add(relationship);
            paths.Add(path);
        }

        CheckDuplicatePairs(errors, result, paths, types);
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
        var errors = context.Errors;
        if (dtos is null || dtos.Count == 0 || dtos.Count > MaxCitations)
        {
            errors.Add(AtlasErrorCode.BoundsExceeded, path, $"1–{MaxCitations} citations are required.");
            return null;
        }

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

            if (availableAt.Value > recordInterval.FromOrder)
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
            default:
                errors.Add(AtlasErrorCode.InvalidField, path, "category must be character, organization, or location.");
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
