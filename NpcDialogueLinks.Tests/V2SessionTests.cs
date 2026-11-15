using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>NDL-008: the v2 lenses composed in the shared session (docs/atlas/ux-design.md, "v2 lenses").</summary>
public class V2LensTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession At(string ceiling, string view, AtlasContentView contentView = AtlasContentView.MainAndOptional) =>
        new(D, new AtlasSpoilerState(ceiling, view), contentView);

    [Fact]
    public void Lens_OpensInStoryPointBeforeAnyArc()
    {
        var s = At("s0", "s0");
        Assert.Equal(AtlasLens.StoryPoint, s.Lens);
        Assert.False(s.LensIsExplicit);
    }

    [Fact]
    public void Lens_OpensInArcWhenAnArcContainsTheView()
    {
        var s = At("m2", "s2");
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.Equal("arc-hold", s.Arc!.ArcId); // earliest-started of the three arcs containing s2
    }

    [Fact]
    public void Lens_DefaultFollowsTheViewUntilThePlayerPicksOne()
    {
        var s = At("m2", "s0");
        Assert.Equal(AtlasLens.StoryPoint, s.Lens);
        s.SetView("s1");
        Assert.Equal(AtlasLens.Arc, s.Lens);
        s.SetView("s5"); // no arc contains s5
        Assert.Equal(AtlasLens.StoryPoint, s.Lens);

        s.SetLens(AtlasLens.Changes);
        s.SetView("s2");
        Assert.Equal(AtlasLens.Changes, s.Lens); // an explicit lens lasts for the session
        Assert.True(s.LensIsExplicit);
    }

    [Fact]
    public void Lens_ExplicitArcWithNoArcHereShowsTheEmptyState()
    {
        var s = At("m2", "s1");
        s.SetLens(AtlasLens.Arc);
        s.SetView("s5");
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.Null(s.Arc);
        Assert.Empty(s.Snapshot.Entities);
        Assert.Null(s.Layout);
        Assert.Empty(s.SearchResults);
    }

    [Fact]
    public void Lens_SwitchingClearsBrowsingWithoutTheResetHint()
    {
        var s = At("m2", "s2");
        s.SetLens(AtlasLens.StoryPoint);
        Assert.True(s.FocusOn("char-bo"));
        s.SetLens(AtlasLens.Arc);
        Assert.Null(s.FocusId);
        Assert.False(s.SelectionWasReset);
    }

    [Fact]
    public void StoryPoint_IsTheUnfilteredProjection()
    {
        var s = At("m2", "s2");
        s.SetLens(AtlasLens.StoryPoint);
        Assert.Equal(AtlasProjector.Project(D, "s2", AtlasContentView.MainAndOptional).Entities.Select(e => e.Id), s.Snapshot.Entities.Select(e => e.Id));
        Assert.Contains(s.SearchResults, e => e.Id == "char-zed"); // not in any cast
    }

    [Fact]
    public void Position_IsTheChosenPointAndCoverageShowsOnSliceStepsOnly()
    {
        var slice = At("m2", "s2");
        Assert.Equal("Viewing: after Quest Two", slice.PositionLabel);
        Assert.Equal(AtlasText.CoverageNote, slice.CoverageNote);

        var milestone = At("m2", "m1");
        Assert.Equal("Viewing: after Patch One complete", milestone.PositionLabel);
        Assert.Null(milestone.CoverageNote);
    }
}

