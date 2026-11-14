using System;
using System.Collections.Generic;

namespace NpcDialogueLinks.Atlas;

// Pure Atlas core. No Dalamud, ImGui, or Plugin dependencies: every file in this folder is
// compile-linked into NpcDialogueLinks.Tests and NpcDialogueLinks.AtlasViewer.
// Contract: docs/atlas/schema.md (schema v1).

public enum AtlasCategory
{
    Character = 0,
    Organization = 1,
    Location = 2,
}

public enum AtlasScope
{
    Main,
    Optional,
}

public enum AtlasReviewStatus
{
    Pending,
    Reviewed,
}

public enum AtlasValidationMode
{
    /// <summary>Structural validation; pending-review records are allowed.</summary>
    Draft,

    /// <summary>Shippable validation; every record must be reviewed. Used by the runtime.</summary>
    Strict,
}

public enum AtlasContentView
{
    /// <summary>Only main-scope records.</summary>
    MainStory,

    /// <summary>Main and optional records; optional presentations replace main ones. Default.</summary>
    MainAndOptional,
}

public sealed record AtlasCheckpoint(string Id, string Label, int Order);

/// <summary>A source citation. <see cref="AvailableAtOrder"/> is the earliest checkpoint where the source is player knowledge.</summary>
public sealed record AtlasCitation(string Title, Uri? Url, int AvailableAtOrder, AtlasScope Scope);

public sealed record AtlasRelationshipType(string Id, string OutgoingLabel, string IncomingLabel, bool Symmetric);

/// <summary>Inclusive-start, exclusive-end interval over checkpoint order. Null end means ongoing.</summary>
public sealed record AtlasInterval(int FromOrder, int? UntilOrder)
{
    public bool Contains(int order) => order >= FromOrder && (UntilOrder is null || order < UntilOrder.Value);

    public bool Overlaps(AtlasInterval other)
    {
        var end = UntilOrder ?? int.MaxValue;
        var otherEnd = other.UntilOrder ?? int.MaxValue;
        return FromOrder < otherEnd && other.FromOrder < end;
    }
}

public sealed record AtlasPresentation(
    AtlasInterval Interval,
    AtlasScope Scope,
    string Name,
    IReadOnlyList<string> Aliases,
    string Summary,
    IReadOnlyList<AtlasCitation> Citations,
    AtlasReviewStatus Review);

public sealed record AtlasEntity(string Id, AtlasCategory Category, IReadOnlyList<AtlasPresentation> Presentations)
{
    /// <summary>The presentation shown at a checkpoint in a view, or null when hidden there.</summary>
    public AtlasPresentation? PresentationAt(int order, AtlasContentView view)
    {
        AtlasPresentation? main = null;
        foreach (var presentation in Presentations)
        {
            if (!presentation.Interval.Contains(order))
            {
                continue;
            }

            if (presentation.Scope == AtlasScope.Optional)
            {
                if (view == AtlasContentView.MainAndOptional)
                {
                    // Whole-record replacement: nothing is merged from the main presentation.
                    return presentation;
                }
            }
            else
            {
                main ??= presentation;
            }
        }

        return main;
    }

    public bool IsVisibleAt(int order, AtlasContentView view) => PresentationAt(order, view) is not null;
}

public sealed record AtlasRelationship(
    string Id,
    string SourceId,
    string TypeId,
    string TargetId,
    AtlasInterval Interval,
    AtlasScope Scope,
    IReadOnlyList<AtlasCitation> Citations,
    AtlasReviewStatus Review)
{
    public bool IsVisibleAt(int order, AtlasContentView view) =>
        Interval.Contains(order) && (Scope == AtlasScope.Main || view == AtlasContentView.MainAndOptional);
}

/// <summary>A validated, immutable Atlas dataset. Only <see cref="AtlasLoader"/> creates one.</summary>
public sealed class AtlasDataset
{
    private readonly Dictionary<string, AtlasCheckpoint> checkpointsById;

    internal AtlasDataset(
        IReadOnlyList<AtlasCheckpoint> checkpoints,
        IReadOnlyDictionary<string, AtlasRelationshipType> relationshipTypes,
        IReadOnlyList<AtlasEntity> entities,
        IReadOnlyList<AtlasRelationship> relationships)
    {
        Checkpoints = checkpoints;
        RelationshipTypes = relationshipTypes;
        Entities = entities;
        Relationships = relationships;
        checkpointsById = new Dictionary<string, AtlasCheckpoint>(StringComparer.Ordinal);
        foreach (var checkpoint in checkpoints)
        {
            checkpointsById[checkpoint.Id] = checkpoint;
        }
    }

    /// <summary>Checkpoints in story order; <see cref="AtlasCheckpoint.Order"/> equals the index.</summary>
    public IReadOnlyList<AtlasCheckpoint> Checkpoints { get; }

    /// <summary>The full type vocabulary. UI code must never render this directly; use snapshot relationships.</summary>
    internal IReadOnlyDictionary<string, AtlasRelationshipType> RelationshipTypes { get; }

    internal IReadOnlyList<AtlasEntity> Entities { get; }

    internal IReadOnlyList<AtlasRelationship> Relationships { get; }

    public AtlasCheckpoint EarliestCheckpoint => Checkpoints[0];

    public bool TryGetCheckpoint(string? id, out AtlasCheckpoint checkpoint)
    {
        if (id is not null && checkpointsById.TryGetValue(id, out var found))
        {
            checkpoint = found;
            return true;
        }

        checkpoint = null!;
        return false;
    }
}
