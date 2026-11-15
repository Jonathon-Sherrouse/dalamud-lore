using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

public class StateAndSessionTests
{
    private static readonly AtlasDataset Sample = Fx.SampleDataset();

    [Fact]
    public void State_DefaultsToEarliest()
    {
        Assert.Equal(new AtlasSpoilerState(Fx.Early, Fx.Early), AtlasSpoilerPolicy.Default(Sample));
    }

    [Theory]
    [InlineData(null, null)]
    [InlineData("cp-hw-3-0", "cp-early")]
    [InlineData("cp-later", "cp-hw-3-0")]
    [InlineData("cp-early", "cp-later")]
    [InlineData("", "")]
    public void State_UnknownOrInvalidSavedStateResetsToEarliest(string? ceiling, string? view)
    {
        Assert.Equal(new AtlasSpoilerState(Fx.Early, Fx.Early), AtlasSpoilerPolicy.Restore(Sample, ceiling, view));
    }

    [Fact]
    public void State_ValidSavedStateIsKept()
    {
        Assert.Equal(new AtlasSpoilerState(Fx.Later, Fx.Early), AtlasSpoilerPolicy.Restore(Sample, Fx.Later, Fx.Early));
    }

    [Fact]
    public void State_RaisingCeilingRequiresConfirmationAndDoesNotAdvanceView()
    {
        var state = AtlasSpoilerPolicy.Default(Sample);
        var unconfirmed = AtlasSpoilerPolicy.SetCeiling(Sample, state, Fx.Later, confirmed: false);
        Assert.Equal(AtlasStateChange.NeedsConfirmation, unconfirmed.Change);
        Assert.Equal(state, unconfirmed.State);

        var confirmed = AtlasSpoilerPolicy.SetCeiling(Sample, state, Fx.Later, confirmed: true);
        Assert.Equal(AtlasStateChange.Changed, confirmed.Change);
        Assert.Equal(new AtlasSpoilerState(Fx.Later, Fx.Early), confirmed.State);
    }

    [Fact]
    public void State_LoweringCeilingClampsView()
    {
        var result = AtlasSpoilerPolicy.SetCeiling(Sample, new AtlasSpoilerState(Fx.Later, Fx.Later), Fx.Early, confirmed: false);
        Assert.Equal(AtlasStateChange.Changed, result.Change);
        Assert.Equal(new AtlasSpoilerState(Fx.Early, Fx.Early), result.State);
    }