public class V2ArcSessionTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession At(string ceiling, string view) => new(D, new AtlasSpoilerState(ceiling, view));

    [Fact]
    public void Arc_RestsOnTheWholeCastWithTheEntryInTheCenter()
    {
        var s = At("m2", "s2");
        Assert.True(s.ShowsWholeCast);
        Assert.Null(s.FocusId);
        var layout = s.Layout!;
        Assert.Equal("evt-hold", layout.Nodes[0].Entity.Id);
        Assert.Equal(s.Snapshot.Entities.Count, layout.Nodes.Count);
        Assert.Equal(s.Snapshot.Relationships.Count, layout.Edges.Count);
        Assert.All(layout.Edges.Where(e => e.Relationship.TypeId == AtlasDataset.ParticipantTypeId), e => Assert.True(e.IsParticipation));
        Assert.Contains(layout.Edges, e => !e.IsParticipation);
    }

    [Fact]
    public void Arc_BrowsingNeverLeavesTheCast()
    {
        var s = At("m2", "s3");
        var cast = s.Arc!.Cast.Entities.Select(e => e.Id).ToHashSet();
        Assert.All(s.SearchResults, e => Assert.Contains(e.Id, cast));
        Assert.False(s.FocusOn("char-zed")); // never a participant
        Assert.True(s.FocusOn("char-bo"));
        Assert.False(s.ShowsWholeCast);
        Assert.All(s.Neighborhood!.Neighbors, n => Assert.Contains(n.Entity.Id, cast));
        s.ShowWholeCast();
        Assert.True(s.ShowsWholeCast);
    }

    [Fact]
    public void Arc_WholeCastEdgesCanBeSelected()
    {
        var s = At("m2", "s3");
        Assert.True(s.SelectRelationship("r-cy-bo-2"));
        Assert.Equal("r-cy-bo-2", s.SelectedRelationship!.Id);
        Assert.False(s.SelectRelationship("r-zed-ana")); // outside the cast
    }

    [Fact]
    public void Arc_PickHoldsThenEndsWhenTheViewDropsBelowItsStart()
    {
        var s = At("m2", "s3");
        Assert.True(s.PickArc("arc-shadow"));
        Assert.Equal("arc-shadow", s.Arc!.ArcId);
        Assert.True(s.ArcPickerOptions.Single(o => o.ArcId == "arc-shadow").IsCurrent);

        s.SetView("s1"); // below arc-shadow's first step: the pick ends
        Assert.Equal("arc-hold", s.Arc!.ArcId);
        Assert.True(s.ArcPickerOptions[0].IsCurrent);

        s.SetView("s3"); // and does not come back
        Assert.Equal("arc-hold", s.Arc!.ArcId);
    }

    [Fact]
    public void Arc_PickerListsOnlyStartedArcsByName()
    {
        var s = At("m2", "s1");
        Assert.Equal(new[] { AtlasText.ArcAutomatic, "The Hold" }, s.ArcPickerOptions.Select(o => o.Label));
        Assert.False(s.PickArc("arc-shadow")); // starts at s2
        Assert.Equal(new[] { AtlasText.ArcAutomatic, "The Hold", "The Shadow", "The Tie" }, At("m2", "s2").ArcPickerOptions.Select(o => o.Label));
    }

    [Fact]
    public void Arc_EndedArcStaysViewableAsOfItsLastQuest()
    {
        var s = At("m2", "s5");
        s.SetLens(AtlasLens.Arc);
        Assert.Null(s.Arc); // the automatic choice: no arc contains s5
        Assert.True(s.PickArc("arc-hold"));
        Assert.True(s.Arc!.PastEnd);
        Assert.Equal(AtlasText.ArcAsOf("Quest Three"), s.Arc.AsOfLabel);
    }

    [Fact]
    public void Arc_AtItsLastStepShowsNoEndMarker()
    {
        var s = At("m2", "s3");
        Assert.Null(s.Arc!.AsOfLabel);
        Assert.False(s.Arc.PastEnd);
    }

    [Fact]
    public void Arc_RowsShowNewAndEndedWithoutSources()
    {
        var s = At("m2", "s3");
        Assert.Equal(new[] { "r-cy-bo-2", "r-dee-bo-2" }, s.ArcNewRows.Select(r => r.Relationship!.Id).Order(StringComparer.Ordinal));
        var ended = s.ArcEndedRows;
        Assert.Equal(new[] { "r-ana-prisoner", "r-bo-possessed" }, ended.Select(r => r.Relationship!.Id));
        Assert.Equal(new[] { AtlasText.EndedIn("Quest Two"), AtlasText.EndedIn("Quest Three") }, ended.Select(r => r.EndedInLabel));
        Assert.All(ended, r =>
        {
            Assert.Empty(r.EndCitations);
            Assert.Empty(r.Relationship!.Citations);
            Assert.Empty(r.Source!.Citations);
            Assert.Empty(r.Target!.Citations);
        });
        Assert.Equal("Ana prisoner of The Foe", ended[0].Text);
    }
}

