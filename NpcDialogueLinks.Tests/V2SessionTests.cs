using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>NDL-018: one map, where whatever is in the middle decides what shows (docs/atlas/ux-design.md, "One map").</summary>
public class V2MapTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession At(string ceiling, string view, string? home = "char-bo") =>
        new(D, new AtlasSpoilerState(ceiling, view), AtlasContentView.MainAndOptional, home);

    [Fact]
    public void Map_RestsOnTheHomeEntryBeforeAnyArc()
    {
        var s = At("s0", "s0");
        Assert.Null(s.Arc);
        Assert.Equal("char-bo", s.FocusId);
        Assert.False(s.ShowsWholeCast);
        Assert.Equal(new[] { new AtlasTrailStep("char-bo", "Bo", false, true) }, s.Trail);
        Assert.False(s.ArcPickerOffered); // no arc has started, so the picker is left out
        Assert.Null(s.ArcPickerNote);
    }

    [Fact]
    public void Map_RestsOnTheStoryArcWhenAnArcContainsTheView()
    {
        var s = At("m2", "s2");
        Assert.Equal("arc-hold", s.Arc!.ArcId); // earliest-started of the three arcs containing s2
        Assert.Equal("evt-hold", s.FocusId);
        Assert.True(s.ShowsWholeCast);
        Assert.Equal(new[] { new AtlasTrailStep("evt-hold", "The Hold", true, true) }, s.Trail);
        Assert.Same(s.Arc.Entry, s.Focus);
        Assert.Null(s.Neighborhood); // the arc panel replaces the connections list
    }

    [Fact]
    public void Map_RestingCentreFollowsTheView()
    {
        var s = At("m2", "s0");
        Assert.Equal("char-bo", s.FocusId);
        s.SetView("s1");
        Assert.Equal("evt-hold", s.FocusId);
        s.SetView("s5"); // no arc contains s5
        Assert.Equal("char-bo", s.FocusId);
        Assert.True(s.ArcPickerOffered); // arcs have started, so the picker stays, and says why none shows
        Assert.Equal(AtlasText.NoArcHere, s.ArcPickerNote);
    }

    [Fact]
    public void Map_WithoutAVisibleHomeEntryShowsNothingOutsideArcs()
    {
        var s = At("m2", "s5", home: null);
        Assert.Null(s.FocusId);
        Assert.Empty(s.Trail);
        Assert.Null(s.Layout);
        Assert.Null(s.Focus);
    }

    [Fact]
    public void Map_APersonInTheMiddleShowsTheirWholeStorySoFar()
    {
        var s = At("m2", "s3");
        Assert.True(s.FocusOn("char-ana"));
        Assert.False(s.ShowsWholeCast);
        Assert.Equal(AtlasProjector.Project(D, "s3", AtlasContentView.MainAndOptional).GetNeighborhood("char-ana")!.Neighbors.Select(n => n.Relationship.Id),
            s.Neighborhood!.Neighbors.Select(n => n.Relationship.Id));
        Assert.Contains(s.Neighborhood.Neighbors, n => n.Entity.Id == "char-zed"); // outside every cast
        Assert.True(s.FocusOn("char-zed"));
        Assert.Equal("arc-hold", s.Arc!.ArcId); // the story arc stays, and so does its cast list
        Assert.Equal(AtlasText.CastHeading(5), s.CastHeading);
    }

    [Fact]
    public void Search_CoversEveryoneAndTheEmptyListIsTheCast()
    {
        var s = At("m2", "s3");
        var cast = s.Arc!.Cast.Entities.Select(e => e.Id).ToHashSet();
        Assert.All(s.SearchResults, e => Assert.Contains(e.Id, cast));
        s.SetSearch("Zed");
        Assert.Equal(new[] { "char-zed" }, s.SearchResults.Select(e => e.Id));
        Assert.Null(s.CastHeading);
        Assert.Contains(At("m2", "s5").SearchResults, e => e.Id == "char-zed"); // no arc: the empty search lists everyone
    }

    [Fact]
    public void Trail_GrowsAndGoesBack()
    {
        var s = At("m2", "s3");
        Assert.True(s.FocusOn("char-bo"));
        Assert.True(s.FocusOn("char-cy"));
        Assert.Equal(new[] { "The Hold", "Bo", "Cy" }, s.Trail.Select(t => t.Name));
        Assert.Equal(new[] { false, false, true }, s.Trail.Select(t => t.IsCurrent));

        Assert.True(s.FocusOn("char-bo")); // already on the trail: cut back to it
        Assert.Equal(new[] { "evt-hold", "char-bo" }, s.Trail.Select(t => t.EntityId));

        Assert.False(s.ReturnTo(1)); // the current step
        Assert.False(s.ReturnTo(-1));
        Assert.True(s.ReturnTo(0));
        Assert.True(s.ShowsWholeCast);
        Assert.Single(s.Trail);
    }

    [Fact]
    public void Trail_KeepsItsFirstStepWhenItGrowsLong()
    {
        var s = At("m2", "s3");
        foreach (var id in new[] { "char-bo", "char-cy", "char-dee", "char-ana", "char-zed", "org-foe", "char-bo" })
        {
            Assert.True(s.FocusOn(id));
        }

        Assert.Equal(new[] { "evt-hold", "char-dee", "char-ana", "char-zed", "org-foe", "char-bo" }, s.Trail.Select(t => t.EntityId));
        Assert.Equal(AtlasSession.MaxTrailSteps, s.Trail.Count);
    }

    [Fact]
    public void Trail_StartsAgainOnAStorySettingChange()
    {
        var s = At("m2", "s3");
        s.FocusOn("char-bo");
        s.SetSearch("Cy");
        s.SetView("s2");
        Assert.Equal(new[] { "evt-hold" }, s.Trail.Select(t => t.EntityId));
        Assert.Equal(string.Empty, s.SearchQuery);
        Assert.True(s.SelectionWasReset);
    }

    [Fact]
    public void Map_AnArcEntryInTheMiddleOpensThatArc()
    {
        var s = At("m2", "s3");
        Assert.True(s.FocusOn("char-ana"));
        Assert.True(s.FocusOn("evt-tie")); // ana's participant-in edge to an ended arc
        Assert.Equal("arc-tie", s.Arc!.ArcId);
        Assert.True(s.ShowsWholeCast);
        Assert.True(s.Arc.PastEnd);
        Assert.True(s.ArcPickerOptions.Single(o => o.ArcId == "arc-tie").IsCurrent); // like a pick in the picker
        Assert.Equal(new[] { "The Hold", "Ana", "The Tie" }, s.Trail.Select(t => t.Name)); // and the way back stays
        Assert.Equal(new[] { true, false, true }, s.Trail.Select(t => t.IsArc));

        Assert.True(s.ReturnTo(0));
        Assert.Equal("arc-hold", s.Arc!.ArcId);
        Assert.True(s.ShowsWholeCast);
    }

    [Fact]
    public void Map_AnArcEntryIsNamedAsOfItsOwnEffectiveStep()
    {
        // The trail names an ended arc the way the picker does, not as some later presentation would.
        var s = At("m2", "s5");
        Assert.True(s.PickArc("arc-hold"));
        Assert.Equal(s.ArcPickerOptions.Single(o => o.ArcId == "arc-hold").Label, s.Trail.Single().Name);
        Assert.Equal("Recap two.", s.Focus!.Summary);
    }

    [Fact]
    public void Position_IsTheChosenPointAndCoverageShowsOnSliceStepsOnly()
    {
        var slice = At("m2", "s2");
        Assert.Equal("Viewing: after Quest Two", slice.PositionLabel);
        Assert.Equal(AtlasText.CoverageNote, slice.CoverageNote);

        var milestone = At("m2", "m1");
        Assert.Equal("Viewing: Patch One complete", milestone.PositionLabel);
        Assert.Null(milestone.CoverageNote);
    }

    [Fact]
    public void Text_MilestonesReadAsPointsNotQuests()
    {
        var quest = new AtlasCheckpoint("q", "After Quest Two", 1) { QuestTitle = "Quest Two" };
        var milestone = new AtlasCheckpoint("m", "Patch One complete", 2) { Milestone = true };
        Assert.Equal("Viewing: after Quest Two", AtlasText.ViewingAt(quest));
        Assert.Equal("Viewing: Patch One complete", AtlasText.ViewingAt(milestone));
        Assert.Equal("Story so far, as of Patch One complete", AtlasText.RecapThrough(milestone));
        Assert.Equal("ended by Patch One complete", AtlasText.EndedIn(milestone));
        Assert.Equal("New as of Patch One complete", AtlasText.ArcNewIn(milestone));
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
        Assert.Equal("evt-hold", s.FocusId);
        var layout = s.Layout!;
        Assert.Equal("evt-hold", layout.Nodes[0].Entity.Id);
        Assert.Equal(s.Arc!.Cast.Entities.Count, layout.Nodes.Count);
        Assert.Equal(s.Arc.Cast.Relationships.Count, layout.Edges.Count);
        Assert.Same(s.Arc.Cast, s.ChartSnapshot);
        Assert.All(layout.Edges.Where(e => e.Relationship.TypeId == AtlasDataset.ParticipantTypeId), e => Assert.True(e.IsParticipation));
        Assert.Contains(layout.Edges, e => !e.IsParticipation);
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
        Assert.Equal("evt-shadow", s.FocusId);
        Assert.True(s.ArcPickerOptions.Single(o => o.ArcId == "arc-shadow").IsCurrent);

        s.SetView("s1"); // below arc-shadow's first step: the pick ends
        Assert.Equal("arc-hold", s.Arc!.ArcId);
        Assert.True(s.ArcPickerOptions[0].IsCurrent);

        s.SetView("s3"); // and does not come back
        Assert.Equal("arc-hold", s.Arc!.ArcId);
    }

    [Fact]
    public void Arc_PickStartsANewTrail()
    {
        var s = At("m2", "s3");
        s.FocusOn("char-bo");
        Assert.True(s.PickArc("arc-shadow"));
        Assert.Equal(new[] { "evt-shadow" }, s.Trail.Select(t => t.EntityId));
        Assert.False(s.SelectionWasReset); // the player did it on purpose
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
    public void Picker_SaysWhereEachArcStartsAndGroupsOnlyAcrossPatches()
    {
        // NDL-011: each arc names the step it starts at, and its patch; headings show only across more than one patch.
        var s = At("m2", "s2");
        var arcs = s.ArcPickerOptions.Where(o => o.ArcId is not null).ToList();
        Assert.Equal(new[] { "from Quest One", "from Quest Two", "from Quest Two" }, arcs.Select(o => o.Detail));
        Assert.All(arcs, o => Assert.Equal("Patch One", o.Group));
        Assert.False(s.ArcPickerGrouped);
        Assert.Equal(string.Empty, s.ArcPickerOptions[0].Detail);
        Assert.Null(s.ArcPickerOptions[0].Group);
        Assert.Equal("A Realm Reborn — Patch 2.0", AtlasText.ArcGroup("A Realm Reborn — Patch 2.0 complete"));
        Assert.Equal("Volume One", AtlasText.ArcGroup("Volume One"));
    }

    [Fact]
    public void Picker_MarksAnArcEndedOnlyOnceTheViewIsPastIt()
    {
        // NDL-011: "· ended" answers "is this arc happening now?", and only after its last step.
        Assert.DoesNotContain(At("m2", "s2").ArcPickerOptions, o => o.Detail.Contains("ended", StringComparison.Ordinal));
        var s3 = At("m2", "s3").ArcPickerOptions;
        Assert.Equal("from Quest Two · ended", s3.Single(o => o.ArcId == "arc-tie").Detail); // its last step is s2
        Assert.Equal("from Quest One", s3.Single(o => o.ArcId == "arc-hold").Detail); // at its last step: not yet
        Assert.Equal("from Quest One · ended", At("m2", "s5").ArcPickerOptions.Single(o => o.ArcId == "arc-hold").Detail);
        Assert.Equal("from Quest One", AtlasText.ArcPickerDetail("from Quest One", ended: false));
    }

    [Fact]
    public void Arc_EndedArcStaysViewableAsOfItsLastQuest()
    {
        var s = At("m2", "s5");
        Assert.Null(s.Arc); // the automatic choice: no arc contains s5
        Assert.True(s.PickArc("arc-hold"));
        Assert.True(s.ShowsWholeCast);
        Assert.True(s.Arc!.PastEnd);
        Assert.Equal(AtlasText.ArcEnded, s.Arc.AsOfLabel);
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
        Assert.Equal(new[] { "r-cy-bo-2", "r-dee-bo-2" }, s.ArcNewRows.Select(r => r.Relationship.Id).Order(StringComparer.Ordinal));
        var ended = s.ArcEndedRows;
        Assert.Equal(new[] { "r-ana-prisoner", "r-bo-possessed" }, ended.Select(r => r.Relationship.Id));
        Assert.Equal(new[] { "ended in Quest Two", "ended in Quest Three" }, ended.Select(r => r.EndedInLabel));
        Assert.All(ended, r =>
        {
            Assert.Empty(r.Relationship.Citations);
            Assert.Empty(r.Source.Citations);
            Assert.Empty(r.Target.Citations);
        });
        Assert.Equal("Ana prisoner of The Foe", ended[0].Text);
    }
}

