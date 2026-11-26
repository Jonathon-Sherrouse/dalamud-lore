using System.Globalization;
using System.Text;

namespace NpcDialogueLinks.Progress;

// NDL-007: pure, host-testable rules for reading completed-quest progress.
// No Dalamud or game types here; the game adapter is AtlasProgressSource.cs.
// Follow's position logic (AtlasFollow) lives in the Atlas core, not here.

/// <summary>What the game client says about one quest. Unknown is never a synonym for incomplete.</summary>
public enum QuestCompletion
{
    Unknown,
    Incomplete,
    Complete,
}

/// <summary>Why a read came back unknown. <see cref="None"/> means the read is trustworthy.</summary>
public enum ProgressUnknownReason
{
    None,
    NotFrameworkThread,
    LoggedOut,
    PlayerNotLoaded,
    NoCharacter,
    Loading,
    QuestDataUnavailable,
    QuestDataEmpty,
    InvalidQuestRow,
    TitleMismatch,
    ReadFailed,
}

/// <summary>One quest read. <see cref="State"/> is <see cref="QuestCompletion.Unknown"/> exactly when <see cref="Reason"/> is not None.</summary>
public readonly record struct QuestCompletionRead(uint QuestRowId, QuestCompletion State, ProgressUnknownReason Reason)
{
    public static QuestCompletionRead Known(uint questRowId, bool complete)
        => new(questRowId, complete ? QuestCompletion.Complete : QuestCompletion.Incomplete, ProgressUnknownReason.None);

    public static QuestCompletionRead Unknown(uint questRowId, ProgressUnknownReason reason)
        => new(questRowId, QuestCompletion.Unknown, reason == ProgressUnknownReason.None ? ProgressUnknownReason.ReadFailed : reason);
}

/// <summary>
/// The conditions sampled from the game before any completion flag is read.
/// Every field is a plain value so the rules can be tested off the game.
/// </summary>
public readonly record struct ProgressGate(
    bool OnFrameworkThread,
    bool IsLoggedIn,
    bool PlayerLoaded,
    ulong ContentId,
    bool LocalPlayerPresent,
    bool BetweenAreas,
    bool QuestDataAvailable,
    int CompletedQuestCount,
    bool SampleFailed = false)
{
    /// <summary>The gate a background thread sees: nothing else is sampled.</summary>
    public static ProgressGate OffThread { get; } = new(false, false, false, 0, false, false, false, 0);

    /// <summary>The gate when sampling itself threw on the framework thread.</summary>
    public static ProgressGate Failed { get; } = new(true, false, false, 0, false, false, false, 0, SampleFailed: true);
}

public static class ProgressRules
{
    /// <summary>
    /// Decide whether completion flags may be read. Order matters: the thread check comes first because
    /// nothing else may be sampled off the framework thread.
    /// </summary>
    public static ProgressUnknownReason Evaluate(in ProgressGate gate)
    {
        if (!gate.OnFrameworkThread)
        {
            return ProgressUnknownReason.NotFrameworkThread;
        }

        if (gate.SampleFailed)
        {
            return ProgressUnknownReason.ReadFailed;
        }

        if (!gate.IsLoggedIn)
        {
            return ProgressUnknownReason.LoggedOut;
        }

        if (!gate.PlayerLoaded)
        {
            return ProgressUnknownReason.PlayerNotLoaded;
        }

        if (gate.ContentId == 0)
        {
            return ProgressUnknownReason.NoCharacter;
        }

        if (gate.BetweenAreas || !gate.LocalPlayerPresent)
        {
            return ProgressUnknownReason.Loading;
        }

        if (!gate.QuestDataAvailable)
        {
            return ProgressUnknownReason.QuestDataUnavailable;
        }

        // A logged-in character with zero completed quests is indistinguishable from "the list hasn't
        // arrived yet". Treat it as unknown: the cost is that a brand-new character sees "unknown"
        // instead of "before coverage", which never moves the view either way.
        if (gate.CompletedQuestCount <= 0)
        {
            return ProgressUnknownReason.QuestDataEmpty;
        }

        return ProgressUnknownReason.None;
    }