    [Fact]
    public void State_ViewCannotExceedCeiling()
    {
        var state = AtlasSpoilerPolicy.Default(Sample);
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetView(Sample, state, Fx.Later).Change);
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetView(Sample, state, "cp-nowhere").Change);
        Assert.Equal(AtlasStateChange.None, AtlasSpoilerPolicy.SetView(Sample, state, Fx.Early).Change);
    }

    [Fact]
    public void Session_CheckpointChangeClearsTransientStateAndPersists()
    {
        AtlasSpoilerState? saved = null;
        var session = new AtlasSession(Sample, new AtlasSpoilerState(Fx.Later, Fx.Early));
        session.SpoilerStateChanged += s => saved = s;
        session.SetSearch("Maren");
        Assert.True(session.FocusOn("org-lantern-guild"));
        Assert.True(session.SelectRelationship("rel-guild-hq-old-hall"));

        Assert.Equal(AtlasStateChange.Changed, session.SetView(Fx.Later));
        Assert.Equal(string.Empty, session.SearchQuery);
        Assert.Null(session.FocusId);
        Assert.Null(session.SelectedRelationshipId);
        Assert.Equal(new AtlasSpoilerState(Fx.Later, Fx.Later), saved);
    }

    [Fact]
    public void Session_RaiseFlowUsesPendingConfirmation()
    {
        var session = new AtlasSession(Sample, AtlasSpoilerPolicy.Default(Sample));
        Assert.Equal(AtlasStateChange.NeedsConfirmation, session.RequestCeiling(Fx.Later));
        Assert.Equal(Fx.Later, session.PendingCeiling!.Id);
        Assert.Equal(Fx.Early, session.SpoilerState.CeilingId);
        Assert.DoesNotContain("Wardens", AtlasText.ConfirmRaise(session.PendingCeiling.Label));

        session.CancelPendingCeiling();
        Assert.Null(session.PendingCeiling);
        Assert.Equal(Fx.Early, session.SpoilerState.CeilingId);

        session.RequestCeiling(Fx.Later);
        Assert.Equal(AtlasStateChange.Changed, session.ConfirmPendingCeiling());
        Assert.Equal(new AtlasSpoilerState(Fx.Later, Fx.Early), session.SpoilerState);
        Assert.Null(session.Snapshot.FindEntity("org-wardens")); // view did not advance
    }

    [Fact]
    public void Session_CannotFocusHiddenEntity()
    {
        var session = new AtlasSession(Sample, AtlasSpoilerPolicy.Default(Sample));
        Assert.False(session.FocusOn("org-wardens"));
        Assert.Null(session.Focus);
        Assert.False(session.SelectRelationship("rel-wardens-control-new-hall"));
    }

    [Fact]
    public void Session_ContentViewSwitchClearsTransientState()
    {
        var session = new AtlasSession(Sample, AtlasSpoilerPolicy.Default(Sample));
        session.FocusOn("char-corin");
        Assert.Contains(session.Neighborhood!.Neighbors, n => n.Entity.Id == "char-ada");
        session.SetContentView(AtlasContentView.MainStory);
        Assert.Null(session.FocusId);
        session.FocusOn("char-corin");
        Assert.Empty(session.Neighborhood!.Neighbors);
    }

    [Fact]
    public void Session_CheckpointOptionsMarkSelectableViews()
    {
        var session = new AtlasSession(Sample, AtlasSpoilerPolicy.Default(Sample));
        var options = session.CheckpointOptions;
        Assert.True(options[0].IsCeiling && options[0].IsView && options[0].ViewSelectable);
        Assert.False(options[1].ViewSelectable);
    }

    [Fact]
    public void Session_SourcesStartCollapsedAndStayAsSetForTheSession()
    {
        var session = new AtlasSession(Sample, new AtlasSpoilerState(Fx.Later, Fx.Early));
        Assert.False(session.SourcesExpanded);

        session.SetSourcesExpanded(true);
        session.FocusOn("org-lantern-guild");
        session.SelectRelationship("rel-guild-hq-old-hall");
        session.SetView(Fx.Later);
        session.SetContentView(AtlasContentView.MainStory);
        Assert.True(session.SourcesExpanded);

        session.SetSourcesExpanded(false);
        Assert.False(session.SourcesExpanded);
        Assert.False(new AtlasSession(Sample, AtlasSpoilerPolicy.Default(Sample)).SourcesExpanded);
    }

    [Fact]
    public void Text_SourcesToggleShowsCount()
    {
        Assert.Equal("Sources (3)", AtlasText.SourcesToggle(3));
    }

    [Fact]
    public void Layout_IsDeterministicAndBounded()
    {
        var neighborhood = Fx.Project(Sample, Fx.Early).GetNeighborhood("org-lantern-guild")!;
        var a = AtlasGraphLayout.Compute(neighborhood);
        var b = AtlasGraphLayout.Compute(neighborhood);
        Assert.Equal(a.Nodes.Select(n => (n.Entity.Id, n.X, n.Y)), b.Nodes.Select(n => (n.Entity.Id, n.X, n.Y)));
        Assert.True(a.Nodes[0].IsFocus);
        Assert.Equal((0d, 0d), (a.Nodes[0].X, a.Nodes[0].Y));
        Assert.Equal((0d, -1d), (a.Nodes[1].X, a.Nodes[1].Y)); // first neighbor at the top
        Assert.All(a.Nodes.Skip(1), n => Assert.InRange(Math.Round(Math.Sqrt((n.X * n.X) + (n.Y * n.Y)), 6), 1, 1));
        Assert.True(a.Nodes.Count <= 1 + AtlasSnapshot.MaxCanvasNeighbors);
    }

    [Fact]
    public void Layout_ParallelEdgesGetSeparateLanes()
    {
        var neighborhood = Fx.Project(Sample, Fx.Early).GetNeighborhood("char-ada")!;
        var bren = AtlasGraphLayout.Compute(neighborhood).Edges.Where(e => e.FromId == "char-bren" || e.ToId == "char-bren").ToList();
        Assert.Single(bren);
        Assert.True(bren[0].Symmetric);

        var guildEdges = AtlasGraphLayout.Compute(Fx.Project(Sample, Fx.Early).GetNeighborhood("org-lantern-guild")!).Edges
            .Where(e => e.FromId == "char-ada" || e.ToId == "char-ada").ToList();
        Assert.Equal(1, guildEdges.Single().LaneCount);
    }
}
