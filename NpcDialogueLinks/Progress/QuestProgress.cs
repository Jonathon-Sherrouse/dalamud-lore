using System.Globalization;
using System.Text;

namespace NpcDialogueLinks.Progress;

// NDL-007: pure, host-testable rules for reading completed-quest progress.
// No Dalamud or game types here; the game adapter is AtlasProgressSource.cs.
// Follow's position logic (FollowPosition) is NDL-006's and lives in the Atlas core, not here.

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