    /// <summary>
    /// Combine the alternative quest rows that stand for one story step (starting-city variants such as the
    /// eight "Close to Home" rows, or a retired row and its replacement). A data error on any row poisons the
    /// step; otherwise any completed row completes it, and only all-incomplete reads as incomplete.
    /// </summary>
    public static QuestCompletion CombineAlternatives(IReadOnlyCollection<QuestCompletionRead> reads)
    {
        if (reads.Count == 0)
        {
            return QuestCompletion.Unknown;
        }

        if (reads.Any(read => read.Reason is ProgressUnknownReason.TitleMismatch or ProgressUnknownReason.InvalidQuestRow))
        {
            return QuestCompletion.Unknown;
        }

        if (reads.Any(read => read.State == QuestCompletion.Complete))
        {
            return QuestCompletion.Complete;
        }

        return reads.Any(read => read.State == QuestCompletion.Unknown)
            ? QuestCompletion.Unknown
            : QuestCompletion.Incomplete;
    }
}

/// <summary>
/// Lumina Quest sheet rows start at 0x10000; the client's completed-quest bitfield is indexed by the low 16 bits.
/// FFXIVClientStructs' <c>QuestManager.IsQuestComplete(uint)</c> applies the same <c>&amp; 0xFFFF</c> mask, and
/// Dalamud's own <c>IUnlockState.IsQuestCompleted(Quest)</c> passes <c>row.RowId</c> straight into it.
/// </summary>
public static class QuestIdMapping
{
    public const uint QuestRowBase = 0x10000;

    /// <summary>
    /// Convert a Lumina Quest row ID to the client quest ID. Rejects anything outside the quest row range,
    /// client ID 0 (the game's "no quest"), and IDs past the end of the completed-quest bitfield.
    /// </summary>
    public static bool TryToClientId(uint questRowId, int completedBitCount, out ushort clientId)
    {
        clientId = 0;
        if (questRowId <= QuestRowBase || questRowId > QuestRowBase + ushort.MaxValue)
        {
            return false;
        }

        var candidate = questRowId - QuestRowBase;
        if (completedBitCount <= 0 || candidate >= (uint)completedBitCount)
        {
            return false;
        }

        clientId = (ushort)candidate;
        return true;
    }
}

/// <summary>The title cross-check: an authored quest title must match the game's title for that row.</summary>
public static class QuestTitles
{
    /// <summary>
    /// Normalise only what never changes meaning: Unicode form, curly vs straight apostrophes, non-breaking
    /// and repeated whitespace, and surrounding whitespace. Case and wording stay strict.
    /// </summary>
    public static string Normalize(string? title)
    {
        if (string.IsNullOrWhiteSpace(title))
        {
            return string.Empty;
        }

        var normalized = title.Normalize(NormalizationForm.FormC);
        var builder = new StringBuilder(normalized.Length);
        var pendingSpace = false;
        foreach (var character in normalized)
        {
            if (char.IsWhiteSpace(character) || CharUnicodeInfo.GetUnicodeCategory(character) == UnicodeCategory.SpaceSeparator)
            {
                pendingSpace = builder.Length > 0;
                continue;
            }

            if (pendingSpace)
            {
                builder.Append(' ');
                pendingSpace = false;
            }

            builder.Append(character switch
            {
                '‘' or '’' or 'ʼ' => '\'',
                '“' or '”' => '"',
                _ => character,
            });
        }

        return builder.ToString();
    }

    /// <summary>True only when both titles are non-empty and equal after normalisation.</summary>
    public static bool Matches(string? expected, string? actual)
    {
        var left = Normalize(expected);
        var right = Normalize(actual);
        return left.Length > 0 && string.Equals(left, right, StringComparison.Ordinal);
    }

    /// <summary>
    /// NDL-017: the cross-check for an Atlas step's authored title. Besides <see cref="Matches"/>, it accepts the Atlas's
    /// city disambiguator ("Close to Home (Ul'dah)" for the game's "Close to Home") and the reviewed typography variants
    /// in <see cref="ReviewedVariants"/>, each pinned to its row and to both spellings. Wording stays strict.
    /// </summary>
    public static bool MatchesAuthored(uint questRowId, string? authored, string? game)
    {
        if (Matches(authored, game) || Matches(StripDisambiguator(authored), game))
        {
            return true;
        }

        return ReviewedVariants.TryGetValue(questRowId, out var variant)
            && Matches(variant.Authored, authored)
            && Matches(variant.Game, game);
    }

