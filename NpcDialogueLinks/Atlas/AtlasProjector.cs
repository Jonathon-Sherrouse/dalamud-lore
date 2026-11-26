using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>A citation as displayed: title and optional outbound link only.</summary>
public sealed record AtlasCitationView(string Title, Uri? Url);

/// <param name="IncludesOptional">
/// True when the shown text is an optional presentation, i.e. it includes knowledge from optional quests.
/// Only ever true in the MainAndOptional view. Display-only; it reveals nothing that is not already visible.
/// </param>
public sealed record AtlasEntityView(
    string Id,
    AtlasCategory Category,
    string Name,
    IReadOnlyList<string> Aliases,
    string Summary,
    IReadOnlyList<AtlasCitationView> Citations,
    bool IncludesOptional = false)
{
    /// <summary>The entity's reviewed portrait, or null to draw its category shape (NDL-011).</summary>
    public AtlasPortrait? Portrait { get; init; }
}

public sealed record AtlasRelationshipView(
    string Id,
    string SourceId,
    string TargetId,
    string TypeId,
    string OutgoingLabel,
    string IncomingLabel,
    bool Symmetric,
    IReadOnlyList<AtlasCitationView> Citations,
    bool IsOptional = false);

public enum AtlasDirection
{
    Outgoing,
    Incoming,
}

/// <summary>One relationship as seen from the focused entity.</summary>
public sealed record AtlasNeighbor(AtlasEntityView Entity, AtlasRelationshipView Relationship, AtlasDirection Direction)
{
    public string Label => Direction == AtlasDirection.Outgoing ? Relationship.OutgoingLabel : Relationship.IncomingLabel;
}

public sealed record AtlasNeighborhood(
    AtlasEntityView Focus,
    IReadOnlyList<AtlasNeighbor> Neighbors,
    IReadOnlyList<AtlasEntityView> CanvasEntities,
    IReadOnlyList<AtlasEntityView> OverflowEntities);

/// <summary>
/// Everything visible at one checkpoint in one content view. Built by filtering first, so it holds
/// no reference to hidden records: search, counts, neighborhoods and citations cannot leak them.
/// </summary>
public sealed class AtlasSnapshot
{
    public const int MaxCanvasNeighbors = 8;
    public const int MaxSearchQueryLength = 100;

    private readonly Dictionary<string, AtlasEntityView> entitiesById;

    internal AtlasSnapshot(AtlasCheckpoint checkpoint, AtlasContentView view, List<AtlasEntityView> entities, List<AtlasRelationshipView> relationships)
    {
        Checkpoint = checkpoint;
        View = view;
        Entities = entities;
        Relationships = relationships;
        entitiesById = entities.ToDictionary(e => e.Id, StringComparer.Ordinal);
    }

    public AtlasCheckpoint Checkpoint { get; }

    public AtlasContentView View { get; }

    /// <summary>Visible entities ordered by category, then id.</summary>
    public IReadOnlyList<AtlasEntityView> Entities { get; }

    /// <summary>Visible relationships ordered by id.</summary>
    public IReadOnlyList<AtlasRelationshipView> Relationships { get; }

    public AtlasEntityView? FindEntity(string? id) =>
        id is not null && entitiesById.TryGetValue(id, out var entity) ? entity : null;

    /// <summary>
    /// The same snapshot restricted to <paramref name="entityIds"/>: only those entities, and only relationships with
    /// both endpoints inside the set. Used for an arc's cast: the whole-cast chart and the arc panel's rows.
    /// </summary>
    public AtlasSnapshot Filter(IReadOnlySet<string> entityIds)
    {
        ArgumentNullException.ThrowIfNull(entityIds);
        var entities = Entities.Where(e => entityIds.Contains(e.Id)).ToList();
        var relationships = Relationships.Where(r => entityIds.Contains(r.SourceId) && entityIds.Contains(r.TargetId)).ToList();
        return new AtlasSnapshot(Checkpoint, View, entities, relationships);
    }

    /// <summary>Case-insensitive substring search over visible names and aliases. Blank returns all.</summary>
    public IReadOnlyList<AtlasEntityView> Search(string? query)
    {
        var trimmed = (query ?? string.Empty).Trim();
        if (trimmed.Length == 0)
        {
            return Entities;
        }

        if (trimmed.Length > MaxSearchQueryLength)
        {
            trimmed = trimmed[..MaxSearchQueryLength];
        }

        return Entities
            .Where(e => e.Name.Contains(trimmed, StringComparison.OrdinalIgnoreCase)
                || e.Aliases.Any(a => a.Contains(trimmed, StringComparison.OrdinalIgnoreCase)))
            .ToList();
    }

