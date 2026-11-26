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
    string EndedAtCheckpointId);

/// <summary>The semantic difference between two projected snapshots.</summary>
public sealed record AtlasDiff(
    IReadOnlyList<AtlasRelationshipView> Added,
    IReadOnlyList<AtlasEndedRelationship> Ended,
    IReadOnlyList<AtlasEntityView> DescriptionUpdated);

/// <summary>
/// Snapshot comparison behind the arc panel's "New at this point" and "Ended so far in this arc" (docs/atlas/v2-plan.md,
/// "Arc lens"). Pure: it compares two safe projected snapshots, never raw intervals, so it can only ever report what is
/// visible at or below the later step. The standalone Changes lens that also used it was removed in NDL-018.
/// </summary>
public static class AtlasChanges
{
    /// <summary>
    /// Compares <paramref name="before"/> with <paramref name="after"/> by triple, so a citation split is not a change.
    /// An entity counts as updated only when its name, aliases or summary differ.
    /// </summary>
    public static AtlasDiff Compare(AtlasSnapshot before, AtlasSnapshot after)
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
                after.Checkpoint.Id))
            .ToList();
        var updated = after.Entities
            .Where(e => before.FindEntity(e.Id) is { } old
                && (old.Name != e.Name || old.Summary != e.Summary || !old.Aliases.SequenceEqual(e.Aliases)))
            .ToList();
        return new AtlasDiff(added, ended, updated);
    }
}
