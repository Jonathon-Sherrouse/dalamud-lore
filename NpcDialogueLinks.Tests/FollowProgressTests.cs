using NpcDialogueLinks.Progress;

namespace NpcDialogueLinks.Tests;

// NDL-007: host tests for the pure rules behind AtlasProgressSource.
public class FollowProgressTests
{
    private static readonly ProgressGate Ready = new(
        OnFrameworkThread: true,
        IsLoggedIn: true,
        PlayerLoaded: true,
        ContentId: 0x1234,
        LocalPlayerPresent: true,
        BetweenAreas: false,
        QuestDataAvailable: true,
        CompletedQuestCount: 812);

    [Fact]
    public void Gate_ReadyOnlyWhenEveryConditionHolds()
    {
        Assert.Equal(ProgressUnknownReason.None, ProgressRules.Evaluate(Ready));
    }

    public static TheoryData<string, ProgressUnknownReason> GateFailures => new()
    {
        { "off-thread", ProgressUnknownReason.NotFrameworkThread },
        { "sample-failed", ProgressUnknownReason.ReadFailed },
        { "logged-out", ProgressUnknownReason.LoggedOut },
        { "player-not-loaded", ProgressUnknownReason.PlayerNotLoaded },
        { "no-character", ProgressUnknownReason.NoCharacter },
        { "between-areas", ProgressUnknownReason.Loading },
        { "no-local-player", ProgressUnknownReason.Loading },
        { "no-quest-data", ProgressUnknownReason.QuestDataUnavailable },
        { "empty-quest-data", ProgressUnknownReason.QuestDataEmpty },
    };

    [Theory]
    [MemberData(nameof(GateFailures))]
    public void Gate_AnyFailedConditionIsUnknownNeverIncomplete(string condition, ProgressUnknownReason expected)
    {
        var gate = condition switch
        {
            "off-thread" => Ready with { OnFrameworkThread = false },
            "sample-failed" => Ready with { SampleFailed = true },
            "logged-out" => Ready with { IsLoggedIn = false },
            "player-not-loaded" => Ready with { PlayerLoaded = false },
            "no-character" => Ready with { ContentId = 0 },
            "between-areas" => Ready with { BetweenAreas = true },
            "no-local-player" => Ready with { LocalPlayerPresent = false },
            "no-quest-data" => Ready with { QuestDataAvailable = false },
            "empty-quest-data" => Ready with { CompletedQuestCount = 0 },
            _ => throw new ArgumentOutOfRangeException(nameof(condition)),
        };

        Assert.Equal(expected, ProgressRules.Evaluate(gate));
    }

    [Fact]
    public void Gate_ThreadCheckWinsOverEverythingElse()
    {
        Assert.Equal(ProgressUnknownReason.NotFrameworkThread, ProgressRules.Evaluate(ProgressGate.OffThread));
        Assert.Equal(ProgressUnknownReason.NotFrameworkThread, ProgressRules.Evaluate(Ready with { OnFrameworkThread = false, IsLoggedIn = false }));
        Assert.Equal(ProgressUnknownReason.ReadFailed, ProgressRules.Evaluate(ProgressGate.Failed));
    }

    [Fact]
    public void Read_UnknownAlwaysCarriesAReason()
    {
        var read = QuestCompletionRead.Unknown(70058, ProgressUnknownReason.None);
        Assert.Equal(QuestCompletion.Unknown, read.State);
        Assert.Equal(ProgressUnknownReason.ReadFailed, read.Reason);
        Assert.Equal(QuestCompletion.Incomplete, QuestCompletionRead.Known(70058, complete: false).State);
        Assert.Equal(ProgressUnknownReason.None, QuestCompletionRead.Known(70058, complete: true).Reason);
    }

    // Real rows from the local game data (Lumina Quest sheet, 2026-11-14): rows 65536..71068.
    [Theory]
    [InlineData(70058u, 4522)] // The Ultimate Weapon (current row)
    [InlineData(66060u, 524)] // The Ultimate Weapon (retired row)
    [InlineData(65964u, 428)] // Before the Dawn
    [InlineData(65621u, 85)] // Close to Home
    [InlineData(70495u, 4959)] // Dawntrail
    [InlineData(71068u, 5532)] // last row in the sheet
    public void Mapping_RowMinusBaseIsTheClientId(uint row, int expected)
    {
        Assert.True(QuestIdMapping.TryToClientId(row, 6008, out var clientId));
        Assert.Equal(expected, clientId);
        Assert.Equal(row & 0xFFFF, clientId); // ClientStructs' IsQuestComplete(uint) masks the same way.
    }

    [Theory]
    [InlineData(0u)]
    [InlineData(4522u)] // a client ID passed where a row was expected
    [InlineData(65535u)]
    [InlineData(65536u)] // client ID 0 is "no quest"
    [InlineData(72144u)] // client ID 6608, past the 6008-bit field
    [InlineData(131072u)] // would silently wrap to 0 under a bare mask
    [InlineData(200000u)]
    public void Mapping_RejectsRowsOutsideTheQuestRange(uint row)
    {
        Assert.False(QuestIdMapping.TryToClientId(row, 6008, out _));
    }

