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
    /// A cast member's <c>participant-in</c> spoke to the arc entry at the centre of a whole-cast chart. Front ends draw it
    /// as a faint, unlabelled, non-interactive line: membership is already shown by the member being on the chart
    /// (NDL-008, D8). Set only by <see cref="AtlasGraphLayout.ComputeWholeCast"/>, and only for edges to its centre, so a
    /// participation edge between two ring members (a nested arc's event in the cast) draws as a normal edge.
    /// </summary>
    public bool IsParticipation { get; init; }
}

/// <summary>
/// Portrait sizes shared by the in-game window and the local viewer (NDL-011), so both draw the same picture. Node
/// radii are in the layout's unit space, where the ring of neighbors has radius 1. Category shapes keep their own sizes.
/// </summary>
public static class AtlasPortraitStyle
{
    /// <summary>A portrait node's radius on a chart, relative to the ring radius.</summary>
    public const double NodeRadius = 0.11;

    /// <summary>The focused (centre) node's radius when it has a portrait.</summary>
    public const double FocusRadius = 0.15;

    /// <summary>The category-coloured ring's width, relative to the portrait's radius.</summary>
    public const double RingWidth = 0.12;

    /// <summary>The category badge's radius and its centre's offset along each axis, relative to the portrait's radius.</summary>
    public const double BadgeRadius = 0.34;

    public const double BadgeOffset = 0.72;

    /// <summary>The portrait's diameter in the details and arc-panel headers, in unscaled pixels.</summary>
    public const int HeaderSize = 48;

    /// <summary>Smallest on-screen radius of a portrait node and of the centre node, in unscaled pixels, so a small window keeps faces legible.</summary>
    public const int MinNodePixels = 14;

    public const int MinFocusPixels = 20;
}

/// <summary>
/// How both front ends place chart text (council round 1, NDL-011). The chart is drawn in screen pixels: ring radius
/// <see cref="RingFraction"/> of the canvas's shorter side, text at the UI font size. Names sit outside the ring (above
/// a node in the upper half, below it otherwise) so chords never cross them. Each edge label sits on its edge, on a
/// backing plate, at the first fraction in <see cref="LabelPositions"/> whose box clears every node, name and label
/// already placed; if none is clear it stays at the middle.
/// </summary>
public static class AtlasChartStyle
{
    public const double RingFraction = 0.36;

    /// <summary>Fractions along an edge to try for its label, in order.</summary>
    public static readonly double[] LabelPositions = [0.5, 0.38, 0.62, 0.28, 0.72, 0.2, 0.8];

    /// <summary>A name's widest truncation, in unscaled pixels; a ring name is also capped to the gap between ring neighbours.</summary>
    public const int NameMaxWidth = 150;

    public const int CentreNameMaxWidth = 200;

    /// <summary>The centre name is also capped to this many ring radii, so in a small window it stays clear of the ring.</summary>
    public const double CentreNameRingWidth = 1.6;

    /// <summary>A ring name's width cap when the ring has fewer than <see cref="FewNodesThreshold"/> members, so a small chart doesn't cut names it has room for.</summary>
    public const int FewNodesNameMaxWidth = 200;

    public const int FewNodesThreshold = 4;

    /// <summary>Clearance kept around nodes, names and labels when placing a label, in unscaled pixels.</summary>
    public const int Clearance = 3;

    /// <summary>
    /// Where a label may sit across its edge, in steps of one plate height plus <see cref="Clearance"/> along the edge's
    /// normal: on the edge first, then to either side. An off-edge label gets a short leader line back to its edge.
    /// Candidates are tried for each fraction in <see cref="LabelPositions"/>, all offsets of one fraction before the next.
    /// </summary>
    public static readonly int[] LabelOffsets = [0, 1, -1, 2, -2];

    /// <summary>
    /// When no candidate is clear, the label takes the one with the least weighted overlap. A name plate weighs most, so
    /// a label never covers a name while any other choice exists; then nodes and other labels.
    /// </summary>
    public const double NameOverlapWeight = 4;

    public const double NodeOverlapWeight = 3;

    public const double LabelOverlapWeight = 3;

    /// <summary>A portrait node's obstacle radius, relative to its radius, so its category badge is covered too.</summary>
    public const double PortraitObstacleScale = 1.1;

    /// <summary>How far a shape reaches from its centre, relative to its radius, so edges and arrowheads stop at its outline.</summary>
    public const double DiamondExtent = 1.25;

    public const double HexagonExtent = 1.15;

    /// <summary>The centre name is shortened until its plate clears every ring node and name, but never below this width.</summary>
    public const int CentreNameMinWidth = 40;

    /// <summary>
    /// Side-pane widths (unscaled pixels) as a fraction of the window's content width, clamped, so a small window
    /// gives its width to the chart (council round 2): browse 20% within 150–200, details 28% within 220–280.
    /// </summary>
    public const double BrowseFraction = 0.2;

    public const int BrowseMin = 150;

    public const int BrowseMax = 200;

    public const double DetailsFraction = 0.28;

    public const int DetailsMin = 220;

    public const int DetailsMax = 280;
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
                edges.Add(new AtlasGraphEdge(relationship, relationship.SourceId, relationship.TargetId, relationship.OutgoingLabel, relationship.Symmetric, lane, lanes.Count)
                {
                    IsParticipation = AtlasArcs.IsSpoke(relationship, center.Id),
                });
            }
        }

        return new AtlasGraphLayout(nodes, edges);
    }
}
