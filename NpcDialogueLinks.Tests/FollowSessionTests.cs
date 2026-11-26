using NpcDialogueLinks.Atlas;
using Xunit;

namespace NpcDialogueLinks.Tests;

/// <summary>NDL-017: Follow in the shared session (docs/atlas/v2-plan.md, "Follow").</summary>
public class FollowSessionTests
{
    private static readonly AtlasDataset D = V2Fx.Load();
    private static readonly AtlasDataset WithOptionalEnding = DatasetWithOptionalRelationship("r-bo-possessed");

    private static Func<int, AtlasQuestProgress> Through(int completeThrough) =>
        id => id <= completeThrough ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete;

    private static AtlasSession Session(string ceiling, string view, bool follow = true, AtlasDataset? dataset = null)
    {
        dataset ??= D;
        var session = new AtlasSession(dataset, AtlasSpoilerPolicy.Restore(dataset, ceiling, view));
        session.SetFollow(follow);
        return session;
    }

    private static AtlasDataset DatasetWithOptionalRelationship(string id)
    {
        var doc = V2Fx.Doc();
        var relationship = V2Fx.Rel(doc, id);
        relationship["scope"] = "optional";
        relationship["citations"]![0]!["title"] = "Optional quest evidence";
        relationship["citations"]![0]!["scope"] = "optional";
        return Fx.Load(doc);
    }

    [Fact]
    public void Follow_MovesTheViewAndSaysItIsYourProgress()
    {
        var s = Session("m2", "s0");
        Assert.Equal(AtlasText.FollowReading, s.FollowStatus);
        Assert.True(s.ApplyFollow(Through(102)));
        Assert.Equal("s2", s.SpoilerState.ViewId);
        Assert.Equal("Your progress: through Quest Two", s.PositionLabel);
        Assert.Null(s.FollowStatus);
        Assert.False(s.FollowRaiseOffered);
    }

    [Fact]
    public void Follow_OffNeverMovesTheViewOrClaimsProgress()
    {
        var s = Session("s1", "s0", follow: false);
        Assert.False(s.ApplyFollow(Through(102)));
        Assert.Equal("s1", s.SpoilerState.CeilingId);
        Assert.Equal("s0", s.SpoilerState.ViewId);
        Assert.Equal("Viewing: after Baseline Quest", s.PositionLabel);
        Assert.Null(s.FollowStatus);
    }

    [Fact]
    public void Follow_UnknownAndBeforeCoverageLeaveTheViewAlone()
    {
        var s = Session("s1", "s1");
        Assert.False(s.ApplyFollow(_ => AtlasQuestProgress.Unknown));
        Assert.Equal(("s1", AtlasText.FollowUnknown), (s.SpoilerState.ViewId, s.FollowStatus));
        Assert.StartsWith("Viewing:", s.PositionLabel);

        Assert.False(s.ApplyFollow(_ => AtlasQuestProgress.Incomplete));
        Assert.Equal(("s1", AtlasText.FollowBeforeCoverage), (s.SpoilerState.ViewId, s.FollowStatus));
    }

    [Fact]
    public void Follow_AManualViewChangeTurnsItOff()
    {
        var s = Session("m2", "s0");
        s.ApplyFollow(Through(103));
        Assert.Equal(AtlasStateChange.Changed, s.SetView("s1"));
        Assert.False(s.FollowEnabled);
        Assert.Null(s.FollowResult);
        Assert.Equal("Viewing: after Quest One", s.PositionLabel);
    }

    [Fact]
    public void Follow_AutomaticallyRaisesAndMovesToConfirmedProgressWithoutSavingTheRaisedLimit()
    {
        var s = Session("s1", "s0");
        AtlasSpoilerState? saved = null;
        s.SpoilerStateChanged += state => saved = state;

        Assert.True(s.ApplyFollow(Through(103)));
        Assert.Equal(new AtlasSpoilerState("s3", "s3"), s.SpoilerState);
        Assert.Equal(new AtlasSpoilerState("s1", "s1"), saved);
        Assert.Equal("Your progress: through Quest Three", s.PositionLabel);
        Assert.False(s.FollowRaiseOffered);
    }