/// <summary>
/// v2 spoiler rule 5, the per-step leak sweep, over every limit × view × content view × arc pick. It runs in fresh
/// sessions, along a walk down to the first step and back up (the pick drops at the bottom), and along a walk that turns
/// at the picked arc's first step so the pick is held both ways. At each stop it gathers every surface the session
/// exposes (including what selecting each chart edge shows, the trail, and every entry put in the middle, arc entries
/// included, which open their arc) and checks:
/// <list type="bullet">
/// <item>every entity, relationship and source shown exists, exactly as shown, in some projection at or before the view
/// (so nothing from a later step; an out-of-date earlier text would not be a leak);</item>
/// <item>no text names a quest past the view, an entity not yet introduced, or a source not yet available;</item>
/// <item>pickers and prompts never name a quest past the limit, milestones included;</item>
/// <item>end evidence appears nowhere since the Changes lens was removed (NDL-018; an end-only source sentinel proves it);</item>
/// <item>"As of" and "New in ‹last quest›" appear only after the arc's last step (rule 7).</item>
/// </list>
/// </summary>
public class V2LeakSweepTests
{
    private const string EndOnlySource = "End-only evidence for the release";

    /// <summary>The exhaustive sweep runs on the synthetic data; the real timeline has its own sweep below.</summary>
    public static TheoryData<string> Datasets() => new() { "v2fx", "arc-sample" };

