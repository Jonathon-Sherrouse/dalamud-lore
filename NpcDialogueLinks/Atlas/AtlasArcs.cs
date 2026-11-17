using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>
/// Everything the Arc lens shows for one arc at one view (docs/atlas/v2-plan.md, "Arc lens"). Built only from steps at or
/// before <see cref="Effective"/>, so nothing later in the arc can leak.
/// </summary>
public sealed record AtlasArcView(
    string ArcId,
    AtlasEntityView Entry,
    AtlasCheckpoint Effective,
    AtlasSnapshot Cast,
    IReadOnlyList<AtlasRelationshipView> New,
    IReadOnlyList<AtlasEndedRelationship> EndedSoFar,
    bool PastEnd)
{
    /// <summary>"Story so far, through ‹quest›", the label above the entry's recap summary.</summary>
    public string RecapLabel => AtlasText.RecapThrough(Effective);

    /// <summary>The "as of ‹last quest›" marker, shown only once the view is after the arc's last step (rule 7).</summary>
    public string? AsOfLabel => PastEnd ? AtlasText.ArcEnded : null;
}

/// <summary>
/// One arc in the picker: its id and its name as of its effective step. Never its span (rule 7). It also says where the
/// arc sits in the story: <see cref="StartLabel"/> names the step it starts at (always at or below the view, so never a
/// spoiler) and <see cref="Group"/> the patch it starts in, from the first milestone at or after its start (milestone
/// labels are neutral). Group is null when no milestone follows. <see cref="Ended"/> is true only once the view is past
/// the arc's last step, the same test as <see cref="AtlasArcView.PastEnd"/>, so it never says an arc will end.
/// </summary>
public sealed record AtlasArcOption(string ArcId, string Name)
{
    public string StartLabel { get; init; } = string.Empty;

    public string? Group { get; init; }

    public bool Ended { get; init; }
}

/// <summary>
/// The arc to show, and whether an explicit pick just ended because the view dropped below its first step. When
/// <see cref="PickDropped"/> is true the session must clear the pick, so it does not return when the view rises again.
/// </summary>
public sealed record AtlasArcResolution(string? ArcId, bool PickDropped);

/// <summary>Pure arc selection and projection. Session composition (lens state, lifetime) lives in the front-end session.</summary>
public static class AtlasArcs
{
    /// <summary>A cast member's <c>participant-in</c> edge to the arc entry <paramref name="entryId"/>: the arc's own membership spoke.</summary>
    public static bool IsSpoke(AtlasRelationshipView relationship, string entryId) =>
        relationship.TypeId == AtlasDataset.ParticipantTypeId && relationship.TargetId == entryId;

    /// <summary>
    /// Arcs whose first step is at or before the view, sorted by first step then authored order (the picker), each named
    /// as of min(view, its last step).
    /// </summary>
    public static IReadOnlyList<AtlasArcOption> Eligible(AtlasDataset dataset, string viewCheckpointId, AtlasContentView view)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (!dataset.TryGetCheckpoint(viewCheckpointId, out var viewPoint))
        {
            return Array.Empty<AtlasArcOption>();
        }

