using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>A relationship identity that survives citation splits: the same triple is the same relationship.</summary>
public readonly record struct AtlasTriple(string SourceId, string TypeId, string TargetId)
{
    public static AtlasTriple Of(AtlasRelationshipView relationship) => new(relationship.SourceId, relationship.TypeId, relationship.TargetId);
}

/// <summary>A relationship that ended between two steps, shown with its endpoints as they were before it ended.</summary>
public sealed record AtlasEndedRelationship(
    AtlasRelationshipView Relationship,
    AtlasEntityView Source,
    AtlasEntityView Target,
    string EndedAtCheckpointId,
    IReadOnlyList<AtlasCitationView> EndCitations);

/// <summary>The semantic difference between two projected snapshots.</summary>
public sealed record AtlasDiff(
    IReadOnlyList<AtlasRelationshipView> Added,
    IReadOnlyList<AtlasEndedRelationship> Ended,
    IReadOnlyList<AtlasEntityView> DescriptionUpdated);

/// <summary>
/// The Changes lens (docs/atlas/v2-plan.md). Pure: it compares two safe projected snapshots, never raw intervals, so it
/// can only ever report what is visible at or below the later step.
/// </summary>
public static class AtlasChanges
{
    /// <summary>
    /// Compares <paramref name="before"/> with <paramref name="after"/> by triple, so a citation split is not a change.
    /// An entity counts as updated only when its name, aliases or summary differ.
    /// </summary>
    public static AtlasDiff Compare(AtlasSnapshot before, AtlasSnapshot after) => Compare(before, after, endCitationsFor: null);

    internal static AtlasDiff Compare(AtlasSnapshot before, AtlasSnapshot after, Func<AtlasRelationshipView, IReadOnlyList<AtlasCitationView>>? endCitationsFor)
    {
        ArgumentNullException.ThrowIfNull(before);
        ArgumentNullException.ThrowIfNull(after);
        var beforeTriples = before.Relationships.ToDictionary(AtlasTriple.Of);
        var afterTriples = after.Relationships.ToDictionary(AtlasTriple.Of);

        var added = after.Relationships.Where(r => !beforeTriples.ContainsKey(AtlasTriple.Of(r))).ToList();
        var ended = before.Relationships
            .Where(r => !afterTriples.ContainsKey(AtlasTriple.Of(r)))
            .Select(r => new AtlasEndedRelationship(
                r,
                before.FindEntity(r.SourceId)!,
                before.FindEntity(r.TargetId)!,
                after.Checkpoint.Id,
                endCitationsFor?.Invoke(r) ?? Array.Empty<AtlasCitationView>()))
            .ToList();
        var updated = after.Entities
            .Where(e => before.FindEntity(e.Id) is { } old
                && (old.Name != e.Name || old.Summary != e.Summary || !old.Aliases.SequenceEqual(e.Aliases)))
            .ToList();
        return new AtlasDiff(added, ended, updated);
    }

    /// <summary>
    /// Whether the Changes lens is offered at a step: from the second step on, and only between steps of the same kind
    /// (slice step to slice step, or milestone to milestone), never across a slice → milestone boundary.
    /// </summary>
    public static bool IsOffered(AtlasDataset dataset, string checkpointId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        return dataset.TryGetCheckpoint(checkpointId, out var current)
            && current.Order > 0
            && dataset.Checkpoints[current.Order - 1].Milestone == current.Milestone;
    }

    /// <summary>"What this quest changed" for a contiguous step; otherwise "Changes since ‹previous point›".</summary>
    public static string? Label(AtlasDataset dataset, string checkpointId)
    {
        if (!IsOffered(dataset, checkpointId) || !dataset.TryGetCheckpoint(checkpointId, out var current))
        {
            return null;
        }

        return current.ContiguousWithPrevious
            ? AtlasText.ChangesThisQuest
            : AtlasText.ChangesSince(dataset.Checkpoints[current.Order - 1].DisplayTitle);
    }

    /// <summary>
    /// The Changes lens at a step: the diff from the previous step, with ending evidence attached to ended rows only.
    /// Returns null where the lens is not offered.
    /// </summary>
    public static AtlasDiff? At(AtlasDataset dataset, string checkpointId, AtlasContentView view)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (!IsOffered(dataset, checkpointId) || !dataset.TryGetCheckpoint(checkpointId, out var current))
        {
            return null;
        }

        var previous = dataset.Checkpoints[current.Order - 1];
        var before = AtlasProjector.Project(dataset, previous.Id, view);
        var after = AtlasProjector.Project(dataset, current.Id, view);
        return Compare(before, after, r => EndCitations(dataset, r));
    }

    private static IReadOnlyList<AtlasCitationView> EndCitations(AtlasDataset dataset, AtlasRelationshipView relationship) =>
        dataset.Relationships.FirstOrDefault(r => r.Id == relationship.Id) is { } record
            ? record.EndCitations.Select(c => new AtlasCitationView(c.Title, c.Url)).ToArray()
            : Array.Empty<AtlasCitationView>();
}
