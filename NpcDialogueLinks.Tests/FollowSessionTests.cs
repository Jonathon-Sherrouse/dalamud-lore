using NpcDialogueLinks.Atlas;
using Xunit;

namespace NpcDialogueLinks.Tests;

/// <summary>NDL-017: Follow in the shared session (docs/atlas/v2-plan.md, "Follow").</summary>
public class FollowSessionTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static Func<int, AtlasQuestProgress> Through(int completeThrough) =>
        id => id <= completeThrough ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete;

    private static AtlasSession Session(string ceiling, string view, bool follow = true)
    {
        var session = new AtlasSession(D, AtlasSpoilerPolicy.Restore(D, ceiling, view));
        session.SetFollow(follow);
        return session;
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
        var s = Session("m2", "s0", follow: false);
        Assert.False(s.ApplyFollow(Through(102)));
        Assert.Equal("s0", s.SpoilerState.ViewId);
        Assert.Equal("Viewing: after Baseline Quest", s.PositionLabel);
        Assert.Null(s.FollowStatus);
    }

    [Fact]
    public void Follow_UnknownAndBeforeCoverageLeaveTheViewAlone()
    {
        var s = Session("m2", "s1");
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
    public void Follow_BeyondTheLimitStopsAtItAndOffersOneNeutralRaise()
    {
        var s = Session("s1", "s0");
        Assert.True(s.ApplyFollow(Through(103))); // reached s3, limit s1
        Assert.Equal("s1", s.SpoilerState.ViewId);
        Assert.Equal("s1", s.SpoilerState.CeilingId); // Follow never raises the limit by itself
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
    public void Follow_ADeclinedRaiseIsNotOfferedAgainUntilTheCharacterChanges()
    {
        var s = Session("s1", "s0");
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
        var s = Session("s1", "s0");
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
        var s = Session("s1", "s0");
        s.ApplyFollow(Through(103));
        s.SetFollow(false);
        Assert.Null(s.FollowResult);
        Assert.False(s.FollowRaiseOffered);
        Assert.Equal("s1", s.SpoilerState.ViewId); // the view stays where Follow left it, as a chosen point
        Assert.Equal("Viewing: after Quest One", s.PositionLabel);
    }
}