        return dataset.Arcs
            .Where(a => a.FirstOrder <= viewPoint.Order)
            .OrderBy(a => a.FirstOrder)
            .ThenBy(a => a.AuthoredOrder)
            .Select(a => new AtlasArcOption(a.Id, AtlasProjector.Project(dataset, dataset.Checkpoints[Math.Min(viewPoint.Order, a.LastOrder)].Id, view).FindEntity(a.EntityId)!.Name)
            {
                StartLabel = AtlasText.ArcStartsAt(dataset.Checkpoints[a.FirstOrder]),
                Group = dataset.Checkpoints.Skip(a.FirstOrder).FirstOrDefault(c => c.Milestone) is { } patch ? AtlasText.ArcGroup(patch.Label) : null,
                Ended = viewPoint.Order > a.LastOrder,
            })
            .ToList();
    }

    /// <summary>
    /// The default selection: among arcs containing the view, the earliest-started, so the player stays with the ongoing
    /// arc until it ends. Ties break by authored order, never by span. Null when no arc contains the view.
    /// </summary>
    public static string? Default(AtlasDataset dataset, string viewCheckpointId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (!dataset.TryGetCheckpoint(viewCheckpointId, out var view))
        {
            return null;
        }

        return dataset.Arcs
            .Where(a => a.Contains(view.Order))
            .OrderBy(a => a.FirstOrder)
            .ThenBy(a => a.AuthoredOrder)
            .FirstOrDefault()?.Id;
    }

    /// <summary>
    /// The arc to show: an explicit pick while its first step is at or before the view, otherwise the default selection.
    /// A pick ends when the view drops below its first step (<see cref="AtlasArcResolution.PickDropped"/>); clearing it
    /// then, and when the user picks again or Follow moves the view, is the session's job.
    /// </summary>
    public static AtlasArcResolution Resolve(AtlasDataset dataset, string viewCheckpointId, string? explicitArcId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (explicitArcId is not null && dataset.TryGetCheckpoint(viewCheckpointId, out var view))
        {
            var picked = dataset.Arcs.FirstOrDefault(a => a.Id == explicitArcId);
            if (picked is not null && picked.FirstOrder <= view.Order)
            {
                return new AtlasArcResolution(picked.Id, false);
            }

            return new AtlasArcResolution(Default(dataset, viewCheckpointId), true);
        }

        return new AtlasArcResolution(Default(dataset, viewCheckpointId), false);
    }

    /// <summary>
    /// Projects one arc at the view. Returns null when the arc has not started by the view. The effective step is
    /// T = min(view, last step); the cast is the entry plus participants visible at T; every snapshot is filtered to it.
    /// </summary>
    public static AtlasArcView? Project(AtlasDataset dataset, string arcId, string viewCheckpointId, AtlasContentView view)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        var arc = dataset.Arcs.FirstOrDefault(a => a.Id == arcId);
        if (arc is null || !dataset.TryGetCheckpoint(viewCheckpointId, out var viewPoint) || arc.FirstOrder > viewPoint.Order)
        {
            return null;
        }

        var effective = dataset.Checkpoints[Math.Min(viewPoint.Order, arc.LastOrder)];
        var atEffective = AtlasProjector.Project(dataset, effective.Id, view);
        var cast = new HashSet<string>(StringComparer.Ordinal) { arc.EntityId };
        foreach (var relationship in atEffective.Relationships)
        {
            if (relationship.TypeId == AtlasDataset.ParticipantTypeId && relationship.TargetId == arc.EntityId)
            {
                cast.Add(relationship.SourceId);
            }
        }

        AtlasSnapshot Filtered(int order) => AtlasProjector.Project(dataset, dataset.Checkpoints[order].Id, view).Filter(cast);

        // Arcs never start on the first timeline step (validated), so every step in the arc has a real previous step.
        var castSnapshot = atEffective.Filter(cast);
        var previous = Filtered(effective.Order - 1);
        var added = AtlasChanges.Compare(previous, castSnapshot).Added;

        // Ended so far: the union of endings across each consecutive pair, latest ending wins, dropped if active again at T.
        var endings = new Dictionary<AtlasTriple, AtlasEndedRelationship>();
        var before = Filtered(arc.FirstOrder - 1);
        for (var order = arc.FirstOrder; order <= effective.Order; order++)
        {
            var current = order == effective.Order ? castSnapshot : Filtered(order);
            foreach (var ended in AtlasChanges.Compare(before, current).Ended)
            {
                endings[AtlasTriple.Of(ended.Relationship)] = ended;
            }

            before = current;
        }

        // "Rows show no sources": strip every citation collection from the Arc-lens ended rows.
        var activeAtEffective = castSnapshot.Relationships.Select(AtlasTriple.Of).ToHashSet();
        var endedSoFar = endings.Values
            .Where(e => !activeAtEffective.Contains(AtlasTriple.Of(e.Relationship)))
            .Select(e => e with
            {
                Relationship = e.Relationship with { Citations = Array.Empty<AtlasCitationView>() },
                Source = e.Source with { Citations = Array.Empty<AtlasCitationView>() },
                Target = e.Target with { Citations = Array.Empty<AtlasCitationView>() },
                EndCitations = Array.Empty<AtlasCitationView>(),
            })
            .OrderBy(e => dataset.Checkpoints.First(c => c.Id == e.EndedAtCheckpointId).Order)
            .ThenBy(e => e.Relationship.Id, StringComparer.Ordinal)
            .ToList();

        return new AtlasArcView(arc.Id, castSnapshot.FindEntity(arc.EntityId)!, effective, castSnapshot, added, endedSoFar, viewPoint.Order > arc.LastOrder);
    }
}
