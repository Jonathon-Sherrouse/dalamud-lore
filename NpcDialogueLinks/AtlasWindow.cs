using System.Numerics;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Utility;
using Dalamud.Interface.Utility.Raii;
using Dalamud.Interface.Windowing;
using Dalamud.Utility;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks;

/// <summary>
/// The in-game Lore Atlas (NDL-004). A thin ImGui renderer over the shared <see cref="AtlasSession"/>: every browsing
/// rule and player-facing string lives in NpcDialogueLinks/Atlas/, and the local viewer renders the same session.
/// Layout and visual language follow docs/atlas/ux-design.md (NDL-005).
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

    private readonly string dataPath;
    private readonly PluginConfiguration configuration;

    private AtlasSession? session;
    private bool loadFailed;
    private string searchBuffer = string.Empty;
    private bool openConfirmNextFrame;

    public AtlasWindow(string dataPath, PluginConfiguration configuration)
        : base($"{AtlasText.WindowTitle}###NpcDialogueLinksAtlas")
    {
        this.dataPath = dataPath;
        this.configuration = configuration;
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

        var footerHeight = ImGui.GetTextLineHeightWithSpacing() + (ImGui.GetStyle().ItemSpacing.Y * 2);
        var bodyHeight = Math.Max(ImGui.GetContentRegionAvail().Y - footerHeight, 100 * scale);
        var browseWidth = 200 * scale;
        var detailsWidth = 280 * scale;
        var graphWidth = Math.Max(ImGui.GetContentRegionAvail().X - browseWidth - detailsWidth - (ImGui.GetStyle().ItemSpacing.X * 2), 120 * scale);

        // ImRaii scopes end every child and popup even if drawing throws, so a failure stays inside the Atlas.
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

        ImGui.SameLine();
        using (var details = ImRaii.Child("AtlasDetails", new Vector2(detailsWidth, bodyHeight), true))
        {
            if (details)
            {
                DrawDetails(s);
            }
        }
        ImGui.TextColored(MutedColor, AtlasText.ContentViewHelp);

        this.DrawConfirmModal(s);
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
        ImGui.SetNextItemWidth(300 * scale);
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
                        this.searchBuffer = s.SearchQuery;
                    }
                }
            }
        }

        ImGui.SameLine(0, 20 * scale);
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

                    this.searchBuffer = s.SearchQuery;
                }
            }
        }

        ImGui.AlignTextToFramePadding();
        ImGui.TextColored(MutedColor, AtlasText.ContentLabel);
        foreach (var contentView in new[] { AtlasContentView.MainAndOptional, AtlasContentView.MainStory })
        {
            ImGui.SameLine();
            var active = s.ContentView == contentView;
            using (ImRaii.PushColor(ImGuiCol.Button, SelectedButtonColor, active))
            {
                if (ImGui.Button($"{AtlasText.ContentViewLabel(contentView)}##cv-{contentView}") && !active)
                {
                    s.SetContentView(contentView);
                    this.searchBuffer = s.SearchQuery;
                }
            }
        }
    }

    private void DrawBrowse(AtlasSession s)
    {
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

        if (s.SelectionWasReset)
        {
            ImGui.Spacing();
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.SelectionReset);
            ImGui.PopTextWrapPos();
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
                var glyphSize = ImGui.GetTextLineHeight() * 0.55f;
                var start = ImGui.GetCursorScreenPos();
                ImGui.Dummy(new Vector2(glyphSize + 4, 0));
                ImGui.SameLine(0, 0);
                if (ImGui.Selectable($"{entry.Name}##browse-{entry.Id}", s.FocusId == entry.Id))
                {
                    s.FocusOn(entry.Id);
                }

                if (ImGui.IsItemHovered() && ImGui.CalcTextSize(entry.Name).X > ImGui.GetItemRectSize().X)
                {
                    ImGui.SetTooltip(entry.Name);
                }

                var center = new Vector2(start.X + (glyphSize / 2), start.Y + (ImGui.GetTextLineHeight() / 2));
                DrawGlyph(ImGui.GetWindowDrawList(), entry.Category, center, glyphSize / 2, ColorFor(entry.Category), false);
            }
        }
    }

    private static void DrawGraph(AtlasSession s)
    {
        var drawList = ImGui.GetWindowDrawList();
        var origin = ImGui.GetCursorScreenPos();
        var size = ImGui.GetContentRegionAvail();
        var layout = s.Layout;
        if (layout is null)
        {
            var text = AtlasText.EmptyFocus;
            var textSize = ImGui.CalcTextSize(text);
            ImGui.SetCursorScreenPos(origin + ((size - textSize) / 2));
            ImGui.TextColored(MutedColor, text);
            return;
        }

        var scale = ImGuiHelpers.GlobalScale;
        var center = origin + (size / 2);
        var ring = Math.Min(size.X * 0.36f, size.Y * 0.36f);
        var focusRadius = 16 * scale;
        var nodeRadius = 11 * scale;
        Vector2 Pos(AtlasGraphNode n) => center + (new Vector2((float)n.X, (float)n.Y) * ring);
        var positions = layout.Nodes.ToDictionary(n => n.Entity.Id, Pos, StringComparer.Ordinal);
        var radii = layout.Nodes.ToDictionary(n => n.Entity.Id, n => n.IsFocus ? focusRadius : nodeRadius, StringComparer.Ordinal);
        var selectedId = s.SelectedRelationshipId;
        var edgeColor = ImGui.GetColorU32(EdgeColor);
        var accent = ImGui.GetColorU32(AccentColor);

        // Edges first, then labels and nodes on top.
        var labels = new List<(Vector2 Pos, string Text, string RelationshipId, bool Selected, bool Optional)>();
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

            var mid = ((p1 + p2) / 2) + (normal * 9 * scale);
            labels.Add((mid, edge.Label, edge.Relationship.Id, selected, edge.Relationship.IsOptional));
        }

        foreach (var label in labels)
        {
            var textSize = ImGui.CalcTextSize(label.Text);
            var min = label.Pos - (textSize / 2) - new Vector2(3 * scale, 1 * scale);
            var max = label.Pos + (textSize / 2) + new Vector2(3 * scale, 1 * scale);
            drawList.AddRectFilled(min, max, ImGui.GetColorU32(LabelBackColor), 3 * scale);
            ImGui.SetCursorScreenPos(min);
            var clicked = ImGui.InvisibleButton($"##edge-{label.RelationshipId}", max - min);
            var hovered = ImGui.IsItemHovered();
            var textColor = label.Selected ? AccentColor : hovered ? HoverColor : MutedColor;
            drawList.AddText(label.Pos - (textSize / 2), ImGui.GetColorU32(textColor), label.Text);
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
            DrawGlyph(drawList, node.Entity.Category, p, r, ColorFor(node.Entity.Category), true);
            if (node.IsFocus)
            {
                DrawGlyphOutline(drawList, node.Entity.Category, p, r + (3 * scale), ImGui.GetColorU32(new Vector4(1, 1, 1, 0.6f)), 2 * scale);
            }
            else if (hovered)
            {
                DrawGlyphOutline(drawList, node.Entity.Category, p, r + (2 * scale), ImGui.GetColorU32(HoverColor), 2 * scale);
            }

            // Name below the node, truncated to a fixed width, on a dark backing for legibility.
            var maxWidth = 150 * scale;
            var name = Truncate(node.Entity.Name, maxWidth, out var truncated);
            var nameSize = ImGui.CalcTextSize(name);
            var namePos = new Vector2(p.X - (nameSize.X / 2), p.Y + r + (3 * scale));
            drawList.AddRectFilled(namePos - new Vector2(2 * scale, 0), namePos + nameSize + new Vector2(2 * scale, 0), ImGui.GetColorU32(LabelBackColor), 2 * scale);
            drawList.AddText(namePos, ImGui.GetColorU32(new Vector4(0.902f, 0.910f, 0.933f, 1f)), name);

            if (hovered)
            {
                ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
                ImGui.SetTooltip(node.Entity.Name);
            }
            else if (truncated && ImGui.IsMouseHoveringRect(namePos, namePos + nameSize))
            {
                ImGui.SetTooltip(node.Entity.Name);
            }

            if (clicked && !node.IsFocus)
            {
                refocus = node.Entity.Id;
            }
        }

        if (refocus is not null)
        {
            s.FocusOn(refocus);
        }
    }

    private static void DrawDetails(AtlasSession s)
    {
        var focus = s.Focus;
        if (focus is null)
        {
            ImGui.PushTextWrapPos();
            ImGui.TextColored(MutedColor, AtlasText.EmptyFocus);
            ImGui.PopTextWrapPos();
            return;
        }

        var glyphSize = ImGui.GetTextLineHeight() * 0.6f;
        var start = ImGui.GetCursorScreenPos();
        ImGui.Dummy(new Vector2(glyphSize + 6, 0));
        ImGui.SameLine(0, 0);
        ImGui.PushTextWrapPos();
        ImGui.TextUnformatted(focus.Name);
        DrawGlyph(ImGui.GetWindowDrawList(), focus.Category, start + new Vector2(glyphSize / 2, ImGui.GetTextLineHeight() / 2), glyphSize / 2, ColorFor(focus.Category), false);

        var meta = AtlasText.CategoryLabel(focus.Category) + (focus.Aliases.Count > 0 ? " · " + string.Join(", ", focus.Aliases) : string.Empty);
        ImGui.TextColored(MutedColor, meta);
        ImGui.Spacing();
        ImGui.TextWrapped(focus.Summary);
        if (focus.IncludesOptional)
        {
            OptionalTag(AtlasText.OptionalSummaryNote);
        }

        ImGui.PopTextWrapPos();
        DrawSources(s, focus.Citations, "entity");

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
            if (ClickableText(neighbor.Label, selected ? AccentColor : MutedColor, $"rel-{relationship.Id}"))
            {
                select = relationship.Id;
            }

            ImGui.SameLine();
            if (ClickableText(neighbor.Entity.Name, new Vector4(0.902f, 0.910f, 0.933f, 1f), $"who-{relationship.Id}-{neighbor.Entity.Id}"))
            {
                refocus = neighbor.Entity.Id;
            }

            if (relationship.IsOptional)
            {
                ImGui.SameLine();
                OptionalTag(AtlasText.OptionalTag);
            }

            if (neighborhood!.CanvasEntities.All(c => c.Id != neighbor.Entity.Id))
            {
                ImGui.SameLine();
                ImGui.TextColored(MutedColor, AtlasText.ListOnlyMarker);
            }
        }

        var chosen = s.SelectedRelationship;
        if (chosen is not null)
        {
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

            DrawSources(s, chosen.Citations, "relationship");
            if (ImGui.SmallButton($"{AtlasText.CloseConnectionButton}##AtlasCloseConnection"))
            {
                s.ClearSelection();
            }
        }

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
    private static void DrawSources(AtlasSession s, IReadOnlyList<AtlasCitationView> citations, string scopeId)
    {
        if (citations.Count == 0)
        {
            return;
        }

        ImGui.Spacing();
        ImGui.SetNextItemOpen(s.SourcesExpanded, ImGuiCond.Always);
        var open = ImGui.CollapsingHeader($"{AtlasText.SourcesToggle(citations.Count)}##sources-{scopeId}");
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

            if (ClickableText(citation.Title, HoverColor, $"src-{scopeId}-{i}", underline: true))
            {
                OpenLink(citation.Url);
            }

            if (ImGui.IsItemHovered())
            {
                ImGui.SetTooltip($"{AtlasText.ExternalLinkWarning}\n{citation.Url}");
            }
        }

        ImGui.PopTextWrapPos();
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
            this.searchBuffer = s.SearchQuery;
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

    private static bool ClickableText(string text, Vector4 color, string id, bool underline = false)
    {
        var start = ImGui.GetCursorScreenPos();
        var size = ImGui.CalcTextSize(text);
        var clicked = ImGui.InvisibleButton($"##{id}", new Vector2(Math.Max(size.X, 1), Math.Max(size.Y, 1)));
        var hovered = ImGui.IsItemHovered();
        var drawList = ImGui.GetWindowDrawList();
        drawList.AddText(start, ImGui.GetColorU32(hovered ? HoverColor : color), text);
        if (hovered || underline)
        {
            drawList.AddLine(new Vector2(start.X, start.Y + size.Y), new Vector2(start.X + size.X, start.Y + size.Y), ImGui.GetColorU32(hovered ? HoverColor : color), 1f);
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