public class V2ChangesSessionTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession Changes(string view)
    {
        var s = new AtlasSession(D, new AtlasSpoilerState("m2", view));
        s.SetLens(AtlasLens.Changes);
        return s;
    }

    [Fact]
    public void Changes_GroupsRowsUnderTheQuestLabel()
    {
        var s = Changes("s2");
        Assert.True(s.ChangesOffered);
        Assert.Equal(AtlasText.ChangesThisQuest, s.ChangesLabel);
        Assert.Equal(new[] { AtlasText.ChangesAdded, AtlasText.ChangesEnded, AtlasText.ChangesUpdated }, s.ChangeGroups.Select(g => g.Label));
        var ended = s.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Ended).Rows.Single(r => r.Relationship!.Id == "r-ana-prisoner");
        Assert.Equal("Src s2", ended.EndCitations.Single().Title); // the one surface that shows end evidence
        Assert.Contains(s.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Updated).Rows, r => r.Entity!.Id == "char-ana");
        Assert.Null(s.Layout); // no chart in the Changes lens
    }

    [Fact]
    public void Changes_AcrossAGapNamesThePreviousPoint()
    {
        Assert.Equal(AtlasText.ChangesSince("Quest Nine"), Changes("s6").ChangesLabel);
    }

    [Fact]
    public void Changes_NotOfferedAcrossASliceMilestoneBoundary()
    {
        var s = Changes("m1");
        Assert.False(s.ChangesOffered);
        Assert.Null(s.ChangesLabel);
        Assert.Empty(s.ChangeGroups);
    }

    [Fact]
    public void Changes_SelectionClearsOnAStorySettingChange()
    {
        var s = Changes("s2");
        Assert.True(s.SelectChange("ended:r-ana-prisoner"));
        Assert.Equal("ended:r-ana-prisoner", s.SelectedChange!.Key);
        Assert.False(s.SelectChange("ended:nope"));
        s.SetView("s3");
        Assert.Null(s.SelectedChangeKey);
        Assert.True(s.SelectionWasReset);
    }

    [Fact]
    public void Changes_RowsAreSelectableOnlyInTheChangesLens()
    {
        var s = new AtlasSession(D, new AtlasSpoilerState("m2", "s2")); // Arc lens
        Assert.False(s.SelectChange("ended:r-ana-prisoner"));
    }
}

/// <summary>
/// v2 spoiler rule 5, the per-step leak sweep: every limit × view × content view × lens × arc pick, every surface the
/// session exposes. Nothing names a step past the view (or, in pickers and prompts, a quest past the limit), an entity
/// not yet introduced by the view, or a source not yet available.
/// </summary>
public class V2LeakSweepTests
{
    public static TheoryData<string> Datasets() => new() { "v2fx", "arc-sample" };