    private static AtlasDataset LoadNamed(string name)
    {
        if (name == "real")
        {
            return AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Draft).Dataset!;
        }

        if (name == "arc-sample")
        {
            return AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "sample-arc-atlas.json"), AtlasValidationMode.Strict).Dataset!;
        }

        // The synthetic timeline, with the ending's evidence replaced by a source cited nowhere else.
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-ana-prisoner")["endCitations"] = new System.Text.Json.Nodes.JsonArray(V2Fx.Cite(EndOnlySource, "s2"));
        return Fx.Load(doc);
    }

    [Theory]
    [MemberData(nameof(Datasets))]
    public void Sweep_NoSurfaceRevealsAnythingBeyondTheViewOrTheLimit(string name)
    {
        var d = LoadNamed(name);
        var stops = 0;
        foreach (var ceiling in d.Checkpoints)
        {
            foreach (var contentView in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
            {
                foreach (var view in d.Checkpoints.Where(c => c.Order <= ceiling.Order))
                {
                    var picks = new List<string?> { null };
                    picks.AddRange(AtlasArcs.Eligible(d, view.Id, contentView).Select(a => a.ArcId));
                    foreach (var pick in picks)
                    {
                        // A fresh session at this stop.
                        var s = Open(d, ceiling, view, contentView, pick);
                        Check(d, s, ceiling, contentView, $"{name} fresh limit={ceiling.Id} view={view.Id} {contentView} pick={pick}");
                        stops++;

                        // The same pick held while the view walks down to the first step and back up.
                        if (pick is not null && view.Order == ceiling.Order)
                        {
                            var walk = d.Checkpoints.Where(c => c.Order < view.Order).Reverse().Concat(d.Checkpoints.Where(c => c.Order > 0 && c.Order <= view.Order));
                            foreach (var step in walk)
                            {
                                s.SetView(step.Id);
                                Check(d, s, ceiling, contentView, $"{name} walk limit={ceiling.Id} at={step.Id} {contentView} pick={pick}");
                                stops++;
                            }

                            // Turn at the arc's first step, so the pick is held all the way down and back up.
                            var first = d.Arcs.First(a => a.Id == pick).FirstOrder;
                            var held = Open(d, ceiling, view, contentView, pick);
                            var turn = d.Checkpoints.Where(c => c.Order >= first && c.Order < view.Order).Reverse()
                                .Concat(d.Checkpoints.Where(c => c.Order > first && c.Order <= view.Order));
                            foreach (var step in turn)
                            {
                                held.SetView(step.Id);
                                Assert.True(held.ArcPickerOptions.Single(o => o.ArcId == pick).IsCurrent, $"pick {pick} lost at {step.Id}");
                                Check(d, held, ceiling, contentView, $"{name} held walk limit={ceiling.Id} at={step.Id} {contentView} pick={pick}");
                                stops++;
                            }
                        }
                    }
                }
            }
        }

        Assert.True(stops > 100, $"only {stops} stops swept");
    }

    /// <summary>
    /// The real timeline (one step per quest, 747 points): sweeping every point made the suite take over half an hour, and
    /// the exhaustive sweep over the synthetic datasets already proves the session code. This one samples the points where
    /// the content changes shape: the first and last points, each milestone and the points on either side, each step that
    /// is not contiguous (parallel paths and starting cities), each arc's first and last steps and the step before it, and
    /// every 10th point. Each sampled view is swept at its own limit (the strictest picker check), in both content views,
    /// with no pick, each arc containing the view, and the most recently ended arc. Arc picks are held
    /// along walks for every arc that shares a step with another and every 5th arc. Surfaces skip the refocus of every
    /// entry: each neighbour's entry and edge is already on the snapshot. The per-point checks in RealDataTests still cover
    /// every point.
    /// </summary>
    [Fact]
    public void Sweep_RealTimeline_EveryViewAndArc()
    {
        var d = LoadNamed("real");
        var stops = 0;
        var sampled = SampledOrders(d);
        var arcsToWalk = d.Arcs.Where((a, i) => i % 5 == 0
            || d.Arcs.Any(o => o.Id != a.Id && o.FirstOrder <= a.LastOrder && a.FirstOrder <= o.LastOrder)).ToList();
        foreach (var contentView in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
        {
            foreach (var view in d.Checkpoints.Where(c => sampled.Contains(c.Order)))
            {
                var eligible = AtlasArcs.Eligible(d, view.Id, contentView).Select(a => a.ArcId).ToHashSet();
                var arcs = d.Arcs.Where(a => eligible.Contains(a.Id)).ToList();
                var picks = new List<string?> { null };
                picks.AddRange(arcs.Where(a => a.LastOrder >= view.Order).Select(a => a.Id));
                picks.AddRange(arcs.Where(a => a.LastOrder < view.Order).OrderByDescending(a => a.LastOrder).Take(1).Select(a => a.Id));
                foreach (var pick in picks)
                {
                    var s = Open(d, view, view, contentView, pick);
                    Check(d, s, view, contentView, $"real limit=view={view.Id} {contentView} pick={pick}", refocus: false);
                    stops++;
                }
            }

            foreach (var arc in arcsToWalk)
            {
                // Held from the last step down to the first and back up, then past the first (where it drops) and back.
                var last = d.Checkpoints[arc.LastOrder];
                var held = Open(d, last, last, contentView, arc.Id);
                var turn = d.Checkpoints.Where(c => c.Order >= arc.FirstOrder && c.Order < last.Order).Reverse()
                    .Concat(d.Checkpoints.Where(c => c.Order > arc.FirstOrder && c.Order <= last.Order));
                foreach (var step in turn)
                {
                    held.SetView(step.Id);
                    Assert.True(held.ArcPickerOptions.Single(o => o.ArcId == arc.Id).IsCurrent, $"pick {arc.Id} lost at {step.Id}");
                    Check(d, held, last, contentView, $"real held walk limit={last.Id} at={step.Id} {contentView} pick={arc.Id}", refocus: false);
                    stops++;
                }

                var bottom = Math.Max(0, arc.FirstOrder - 2);
                var below = d.Checkpoints.Where(c => c.Order >= bottom && c.Order < last.Order).Reverse()
                    .Concat(d.Checkpoints.Where(c => c.Order > bottom && c.Order <= arc.FirstOrder));
                foreach (var step in below)
                {
                    held.SetView(step.Id);
                    Check(d, held, last, contentView, $"real walk limit={last.Id} at={step.Id} {contentView} pick={arc.Id}", refocus: false);
                    stops++;
                }
            }
        }

        Assert.True(stops > 1000, $"only {stops} stops swept");
    }

    /// <summary>The real timeline's sampled points (see <see cref="Sweep_RealTimeline_EveryViewAndArc"/>).</summary>
    private static HashSet<int> SampledOrders(AtlasDataset d)
    {
        var last = d.Checkpoints.Count - 1;
        var orders = new HashSet<int> { 0, last };
        foreach (var c in d.Checkpoints)
        {
            if (c.Order % 10 == 0 || !c.ContiguousWithPrevious)
            {
                orders.Add(c.Order);
            }

            if (c.Milestone)
            {
                orders.UnionWith(new[] { c.Order - 1, c.Order, c.Order + 1 });
            }
        }

        foreach (var a in d.Arcs)
        {
            orders.UnionWith(new[] { a.FirstOrder - 1, a.FirstOrder, a.LastOrder });
        }

        orders.RemoveWhere(o => o < 0 || o > last);
        return orders;
    }

    private static AtlasSession Open(AtlasDataset d, AtlasCheckpoint ceiling, AtlasCheckpoint view, AtlasContentView contentView, string? pick)
    {
        var s = new AtlasSession(d, new AtlasSpoilerState(ceiling.Id, view.Id), contentView);
        Assert.True(s.PickArc(pick));
        return s;
    }

    private static void Check(AtlasDataset d, AtlasSession s, AtlasCheckpoint ceiling, AtlasContentView contentView, string where, bool refocus = true)
    {
        Assert.True(d.TryGetCheckpoint(s.SpoilerState.ViewId, out var view));
        var surface = Gather(s, refocus);
        var known = Known(d, contentView);
        var at = view.Order;

        foreach (var entity in surface.Entities)
        {
            Assert.True(known.EntityFrom.TryGetValue(EntityKey(entity), out var from) && from <= at, $"entity {entity.Id} '{entity.Summary}' is not as of the view at {where}");
        }

        foreach (var relationship in surface.Relationships)
        {
            Assert.True(known.RelationshipFrom.TryGetValue(RelationshipKey(relationship), out var from) && from <= at, $"relationship {relationship.Id} is not as of the view at {where}");
        }

        foreach (var citation in surface.Citations)
        {
            Assert.True(known.SourceFrom.TryGetValue(citation, out var from) && from <= at, $"source '{citation.Title}' ({citation.Url}) is not available by the view at {where}");
        }

        // End evidence: shown nowhere, so an end-only source never appears.
        AssertNoText(surface.Texts, EndOnlySource, where);

        // No text names a later quest, an entity not yet introduced, or a source not yet available. A citation's own title
        // and link are checked above (available by the view), and a later quest title inside one spoils nothing: 5.0's
        // "On Track" and 7.0's, or "Travelers at the Crossroads" (6.0) and "Crossroads" (7.1). Mirrors the build's lint.
        var cited = surface.Citations.SelectMany(c => new[] { c.Title, c.Url?.ToString() }).OfType<string>().ToHashSet();
        var later = known.Later.FirstHit(surface.Texts.Where(t => !cited.Contains(t)), at);
        Assert.True(later is null, $"'{later?.Needle}' leaked at {where}: {later?.Text}");

        // Pickers and prompts never name a quest past the limit (milestones are named on purpose).
        var locked = Locked(d).FirstHit(Pickers(s).ToList(), ceiling.Order);
        Assert.True(locked is null, $"'{locked?.Needle}' leaked at {where} (pickers): {locked?.Text}");

        // Rule 7: an arc in the middle before or at its last step looks exactly like a mid-arc step.
        Assert.True(surface.EndMarkedEarly.Count == 0, $"arc {string.Join(", ", surface.EndMarkedEarly)} marked as ended before its end at {where}");
    }

    /// <summary>
    /// What is known from which point, per content view, computed once per dataset: the order each entity text,
    /// relationship and source first appears, and a scanner for every string that must not appear before a given order
    /// (a later entity's name or alias, a later source's title, a later quest's title). Each check is then a lookup, so
    /// the sweep grows linearly with the timeline (2026-11-19: rebuilding these per view made 747 points take over 30 min).
    /// </summary>
    private sealed record KnownFrom(
        Dictionary<(string, string, string, string), int> EntityFrom,
        Dictionary<(string, string, string, string), int> RelationshipFrom,
        Dictionary<AtlasCitationView, int> SourceFrom,
        TextScanner Later);

    private static KnownFrom Known(AtlasDataset d, AtlasContentView contentView)
    {
        var cache = KnownCache.GetOrCreateValue(d);
        lock (cache)
        {
            if (cache.TryGetValue(contentView, out var hit))
            {
                return hit;
            }

            var entityFrom = new Dictionary<(string, string, string, string), int>();
            var relationshipFrom = new Dictionary<(string, string, string, string), int>();
            var sourceFrom = new Dictionary<AtlasCitationView, int>();
            var nameFrom = new Dictionary<string, int>();
            var titleFrom = new Dictionary<string, int>();
            var nameLast = new Dictionary<string, int>();
            var titleLast = new Dictionary<string, int>();
            foreach (var c in d.Checkpoints)
            {
                var p = Project(d, c.Id, contentView);
                foreach (var e in p.Entities)
                {
                    entityFrom.TryAdd(EntityKey(e), c.Order);
                    foreach (var n in e.Aliases.Append(e.Name))
                    {
                        nameFrom.TryAdd(n, c.Order);
                    }
                }

                foreach (var r in p.Relationships)
                {
                    relationshipFrom.TryAdd(RelationshipKey(r), c.Order);
                }

                foreach (var cite in p.Entities.SelectMany(e => e.Citations).Concat(p.Relationships.SelectMany(r => r.Citations)))
                {
                    sourceFrom.TryAdd(cite, c.Order);
                    titleFrom.TryAdd(cite.Title, c.Order);
                }

                var full = Project(d, c.Id, AtlasContentView.MainAndOptional);
                foreach (var n in full.Entities.SelectMany(e => e.Aliases.Append(e.Name)))
                {
                    nameLast[n] = c.Order;
                }

                foreach (var cite in full.Entities.SelectMany(e => e.Citations).Concat(full.Relationships.SelectMany(r => r.Citations)))
                {
                    titleLast[cite.Title] = c.Order;
                }
            }

            // A name or source title is bad at a view before the earlier of two points: where it becomes known in this
            // content view, and the last point it still appears anywhere (after which it is no longer "later"). A quest
            // title is bad before its own step.
            var later = new TextScanner();
            foreach (var (n, last) in nameLast)
            {
                later.Add(n, Math.Min(last, nameFrom.GetValueOrDefault(n, int.MaxValue)));
            }

            foreach (var (title, last) in titleLast)
            {
                later.Add(title, Math.Min(last, titleFrom.GetValueOrDefault(title, int.MaxValue)));
            }

            // A quest title shared by two steps (Shadowbringers' and Dawntrail's "On Track") is known from the earlier one.
            foreach (var c in d.Checkpoints.Where(c => c.QuestTitle is not null).DistinctBy(c => c.QuestTitle))
            {
                later.Add(c.QuestTitle!, c.Order);
            }

            later.AddTitleContainers(d);
            return cache[contentView] = new KnownFrom(entityFrom, relationshipFrom, sourceFrom, later);
        }
    }

    /// <summary>Quest titles and step labels, each bad in a picker while the limit is below its step.</summary>
    private static TextScanner Locked(AtlasDataset d) => LockedCache.GetValue(d, data =>
    {
        // A label or title is fine once its earliest step is reached: Shadowbringers' "On Track" (#613) and Dawntrail's
        // (#911) share one, and only the earlier counts (2026-11-19).
        var first = new Dictionary<string, int>();
        foreach (var c in data.Checkpoints)
        {
            foreach (var text in new[] { c.Milestone ? null : c.Label, c.QuestTitle }.OfType<string>())
            {
                first.TryAdd(text, c.Order);
            }
        }

        var scanner = new TextScanner();
        foreach (var (text, order) in first)
        {
            scanner.Add(text, order);
        }

        scanner.AddTitleContainers(data);
        return scanner;
    });

    /// <summary>Finds any registered string (case-sensitive) that is bad at an order: bad while order &lt; its threshold.</summary>
    private sealed class TextScanner
    {
        private readonly Dictionary<string, int> until = new();
        private Dictionary<(char, char), List<(string Needle, int Until)>>? byPrefix;

        public void Add(string needle, int badUntil)
        {
            if (needle.Length < 2)
            {
                return;
            }

            until[needle] = Math.Max(badUntil, until.GetValueOrDefault(needle, int.MinValue));
            byPrefix = null;
        }

        private readonly Dictionary<string, List<(string Container, int From)>> containers = new();

        /// <summary>
        /// A needle inside a longer string that is fine from a given order is no leak there: "Crossroads" (7.1) inside
        /// "Travelers at the Crossroads" (6.0) once that quest is reached.
        /// </summary>
        public void AddContainer(string needle, string container, int from)
        {
            if (!containers.TryGetValue(needle, out var list))
            {
                containers[needle] = list = new();
            }

            list.Add((container, from));
        }

        private bool InsideKnownContainer(string text, int i, string needle, int at)
        {
            if (!containers.TryGetValue(needle, out var list))
            {
                return false;
            }

            foreach (var (container, from) in list.Where(c => c.From <= at))
            {
                for (var p = text.IndexOf(container, StringComparison.Ordinal); p >= 0; p = text.IndexOf(container, p + 1, StringComparison.Ordinal))
                {
                    if (p <= i && i + needle.Length <= p + container.Length)
                    {
                        return true;
                    }
                }
            }

            return false;
        }

        /// <summary>Registers every quest title that sits inside another, earlier-or-equal quest title as such.</summary>
        public void AddTitleContainers(AtlasDataset d)
        {
            var first = new Dictionary<string, int>();
            foreach (var c in d.Checkpoints.Where(c => c.QuestTitle is not null))
            {
                first.TryAdd(c.QuestTitle!, c.Order);
            }

            foreach (var (needle, _) in first)
            {
                foreach (var (container, from) in first)
                {
                    if (container != needle && container.Contains(needle, StringComparison.Ordinal))
                    {
                        AddContainer(needle, container, from);
                    }
                }
            }
        }

        public (string Needle, string Text)? FirstHit(IEnumerable<string> texts, int at)
        {
            var index = byPrefix ??= until.GroupBy(kv => (kv.Key[0], kv.Key[1]))
                .ToDictionary(g => g.Key, g => g.Select(kv => (kv.Key, kv.Value)).ToList());
            foreach (var text in texts)
            {
                for (var i = 0; i + 1 < text.Length; i++)
                {
                    if (!index.TryGetValue((text[i], text[i + 1]), out var list))
                    {
                        continue;
                    }

                    foreach (var (needle, u) in list)
                    {
                        if (at < u && i + needle.Length <= text.Length && string.CompareOrdinal(text, i, needle, 0, needle.Length) == 0
                            && !InsideKnownContainer(text, i, needle, at))
                        {
                            return (needle, text);
                        }
                    }
                }
            }

            return null;
        }
    }

    private static readonly System.Runtime.CompilerServices.ConditionalWeakTable<AtlasDataset, Dictionary<AtlasContentView, KnownFrom>> KnownCache = new();

    private static readonly System.Runtime.CompilerServices.ConditionalWeakTable<AtlasDataset, TextScanner> LockedCache = new();

    private static readonly System.Runtime.CompilerServices.ConditionalWeakTable<AtlasDataset, Dictionary<(string, AtlasContentView), AtlasSnapshot>> ProjectionCache = new();

    private static AtlasSnapshot Project(AtlasDataset d, string checkpointId, AtlasContentView view)
    {
        var cache = ProjectionCache.GetOrCreateValue(d);
        lock (cache)
        {
            if (!cache.TryGetValue((checkpointId, view), out var snapshot))
            {
                cache[(checkpointId, view)] = snapshot = AtlasProjector.Project(d, checkpointId, view);
            }

            return snapshot;
        }
    }

    private static (string, string, string, string) EntityKey(AtlasEntityView e) => (e.Id, e.Name, e.Summary, string.Join("|", e.Aliases));

    private static (string, string, string, string) RelationshipKey(AtlasRelationshipView r) => (r.SourceId, r.TypeId, r.TargetId, r.OutgoingLabel);

    private static void AssertNoText(IEnumerable<string> texts, string bad, string where)
    {
        var hit = texts.FirstOrDefault(t => t.Contains(bad, StringComparison.Ordinal));
        Assert.True(hit is null, $"'{bad}' leaked at {where}: {hit}");
    }

    private sealed class Surface
    {
        public List<string> Texts { get; } = new();

        public List<AtlasEntityView> Entities { get; } = new();

        public List<AtlasRelationshipView> Relationships { get; } = new();

        public List<AtlasCitationView> Citations { get; } = new();

        /// <summary>Arcs shown in the middle with an end marker although the view is not past their last step (rule 7).</summary>
        public List<string> EndMarkedEarly { get; } = new();

        public void Add(AtlasEntityView? e)
        {
            if (e is null)
            {
                return;
            }

            Entities.Add(e);
            Texts.AddRange(e.Aliases.Append(e.Name).Append(e.Summary));
            Cite(e.Citations);
        }

        public void Add(AtlasRelationshipView? r)
        {
            if (r is null)
            {
                return;
            }

            Relationships.Add(r);
            Texts.Add(r.OutgoingLabel);
            Texts.Add(r.IncomingLabel);
            Cite(r.Citations);
        }

        public void Add(AtlasArcRow row)
        {
            Texts.Add(row.Text);
            Texts.AddRange(new[] { row.EndedInLabel }.OfType<string>());
            Add(row.Relationship);
            Add(row.Source);
            Add(row.Target);
        }

        private void Cite(IEnumerable<AtlasCitationView> citations)
        {
            foreach (var c in citations)
            {
                Citations.Add(c);
                Texts.Add(c.Title);
                Texts.AddRange(new[] { c.Url?.ToString() }.OfType<string>());
            }
        }
    }

    private static Surface Gather(AtlasSession s, bool refocus = true)
    {
        var x = new Surface();
        x.Texts.Add(s.PositionLabel);
        x.Texts.AddRange(new[] { s.CoverageNote, s.CastHeading, s.ArcPickerNote }.OfType<string>());
        x.Texts.AddRange(s.ArcPickerOptions.SelectMany(o => new[] { o.Label, o.Detail, o.Group ?? string.Empty }));
        GatherCentre(s, x);
        s.Snapshot.Entities.ToList().ForEach(x.Add);
        s.Snapshot.Relationships.ToList().ForEach(x.Add);
        s.SearchResultGroups.SelectMany(g => g.Entries).ToList().ForEach(x.Add);

        // Putting every entry on the snapshot in the middle (arc entries included, which open their arc) shows its
        // one-hop surface or its arc panel, and grows the trail. The pick in force is put back afterwards.
        var pick = s.ArcPickerOptions.First(o => o.IsCurrent).ArcId;
        foreach (var entity in refocus ? s.Snapshot.Entities.ToList() : [])
        {
            if (s.FocusOn(entity.Id))
            {
                GatherCentre(s, x);
            }
        }

        if (refocus)
        {
            Assert.True(s.PickArc(pick));
        }

        return x;
    }

    /// <summary>What the middle of the map shows: the trail, the chart and every edge's card, and the arc panel or the connections.</summary>
    private static void GatherCentre(AtlasSession s, Surface x)
    {
        x.Texts.AddRange(s.Trail.Select(t => t.Name));
        x.Texts.AddRange(new[] { s.ArcNewHeading }.OfType<string>());
        x.Add(s.Focus);
        if (s.ShowsWholeCast)
        {
            var arc = s.Arc!;
            if (!arc.PastEnd && (arc.AsOfLabel is not null || s.ArcNewHeading!.StartsWith("New in", StringComparison.Ordinal)))
            {
                x.EndMarkedEarly.Add(arc.ArcId);
            }

            x.Texts.Add(arc.RecapLabel);
            x.Texts.AddRange(new[] { arc.AsOfLabel }.OfType<string>());
            x.Add(arc.Entry);
            arc.Cast.Entities.ToList().ForEach(x.Add);
            arc.Cast.Relationships.ToList().ForEach(x.Add);
            foreach (var row in s.ArcNewRows.Concat(s.ArcEndedRows))
            {
                x.Add(row);
            }
        }
        foreach (var neighbor in s.Neighborhood?.Neighbors ?? [])
        {
            x.Texts.Add(neighbor.Label);
            x.Add(neighbor.Entity);
            x.Add(neighbor.Relationship);
        }

        if (s.Layout is { } layout)
        {
            layout.Nodes.Select(n => n.Entity).ToList().ForEach(x.Add);
            foreach (var edge in layout.Edges)
            {
                x.Texts.Add(edge.Label);
                x.Add(edge.Relationship);
            }

            // Selecting each chart edge shows its card.
            foreach (var edge in layout.Edges)
            {
                if (s.SelectRelationship(edge.Relationship.Id))
                {
                    x.Add(s.SelectedRelationship);
                    x.Add(s.ChartSnapshot.FindEntity(s.SelectedRelationship!.SourceId));
                    x.Add(s.ChartSnapshot.FindEntity(s.SelectedRelationship.TargetId));
                }
            }

            s.ClearSelection();
        }
    }

    private static IEnumerable<string> Pickers(AtlasSession s)
    {
        foreach (var option in s.CheckpointOptions.ToList())
        {
            yield return option.Label;
            yield return AtlasText.LockedCheckpoint(option.Label);
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
}

/// <summary>Round-1 council cases: pick lifetime edges, caching and the cast heading.</summary>
public class V2SessionEdgeTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession At(string ceiling, string view, string? home = AtlasDefaults.HomeEntityId) =>
        new(D, new AtlasSpoilerState(ceiling, view), AtlasContentView.MainAndOptional, home);

    [Fact]
    public void Pick_StaysOnScreenPastItsEnd()
    {
        var s = At("m2", "s2");
        Assert.True(s.PickArc("arc-hold"));
        s.SetView("s5"); // no arc contains s5, so the automatic choice alone would rest on the home entry
        Assert.True(s.ShowsWholeCast);
        Assert.Equal(AtlasText.ArcEnded, s.Arc!.AsOfLabel);
        Assert.Equal("New in Quest Three", s.ArcNewHeading);
    }

    [Fact]
    public void Pick_OnceItEndsTheMapRestsOnTheHomeEntry()
    {
        // NDL-018 retires D12: without lenses, an ended or cleared pick simply returns the map to its resting centre.
        var dropped = At("m2", "s3", home: "char-bo");
        dropped.PickArc("arc-shadow");
        dropped.SetView("s0");
        Assert.Null(dropped.Arc);
        Assert.Equal("char-bo", dropped.FocusId);

        var cleared = At("m2", "s2", home: "char-bo");
        cleared.PickArc("arc-hold");
        cleared.PickArc(null);
        cleared.SetView("s5");
        Assert.Null(cleared.Arc);
        Assert.Equal("char-bo", cleared.FocusId);
    }

    [Fact]
    public void Pick_ClearedByTheAutomaticChoice()
    {
        var s = At("m2", "s3");
        s.PickArc("arc-shadow");
        Assert.True(s.PickArc(null));
        Assert.Equal("arc-hold", s.Arc!.ArcId);
        Assert.True(s.ArcPickerOptions[0].IsCurrent);
    }

    [Fact]
    public void Pick_SurvivesAContentViewSwitch()
    {
        var s = At("m2", "s3");
        s.PickArc("arc-shadow");
        s.SetContentView(AtlasContentView.MainStory);
        Assert.Equal("arc-shadow", s.Arc!.ArcId);
    }

    [Fact]
    public void Pick_EndsWhenLoweringTheLimitClampsTheViewBelowItsStart()
    {
        var s = At("m2", "s3");
        s.PickArc("arc-shadow"); // starts at s2
        Assert.Equal(AtlasStateChange.Changed, s.RequestCeiling("s1")); // lowering needs no confirmation and clamps the view
        Assert.Equal("s1", s.SpoilerState.ViewId);
        Assert.Equal("arc-hold", s.Arc!.ArcId);
    }

    [Fact]
    public void PickChangesDismissAPendingRaise()
    {
        var s = At("s2", "s2");
        Assert.Equal(AtlasStateChange.NeedsConfirmation, s.RequestCeiling("s3"));
        s.PickArc("arc-tie");
        Assert.Null(s.PendingCeilingId);
    }

    [Fact]
    public void ResetHint_OnlyAfterTheSessionLeftItsResting()
    {
        var s = At("m2", "s2");
        s.SetView("s3");
        Assert.False(s.SelectionWasReset); // the whole cast is the map's resting view
        s.FocusOn("char-bo");
        s.SetView("s2");
        Assert.True(s.SelectionWasReset);
    }

    [Fact]
    public void Snapshot_IsAlwaysTheUnfilteredProjection()
    {
        var s = At("m2", "s0", home: "char-bo");
        foreach (var view in new[] { "s1", "s2", "s3", "m1", "s5" })
        {
            s.SetView(view);
            Assert.Equal(AtlasProjector.Project(D, view, AtlasContentView.MainAndOptional).Entities.Select(e => e.Id), s.Snapshot.Entities.Select(e => e.Id));
        }
    }

    [Fact]
    public void DerivedState_IsCachedUntilSomethingChanges()
    {
        var arc = At("m2", "s3");
        var trail = arc.Trail;
        Assert.Same(trail, arc.Trail);
        arc.FocusOn("char-bo");
        Assert.NotSame(trail, arc.Trail);
        arc.ReturnTo(0);

        var (picker, rows, ended, layout) = (arc.ArcPickerOptions, arc.ArcNewRows, arc.ArcEndedRows, arc.Layout);
        Assert.Same(picker, arc.ArcPickerOptions);
        Assert.Same(rows, arc.ArcNewRows);
        Assert.Same(ended, arc.ArcEndedRows);
        Assert.Same(layout, arc.Layout);
        arc.SetView("s2");
        Assert.NotSame(picker, arc.ArcPickerOptions);
        Assert.NotSame(rows, arc.ArcNewRows);
        Assert.NotSame(ended, arc.ArcEndedRows);
        Assert.NotSame(layout, arc.Layout);
    }

    [Fact]
    public void Search_StillFindsTheArcEntryByName()
    {
        var s = At("m2", "s2");
        s.SetSearch("The Hold");
        Assert.Contains(s.SearchResults, e => e.Id == "evt-hold");
    }

    [Fact]
    public void ArcPanelSurfaces_AreEmptyAwayFromTheArcEntry()
    {
        var s = At("m2", "s3");
        Assert.True(s.FocusOn("char-bo"));
        Assert.Empty(s.ArcNewRows);
        Assert.Empty(s.ArcEndedRows);
        Assert.Null(s.ArcNewHeading);
        Assert.NotNull(s.CastHeading); // the browse list keeps the story arc's cast
        Assert.Null(At("m2", "s5").CastHeading); // no story arc here
    }

    [Fact]
    public void Cast_HeadingCountsMembersAndTheListLeavesOutTheEntry()
    {
        var s = At("m2", "s2"); // arc-hold at s2: ana, bo, cy, foe, dee
        Assert.Equal(AtlasText.CastHeading(5), s.CastHeading);
        Assert.Equal(5, s.SearchResults.Count);
        Assert.DoesNotContain(s.SearchResults, e => e.Id == "evt-hold");
        s.SetSearch("o");
        Assert.Null(s.CastHeading); // a search lists matches from everyone
    }

    [Fact]
    public void NewRows_LeaveOutParticipation()
    {
        var s = At("m2", "s2");
        Assert.Contains(s.Arc!.New, r => r.Id == "p-dee-hold"); // the core reports the joiner's edge
        Assert.DoesNotContain(s.ArcNewRows, r => r.Relationship.TypeId == AtlasDataset.ParticipantTypeId);
    }

    [Fact]
    public void WholeCast_OnlySpokesToTheArcEntryAreFaint()
    {
        // A nested arc's event joins arc-hold's cast, so ana's participant-in edge to it runs between two ring members.
        var doc = V2Fx.Doc();
        Fx.Relationships(doc).Add(new System.Text.Json.Nodes.JsonObject
        {
            ["id"] = "p-tie-hold", ["source"] = "evt-tie", ["type"] = "participant-in", ["target"] = "evt-hold", ["validFrom"] = "s2", ["scope"] = "main",
            ["citations"] = new System.Text.Json.Nodes.JsonArray(V2Fx.Cite("Src s2", "s2")), ["review"] = "reviewed",
        });
        var s = new AtlasSession(Fx.Load(doc), new AtlasSpoilerState("m2", "s2"));
        Assert.Equal("arc-hold", s.Arc!.ArcId);
        var ringEdge = s.Layout!.Edges.Single(e => e.Relationship.Id == "p-ana-tie");
        Assert.False(ringEdge.IsParticipation);
        Assert.True(s.Layout.Edges.Single(e => e.Relationship.Id == "p-tie-hold").IsParticipation);
        Assert.Contains(s.ArcNewRows, r => r.Relationship.Id == "p-ana-tie");
        Assert.True(s.SelectRelationship("p-ana-tie"));
    }

    [Fact]
    public void WholeCast_ParticipationSpokesAreNotSelectable()
    {
        var s = At("m2", "s3");
        Assert.False(s.SelectRelationship("p-bo-hold"));
        s.FocusOn("char-bo");
        Assert.True(s.SelectRelationship("p-bo-hold")); // a normal edge in the one-hop view
    }
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
        Assert.True(s.ShowsWholeCast);
        Assert.Equal("The Siege of Saltmere", s.Arc!.Entry.Name);
        Assert.Equal("Story so far, through The Captain's Bargain", s.Arc.RecapLabel);
        Assert.DoesNotContain(s.Arc.Cast.Entities, e => e.Id == "char-orrin"); // in the story, not in the cast
        Assert.Contains(s.Snapshot.Entities, e => e.Id == "char-orrin");
        Assert.Equal(new[] { "Captain Mira allied with Vessa", "Vessa member of The Drowned Court" }, s.ArcNewRows.Select(r => r.Text));
        Assert.Equal(new[] { "Captain Mira member of The Harbor Watch" }, s.ArcEndedRows.Select(r => r.Text));

        s.SetView("q3");
        Assert.Equal(new[] { AtlasText.ArcAutomatic, "The Siege of Saltmere", "The Undercity Rescue" }, s.ArcPickerOptions.Select(o => o.Label));
        Assert.Contains(s.ArcEndedRows, r => r.Relationship.Id == "rel-tobin-prisoner-court");

        s.SetView("v2");
        Assert.Null(s.CoverageNote);
    }
}
