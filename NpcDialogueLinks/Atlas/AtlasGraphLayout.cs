using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

public sealed record AtlasGraphNode(AtlasEntityView Entity, double X, double Y, bool IsFocus);

/// <summary>
/// One drawn edge between the focus and a canvas neighbor. <see cref="FromId"/> → <see cref="ToId"/> is the stored direction;
/// symmetric edges are drawn without an arrowhead. <see cref="LaneIndex"/>/<see cref="LaneCount"/> separate parallel edges.
/// </summary>
public sealed record AtlasGraphEdge(AtlasRelationshipView Relationship, string FromId, string ToId, string Label, bool Symmetric, int LaneIndex, int LaneCount);

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
}