    private static AtlasDataset LoadNamed(string name) => name == "v2fx"
        ? V2Fx.Load()
        : AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "sample-arc-atlas.json"), AtlasValidationMode.Strict).Dataset!;

    [Theory]
    [MemberData(nameof(Datasets))]
    public void Sweep_NoSurfaceRevealsAnythingBeyondTheViewOrTheLimit(string name)
    {
        var d = LoadNamed(name);
        var checked_ = 0;
        foreach (var ceiling in d.Checkpoints)
        {
            foreach (var view in d.Checkpoints.Where(c => c.Order <= ceiling.Order))
            {
                foreach (var contentView in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
                {
                    var forbidden = Forbidden(d, ceiling, view, contentView);
                    foreach (var lens in new[] { AtlasLens.Arc, AtlasLens.StoryPoint, AtlasLens.Changes })
                    {
                        var picks = new List<string?> { null };
                        picks.AddRange(AtlasArcs.Eligible(d, view.Id, contentView).Select(a => a.ArcId));
                        foreach (var pick in picks)
                        {
                            var s = new AtlasSession(d, new AtlasSpoilerState(ceiling.Id, view.Id), contentView);
                            s.SetLens(lens);
                            Assert.True(s.PickArc(pick));
                            var content = Content(s).ToList();
                            AssertClean(content, forbidden.Content, $"{name} limit={ceiling.Id} view={view.Id} {contentView} {lens} pick={pick}");
                            AssertClean(Pickers(s).ToList(), forbidden.Pickers, $"{name} pickers limit={ceiling.Id} view={view.Id}");
                            if (s.Arc is { } arc && !arc.PastEnd)
                            {
                                Assert.DoesNotContain(content, t => t.StartsWith("As of", StringComparison.Ordinal)); // rule 7
                            }

                            checked_++;
                        }
                    }
                }
            }
        }

        Assert.True(checked_ > 50, $"only {checked_} combinations swept");
    }

    private sealed record ForbiddenSet(IReadOnlyList<string> Content, IReadOnlyList<string> Pickers);

    private static ForbiddenSet Forbidden(AtlasDataset d, AtlasCheckpoint ceiling, AtlasCheckpoint view, AtlasContentView contentView)
    {
        var known = d.Checkpoints.Where(c => c.Order <= view.Order)
            .SelectMany(c => AtlasProjector.Project(d, c.Id, contentView).Entities)
            .Select(e => e.Name).ToHashSet();
        var later = d.Checkpoints.Where(c => c.Order > view.Order).ToList();
        var laterNames = later.SelectMany(c => AtlasProjector.Project(d, c.Id, AtlasContentView.MainAndOptional).Entities)
            .Select(e => e.Name).Where(n => !known.Contains(n)).Distinct().ToList();
        var knownSources = d.Checkpoints.Where(c => c.Order <= view.Order)
            .SelectMany(c => AtlasProjector.Project(d, c.Id, contentView).Entities.SelectMany(e => e.Citations)
                .Concat(AtlasProjector.Project(d, c.Id, contentView).Relationships.SelectMany(r => r.Citations)))
            .Select(c => c.Title).ToHashSet();
        var laterSources = later.SelectMany(c => AtlasProjector.Project(d, c.Id, AtlasContentView.MainAndOptional).Entities.SelectMany(e => e.Citations)
                .Concat(AtlasProjector.Project(d, c.Id, AtlasContentView.MainAndOptional).Relationships.SelectMany(r => r.Citations)))
            .Select(c => c.Title).Where(t => !knownSources.Contains(t)).Distinct().ToList();
        var laterTitles = later.Where(c => c.QuestTitle is not null).Select(c => c.QuestTitle!).ToList();
        var lockedTitles = d.Checkpoints.Where(c => c.Order > ceiling.Order && !c.Milestone)
            .SelectMany(c => new[] { c.Label, c.QuestTitle }).OfType<string>().ToList();
        return new ForbiddenSet([.. laterNames, .. laterSources, .. laterTitles], lockedTitles);
    }

    private static void AssertClean(IReadOnlyList<string> surface, IReadOnlyList<string> forbidden, string where)
    {
        foreach (var bad in forbidden)
        {
            var hit = surface.FirstOrDefault(t => t.Contains(bad, StringComparison.Ordinal));
            Assert.True(hit is null, $"'{bad}' leaked at {where}: {hit}");
        }
    }

    private static IEnumerable<string> Pickers(AtlasSession s)
    {
        foreach (var option in s.CheckpointOptions)
        {
            yield return option.Label;
            if (!option.ViewSelectable)
            {
                s.RequestCeiling(option.Id);
                if (s.PendingCeilingPrompt is { } prompt)
                {
                    yield return prompt;
                }

                s.CancelPendingCeiling();
            }
        }
    }

    private static IEnumerable<string> Content(AtlasSession s)
    {
        yield return s.PositionLabel;
        if (s.CoverageNote is { } note)
        {
            yield return note;
        }

        foreach (var option in s.ArcPickerOptions)
        {
            yield return option.Label;
        }

        if (s.Arc is { } arc)
        {
            yield return arc.RecapLabel;
            if (arc.AsOfLabel is { } asOf)
            {
                yield return asOf;
            }

            foreach (var text in Entity(arc.Entry))
            {
                yield return text;
            }
        }

        foreach (var row in s.ArcNewRows.Concat(s.ArcEndedRows).Concat(s.ChangeGroups.SelectMany(g => g.Rows)))
        {
            foreach (var text in Row(row))
            {
                yield return text;
            }
        }

        if (s.ChangesLabel is { } label)
        {
            yield return label;
        }

        foreach (var entity in s.Snapshot.Entities)
        {
            foreach (var text in Entity(entity))
            {
                yield return text;
            }
        }

        foreach (var relationship in s.Snapshot.Relationships)
        {
            foreach (var text in Relationship(relationship))
            {
                yield return text;
            }
        }

        if (s.Layout is { } layout)
        {
            foreach (var node in layout.Nodes)
            {
                yield return node.Entity.Name;
            }

            foreach (var edge in layout.Edges)
            {
                yield return edge.Label;
            }
        }

        // Refocus every reachable entry and collect its one-hop surface too.
        foreach (var entity in s.SearchResults.ToList())
        {
            if (s.FocusOn(entity.Id) && s.Neighborhood is { } neighborhood)
            {
                foreach (var neighbor in neighborhood.Neighbors)
                {
                    yield return neighbor.Label;
                    yield return neighbor.Entity.Name;
                }
            }
        }
    }

    private static IEnumerable<string> Row(AtlasChangeRow row)
    {
        yield return row.Text;
        if (row.EndedInLabel is { } ended)
        {
            yield return ended;
        }

        foreach (var c in row.EndCitations)
        {
            yield return c.Title;
        }

        if (row.Relationship is { } r)
        {
            foreach (var text in Relationship(r))
            {
                yield return text;
            }
        }

        foreach (var e in new[] { row.Source, row.Target, row.Entity }.OfType<AtlasEntityView>())
        {
            foreach (var text in Entity(e))
            {
                yield return text;
            }
        }
    }

    private static IEnumerable<string> Entity(AtlasEntityView e) =>
        new[] { e.Name, e.Summary }.Concat(e.Aliases).Concat(e.Citations.Select(c => c.Title));

    private static IEnumerable<string> Relationship(AtlasRelationshipView r) =>
        new[] { r.OutgoingLabel, r.IncomingLabel }.Concat(r.Citations.Select(c => c.Title));
}