    /// <summary>"Close to Home (Ul'dah)" → "Close to Home". Null when the title has no single trailing parenthetical.</summary>
    public static string? StripDisambiguator(string? title)
    {
        var normalized = Normalize(title);
        if (!normalized.EndsWith(')'))
        {
            return null;
        }

        var open = normalized.LastIndexOf(" (", StringComparison.Ordinal);
        if (open <= 0 || open + 3 >= normalized.Length || normalized.IndexOf('(', open + 2) >= 0 || normalized.IndexOf(')', open) != normalized.Length - 1)
        {
            return null;
        }

        return normalized[..open];
    }

    /// <summary>
    /// Authored titles that differ from the English Quest sheet only in typography, checked against the user's install
    /// on 2026-11-26 with <c>tools/atlas/QuestRowCheck</c>. The Atlas keeps its spelling because citations and the
    /// same-title rule use it; the game's spelling is pinned too, so a later rename still fails the check.
    /// </summary>
    public static IReadOnlyDictionary<uint, (string Authored, string Game)> ReviewedVariants { get; } = new Dictionary<uint, (string, string)>
    {
        [68865] = ("Stirring up Trouble", "Stirring Up Trouble"),
        [68877] = ("Bearing With It", "Bearing with It"),
        [69991] = ("A Test of Wιll", "Α Test of Wιll"), // the game's first letter is a Greek capital alpha
    };
}

/// <summary>
/// NDL-017: one gated read of every quest the Atlas covers, taken in a single framework tick. <see cref="Reason"/> is the
/// gate's verdict, or the first data error (title mismatch, invalid row) when the gate passed.
/// </summary>
public sealed record QuestProgressSnapshot(int Generation, ProgressUnknownReason Reason, IReadOnlyDictionary<uint, QuestCompletion> Quests)
{
    public static QuestProgressSnapshot Failed(int generation) =>
        new(generation, ProgressUnknownReason.ReadFailed, new Dictionary<uint, QuestCompletion>());

    /// <summary>Unread rows are unknown, never incomplete.</summary>
    public QuestCompletion this[uint questRowId] => Quests.TryGetValue(questRowId, out var state) ? state : QuestCompletion.Unknown;
}

/// <summary>NDL-017: what Follow tells the player when progress reads unknown, and whether waiting can fix it.</summary>
public static class FollowStatusText
{
    public static string? Hint(ProgressUnknownReason reason) => reason switch
    {
        ProgressUnknownReason.None => null,
        ProgressUnknownReason.LoggedOut or ProgressUnknownReason.PlayerNotLoaded or ProgressUnknownReason.NoCharacter
            => "Log in to a character to read your progress.",
        ProgressUnknownReason.TitleMismatch or ProgressUnknownReason.InvalidQuestRow
            => "The Atlas quest list doesn't match this game version, so Follow can't place you.",
        ProgressUnknownReason.ReadFailed => "The game didn't return your progress. Try Refresh.",
        _ => "Waiting for the game to finish loading.",
    };

    /// <summary>Unknown for a reason that can clear by itself (logging in, loading). Data errors never do.</summary>
    public static bool IsTransient(ProgressUnknownReason reason) =>
        reason is not (ProgressUnknownReason.None or ProgressUnknownReason.TitleMismatch or ProgressUnknownReason.InvalidQuestRow);
}

/// <summary>
/// Tracks which character the last read belonged to. A different character, or an explicit invalidation
/// (login or logout), bumps <see cref="Generation"/>; anything a consumer tagged with an older generation
/// (a Follow result, a pending raise offer) is stale and must be dropped and re-read.
/// </summary>
public sealed class CharacterTracker
{
    public ulong? Current { get; private set; }

    public int Generation { get; private set; }

    /// <summary>Record the character seen by a trustworthy read. Returns true when this is a switch.</summary>
    public bool Observe(ulong contentId)
    {
        if (contentId == 0 || this.Current == contentId)
        {
            return false;
        }

        var switched = this.Current.HasValue;
        this.Current = contentId;
        this.Generation++;
        return switched;
    }

    /// <summary>Forget the character (login, logout). The next trustworthy read starts a new generation.</summary>
    public void Invalidate()
    {
        if (this.Current is null)
        {
            return;
        }

        this.Current = null;
        this.Generation++;
    }

    public bool IsCurrent(int generation) => generation == this.Generation && this.Current.HasValue;
}
