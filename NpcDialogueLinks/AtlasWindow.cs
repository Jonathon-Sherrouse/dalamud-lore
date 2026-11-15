using System.Numerics;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Utility;
using Dalamud.Interface.Utility.Raii;
using Dalamud.Interface.Textures;
using Dalamud.Interface.Textures.TextureWraps;
using Dalamud.Interface.Windowing;
using Dalamud.Plugin.Services;
using Dalamud.Utility;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks;

/// <summary>
/// The in-game Lore Atlas (NDL-004, v2 lenses in NDL-010). A thin ImGui renderer over the shared <see cref="AtlasSession"/>:
/// every browsing rule and player-facing string lives in NpcDialogueLinks/Atlas/, and the local viewer renders the same
/// session. Layout and visual language follow docs/atlas/ux-design.md (NDL-005, and "v2 lenses" from NDL-008).
/// </summary>
internal sealed class AtlasWindow : Window
{
    private const string LimitMenuId = "AtlasLimitMenu";
    private const string ConfirmModalId = AtlasText.WindowTitle + "##AtlasConfirmRaise";

    // Palette shared with the local viewer's CSS (docs/atlas/ux-design.md, visual language).
    private static readonly Vector4 CharacterColor = new(0.498f, 0.698f, 0.898f, 1f);
    private static readonly Vector4 OrganizationColor = new(0.851f, 0.706f, 0.353f, 1f);
    private static readonly Vector4 LocationColor = new(0.498f, 0.812f, 0.604f, 1f);
    private static readonly Vector4 EventColor = new(0.765f, 0.608f, 0.827f, 1f);
    private static readonly Vector4 MutedColor = new(0.604f, 0.639f, 0.698f, 1f);
    private static readonly Vector4 AccentColor = new(0.851f, 0.706f, 0.353f, 1f);
    private static readonly Vector4 HoverColor = new(0.498f, 0.698f, 0.898f, 1f);
    private static readonly Vector4 EdgeColor = new(0.42f, 0.455f, 0.525f, 1f);
    private static readonly Vector4 LabelBackColor = new(0.118f, 0.122f, 0.141f, 0.85f);
    private static readonly Vector4 SelectedButtonColor = new(0.231f, 0.259f, 0.337f, 1f);
    private static readonly Vector4 TextColor = new(0.902f, 0.910f, 0.933f, 1f);

    private readonly string dataPath;
    private readonly PluginConfiguration configuration;
    private readonly ITextureProvider textures;

    private AtlasSession? session;
    private bool loadFailed;
    private string searchBuffer = string.Empty;

    // The search text the window last saw in the session. When the session changes it (a lens, view or limit change
    // clears it), the input box is reset to match instead of pushing its stale text back.
    private string syncedQuery = string.Empty;
    private bool openConfirmNextFrame;

    public AtlasWindow(string dataPath, PluginConfiguration configuration, ITextureProvider textures)
        : base($"{AtlasText.WindowTitle}###NpcDialogueLinksAtlas")
    {
        this.dataPath = dataPath;
        this.configuration = configuration;
        this.textures = textures;
        this.Size = new Vector2(960, 600);
        this.SizeCondition = ImGuiCond.FirstUseEver;
        this.SizeConstraints = new()
        {
            MinimumSize = new Vector2(760, 480),
            MaximumSize = new Vector2(4096, 4096),
        };
        this.ShowCloseButton = true;
        this.RespectCloseHotkey = true;
    }

    /// <summary>Load the bundled data once per open, in Strict mode. Failure only ever affects this window.</summary>
    public override void OnOpen()
    {
        this.session = null;
        this.loadFailed = false;
        this.searchBuffer = string.Empty;
        this.syncedQuery = string.Empty;
        this.openConfirmNextFrame = false;

        var result = AtlasLoader.LoadFile(this.dataPath, AtlasValidationMode.Strict);
        if (!result.Success)
        {
            this.loadFailed = true;
            Plugin.Log.Warning($"Lore Atlas failed to load {this.dataPath} with {result.Errors.Count} error(s).");
            foreach (var error in result.Errors.Take(50))
            {
                Plugin.Log.Warning($"  {error.Code} at {error.Path}: {error.Message}");
            }

            return;
        }

        try
        {
            var saved = new AtlasSpoilerState(this.configuration.AtlasCeilingId ?? string.Empty, this.configuration.AtlasViewId ?? string.Empty);
            var newSession = new AtlasSession(result.Dataset!, saved);
            newSession.SpoilerStateChanged += this.SaveSpoilerState;
            this.session = newSession;

            // Persist the revalidated state, so a stale or invalid saved state is repaired after content updates.
            this.SaveSpoilerState(newSession.SpoilerState);
        }
        catch (Exception exception)
        {
            this.Fail(exception);
        }
    }

    public override void OnClose()
    {
        if (this.session is not null)
        {
            this.session.SpoilerStateChanged -= this.SaveSpoilerState;
        }

        this.session = null;
    }

    public override void Draw()
    {
        if (this.loadFailed || this.session is null)
        {
            ImGui.TextWrapped(AtlasText.LoadFailed);
            return;
        }

        try
        {
            this.DrawSession(this.session);
        }
        catch (Exception exception)
        {
            this.Fail(exception);
        }
    }

    private void Fail(Exception exception)
    {
        Plugin.Log.Error(exception, "Lore Atlas hit an unexpected error; the Atlas window is disabled until it is reopened.");
        this.loadFailed = true;
        this.session = null;
    }

    private void SaveSpoilerState(AtlasSpoilerState state)
    {
        if (this.configuration.AtlasCeilingId == state.CeilingId && this.configuration.AtlasViewId == state.ViewId)
        {
            return;
        }

        this.configuration.AtlasCeilingId = state.CeilingId;
        this.configuration.AtlasViewId = state.ViewId;
        this.configuration.Save();
    }