    [Fact]
    public void Follow_AutomaticallyRaisesFromDawntrailToAlexandriaMournsWithOptionalContentOn()
    {
        var dataset = AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Strict).Dataset!;
        const string approved = "cp-dt-7-0";
        const string completed = "cp-msq-955";
        Assert.True(dataset.TryGetCheckpoint(completed, out var checkpoint));
        var questId = Assert.Single(checkpoint.GameQuestIds);
        var s = Session(approved, approved, dataset: dataset);

        Assert.True(s.ApplyFollow(id => id == questId ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete));
        Assert.Equal(new AtlasSpoilerState(completed, completed), s.SpoilerState);
    }

    [Fact]
    public void Follow_NewOptionalRelationshipBlocksAnAutomaticRaise()
    {
        var s = Session("s1", "s0", dataset: DatasetWithOptionalRelationship("r-dee-bo-2"));
        s.ApplyFollow(Through(103));
        Assert.Equal(new AtlasSpoilerState("s1", "s1"), s.SpoilerState);
        Assert.True(s.FollowRaiseOffered);
    }

    [Fact]
    public void Follow_NewOptionalLoreStopsAtTheLimitAndOffersOneNeutralRaise()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        Assert.True(s.ApplyFollow(Through(103))); // reached s3, limit s1
        Assert.Equal("s1", s.SpoilerState.ViewId);
        Assert.Equal("s1", s.SpoilerState.CeilingId);
        Assert.Equal($"{AtlasText.FollowBeyondLimit} Viewing: after Quest One", s.PositionLabel);
        Assert.DoesNotContain("Quest Three", s.PositionLabel);
        Assert.True(s.FollowRaiseOffered);

        Assert.True(s.RequestFollowRaise());
        Assert.Equal(AtlasText.ConfirmRaiseToProgress, s.FollowRaisePrompt);
        Assert.Equal(AtlasStateChange.Changed, s.ConfirmFollowRaise());
        Assert.Equal(new AtlasSpoilerState("s3", "s1"), s.SpoilerState); // the view does not move
        Assert.False(s.FollowRaiseOffered);
        Assert.Equal("Your progress: through Quest Three", s.FollowStatus);

        // The next read (Refresh, or a completed quest) moves the view.
        Assert.True(s.ApplyFollow(Through(103)));
        Assert.Equal("s3", s.SpoilerState.ViewId);
    }

    [Fact]
    public void Follow_AlreadyApprovedOptionalLoreDoesNotBlockAutomaticRaise()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        Assert.True(s.ApplyFollow(Through(102)));
        Assert.Equal(new AtlasSpoilerState("s2", "s2"), s.SpoilerState);
    }

    [Fact]
    public void Follow_EnablingOptionalLoreWithdrawsAnIncompatibleAutomaticRaiseBeforeProjection()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        s.SetContentView(AtlasContentView.MainStory);
        s.ApplyFollow(Through(103));
        Assert.Equal(new AtlasSpoilerState("s3", "s3"), s.SpoilerState);

        s.SetContentView(AtlasContentView.MainAndOptional);
        Assert.Equal(new AtlasSpoilerState("s1", "s1"), s.SpoilerState);
        Assert.DoesNotContain("Quest Three", s.PositionLabel);
        s.ApplyFollow(Through(103));
        Assert.True(s.FollowRaiseOffered);
    }

    [Fact]
    public void Follow_CharacterSwitchDropsAnAutomaticRaiseEvenAfterManualBrowsing()
    {
        var s = Session("s1", "s0");
        s.ApplyFollow(Through(103));
        Assert.Equal(AtlasStateChange.Changed, s.SetView("s2"));
        Assert.False(s.FollowEnabled);
        Assert.Equal(new AtlasSpoilerState("s3", "s2"), s.SpoilerState);

        s.ResetFollowForCharacter();
        Assert.Equal(new AtlasSpoilerState("s1", "s1"), s.SpoilerState);
        Assert.DoesNotContain(s.CheckpointOptions, option => option.Label.Contains("Quest Two"));
    }

    [Fact]
    public void Follow_LoweringAnAutomaticLimitDoesNotApproveAStillUnapprovedPoint()
    {
        var s = Session("s1", "s0");
        AtlasSpoilerState? saved = null;
        s.SpoilerStateChanged += state => saved = state;
        s.ApplyFollow(Through(103));

        Assert.Equal(AtlasStateChange.Changed, s.RequestCeiling("s2"));
        Assert.Equal(new AtlasSpoilerState("s2", "s2"), s.SpoilerState);
        Assert.Equal(new AtlasSpoilerState("s1", "s1"), saved);
    }

    [Fact]
    public void Follow_ADeclinedRaiseIsNotOfferedAgainUntilTheCharacterChanges()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        s.ApplyFollow(Through(103));
        s.RequestFollowRaise();
        s.CancelFollowRaise();
        Assert.Equal("s1", s.SpoilerState.CeilingId);

        s.ApplyFollow(Through(103));
        Assert.False(s.FollowRaiseOffered);

        s.ResetFollowForCharacter();
        Assert.Null(s.FollowResult);
        Assert.Equal(AtlasText.FollowReading, s.FollowStatus);
        s.ApplyFollow(Through(103));
        Assert.True(s.FollowRaiseOffered);
    }

    [Fact]
    public void Follow_ACharacterSwitchDropsAPendingRaise()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        s.ApplyFollow(Through(103));
        s.RequestFollowRaise();
        s.ResetFollowForCharacter();
        Assert.False(s.FollowRaisePending);
        Assert.Equal(AtlasStateChange.None, s.ConfirmFollowRaise());
        Assert.Equal("s1", s.SpoilerState.CeilingId);
    }

    [Fact]
    public void Follow_LoweringTheLimitReclampsWithoutTurningItOff()
    {
        var s = Session("m1", "s0");
        s.ApplyFollow(Through(103));
        Assert.Equal("s3", s.SpoilerState.ViewId);
        Assert.Equal(AtlasStateChange.Changed, s.RequestCeiling("s2"));
        Assert.True(s.FollowEnabled);
        Assert.Equal("s2", s.SpoilerState.ViewId);
        Assert.True(s.FollowedHere);
        Assert.True(s.FollowResult!.BeyondLimit);
        Assert.False(s.FollowRaiseOffered); // only a fresh read offers, and only once
    }

    [Fact]
    public void Follow_MovingTheViewEndsAnExplicitArcPickButKeepsTheLens()
    {
        var s = Session("m2", "s2");
        Assert.True(s.PickArc("arc-tie"));
        Assert.Equal("arc-tie", s.Arc!.ArcId);
        s.ApplyFollow(Through(103));
        Assert.Equal("s3", s.SpoilerState.ViewId);
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.NotEqual("arc-tie", s.Arc?.ArcId);
    }

    [Fact]
    public void Follow_TheDefaultLensRuleAppliesWhenFollowMovesIntoAnArc()
    {
        var s = Session("m2", "s0");
        Assert.Equal(AtlasLens.StoryPoint, s.Lens);
        s.ApplyFollow(Through(102));
        Assert.Equal(AtlasLens.Arc, s.Lens);
    }

    [Fact]
    public void Follow_TurningItOffForgetsTheResult()
    {
        var s = Session("s1", "s0", dataset: WithOptionalEnding);
        s.ApplyFollow(Through(103));
        s.SetFollow(false);
        Assert.Null(s.FollowResult);
        Assert.False(s.FollowRaiseOffered);
        Assert.Equal("s1", s.SpoilerState.ViewId); // the view stays where Follow left it, as a chosen point
        Assert.Equal("Viewing: after Quest One", s.PositionLabel);
    }
}
