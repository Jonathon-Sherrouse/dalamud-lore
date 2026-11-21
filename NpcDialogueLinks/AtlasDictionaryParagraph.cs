using System.Globalization;
using System.Numerics;
using System.Text.RegularExpressions;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Utility.Raii;

namespace NpcDialogueLinks;

internal static partial class AtlasDictionaryParagraph
{
    private static readonly Vector4 LinkColor = new(0.498f, 0.698f, 0.898f, 1);

    public static void Draw(string text, IReadOnlyList<AtlasTermMatch> links, Action<string> openTerm)
    {
        var width = Math.Max(1, ImGui.GetContentRegionAvail().X);
        var spacing = ImGui.GetStyle().ItemSpacing;
        var linkIndex = 0;
        using (ImRaii.PushStyle(ImGuiStyleVar.ItemSpacing, new Vector2(spacing.X, 0)))
        {
            for (var start = 0; start < text.Length;)
            {
                var newline = text.IndexOf('\n', start);
                var end = newline < 0 ? text.Length : newline;
                DrawWrappedLine(text, start, end, width, links, ref linkIndex, openTerm);
                start = end + 1;
            }
        }

        ImGui.SetCursorPosY(ImGui.GetCursorPosY() + spacing.Y);
    }

    private static void DrawWrappedLine(string text, int start, int end, float width, IReadOnlyList<AtlasTermMatch> links,
        ref int linkIndex, Action<string> openTerm)
    {
        var lineStart = start;
        var lineEnd = start;
        foreach (var word in Words().EnumerateMatches(text.AsSpan(start, end - start)))
        {
            var wordStart = start + word.Index;
            var wordEnd = wordStart + word.Length;
            if (lineStart == lineEnd && lineStart > start)
            {
                lineStart = wordStart;
            }

            if (lineEnd > lineStart && ImGui.CalcTextSize(text[lineStart..wordEnd]).X > width)
            {
                DrawLine(text, lineStart, lineEnd, links, ref linkIndex, openTerm);
                lineStart = wordStart;
            }

            // Break an unusually long word at a text-element boundary in a narrow pane.
            while (ImGui.CalcTextSize(text[lineStart..wordEnd]).X > width)
            {
                var split = lineStart + StringInfo.GetNextTextElementLength(text.AsSpan(lineStart, wordEnd - lineStart));
                while (split < wordEnd)
                {
                    var next = split + StringInfo.GetNextTextElementLength(text.AsSpan(split, wordEnd - split));
                    if (ImGui.CalcTextSize(text[lineStart..next]).X > width)
                    {
                        break;
                    }

                    split = next;
                }

                DrawLine(text, lineStart, split, links, ref linkIndex, openTerm);
                lineStart = split;
                if (split == wordEnd)
                {
                    break;
                }
            }

            lineEnd = wordEnd;
        }

        if (lineStart < end || start == end)
        {
            DrawLine(text, lineStart, end, links, ref linkIndex, openTerm);
        }
    }

    private static void DrawLine(string text, int start, int end, IReadOnlyList<AtlasTermMatch> links,
        ref int linkIndex, Action<string> openTerm)
    {
        if (start == end)
        {
            ImGui.NewLine();
            return;
        }

        for (var cursor = start; cursor < end;)
        {
            while (linkIndex < links.Count && links[linkIndex].Start + links[linkIndex].Term.Length <= cursor)
            {
                linkIndex++;
            }

            if (cursor > start)
            {
                ImGui.SameLine(0, 0);
            }

            var link = linkIndex < links.Count ? links[linkIndex] : null;
            if (link is null || link.Start > cursor)
            {
                var next = Math.Min(end, link?.Start ?? end);
                ImGui.TextUnformatted(text[cursor..next]);
                cursor = next;
            }
            else
            {
                var next = Math.Min(end, link.Start + link.Term.Length);
                DrawLink(text[cursor..next], cursor, link, openTerm);
                cursor = next;
            }
        }
    }

    private static void DrawLink(string text, int start, AtlasTermMatch match, Action<string> openTerm)
    {
        var origin = ImGui.GetCursorScreenPos();
        var size = ImGui.CalcTextSize(text);
        var clicked = ImGui.InvisibleButton($"##AtlasTerm-{start}", new Vector2(Math.Max(1, size.X), size.Y));
        var hovered = ImGui.IsItemHovered();
        var drawList = ImGui.GetWindowDrawList();
        var color = hovered ? ImGui.GetColorU32(LinkColor) : ImGui.GetColorU32(ImGuiCol.Text);
        drawList.AddText(origin, color, text);
        var underline = ImGui.GetColorU32(LinkColor with { W = hovered ? 1f : 0.45f });
        for (var offset = 0f; offset < size.X; offset += 3f)
        {
            var y = origin.Y + size.Y - 1;
            drawList.AddLine(new Vector2(origin.X + offset, y), new Vector2(origin.X + Math.Min(offset + 1.5f, size.X), y), underline, 1);
        }

        if (hovered)
        {
            ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
            ImGui.BeginTooltip();
            ImGui.PushTextWrapPos(ImGui.GetFontSize() * 30);
            ImGui.TextUnformatted(match.Definition);
            ImGui.PopTextWrapPos();
            ImGui.EndTooltip();
        }

        if (clicked)
        {
            openTerm(match.Term);
        }
    }

    [GeneratedRegex(@"\S+")]
    private static partial Regex Words();
}