    private void DrawSession(AtlasSession s)
    {
        var scale = ImGuiHelpers.GlobalScale;
        this.DrawTopBar(s);
        ImGui.Separator();
        DrawLensBar(s);
        ImGui.Separator();

        var footerHeight = ImGui.GetTextLineHeightWithSpacing() + (ImGui.GetStyle().ItemSpacing.Y * 2);
        var bodyHeight = Math.Max(ImGui.GetContentRegionAvail().Y - footerHeight, 100 * scale);
        var browseWidth = 200 * scale;
        var detailsWidth = 280 * scale;
        var spacing = ImGui.GetStyle().ItemSpacing.X;
        var graphWidth = Math.Max(ImGui.GetContentRegionAvail().X - browseWidth - detailsWidth - (spacing * 2), 120 * scale);

        // ImRaii scopes end every child and popup even if drawing throws, so a failure stays inside the Atlas.
        if (s.Lens == AtlasLens.Changes)
        {
            // D7: the change list takes the browse pane and the canvas.
            using (var list = ImRaii.Child("AtlasChanges", new Vector2(browseWidth + spacing + graphWidth, bodyHeight), true))
            {
                if (list)
                {
                    DrawChangesList(s);
                }
            }
        }
        else
        {
            using (var browse = ImRaii.Child("AtlasBrowse", new Vector2(browseWidth, bodyHeight), true))
            {
                if (browse)
                {
                    this.DrawBrowse(s);
                }
            }

            ImGui.SameLine();
            using (var graph = ImRaii.Child("AtlasGraph", new Vector2(graphWidth, bodyHeight), true, ImGuiWindowFlags.NoScrollbar | ImGuiWindowFlags.NoScrollWithMouse))
            {
                if (graph)
                {
                    DrawGraph(s);
                }
            }
        }

        ImGui.SameLine();
        using (var details = ImRaii.Child("AtlasDetails", new Vector2(detailsWidth, bodyHeight), true))
        {
            if (details)
            {
                if (s.Lens == AtlasLens.Changes)
                {
                    DrawChangeDetails(s);
                }
                else if (s.ShowsWholeCast)
                {
                    DrawArcPanel(s);
                }
                else if (NoArcHere(s))
                {
                    Muted(AtlasText.NoArcHere);
                }
                else
                {
                    DrawDetails(s);
                }
            }
        }

        ImGui.TextColored(MutedColor, AtlasText.ContentViewHelp);

        this.DrawConfirmModal(s);
    }

    /// <summary>The Arc lens with no arc covering the view (L7): the picker stays, everything else says so.</summary>
    private static bool NoArcHere(AtlasSession s) => s.Lens == AtlasLens.Arc && s.Arc is null;

    /// <summary>The v2 lens bar (D6): the lens switch, the position line, and the coverage note on slice steps.</summary>
    private static void DrawLensBar(AtlasSession s)
    {
        ImGui.AlignTextToFramePadding();
        ImGui.TextColored(MutedColor, AtlasText.LensLabelHeading);
        AtlasLens? picked = null;
        foreach (var option in s.LensOptions)
        {
            ImGui.SameLine();
            if (ToggleButton($"{option.Label}##lens-{option.Lens}", option.IsCurrent) && !option.IsCurrent)
            {
                picked = option.Lens;
            }
        }

        // The position line moves to its own row when the window is too narrow for it.
        SameLineIfFits(ImGui.CalcTextSize(s.PositionLabel).X, 16 * ImGuiHelpers.GlobalScale);
        ImGui.AlignTextToFramePadding();
        ImGui.TextUnformatted(s.PositionLabel);
        if (s.CoverageNote is { } coverage)
        {
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, coverage);
            ImGui.PopTextWrapPos();
        }