    [Fact]
    public void Mapping_RespectsTheBitfieldLength()
    {
        Assert.True(QuestIdMapping.TryToClientId(QuestIdMapping.QuestRowBase + 6007, 6008, out _));
        Assert.False(QuestIdMapping.TryToClientId(QuestIdMapping.QuestRowBase + 6008, 6008, out _));
        Assert.False(QuestIdMapping.TryToClientId(70058, 0, out _));
    }

    [Theory]
    [InlineData("The Ultimate Weapon", "The Ultimate Weapon")]
    [InlineData("  The Ultimate  Weapon ", "The Ultimate Weapon")]
    [InlineData("Coming to Ul’dah", "Coming to Ul'dah")]
    [InlineData("Before the Dawn", "Before the Dawn")]
    [InlineData("Close to Home", "Close to Home")]
    public void Titles_MatchAcrossHarmlessDifferences(string authored, string game)
    {
        Assert.True(QuestTitles.Matches(authored, game));
    }

    [Theory]
    [InlineData("Before the Dawn", "The Ultimate Weapon")]
    [InlineData("the ultimate weapon", "The Ultimate Weapon")]
    [InlineData("The Ultimate Weapon", "")]
    [InlineData("", "")]
    [InlineData(null, "The Ultimate Weapon")]
    [InlineData("The Ultimate Weapon", null)]
    [InlineData("The Ultimate Weapons", "The Ultimate Weapon")]
    public void Titles_MismatchIsStrict(string? authored, string? game)
    {
        Assert.False(QuestTitles.Matches(authored, game));
    }

    [Fact]
    public void Alternatives_AnyCompletedRowCompletesTheStep()
    {
        var reads = new[] { Incomplete(65621), Complete(65644), Incomplete(66104) };
        Assert.Equal(QuestCompletion.Complete, ProgressRules.CombineAlternatives(reads));
    }

    [Fact]
    public void Alternatives_OnlyAllIncompleteIsIncomplete()
    {
        Assert.Equal(QuestCompletion.Incomplete, ProgressRules.CombineAlternatives([Incomplete(66060), Incomplete(70058)]));
    }

    [Fact]
    public void Alternatives_UnknownWithoutCompletionIsUnknown()
    {
        var reads = new[] { Incomplete(66060), QuestCompletionRead.Unknown(70058, ProgressUnknownReason.Loading) };
        Assert.Equal(QuestCompletion.Unknown, ProgressRules.CombineAlternatives(reads));
        Assert.Equal(QuestCompletion.Unknown, ProgressRules.CombineAlternatives([]));
    }

    [Theory]
    [InlineData(ProgressUnknownReason.TitleMismatch)]
    [InlineData(ProgressUnknownReason.InvalidQuestRow)]
    public void Alternatives_DataErrorPoisonsTheStepEvenIfAnotherRowIsComplete(ProgressUnknownReason reason)
    {
        var reads = new[] { Complete(70058), QuestCompletionRead.Unknown(66060, reason) };
        Assert.Equal(QuestCompletion.Unknown, ProgressRules.CombineAlternatives(reads));
    }

    [Fact]
    public void Characters_FirstCharacterStartsAGenerationButIsNotASwitch()
    {
        var tracker = new CharacterTracker();
        Assert.False(tracker.Observe(0xA));
        Assert.Equal(1, tracker.Generation);
        Assert.True(tracker.IsCurrent(1));
        Assert.False(tracker.Observe(0xA));
        Assert.Equal(1, tracker.Generation);
    }

    [Fact]
    public void Characters_SwitchingWithoutLogoutIsDetectedAndInvalidates()
    {
        var tracker = new CharacterTracker();
        tracker.Observe(0xA);
        var tagged = tracker.Generation;

        Assert.True(tracker.Observe(0xB));
        Assert.False(tracker.IsCurrent(tagged));
        Assert.Equal(0xBUL, tracker.Current);
    }

    [Fact]
    public void Characters_LogoutInvalidatesAndTheNextReadStartsFresh()
    {
        var tracker = new CharacterTracker();
        tracker.Observe(0xA);
        var tagged = tracker.Generation;

        tracker.Invalidate(); // logout
        Assert.False(tracker.IsCurrent(tagged));
        Assert.Null(tracker.Current);

        tracker.Invalidate(); // login right after: no double bump needed
        var afterLogin = tracker.Generation;

        Assert.False(tracker.Observe(0xA)); // same character back: still a new generation
        Assert.True(tracker.Generation > afterLogin);
        Assert.False(tracker.IsCurrent(tagged));
    }

    [Fact]
    public void Characters_ZeroContentIdIsIgnored()
    {
        var tracker = new CharacterTracker();
        Assert.False(tracker.Observe(0));
        Assert.Null(tracker.Current);
        Assert.Equal(0, tracker.Generation);
        Assert.False(tracker.IsCurrent(0));
    }

    private static QuestCompletionRead Complete(uint row) => QuestCompletionRead.Known(row, complete: true);

    private static QuestCompletionRead Incomplete(uint row) => QuestCompletionRead.Known(row, complete: false);
}