    /// <summary>The directed one-hop neighborhood of a visible entity, or null if it is not visible.</summary>
    public AtlasNeighborhood? GetNeighborhood(string? focusId)
    {
        var focus = FindEntity(focusId);
        if (focus is null)
        {
            return null;
        }

        var neighbors = new List<AtlasNeighbor>();
        foreach (var relationship in Relationships)
        {
            if (relationship.SourceId == focus.Id)
            {
                neighbors.Add(new AtlasNeighbor(entitiesById[relationship.TargetId], relationship, AtlasDirection.Outgoing));
            }
            else if (relationship.TargetId == focus.Id)
            {
                neighbors.Add(new AtlasNeighbor(entitiesById[relationship.SourceId], relationship, AtlasDirection.Incoming));
            }
        }

        neighbors.Sort((a, b) =>
        {
            var byEntity = AtlasProjector.CompareEntities(a.Entity, b.Entity);
            return byEntity != 0 ? byEntity : string.CompareOrdinal(a.Relationship.Id, b.Relationship.Id);
        });

        var distinct = new List<AtlasEntityView>();
        foreach (var neighbor in neighbors)
        {
            if (distinct.Count == 0 || distinct[^1].Id != neighbor.Entity.Id)
            {
                distinct.Add(neighbor.Entity);
            }
        }

        var canvas = distinct.Take(MaxCanvasNeighbors).ToList();
        var overflow = distinct.Skip(MaxCanvasNeighbors).ToList();
        return new AtlasNeighborhood(focus, neighbors, canvas, overflow);
    }
}

public static class AtlasProjector
{
    /// <summary>Pure projection of the dataset as of one checkpoint. Only the view checkpoint decides what is shown.</summary>
    public static AtlasSnapshot Project(AtlasDataset dataset, string viewCheckpointId, AtlasContentView view)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (!dataset.TryGetCheckpoint(viewCheckpointId, out var checkpoint))
        {
            throw new ArgumentException($"Unknown checkpoint '{viewCheckpointId}'.", nameof(viewCheckpointId));
        }

        var order = checkpoint.Order;
        var entities = new List<AtlasEntityView>();
        foreach (var entity in dataset.Entities)
        {
            var presentation = entity.PresentationAt(order, view);
            if (presentation is null)
            {
                continue;
            }

            entities.Add(new AtlasEntityView(
                entity.Id,
                entity.Category,
                presentation.Name,
                presentation.Aliases.ToArray(),
                presentation.Summary,
                ToViews(presentation.Citations),
                presentation.Scope == AtlasScope.Optional)
            {
                Portrait = entity.Portrait,
            });
        }

        entities.Sort(CompareEntities);
        var visibleIds = new HashSet<string>(entities.Select(e => e.Id), StringComparer.Ordinal);

        var relationships = new List<AtlasRelationshipView>();
        foreach (var relationship in dataset.Relationships)
        {
            // Validation guarantees visible endpoints; the id check is defense in depth.
            if (!relationship.IsVisibleAt(order, view)
                || !visibleIds.Contains(relationship.SourceId)
                || !visibleIds.Contains(relationship.TargetId))
            {
                continue;
            }

            var type = dataset.RelationshipTypes[relationship.TypeId];
            relationships.Add(new AtlasRelationshipView(
                relationship.Id,
                relationship.SourceId,
                relationship.TargetId,
                type.Id,
                type.OutgoingLabel,
                type.IncomingLabel,
                type.Symmetric,
                ToViews(relationship.Citations),
                relationship.Scope == AtlasScope.Optional));
        }

        relationships.Sort((a, b) => string.CompareOrdinal(a.Id, b.Id));
        return new AtlasSnapshot(checkpoint, view, entities, relationships);
    }

    private static AtlasCitationView[] ToViews(IReadOnlyList<AtlasCitation> citations) =>
        citations.Select(c => new AtlasCitationView(c.Title, c.Url)).ToArray();

    internal static int CompareEntities(AtlasEntityView a, AtlasEntityView b)
    {
        var byCategory = ((int)a.Category).CompareTo((int)b.Category);
        return byCategory != 0 ? byCategory : string.CompareOrdinal(a.Id, b.Id);
    }
}