/// <summary>The synthetic arc sample the viewer walkthrough uses must load like real data.</summary>
public class ArcSampleTests
{
    private static AtlasDataset Load()
    {
        var result = AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "sample-arc-atlas.json"), AtlasValidationMode.Strict);
        Assert.True(result.Success, string.Join("\n", result.Errors));
        return result.Dataset!;
    }

    [Fact]
    public void ArcSample_LoadsStrictWithTwoArcs()
    {
        var d = Load();
        Assert.Equal(new[] { "arc-siege", "arc-rescue" }, AtlasArcs.Eligible(d, "v2", AtlasContentView.MainAndOptional).Select(a => a.ArcId));
    }

    [Fact]
    public void ArcSample_WalkthroughStops()
    {
        var d = Load();
        var s = new AtlasSession(d, new AtlasSpoilerState("v2", "q2"));
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.Equal("The Siege of Saltmere", s.Arc!.Entry.Name);
        Assert.Equal(AtlasText.RecapThrough("The Captain's Bargain"), s.Arc.RecapLabel);
        Assert.DoesNotContain(s.Snapshot.Entities, e => e.Id == "char-orrin"); // in the story, not in the cast

        s.SetView("q3");
        Assert.Equal(new[] { AtlasText.ArcAutomatic, "The Siege of Saltmere", "The Undercity Rescue" }, s.ArcPickerOptions.Select(o => o.Label));
        Assert.Contains(s.ArcEndedRows, r => r.Relationship!.Id == "rel-tobin-prisoner-court");

        s.SetLens(AtlasLens.Changes);
        Assert.Equal(AtlasText.ChangesThisQuest, s.ChangesLabel);
        Assert.Equal("Journal: Into the Undercity", s.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Ended).Rows.Single().EndCitations.Single().Title);

        s.SetView("v2");
        Assert.Equal(AtlasText.ChangesSince("Volume One complete"), s.ChangesLabel);
        Assert.Null(s.CoverageNote);
    }
}
