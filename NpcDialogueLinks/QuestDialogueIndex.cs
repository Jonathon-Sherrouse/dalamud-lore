using System.Globalization;
using System.Text.RegularExpressions;
using Lumina;
using Lumina.Data;
using Lumina.Excel;
using Lumina.Excel.Sheets;
using Lumina.Text.Payloads;
using Lumina.Text.ReadOnly;

namespace NpcDialogueLinks;

internal sealed record QuestDialogueMatch(string Status, uint? QuestRowId, string? QuestName);

internal sealed partial class QuestDialogueIndex
{
    private static readonly QuestDialogueMatch Unknown = new("unknown", null, null);
    private static readonly QuestDialogueMatch Ambiguous = new("ambiguous", null, null);
    private readonly Dictionary<string, Owner> owners = new(StringComparer.Ordinal);
    private readonly Dictionary<uint, QuestDialogueMatch> quests = [];

    private QuestDialogueIndex() { }

    public static QuestDialogueIndex Build(string sqpackPath, Language language, CancellationToken ct)
    {
        ct.ThrowIfCancellationRequested();
        // Loading thousands of Excel sheets into the shared Dalamud reader would keep them alive after indexing.
        using var game = new GameData(sqpackPath, new LuminaOptions { CacheFileResources = false });
        var quests = game.Excel.GetSheet<Quest>(language);
        var index = new QuestDialogueIndex();
        foreach (var path in game.Excel.SheetNames)
        {
            ct.ThrowIfCancellationRequested();
            if (!path.StartsWith("quest/", StringComparison.OrdinalIgnoreCase))
                continue;

            var scriptId = path[(path.LastIndexOf('/') + 1)..];
            var suffix = scriptId.LastIndexOf('_');
            if (suffix < 0 || !ushort.TryParse(scriptId.AsSpan(suffix + 1), NumberStyles.None, CultureInfo.InvariantCulture, out var shortId))
                throw new InvalidDataException($"Unrecognized quest script ID in {path}.");

            var ownerId = uint.MaxValue;
            var quest = quests.GetRowOrDefault(0x10000u + shortId);
            if (quest is { } rowMetadata && scriptId.Equals(rowMetadata.Id.ExtractText(), StringComparison.OrdinalIgnoreCase))
            {
                ownerId = rowMetadata.RowId;
                // The journal prefixes some titles with a quest-type icon.
                var title = rowMetadata.Name.ExtractText().Trim().TrimStart('\uE0BE', '\uE0BF').TrimStart();
                if (title.Length != 0)
                    index.quests.Add(ownerId, new QuestDialogueMatch("unique", ownerId, title));
            }

            var keyPrefix = $"TEXT_{scriptId}_";
            foreach (var row in game.Excel.GetSheet<RawRow>(language, path))
            {
                ct.ThrowIfCancellationRequested();
                var value = row.ReadStringColumn(1);
                if (value.IsEmpty || !IsLiteral(value))
                    continue;

                var text = DialogueText.Normalize(value.ExtractText());
                if (text.Length == 0)
                    continue;

                var key = row.ReadStringColumn(0).ExtractText();
                var isDialogue = key.StartsWith(keyPrefix, StringComparison.OrdinalIgnoreCase)
                    && SpokenKey().IsMatch(key.AsSpan(keyPrefix.Length));
                // Orphan/test scripts can veto a match, even when their numeric suffix points to another quest.
                index.Add(text, ownerId, isDialogue);
            }
        }

        ct.ThrowIfCancellationRequested();
        if (index.quests.Count == 0 || index.owners.Count == 0)
            throw new InvalidDataException("The game data contains no localized quest scripts.");

        return index;
    }

    public QuestDialogueMatch Match(string dialogue)
    {
        if (!this.owners.TryGetValue(DialogueText.Normalize(dialogue), out var owner))
            return Unknown;

        if (owner.RowId == 0)
            return Ambiguous;

        return owner.IsDialogue && this.quests.TryGetValue(owner.RowId, out var quest) ? quest : Unknown;
    }

    private void Add(string text, uint rowId, bool isDialogue)
    {
        // Journal text and unrecognized script keys can disqualify a match, but only dialogue can nominate one.
        if (this.owners.TryGetValue(text, out var existing))
        {
            if (existing.RowId != rowId)
                this.owners[text] = default;
            else if (!existing.IsDialogue && isDialogue)
                this.owners[text] = new Owner(rowId, true);
        }
        else
        {
            this.owners.Add(text, new Owner(rowId, isDialogue));
        }
    }

    // Scripts use SPEAKER_scene_line, legacy SPEAKER_line or line_SPEAKER, and occasionally an extra numbered segment.
    [GeneratedRegex("""
        ^ (?=.*_) (?: [0-9]{5,6}_ )?
        (?! (?: [AQ][0-9]+ | SYSTEM[0-9]* | (?:SAY|DUMMY)?TODO | SEQ ) (?: _ | $ ) | CHOICE )
        [A-Z][A-Z0-9]* (?: _[0-9]{3,4} ){0,3} $
        """, RegexOptions.IgnorePatternWhitespace | RegexOptions.IgnoreCase | RegexOptions.CultureInvariant)]
    private static partial Regex SpokenKey();

    private static bool IsLiteral(ReadOnlySeString value)
    {
        // ExtractText skips dynamic expressions. Their surviving fragments could otherwise look like complete lines.
        foreach (var payload in value)
        {
            if (payload.Type == ReadOnlySePayloadType.Text)
                continue;

            if (payload.Type != ReadOnlySePayloadType.Macro || payload.MacroCode is not
                (MacroCode.Bold or MacroCode.Italic or MacroCode.Color or MacroCode.EdgeColor or MacroCode.ShadowColor
                or MacroCode.ColorType or MacroCode.EdgeColorType or MacroCode.NewLine or MacroCode.Hyphen
                or MacroCode.NonBreakingSpace or MacroCode.SoftHyphen))
                return false;
        }
        return true;
    }

    private readonly record struct Owner(uint RowId, bool IsDialogue);
}