        if (picked is { } lens)
        {
            s.SetLens(lens);
        }
    }

    private void DrawTopBar(AtlasSession s)
    {
        var scale = ImGuiHelpers.GlobalScale;
        var options = s.CheckpointOptions;
        var view = options.First(o => o.IsView);
        var ceiling = options.First(o => o.IsCeiling);

        ImGui.AlignTextToFramePadding();
        ImGui.TextColored(MutedColor, AtlasText.ViewLabel);
        ImGui.SameLine();

        // The picker gives up width before anything is pushed past the window edge (minimum 760 px wide).
        ImGui.SetNextItemWidth(Math.Clamp(ImGui.GetContentRegionAvail().X, 160 * scale, 300 * scale));
        using (var combo = ImRaii.Combo("##AtlasView", view.Label))
        {
            foreach (var option in combo ? options : Array.Empty<AtlasCheckpointOption>())
            {
                using (ImRaii.Disabled(!option.ViewSelectable))
                {
                    var label = option.ViewSelectable ? option.Label : AtlasText.LockedCheckpoint(option.Label);
                    if (ImGui.Selectable($"{label}##view-{option.Id}", option.IsView) && !option.IsView)
                    {
                        s.SetView(option.Id);
                    }
                }
            }
        }

        // The spoiler-limit group (label, limit, Raise…) wraps to its own row as a whole when it doesn't fit, so Raise…
        // is always on screen.
        var spacing = ImGui.GetStyle().ItemSpacing.X;
        var limitWidth = ImGui.CalcTextSize(AtlasText.CeilingLabel).X + spacing + ImGui.CalcTextSize(ceiling.Label).X + spacing
            + ImGui.CalcTextSize(AtlasText.RaiseButton).X + (ImGui.GetStyle().FramePadding.X * 2);
        SameLineIfFits(limitWidth, 20 * scale);
        ImGui.AlignTextToFramePadding();
        ImGui.TextColored(MutedColor, AtlasText.CeilingLabel);
        ImGui.SameLine();
        ImGui.TextUnformatted(ceiling.Label);
        ImGui.SameLine();
        if (ImGui.Button($"{AtlasText.RaiseButton}##AtlasRaise"))
        {
            ImGui.OpenPopup(LimitMenuId);
        }

        using (var menu = ImRaii.Popup(LimitMenuId))
        {
            foreach (var option in menu ? options : Array.Empty<AtlasCheckpointOption>())
            {
                if (option.IsCeiling)
                {
                    using (ImRaii.Disabled())
                    {
                        ImGui.Selectable($"{option.Label}##limit-{option.Id}", true);
                    }

                    continue;
                }

                if (ImGui.Selectable($"{option.Label}##limit-{option.Id}"))
                {
                    if (s.RequestCeiling(option.Id) == AtlasStateChange.NeedsConfirmation)
                    {
                        this.openConfirmNextFrame = true;
                    }
                }
            }
        }

        ImGui.AlignTextToFramePadding();
        ImGui.TextColored(MutedColor, AtlasText.ContentLabel);
        foreach (var contentView in new[] { AtlasContentView.MainAndOptional, AtlasContentView.MainStory })
        {
            ImGui.SameLine();
            var active = s.ContentView == contentView;
            if (ToggleButton($"{AtlasText.ContentViewLabel(contentView)}##cv-{contentView}", active) && !active)
            {
                s.SetContentView(contentView);
            }
        }
    }

    private void DrawBrowse(AtlasSession s)
    {
        if (s.Lens == AtlasLens.Arc)
        {
            DrawArcPicker(s);

            // L7: with no arc here the browse pane is empty apart from the picker, so there is nothing to search.
            if (s.Arc is null)
            {
                return;
            }
        }

        if (!string.Equals(s.SearchQuery, this.syncedQuery, StringComparison.Ordinal))
        {
            this.searchBuffer = s.SearchQuery;
        }

        ImGui.SetNextItemWidth(-1);
        if (ImGui.InputTextWithHint("##AtlasSearch", AtlasText.SearchPlaceholder, ref this.searchBuffer, AtlasSnapshot.MaxSearchQueryLength, ImGuiInputTextFlags.EnterReturnsTrue))
        {
            s.SetSearch(this.searchBuffer);
            var first = s.SearchResultGroups.FirstOrDefault()?.Entries.FirstOrDefault();
            if (first is not null)
            {
                s.FocusOn(first.Id);
            }
        }
        else if (!string.Equals(this.searchBuffer, s.SearchQuery, StringComparison.Ordinal))
        {
            s.SetSearch(this.searchBuffer);
        }

        this.syncedQuery = s.SearchQuery;

        if (s.SelectionWasReset)
        {
            ImGui.Spacing();
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.SelectionReset);
            ImGui.PopTextWrapPos();
        }

        if (NoArcHere(s))
        {
            return;
        }

        if (s.CastHeading is { } castHeading)
        {
            ImGui.Spacing();
            ImGui.TextColored(MutedColor, castHeading.ToUpperInvariant());
            ImGui.Separator();
        }

        var groups = s.SearchResultGroups;
        if (groups.Count == 0)
        {
            ImGui.Spacing();
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.NoResults);
            ImGui.PopTextWrapPos();
            return;
        }

        foreach (var group in groups)
        {
            ImGui.Spacing();
            ImGui.TextColored(MutedColor, group.Label.ToUpperInvariant());
            ImGui.Separator();
            foreach (var entry in group.Entries)
            {
                var line = ImGui.GetTextLineHeight();
                var glyphSize = entry.Portrait is null ? line * 0.55f : line * 0.95f;
                var start = ImGui.GetCursorScreenPos();
                ImGui.Dummy(new Vector2(line + 4, 0));
                ImGui.SameLine(0, 0);
                if (ImGui.Selectable($"{entry.Name}##browse-{entry.Id}", s.FocusId == entry.Id))
                {
                    s.FocusOn(entry.Id);
                }

                if (ImGui.IsItemHovered() && ImGui.CalcTextSize(entry.Name).X > ImGui.GetItemRectSize().X)
                {
                    ImGui.SetTooltip(entry.Name);
                }

                var center = new Vector2(start.X + (line / 2), start.Y + (line / 2));
                this.DrawMark(ImGui.GetWindowDrawList(), entry.Category, entry.Portrait, center, glyphSize / 2, false, badge: false);
            }
        }
    }

    private void DrawGraph(AtlasSession s)
    {
        var drawList = ImGui.GetWindowDrawList();
        var origin = ImGui.GetCursorScreenPos();
        var size = ImGui.GetContentRegionAvail();
        var layout = s.Layout;
        if (layout is null)
        {
            var text = NoArcHere(s) ? AtlasText.NoArcHere : AtlasText.EmptyFocus;
            var textSize = ImGui.CalcTextSize(text);
            ImGui.SetCursorScreenPos(origin + ((size - textSize) / 2));
            ImGui.TextColored(MutedColor, text);
            return;
        }

        var scale = ImGuiHelpers.GlobalScale;
        var center = origin + (size / 2);
        var ring = Math.Min(size.X, size.Y) * (float)AtlasChartStyle.RingFraction;
        var focusRadius = 16 * scale;
        var nodeRadius = 11 * scale;
        var gap = AtlasChartStyle.Clearance * scale;
        Vector2 Pos(AtlasGraphNode n) => center + (new Vector2((float)n.X, (float)n.Y) * ring);
        var positions = layout.Nodes.ToDictionary(n => n.Entity.Id, Pos, StringComparer.Ordinal);

        // Portrait nodes scale with the ring but never shrink below a legible size (AtlasPortraitStyle).
        float Radius(AtlasGraphNode n) => n.Entity.Portrait is null
            ? (n.IsFocus ? focusRadius : nodeRadius)
            : Math.Max(
                (float)((n.IsFocus ? AtlasPortraitStyle.FocusRadius : AtlasPortraitStyle.NodeRadius) * ring),
                (n.IsFocus ? AtlasPortraitStyle.MinFocusPixels : AtlasPortraitStyle.MinNodePixels) * scale);
        var radii = layout.Nodes.ToDictionary(n => n.Entity.Id, Radius, StringComparer.Ordinal);
        var selectedId = s.SelectedRelationshipId;
        var edgeColor = ImGui.GetColorU32(EdgeColor);
        var accent = ImGui.GetColorU32(AccentColor);
        var spokeColor = ImGui.GetColorU32(EventColor with { W = 0.28f });
        var wholeCast = s.ShowsWholeCast;

        // Names sit outside the ring (above a node in the upper half, below it otherwise), so chords never cross them,
        // truncated to the gap between ring neighbours (AtlasChartStyle).
        var ringCount = layout.Nodes.Count(n => !n.IsFocus);
        var chord = ringCount >= 3 ? (float)(2 * ring * Math.Sin(Math.PI / ringCount)) - (8 * scale) : float.MaxValue;
        var names = new Dictionary<string, (string Text, bool Truncated, Vector2 Min, Vector2 Max)>(StringComparer.Ordinal);
        foreach (var node in layout.Nodes)
        {
            var p = positions[node.Entity.Id];
            var r = radii[node.Entity.Id];
            var maxWidth = node.IsFocus
                ? Math.Min(AtlasChartStyle.CentreNameMaxWidth * scale, (float)(AtlasChartStyle.CentreNameRingWidth * ring))
                : Math.Min(AtlasChartStyle.NameMaxWidth * scale, chord);
            var text = Truncate(node.Entity.Name, maxWidth, out var truncated);
            var textSize = ImGui.CalcTextSize(text);
            var above = !node.IsFocus && node.Y < -0.01;
            var top = above ? p.Y - r - (3 * scale) - textSize.Y : p.Y + r + (3 * scale);
            var min = new Vector2(p.X - (textSize.X / 2) - (2 * scale), top);
            names[node.Entity.Id] = (text, truncated, min, min + textSize + new Vector2(4 * scale, 0));
        }

        // Edges first, then labels and nodes on top.
        var labels = new List<(Vector2 P1, Vector2 P2, string Text, string RelationshipId, bool Selected, bool Optional)>();
        foreach (var edge in layout.Edges)
        {
            var a = positions[edge.FromId];
            var b = positions[edge.ToId];
            var delta = b - a;
            var length = Math.Max(delta.Length(), 1f);
            var dir = delta / length;
            var normal = new Vector2(-dir.Y, dir.X);
            var lane = (float)((edge.LaneIndex - ((edge.LaneCount - 1) / 2.0)) * 0.12 * ring);
            var p1 = a + (dir * (radii[edge.FromId] + (4 * scale))) + (normal * lane);
            var p2 = b - (dir * (radii[edge.ToId] + (4 * scale))) + (normal * lane);

            // D8: on the whole-cast chart a participation spoke is a faint line with no label, arrow or click target.
            if (edge.IsParticipation && wholeCast)
            {
                drawList.AddLine(p1, p2, spokeColor, 1f * scale);
                continue;
            }

            var selected = edge.Relationship.Id == selectedId;
            var color = selected ? accent : edgeColor;
            var thickness = (selected ? 2.2f : 1.4f) * scale;

            if (edge.Relationship.IsOptional)
            {
                DrawDashedLine(drawList, p1, p2, color, thickness, 6 * scale, 4 * scale);
            }
            else
            {
                drawList.AddLine(p1, p2, color, thickness);
            }

            if (!edge.Symmetric)
            {
                var tip = p2;
                var back = tip - (dir * 8 * scale);
                drawList.AddTriangleFilled(tip, back + (normal * 4 * scale), back - (normal * 4 * scale), color);
            }

            labels.Add((p1, p2, edge.Label, edge.Relationship.Id, selected, edge.Relationship.IsOptional));
        }

        // Each label sits on its edge at the first position that clears every node, name and placed label.
        var nodeDiscs = layout.Nodes.Select(n => (Center: positions[n.Entity.Id], Radius: radii[n.Entity.Id] + gap)).ToList();
        var blocked = names.Values.Select(n => (n.Min - new Vector2(gap, gap), n.Max + new Vector2(gap, gap))).ToList();
        foreach (var label in labels)
        {
            var textSize = ImGui.CalcTextSize(label.Text);
            var half = (textSize / 2) + new Vector2(3 * scale, 1 * scale);
            (Vector2 Min, Vector2 Max) Box(double t)
            {
                var at = label.P1 + ((label.P2 - label.P1) * (float)t);
                return (at - half, at + half);
            }

            var chosen = Box(0.5);
            foreach (var t in AtlasChartStyle.LabelPositions)
            {
                var box = Box(t);
                var padded = (box.Min - new Vector2(gap, gap), box.Max + new Vector2(gap, gap));
                if (!nodeDiscs.Any(d => RectHitsCircle(padded, d.Center, d.Radius)) && !blocked.Any(b => RectsOverlap(padded, b)))
                {
                    chosen = box;
                    break;
                }
            }

            blocked.Add(chosen);
            drawList.AddRectFilled(chosen.Min, chosen.Max, ImGui.GetColorU32(LabelBackColor), 3 * scale);
            ImGui.SetCursorScreenPos(chosen.Min);
            var clicked = ImGui.InvisibleButton($"##edge-{label.RelationshipId}", chosen.Max - chosen.Min);
            var hovered = ImGui.IsItemHovered();
            var textColor = label.Selected ? AccentColor : hovered ? HoverColor : MutedColor;
            drawList.AddText(((chosen.Min + chosen.Max) / 2) - (textSize / 2), ImGui.GetColorU32(textColor), label.Text);
            if (hovered)
            {
                ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
                if (label.Optional)
                {
                    ImGui.SetTooltip(AtlasText.OptionalTooltip);
                }
            }

            if (clicked)
            {
                s.SelectRelationship(label.RelationshipId);
            }
        }

        string? refocus = null;
        foreach (var node in layout.Nodes)
        {
            var p = positions[node.Entity.Id];
            var r = radii[node.Entity.Id];
            ImGui.SetCursorScreenPos(p - new Vector2(r, r));
            var clicked = ImGui.InvisibleButton($"##node-{node.Entity.Id}", new Vector2(r * 2, r * 2));
            var hovered = ImGui.IsItemHovered();
            var round = this.DrawMark(drawList, node.Entity.Category, node.Entity.Portrait, p, r, true, badge: true);
            if (node.IsFocus)
            {
                DrawMarkOutline(drawList, node.Entity.Category, round, p, r + (3 * scale), ImGui.GetColorU32(new Vector4(1, 1, 1, 0.6f)), 2 * scale);
            }
            else if (hovered)
            {
                DrawMarkOutline(drawList, node.Entity.Category, round, p, r + (2 * scale), ImGui.GetColorU32(HoverColor), 2 * scale);
            }

            var name = names[node.Entity.Id];
            drawList.AddRectFilled(name.Min, name.Max, ImGui.GetColorU32(LabelBackColor), 2 * scale);
            drawList.AddText(name.Min + new Vector2(2 * scale, 0), ImGui.GetColorU32(TextColor), name.Text);

            if (hovered)
            {
                ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
                ImGui.SetTooltip(node.Entity.Name);
            }
            else if (ImGui.IsMouseHoveringRect(name.Min, name.Max) && ImGui.IsWindowHovered())
            {
                // A node's name is part of its click target, as in the viewer.
                ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
                if (name.Truncated)
                {
                    ImGui.SetTooltip(node.Entity.Name);
                }

                clicked |= ImGui.IsMouseClicked(ImGuiMouseButton.Left);
            }

            // The arc entry at the centre of the whole-cast chart can always be clicked (L4); a focused node cannot.
            if (clicked && (!node.IsFocus || wholeCast))
            {
                refocus = node.Entity.Id;
            }
        }

        if (refocus is not null)
        {
            s.FocusOn(refocus);
        }
    }

    private void DrawDetails(AtlasSession s)
    {
        var focus = s.Focus;
        if (focus is null)
        {
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.EmptyFocus);
            ImGui.PopTextWrapPos();
            return;
        }

        // L4: refocused inside an arc, a button returns to the whole-cast chart.
        if (s.Lens == AtlasLens.Arc && s.Arc is not null)
        {
            if (ImGui.SmallButton($"< {AtlasText.WholeCastButton}##AtlasWholeCast"))
            {
                s.ShowWholeCast();
                return;
            }

            ImGui.Spacing();
        }

        DrawEntityHeader(focus, withAliases: true);
        ImGui.Spacing();
        DrawEntitySummary(focus);
        DrawSources(s, focus.Citations, "entity", AtlasText.SourcesToggle(focus.Citations.Count));

        var neighborhood = s.Neighborhood;
        var neighbors = neighborhood?.Neighbors ?? Array.Empty<AtlasNeighbor>();
        ImGui.Spacing();
        ImGui.TextColored(MutedColor, $"{AtlasText.ConnectionsHeading.ToUpperInvariant()} ({neighbors.Count})");
        ImGui.Separator();
        if (neighbors.Count == 0)
        {
            ImGui.TextColored(MutedColor, AtlasText.NoConnections);
        }

        string? refocus = null;
        string? select = null;
        foreach (var neighbor in neighbors)
        {
            var relationship = neighbor.Relationship;
            var selected = relationship.Id == s.SelectedRelationshipId;
            DrawDirectionArrow(neighbor.Direction, relationship.Symmetric, selected);
            ImGui.SameLine();

            // The row wraps inside the pane, so long names stay readable; the label selects, the name refocuses.
            var pieces = new List<FlowPiece>
            {
                new(neighbor.Label, selected ? AccentColor : MutedColor, $"rel-{relationship.Id}", "rel"),
                new(neighbor.Entity.Name, TextColor, $"who-{relationship.Id}-{neighbor.Entity.Id}", "who", Underline: true),
            };
            if (relationship.IsOptional)
            {
                pieces.Add(new($"[{AtlasText.OptionalTag}]", MutedColor));
            }

            if (neighborhood!.CanvasEntities.All(c => c.Id != neighbor.Entity.Id))
            {
                pieces.Add(new(AtlasText.ListOnlyMarker, MutedColor));
            }

            switch (Flow(pieces))
            {
                case "rel":
                    select = relationship.Id;
                    break;
                case "who":
                    refocus = neighbor.Entity.Id;
                    break;
            }
        }

        DrawSelectedCard(s);

        if (select is not null)
        {
            s.SelectRelationship(select);
        }

        if (refocus is not null)
        {
            s.FocusOn(refocus);
        }
    }

    /// <summary>Collapsible sources, collapsed by default (D1). The open state lives in the shared session.</summary>
    private static void DrawSources(AtlasSession s, IReadOnlyList<AtlasCitationView> citations, string scopeId, string label)
    {
        if (citations.Count == 0)
        {
            return;
        }

        ImGui.Spacing();
        ImGui.SetNextItemOpen(s.SourcesExpanded, ImGuiCond.Always);
        var open = ImGui.CollapsingHeader($"{label}##sources-{scopeId}");
        if (open != s.SourcesExpanded)
        {
            s.SetSourcesExpanded(open);
        }

        if (!open)
        {
            return;
        }

        ImGui.PushTextWrapPos();
        if (citations.Any(c => c.Url is not null))
        {
            ImGui.TextColored(MutedColor, AtlasText.ExternalLinkWarning);
        }

        for (var i = 0; i < citations.Count; i++)
        {
            var citation = citations[i];
            if (citation.Url is null)
            {
                ImGui.TextWrapped(citation.Title);
                continue;
            }

            // Long titles wrap; every word of a title is part of the same link.
            if (Flow([new(citation.Title, HoverColor, $"src-{scopeId}-{i}", "open", Underline: true, Tooltip: $"{AtlasText.ExternalLinkWarning}\n{citation.Url}")]) is not null)
            {
                OpenLink(citation.Url);
            }
        }

        ImGui.PopTextWrapPos();
    }

    /// <summary>The selected connection's card (L3), shared by the details pane and the arc panel: its sources and Close.</summary>
    private static void DrawSelectedCard(AtlasSession s)
    {
        var chosen = s.SelectedRelationship;
        if (chosen is null)
        {
            return;
        }

        ImGui.Spacing();
        ImGui.TextColored(MutedColor, AtlasText.SelectedConnectionHeading.ToUpperInvariant());
        ImGui.Separator();
        var source = s.Snapshot.FindEntity(chosen.SourceId)?.Name ?? string.Empty;
        var target = s.Snapshot.FindEntity(chosen.TargetId)?.Name ?? string.Empty;
        ImGui.PushTextWrapPos();
        ImGui.TextWrapped($"{source} {chosen.OutgoingLabel} {target}");
        ImGui.PopTextWrapPos();
        if (chosen.IsOptional)
        {
            OptionalTag(AtlasText.OptionalTag);
        }

        DrawSources(s, chosen.Citations, "relationship", AtlasText.SourcesToggle(chosen.Citations.Count));
        if (ImGui.SmallButton($"{AtlasText.CloseConnectionButton}##AtlasCloseConnection"))
        {
            s.ClearSelection();
        }
    }

    /// <summary>The Story arc picker (L5): "The arc at this point" first, then every arc the view has started.</summary>
    private static void DrawArcPicker(AtlasSession s)
    {
        var options = s.ArcPickerOptions;
        var current = options.FirstOrDefault(o => o.IsCurrent) ?? options[0];
        ImGui.TextColored(MutedColor, AtlasText.ArcPickerLabel);
        ImGui.SetNextItemWidth(-1);
        AtlasArcPickerOption? picked = null;
        using (var combo = ImRaii.Combo("##AtlasArcPicker", current.Label))
        {
            foreach (var option in combo ? options : Array.Empty<AtlasArcPickerOption>())
            {
                if (ImGui.Selectable($"{option.Label}##arc-{option.ArcId ?? "auto"}", option.IsCurrent) && !option.IsCurrent)
                {
                    picked = option;
                }
            }
        }

        if (picked is not null)
        {
            s.PickArc(picked.ArcId);
        }

        ImGui.Spacing();
    }

    /// <summary>The Arc lens at rest (L3): the arc's name, its reviewed recap, and what is new and what has ended so far.</summary>
    private void DrawArcPanel(AtlasSession s)
    {
        var arc = s.Arc!;
        if (s.SelectedRelationship is not null)
        {
            DrawSelectedCard(s);
            ImGui.Spacing();
            ImGui.Spacing();
        }

        var entry = arc.Entry;
        DrawEntityHeader(entry, withAliases: false);
        ImGui.Spacing();
        ImGui.PushTextWrapPos();
        ImGui.TextColored(AccentColor, arc.RecapLabel.ToUpperInvariant());
        if (arc.AsOfLabel is { } asOf)
        {
            ImGui.TextColored(MutedColor, asOf);
        }

        ImGui.TextWrapped(entry.Summary);
        ImGui.PopTextWrapPos();
        DrawSources(s, entry.Citations, "arc-entry", AtlasText.SourcesToggle(entry.Citations.Count));

        string? refocus = null;
        DrawRowSection(s.ArcNewHeading ?? AtlasText.ArcNewHeading, s.ArcNewRows, AtlasText.ArcNothingNew, ref refocus);
        DrawRowSection(AtlasText.ArcEndedHeading, s.ArcEndedRows, AtlasText.ArcNothingEnded, ref refocus);
        if (refocus is not null)
        {
            s.FocusOn(refocus);
        }
    }

    /// <summary>An Arc-panel row list. Names refocus; ended rows say when they ended and carry no sources of any kind.</summary>
    private static void DrawRowSection(string heading, IReadOnlyList<AtlasChangeRow> rows, string none, ref string? refocus)
    {
        ImGui.Spacing();
        ImGui.TextColored(MutedColor, heading.ToUpperInvariant());
        ImGui.Separator();
        if (rows.Count == 0)
        {
            Muted(none);
            return;
        }

        foreach (var row in rows)
        {
            if (row.Relationship is null)
            {
                continue;
            }

            var pieces = new List<FlowPiece>
            {
                new(row.Source!.Name, TextColor, $"arcrow-{row.Key}-s", row.Source.Id, Underline: true),
                new(row.Relationship.OutgoingLabel, MutedColor),
                new(row.Target!.Name, TextColor, $"arcrow-{row.Key}-t", row.Target.Id, Underline: true),
            };
            if (row.Relationship.IsOptional)
            {
                pieces.Add(new($"[{AtlasText.OptionalTag}]", MutedColor));
            }

            if (row.EndedInLabel is { } endedIn)
            {
                pieces.Add(new($"({endedIn})", MutedColor));
            }

            refocus = Flow(pieces) ?? refocus;
        }
    }

    /// <summary>The Changes lens (L8, L9): a heading, then Added (+), Ended (−) and Description updated (~) rows.</summary>
    private static void DrawChangesList(AtlasSession s)
    {
        if (!s.ChangesOffered)
        {
            Muted(AtlasText.ChangesNotOffered);
            return;
        }

        ImGui.TextUnformatted(s.ChangesLabel ?? string.Empty);
        var groups = s.ChangeGroups;
        if (groups.Count == 0)
        {
            ImGui.Spacing();
            Muted(AtlasText.NoChanges);
            return;
        }

        string? pick = null;
        foreach (var group in groups)
        {
            ImGui.Spacing();
            ImGui.TextColored(MutedColor, group.Label.ToUpperInvariant());
            ImGui.Separator();
            foreach (var row in group.Rows)
            {
                var mark = ChangeMark(row.Kind);
                var optional = row.Relationship?.IsOptional == true ? $"  [{AtlasText.OptionalTag}]" : string.Empty;
                if (WrappedSelectable(mark, row.Text + optional, $"change-{row.Key}", row.Key == s.SelectedChangeKey) && row.Key != s.SelectedChangeKey)
                {
                    pick = row.Key;
                }
            }
        }

        if (pick is not null)
        {
            s.SelectChange(pick);
        }
    }

    /// <summary>The selected change. End evidence appears here, on an "ended" row, and nowhere else (v2 spoiler rule 2).</summary>
    private void DrawChangeDetails(AtlasSession s)
    {
        // The reset hint only makes sense where there is something to pick.
        if (s.SelectionWasReset && s.ChangesOffered)
        {
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.SelectionReset);
            ImGui.PopTextWrapPos();
            ImGui.Spacing();
        }

        if (!s.ChangesOffered)
        {
            return;
        }

        var row = s.SelectedChange;
        if (row is null)
        {
            Muted(AtlasText.ChangesPickHint);
            return;
        }

        // What the row did, first, so an ended relationship never reads as current (council round 1).
        ImGui.PushTextWrapPos();
        ImGui.TextColored(AccentColor, $"{ChangeMark(row.Kind)} {s.SelectedChangeStatus}");
        ImGui.PopTextWrapPos();
        ImGui.Spacing();

        if (row.Entity is { } entity)
        {
            DrawEntityHeader(entity, withAliases: false);
            ImGui.Spacing();
            DrawEntitySummary(entity);
            DrawSources(s, entity.Citations, "change-entity", AtlasText.SourcesToggle(entity.Citations.Count));
            return;
        }

        var relationship = row.Relationship!;
        ImGui.PushTextWrapPos();
        ImGui.TextWrapped(row.Text);
        ImGui.PopTextWrapPos();
        if (relationship.IsOptional)
        {
            OptionalTag(AtlasText.OptionalTag);
        }

        DrawSources(s, relationship.Citations, "change-relationship", AtlasText.SourcesToggle(relationship.Citations.Count));
        if (row.Kind == AtlasChangeKind.Ended)
        {
            DrawSources(s, row.EndCitations, "change-ending", AtlasText.EndSourcesToggle(row.EndCitations.Count));
        }
    }

    private void DrawEntityHeader(AtlasEntityView entity, bool withAliases)
    {
        var meta = AtlasText.CategoryLabel(entity.Category) + (withAliases && entity.Aliases.Count > 0 ? " · " + string.Join(", ", entity.Aliases) : string.Empty);
        if (entity.Portrait is not null)
        {
            // A large portrait beside the name and category, as in the viewer's header.
            var size = AtlasPortraitStyle.HeaderSize * ImGuiHelpers.GlobalScale;
            var origin = ImGui.GetCursorScreenPos();
            ImGui.Dummy(new Vector2(size, size));
            this.DrawMark(ImGui.GetWindowDrawList(), entity.Category, entity.Portrait, origin + new Vector2(size / 2, size / 2), size / 2, false, badge: true);
            ImGui.SameLine();
            using (ImRaii.Group())
            {
                ImGui.SetCursorPosY(ImGui.GetCursorPosY() + Math.Max((size - (ImGui.GetTextLineHeightWithSpacing() * 2)) / 2, 0));
                ImGui.PushTextWrapPos();
                ImGui.TextUnformatted(entity.Name);
                ImGui.TextColored(MutedColor, meta);
                ImGui.PopTextWrapPos();
            }

            return;
        }

        var glyphSize = ImGui.GetTextLineHeight() * 0.6f;
        var start = ImGui.GetCursorScreenPos();
        ImGui.Dummy(new Vector2(glyphSize + 6, 0));
        ImGui.SameLine(0, 0);
        ImGui.PushTextWrapPos();
        ImGui.TextUnformatted(entity.Name);
        DrawGlyph(ImGui.GetWindowDrawList(), entity.Category, start + new Vector2(glyphSize / 2, ImGui.GetTextLineHeight() / 2), glyphSize / 2, ColorFor(entity.Category), false);
        ImGui.TextColored(MutedColor, meta);
        ImGui.PopTextWrapPos();
    }

    private static void DrawEntitySummary(AtlasEntityView entity)
    {
        ImGui.PushTextWrapPos();
        ImGui.TextWrapped(entity.Summary);
        if (entity.IncludesOptional)
        {
            OptionalTag(AtlasText.OptionalSummaryNote);
        }

        ImGui.PopTextWrapPos();
    }

    private static void Muted(string text)
    {
        ImGui.PushTextWrapPos();
        ImGui.TextColored(MutedColor, text);
        ImGui.PopTextWrapPos();
    }

    /// <summary>
    /// A run of inline text. A clickable piece (with <see cref="ClickId"/>) returns <see cref="Value"/> when any of its
    /// words is clicked; <see cref="Underline"/> gives it a faint persistent underline so it reads as clickable.
    /// </summary>
    private sealed record FlowPiece(string Text, Vector4 Color, string? ClickId = null, string? Value = null, bool Underline = false, string? Tooltip = null);

    /// <summary>
    /// Draws pieces inline, wrapping word by word at the pane edge so nothing runs past it. Starts on the current line
    /// (after a <c>SameLine</c>) or a fresh one. Returns the <see cref="FlowPiece.Value"/> of a clicked piece.
    /// </summary>
    private static string? Flow(IReadOnlyList<FlowPiece> pieces)
    {
        var space = ImGui.CalcTextSize(" ").X;
        var width = ImGui.GetContentRegionAvail().X;
        var used = 0f;
        string? clicked = null;
        foreach (var piece in pieces)
        {
            var words = piece.Text.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            for (var w = 0; w < words.Length; w++)
            {
                var word = words[w];
                var wordWidth = ImGui.CalcTextSize(word).X;
                if (used > 0)
                {
                    if (used + space + wordWidth > width)
                    {
                        // A new row starts at the pane's left edge with the pane's full width.
                        used = 0;
                        width = ImGui.GetContentRegionAvail().X;
                    }
                    else
                    {
                        ImGui.SameLine(0, space);
                        used += space;
                    }
                }

                if (piece.ClickId is not null)
                {
                    if (ClickableText(word, piece.Color, $"{piece.ClickId}-{w}", underline: piece.Underline, underlineColor: piece.Color with { W = 0.45f }))
                    {
                        clicked = piece.Value;
                    }
                }
                else
                {
                    ImGui.TextColored(piece.Color, word);
                }

                if (piece.Tooltip is not null && ImGui.IsItemHovered())
                {
                    ImGui.SetTooltip(piece.Tooltip);
                }

                used += wordWidth;
            }
        }

        return clicked;
    }

    private static string ChangeMark(AtlasChangeKind kind) => kind switch
    {
        AtlasChangeKind.Added => "+",
        AtlasChangeKind.Ended => "-",
        _ => "~",
    };

    /// <summary>A full-width selectable row whose text wraps under a fixed mark column, for long Changes rows.</summary>
    private static bool WrappedSelectable(string mark, string text, string id, bool selected)
    {
        var markWidth = ImGui.CalcTextSize("~").X + (10 * ImGuiHelpers.GlobalScale);
        var start = ImGui.GetCursorScreenPos();
        var wrap = Math.Max(ImGui.GetContentRegionAvail().X - markWidth, 40 * ImGuiHelpers.GlobalScale);
        var height = ImGui.CalcTextSize(text, false, wrap).Y;
        var clicked = ImGui.Selectable($"##{id}", selected, ImGuiSelectableFlags.None, new Vector2(0, height));
        var drawList = ImGui.GetWindowDrawList();
        drawList.AddText(start, ImGui.GetColorU32(MutedColor), mark);
        drawList.AddText(ImGui.GetFont(), ImGui.GetFontSize(), start + new Vector2(markWidth, 0), ImGui.GetColorU32(TextColor), text, wrap);
        return clicked;
    }

    /// <summary>Opens only explicit http(s) links, only on click. Nothing is fetched automatically.</summary>
    private static void OpenLink(Uri url)
    {
        if (url.Scheme != Uri.UriSchemeHttp && url.Scheme != Uri.UriSchemeHttps)
        {
            return;
        }

        Util.OpenLink(url.AbsoluteUri);
    }

    private void DrawConfirmModal(AtlasSession s)
    {
        if (this.openConfirmNextFrame)
        {
            ImGui.OpenPopup(ConfirmModalId);
            this.openConfirmNextFrame = false;
        }

        var pending = s.PendingCeilingId;
        ImGui.SetNextWindowSize(new Vector2(420 * ImGuiHelpers.GlobalScale, 0), ImGuiCond.Appearing);
        using var modal = ImRaii.PopupModal(ConfirmModalId, ImGuiWindowFlags.AlwaysAutoResize);
        if (!modal)
        {
            return;
        }

        if (pending is null)
        {
            ImGui.CloseCurrentPopup();
            return;
        }

        ImGui.PushTextWrapPos(400 * ImGuiHelpers.GlobalScale);
        ImGui.TextWrapped(s.PendingCeilingPrompt ?? string.Empty);
        ImGui.PopTextWrapPos();
        ImGui.Spacing();
        if (ImGui.Button($"{AtlasText.CancelRaiseButton}##AtlasCancelRaise"))
        {
            s.CancelPendingCeiling();
            ImGui.CloseCurrentPopup();
        }

        ImGui.SameLine();
        if (ImGui.Button($"{AtlasText.ConfirmRaiseButton}##AtlasConfirmRaise"))
        {
            s.ConfirmPendingCeiling();
            ImGui.CloseCurrentPopup();
        }
    }

    private static Vector4 ColorFor(AtlasCategory category) => AtlasText.CategoryGlyph(category) switch
    {
        AtlasGlyph.Square => OrganizationColor,
        AtlasGlyph.Diamond => LocationColor,
        AtlasGlyph.Hexagon => EventColor,
        _ => CharacterColor,
    };

    /// <summary>
    /// An entity's mark: its reviewed portrait from the game's own icons, clipped round inside a ring in the category
    /// colour with the category shape as a badge, or the category shape alone when there is no portrait or its texture
    /// is not loaded yet (NDL-011). Returns true when it drew a round portrait.
    /// </summary>
    private bool DrawMark(ImDrawListPtr drawList, AtlasCategory category, AtlasPortrait? portrait, Vector2 center, float radius, bool border, bool badge)
    {
        if (portrait is null || !this.TryPortraitTexture(portrait, out var wrap))
        {
            DrawGlyph(drawList, category, center, portrait is null ? radius : radius * 0.8f, ColorFor(category), border);
            return false;
        }

        var (u0, v0, u1, v1) = portrait.Uv(wrap.Width, wrap.Height);
        var half = new Vector2(radius, radius);
        drawList.AddImageRounded(wrap.Handle, center - half, center + half, new Vector2((float)u0, (float)v0), new Vector2((float)u1, (float)v1), 0xFFFFFFFF, radius);
        drawList.AddCircle(center, radius, ImGui.GetColorU32(ColorFor(category)), 0, Math.Max((float)(radius * AtlasPortraitStyle.RingWidth), 1.5f));
        if (badge)
        {
            var offset = (float)(radius * AtlasPortraitStyle.BadgeOffset);
            DrawGlyph(drawList, category, center + new Vector2(offset, offset), (float)(radius * AtlasPortraitStyle.BadgeRadius), ColorFor(category), true);
        }

        return true;
    }

    /// <summary>The game icon's texture, once Dalamud has loaded it from the game data. Never throws.</summary>
    private bool TryPortraitTexture(AtlasPortrait portrait, out IDalamudTextureWrap wrap)
    {
        wrap = null!;
        try
        {
            if (this.textures.GetFromGameIcon(new GameIconLookup(portrait.GameIcon, false, true)).TryGetWrap(out var loaded, out _) && loaded is not null)
            {
                wrap = loaded;
                return true;
            }
        }
        catch (Exception exception)
        {
            Plugin.Log.Verbose(exception, $"Lore Atlas portrait icon {portrait.GameIcon} is unavailable; drawing the category shape.");
        }

        return false;
    }

    private static void DrawMarkOutline(ImDrawListPtr drawList, AtlasCategory category, bool round, Vector2 center, float radius, uint color, float thickness)
    {
        if (round)
        {
            drawList.AddCircle(center, radius, color, 0, thickness);
        }
        else
        {
            DrawGlyphOutline(drawList, category, center, radius, color, thickness);
        }
    }

    private static void DrawGlyph(ImDrawListPtr drawList, AtlasCategory category, Vector2 center, float radius, Vector4 color, bool border)
    {
        var fill = ImGui.GetColorU32(color);
        var dark = ImGui.GetColorU32(new Vector4(0.055f, 0.059f, 0.071f, 1f));
        switch (AtlasText.CategoryGlyph(category))
        {
            case AtlasGlyph.Square:
                drawList.AddRectFilled(center - new Vector2(radius, radius), center + new Vector2(radius, radius), fill, radius * 0.15f);
                break;
            case AtlasGlyph.Diamond:
                var d = radius * 1.25f;
                drawList.AddQuadFilled(center - new Vector2(0, d), center + new Vector2(d, 0), center + new Vector2(0, d), center - new Vector2(d, 0), fill);
                break;
            case AtlasGlyph.Hexagon:
                drawList.AddNgonFilled(center, radius * 1.15f, fill, 6);
                break;
            default:
                drawList.AddCircleFilled(center, radius, fill);
                break;
        }

        if (border)
        {
            DrawGlyphOutline(drawList, category, center, radius, dark, 1.2f * ImGuiHelpers.GlobalScale);
        }
    }

    private static void DrawGlyphOutline(ImDrawListPtr drawList, AtlasCategory category, Vector2 center, float radius, uint color, float thickness)
    {
        switch (AtlasText.CategoryGlyph(category))
        {
            case AtlasGlyph.Square:
                drawList.AddRect(center - new Vector2(radius, radius), center + new Vector2(radius, radius), color, radius * 0.15f, ImDrawFlags.None, thickness);
                break;
            case AtlasGlyph.Diamond:
                var d = radius * 1.25f;
                drawList.AddQuad(center - new Vector2(0, d), center + new Vector2(d, 0), center + new Vector2(0, d), center - new Vector2(d, 0), color, thickness);
                break;
            case AtlasGlyph.Hexagon:
                drawList.AddNgon(center, radius * 1.15f, color, 6, thickness);
                break;
            default:
                drawList.AddCircle(center, radius, color, 0, thickness);
                break;
        }
    }

    /// <summary>ImGui has no dash style, so optional edges are drawn as short segments (D3).</summary>
    private static void DrawDashedLine(ImDrawListPtr drawList, Vector2 from, Vector2 to, uint color, float thickness, float dash, float gap)
    {
        var delta = to - from;
        var length = delta.Length();
        if (length <= 0)
        {
            return;
        }

        var dir = delta / length;
        for (var t = 0f; t < length; t += dash + gap)
        {
            drawList.AddLine(from + (dir * t), from + (dir * Math.Min(t + dash, length)), color, thickness);
        }
    }

    /// <summary>Direction drawn as a small arrow, so it never depends on font glyph coverage (← → ↔ in the viewer).</summary>
    private static void DrawDirectionArrow(AtlasDirection direction, bool symmetric, bool selected)
    {
        var scale = ImGuiHelpers.GlobalScale;
        var size = new Vector2(14 * scale, ImGui.GetTextLineHeight());
        var start = ImGui.GetCursorScreenPos();
        ImGui.Dummy(size);
        var drawList = ImGui.GetWindowDrawList();
        var color = ImGui.GetColorU32(selected ? AccentColor : MutedColor);
        var y = start.Y + (size.Y / 2);
        var left = new Vector2(start.X + (2 * scale), y);
        var right = new Vector2(start.X + size.X - (2 * scale), y);
        drawList.AddLine(left, right, color, 1.2f * scale);
        var head = 3.5f * scale;
        if (symmetric || direction == AtlasDirection.Outgoing)
        {
            drawList.AddTriangleFilled(right, right - new Vector2(head, head), right - new Vector2(head, -head), color);
        }

        if (symmetric || direction == AtlasDirection.Incoming)
        {
            drawList.AddTriangleFilled(left, left + new Vector2(head, head), left + new Vector2(head, -head), color);
        }
    }

    private static bool ClickableText(string text, Vector4 color, string id, bool underline = false, Vector4? underlineColor = null)
    {
        var start = ImGui.GetCursorScreenPos();
        var size = ImGui.CalcTextSize(text);
        var clicked = ImGui.InvisibleButton($"##{id}", new Vector2(Math.Max(size.X, 1), Math.Max(size.Y, 1)));
        var hovered = ImGui.IsItemHovered();
        var drawList = ImGui.GetWindowDrawList();
        drawList.AddText(start, ImGui.GetColorU32(hovered ? HoverColor : color), text);
        if (hovered || underline)
        {
            var line = hovered ? HoverColor : underlineColor ?? color;
            drawList.AddLine(new Vector2(start.X, start.Y + size.Y), new Vector2(start.X + size.X, start.Y + size.Y), ImGui.GetColorU32(line), 1f);
        }

        if (hovered)
        {
            ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
        }

        return clicked;
    }

    private static void OptionalTag(string text)
    {
        ImGui.TextColored(MutedColor, $"[{text}]");
        if (ImGui.IsItemHovered())
        {
            ImGui.SetTooltip(AtlasText.OptionalTooltip);
        }
    }

    /// <summary>Continues the current row when <paramref name="width"/> still fits on it, otherwise starts a new row.</summary>
    private static void SameLineIfFits(float width, float spacing)
    {
        var rowEnd = ImGui.GetWindowPos().X + ImGui.GetWindowContentRegionMax().X;
        if (ImGui.GetItemRectMax().X + spacing + width <= rowEnd)
        {
            ImGui.SameLine(0, spacing);
        }
    }

    /// <summary>
    /// A segmented-control button. The active one is filled and underlined in the accent colour, so the choice never
    /// rests on a slight colour difference alone.
    /// </summary>
    private static bool ToggleButton(string label, bool active)
    {
        bool clicked;
        using (ImRaii.PushColor(ImGuiCol.Button, SelectedButtonColor, active))
        {
            clicked = ImGui.Button(label);
        }

        if (active)
        {
            var min = ImGui.GetItemRectMin();
            var max = ImGui.GetItemRectMax();
            var inset = 4 * ImGuiHelpers.GlobalScale;
            ImGui.GetWindowDrawList().AddLine(new Vector2(min.X + inset, max.Y - 1), new Vector2(max.X - inset, max.Y - 1), ImGui.GetColorU32(AccentColor), 2 * ImGuiHelpers.GlobalScale);
        }

        return clicked;
    }

    private static bool RectsOverlap((Vector2 Min, Vector2 Max) a, (Vector2 Min, Vector2 Max) b) =>
        a.Min.X < b.Max.X && b.Min.X < a.Max.X && a.Min.Y < b.Max.Y && b.Min.Y < a.Max.Y;

    private static bool RectHitsCircle((Vector2 Min, Vector2 Max) rect, Vector2 center, float radius)
    {
        var nearest = Vector2.Clamp(center, rect.Min, rect.Max);
        return Vector2.DistanceSquared(nearest, center) < radius * radius;
    }

    private static string Truncate(string text, float maxWidth, out bool truncated)
    {
        truncated = false;
        if (ImGui.CalcTextSize(text).X <= maxWidth)
        {
            return text;
        }

        truncated = true;
        const string ellipsis = "…";
        var end = text.Length;
        while (end > 1 && ImGui.CalcTextSize(text[..end] + ellipsis).X > maxWidth)
        {
            end--;
        }

        return text[..end].TrimEnd() + ellipsis;
    }
}
