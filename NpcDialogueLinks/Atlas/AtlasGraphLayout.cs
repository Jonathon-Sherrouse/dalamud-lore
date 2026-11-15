using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

public sealed record AtlasGraphNode(AtlasEntityView Entity, double X, double Y, bool IsFocus);

/// <summary>
/// One drawn edge between the focus and a canvas neighbor. <see cref="FromId"/> → <see cref="ToId"/> is the stored direction;
/// symmetric edges are drawn without an arrowhead. <see cref="LaneIndex"/>/<see cref="LaneCount"/> separate parallel edges.
/// </summary>
public sealed record AtlasGraphEdge(AtlasRelationshipView Relationship, string FromId, string ToId, string Label, bool Symmetric, int LaneIndex, int LaneCount)
{
    /// <summary>
    /// A cast member's <c>participant-in</c> spoke to the arc entry. Front ends draw it as a faint, unlabelled,
    /// non-interactive line: membership is already shown by the member being on the chart (NDL-008).
    /// </summary>
    public bool IsParticipation => Relationship.TypeId == AtlasDataset.ParticipantTypeId;
}

/// <summary>
/// Deterministic one-hop layout in a unit coordinate space: focus at (0, 0), up to eight canvas neighbors on a unit
/// circle, clockwise from the top, in neighborhood order (category, then id). No physics; renderers only scale.
/// </summary>
public sealed record AtlasGraphLayout(IReadOnlyList<AtlasGraphNode> Nodes, IReadOnlyList<AtlasGraphEdge> Edges)
{
    public static AtlasGraphLayout Compute(AtlasNeighborhood neighborhood)
    {
        ArgumentNullException.ThrowIfNull(neighborhood);
        var nodes = new List<AtlasGraphNode> { new(neighborhood.Focus, 0, 0, true) };
        var count = neighborhood.CanvasEntities.Count;
        for (var i = 0; i < count; i++)
        {
            var angle = (-Math.PI / 2) + (2 * Math.PI * i / count);
            nodes.Add(new AtlasGraphNode(neighborhood.CanvasEntities[i], Math.Round(Math.Cos(angle), 6), Math.Round(Math.Sin(angle), 6), false));
        }

        var onCanvas = new HashSet<string>(neighborhood.CanvasEntities.Select(e => e.Id), StringComparer.Ordinal);
        var edges = new List<AtlasGraphEdge>();
        foreach (var group in neighborhood.Neighbors.Where(n => onCanvas.Contains(n.Entity.Id)).GroupBy(n => n.Entity.Id))
        {
            var lanes = group.ToList();
            for (var lane = 0; lane < lanes.Count; lane++)
            {
                var neighbor = lanes[lane];
                var relationship = neighbor.Relationship;
                edges.Add(new AtlasGraphEdge(
                    relationship,
                    relationship.SourceId,
                    relationship.TargetId,
                    relationship.OutgoingLabel,
                    relationship.Symmetric,
                    lane,
                    lanes.Count));
            }
        }

        return new AtlasGraphLayout(nodes, edges);
    }

    /// <summary>
    /// Deterministic whole-cast layout for the Arc lens: <paramref name="centerId"/> (the arc entry) at (0, 0), every other
    /// cast member on a unit circle clockwise from the top in category-then-id order, and every cast-to-cast relationship
    /// drawn, with parallel edges between the same pair in separate lanes. The cast cap keeps it small.
    /// </summary>
    public static AtlasGraphLayout ComputeWholeCast(AtlasSnapshot cast, string centerId)
    {
        ArgumentNullException.ThrowIfNull(cast);
        var center = cast.FindEntity(centerId) ?? throw new ArgumentException("The center must be in the cast.", nameof(centerId));
        var nodes = new List<AtlasGraphNode> { new(center, 0, 0, true) };
        var ring = cast.Entities.Where(e => e.Id != center.Id).ToList();
        for (var i = 0; i < ring.Count; i++)
        {
            var angle = (-Math.PI / 2) + (2 * Math.PI * i / ring.Count);
            nodes.Add(new AtlasGraphNode(ring[i], Math.Round(Math.Cos(angle), 6), Math.Round(Math.Sin(angle), 6), false));
        }

        var edges = new List<AtlasGraphEdge>();
        foreach (var pair in cast.Relationships.GroupBy(r => string.CompareOrdinal(r.SourceId, r.TargetId) < 0 ? (r.SourceId, r.TargetId) : (r.TargetId, r.SourceId)))
        {
            var lanes = pair.OrderBy(r => r.Id, StringComparer.Ordinal).ToList();
            for (var lane = 0; lane < lanes.Count; lane++)
            {
                var relationship = lanes[lane];
                edges.Add(new AtlasGraphEdge(relationship, relationship.SourceId, relationship.TargetId, relationship.OutgoingLabel, relationship.Symmetric, lane, lanes.Count));
            }
        }

        return new AtlasGraphLayout(nodes, edges);
    }
}
