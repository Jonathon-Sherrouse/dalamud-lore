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
        Assert.Equal("Viewing: Patch One complete", milestone.PositionLabel);
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
        s.SetLens(AtlasLens.Arc);
        Assert.Null(s.Arc); // the automatic choice: no arc contains s5
        Assert.True(s.PickArc("arc-hold"));
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
        Assert.Equal(new[] { "r-cy-bo-2", "r-dee-bo-2" }, s.ArcNewRows.Select(r => r.Relationship!.Id).Order(StringComparer.Ordinal));
        var ended = s.ArcEndedRows;
        Assert.Equal(new[] { "r-ana-prisoner", "r-bo-possessed" }, ended.Select(r => r.Relationship!.Id));
        Assert.Equal(new[] { "ended in Quest Two", "ended in Quest Three" }, ended.Select(r => r.EndedInLabel));
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
    public void Changes_PickedRowSaysWhatHappenedAndWhen()
    {
        // Council round 1 (NDL-011): an ended row's details must not read as a live relationship.
        var s = Changes("s2");
        Assert.Null(s.SelectedChangeStatus);
        Assert.True(s.SelectChange("ended:r-ana-prisoner"));
        Assert.Equal("Ended in Quest Two", s.SelectedChangeStatus);
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
        Assert.Equal("Added by Patch One complete", AtlasText.ChangeStatus(AtlasChangeKind.Added, milestone));
        Assert.Equal("Description updated in Quest Two", AtlasText.ChangeStatus(AtlasChangeKind.Updated, quest));
    }

    [Fact]
    public void Changes_RowsAreSelectableOnlyInTheChangesLens()
    {
        var s = new AtlasSession(D, new AtlasSpoilerState("m2", "s2")); // Arc lens
        Assert.False(s.SelectChange("ended:r-ana-prisoner"));
    }
}

/// <summary>
/// v2 spoiler rule 5, the per-step leak sweep, over every limit × view × content view × lens × arc pick. It runs in fresh
/// sessions, along a walk down to the first step and back up (the pick drops at the bottom), and along a walk that turns
/// at the picked arc's first step so the pick is held both ways. At each stop it gathers every surface the session
/// exposes (including what selecting each chart edge and each change shows, and every refocus) and checks:
/// <list type="bullet">
/// <item>every entity, relationship and source shown exists, exactly as shown, in some projection at or before the view
/// (so nothing from a later step; an out-of-date earlier text would not be a leak);</item>
/// <item>every end citation on a Changes "ended" row is that relationship's own end evidence (title and URL), available by the view;</item>
/// <item>no text names a quest past the view, an entity not yet introduced, or a source not yet available;</item>
/// <item>pickers and prompts never name a quest past the limit, milestones included;</item>
/// <item>end evidence appears only on a Changes "ended" row (an end-only source sentinel proves it);</item>
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
                foreach (var lens in new[] { AtlasLens.Arc, AtlasLens.StoryPoint, AtlasLens.Changes })
                {
                    foreach (var view in d.Checkpoints.Where(c => c.Order <= ceiling.Order))
                    {
                        var picks = new List<string?> { null };
                        picks.AddRange(AtlasArcs.Eligible(d, view.Id, contentView).Select(a => a.ArcId));
                        foreach (var pick in picks)
                        {
                            // A fresh session at this stop.
                            var s = Open(d, ceiling, view, contentView, lens, pick);
                            Check(d, s, ceiling, contentView, $"{name} fresh limit={ceiling.Id} view={view.Id} {contentView} {lens} pick={pick}");
                            stops++;

                            // The same pick held while the view walks down to the first step and back up.
                            if (pick is not null && view.Order == ceiling.Order)
                            {
                                var walk = d.Checkpoints.Where(c => c.Order < view.Order).Reverse().Concat(d.Checkpoints.Where(c => c.Order > 0 && c.Order <= view.Order));
                                foreach (var step in walk)
                                {
                                    s.SetView(step.Id);
                                    Check(d, s, ceiling, contentView, $"{name} walk limit={ceiling.Id} at={step.Id} {contentView} {lens} pick={pick}");
                                    stops++;
                                }

                                // Turn at the arc's first step, so the pick is held all the way down and back up.
                                var first = d.Arcs.First(a => a.Id == pick).FirstOrder;
                                var held = Open(d, ceiling, view, contentView, lens, pick);
                                var turn = d.Checkpoints.Where(c => c.Order >= first && c.Order < view.Order).Reverse()
                                    .Concat(d.Checkpoints.Where(c => c.Order > first && c.Order <= view.Order));
                                foreach (var step in turn)
                                {
                                    held.SetView(step.Id);
                                    Assert.True(held.ArcPickerOptions.Single(o => o.ArcId == pick).IsCurrent, $"pick {pick} lost at {step.Id}");
                                    Check(d, held, ceiling, contentView, $"{name} held walk limit={ceiling.Id} at={step.Id} {contentView} {lens} pick={pick}");
                                    stops++;
                                }
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
    /// every 10th point. Each sampled view is swept at its own limit (the strictest picker check), in both content views and
    /// all three lenses, with no pick, each arc containing the view, and the most recently ended arc. Arc picks are held
    /// along walks for every arc that shares a step with another and every 5th arc. Surfaces skip the refocus of every
    /// entry: each neighbour's entry and edge is already on the snapshot. The per-point checks in RealDataTests still cover
    /// every point.
    /// </summary>
    [Fact]
    public void Sweep_RealTimeline_EveryViewLensAndArc()
    {
        var d = LoadNamed("real");
        var stops = 0;
        var sampled = SampledOrders(d);
        var arcsToWalk = d.Arcs.Where((a, i) => i % 5 == 0
            || d.Arcs.Any(o => o.Id != a.Id && o.FirstOrder <= a.LastOrder && a.FirstOrder <= o.LastOrder)).ToList();
        foreach (var contentView in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
        {
            foreach (var lens in new[] { AtlasLens.Arc, AtlasLens.StoryPoint, AtlasLens.Changes })
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
                        var s = Open(d, view, view, contentView, lens, pick);
                        Check(d, s, view, contentView, $"real limit=view={view.Id} {contentView} {lens} pick={pick}", refocus: false);
                        stops++;
                    }
                }

                foreach (var arc in arcsToWalk)
                {
                    // Held from the last step down to the first and back up, then past the first (where it drops) and back.
                    var last = d.Checkpoints[arc.LastOrder];
                    var held = Open(d, last, last, contentView, lens, arc.Id);
                    var turn = d.Checkpoints.Where(c => c.Order >= arc.FirstOrder && c.Order < last.Order).Reverse()
                        .Concat(d.Checkpoints.Where(c => c.Order > arc.FirstOrder && c.Order <= last.Order));
                    foreach (var step in turn)
                    {
                        held.SetView(step.Id);
                        Assert.True(held.ArcPickerOptions.Single(o => o.ArcId == arc.Id).IsCurrent, $"pick {arc.Id} lost at {step.Id}");
                        Check(d, held, last, contentView, $"real held walk limit={last.Id} at={step.Id} {contentView} {lens} pick={arc.Id}", refocus: false);
                        stops++;
                    }

                    var bottom = Math.Max(0, arc.FirstOrder - 2);
                    var below = d.Checkpoints.Where(c => c.Order >= bottom && c.Order < last.Order).Reverse()
                        .Concat(d.Checkpoints.Where(c => c.Order > bottom && c.Order <= arc.FirstOrder));
                    foreach (var step in below)
                    {
                        held.SetView(step.Id);
                        Check(d, held, last, contentView, $"real walk limit={last.Id} at={step.Id} {contentView} {lens} pick={arc.Id}", refocus: false);
                        stops++;
                    }
                }
            }
        }

        Assert.True(stops > 1000, $"only {stops} stops swept");
    }

    /// <summary>The real timeline's sampled points (see <see cref="Sweep_RealTimeline_EveryViewLensAndArc"/>).</summary>
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

    private static AtlasSession Open(AtlasDataset d, AtlasCheckpoint ceiling, AtlasCheckpoint view, AtlasContentView contentView, AtlasLens lens, string? pick)
    {
        var s = new AtlasSession(d, new AtlasSpoilerState(ceiling.Id, view.Id), contentView);
        Assert.True(s.PickArc(pick));
        s.SetLens(lens);
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

        // End evidence: only on a Changes "ended" row, and an end-only source never appears anywhere else.
        foreach (var (row, inChangesEnded) in surface.Rows)
        {
            if (!inChangesEnded)
            {
                Assert.True(row.EndCitations.Count == 0, $"end evidence on {row.Key} outside a Changes ended row at {where}");
            }
        }

        AssertNoText(surface.Texts, EndOnlySource, where);

        foreach (var (row, inChangesEnded) in surface.Rows.Where(r => r.InChangesEnded))
        {
            var raw = d.Relationships.Single(r => r.Id == row.Relationship!.Id);
            var allowed = raw.EndCitations.Where(c => c.AvailableAtOrder <= view.Order).Select(c => (c.Title, c.Url?.ToString())).ToHashSet();
            Assert.All(row.EndCitations, c => Assert.True(allowed.Contains((c.Title, c.Url?.ToString())), $"end citation '{c.Title}' ({c.Url}) is not {row.Key}'s own available end evidence at {where}"));
        }

        // No text names a later quest, an entity not yet introduced, or a source not yet available.
        var later = known.Later.FirstHit(surface.Texts, at);
        Assert.True(later is null, $"'{later?.Needle}' leaked at {where}: {later?.Text}");

        // Pickers and prompts never name a quest past the limit (milestones are named on purpose).
        var locked = Locked(d).FirstHit(Pickers(s).ToList(), ceiling.Order);
        Assert.True(locked is null, $"'{locked?.Needle}' leaked at {where} (pickers): {locked?.Text}");

        if (s.Arc is { PastEnd: false })
        {
            Assert.DoesNotContain(surface.Texts, t => t.StartsWith("As of", StringComparison.Ordinal)); // rule 7
            Assert.DoesNotContain(surface.Texts, t => t.StartsWith("New in", StringComparison.Ordinal));
        }
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

            foreach (var c in d.Checkpoints.Where(c => c.QuestTitle is not null))
            {
                later.Add(c.QuestTitle!, c.Order);
            }

            return cache[contentView] = new KnownFrom(entityFrom, relationshipFrom, sourceFrom, later);
        }
    }

    /// <summary>Quest titles and step labels, each bad in a picker while the limit is below its step.</summary>
    private static TextScanner Locked(AtlasDataset d) => LockedCache.GetValue(d, data =>
    {
        var scanner = new TextScanner();
        foreach (var c in data.Checkpoints)
        {
            foreach (var text in new[] { c.Milestone ? null : c.Label, c.QuestTitle }.OfType<string>())
            {
                scanner.Add(text, c.Order);
            }
        }

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
                        if (at < u && i + needle.Length <= text.Length && string.CompareOrdinal(text, i, needle, 0, needle.Length) == 0)
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

        public List<(AtlasChangeRow Row, bool InChangesEnded)> Rows { get; } = new();

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

        public void Add(AtlasChangeRow row, bool inChangesEnded)
        {
            Rows.Add((row, inChangesEnded));
            Texts.Add(row.Text);
            Texts.AddRange(new[] { row.EndedInLabel }.OfType<string>());
            Add(row.Relationship);
            Add(row.Source);
            Add(row.Target);
            Add(row.Entity);
            if (inChangesEnded)
            {
                // The one allowed place: checked against the relationship's own end evidence, not the ordinary sources.
                Texts.AddRange(row.EndCitations.Where(c => c.Title != EndOnlySource).SelectMany(c => new[] { c.Title, c.Url?.ToString() }).OfType<string>());
            }
            else
            {
                Cite(row.EndCitations);
            }
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
        x.Texts.AddRange(new[] { s.CoverageNote, s.CastHeading, s.ArcNewHeading, s.ChangesLabel }.OfType<string>());
        x.Texts.AddRange(s.LensOptions.Select(o => o.Label));
        x.Texts.AddRange(s.ArcPickerOptions.SelectMany(o => new[] { o.Label, o.Detail, o.Group ?? string.Empty }));
        if (s.Arc is { } arc)
        {
            x.Texts.Add(arc.RecapLabel);
            x.Texts.AddRange(new[] { arc.AsOfLabel }.OfType<string>());
            x.Add(arc.Entry);
            arc.Cast.Entities.ToList().ForEach(x.Add);
            arc.Cast.Relationships.ToList().ForEach(x.Add);
        }

        foreach (var row in s.ArcNewRows.Concat(s.ArcEndedRows))
        {
            x.Add(row, inChangesEnded: false);
        }

        foreach (var group in s.ChangeGroups)
        {
            foreach (var row in group.Rows)
            {
                x.Add(row, inChangesEnded: group.Kind == AtlasChangeKind.Ended);
            }
        }

        s.Snapshot.Entities.ToList().ForEach(x.Add);
        s.Snapshot.Relationships.ToList().ForEach(x.Add);
        s.SearchResultGroups.SelectMany(g => g.Entries).ToList().ForEach(x.Add);

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
                }
            }

            s.ClearSelection();
        }

        // Selecting each change shows its details.
        foreach (var row in s.ChangeGroups.SelectMany(g => g.Rows).ToList())
        {
            if (s.SelectChange(row.Key))
            {
                x.Add(s.SelectedChange!, inChangesEnded: s.SelectedChange!.Kind == AtlasChangeKind.Ended);
            }
        }

        // Refocusing every entry on the snapshot (the arc entry included) shows its one-hop surface.
        var focusBefore = s.FocusId;
        foreach (var entity in refocus ? s.Snapshot.Entities.ToList() : [])
        {
            if (s.FocusOn(entity.Id) && s.Neighborhood is { } neighborhood)
            {
                foreach (var neighbor in neighborhood.Neighbors)
                {
                    x.Texts.Add(neighbor.Label);
                    x.Add(neighbor.Entity);
                    x.Add(neighbor.Relationship);
                }
            }
        }

        if (focusBefore is null)
        {
            s.ShowWholeCast();
        }
        else
        {
            s.FocusOn(focusBefore);
        }

        return x;
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

/// <summary>Round-1 council cases: pick lifetime edges, the window pin, caching and the cast heading.</summary>
public class V2SessionEdgeTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasSession At(string ceiling, string view, string? home = AtlasDefaults.HomeEntityId) =>
        new(D, new AtlasSpoilerState(ceiling, view), AtlasContentView.MainAndOptional, home);

    [Fact]
    public void Pick_StaysOnScreenPastItsEndUnderTheDefaultLens()
    {
        var s = At("m2", "s2");
        Assert.False(s.LensIsExplicit);
        Assert.True(s.PickArc("arc-hold"));
        Assert.True(s.LensIsExplicit); // picking an arc is choosing the Arc lens
        s.SetView("s5"); // no arc contains s5, so the default rule alone would have switched to Story point
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.Equal(AtlasText.ArcEnded, s.Arc!.AsOfLabel);
        Assert.Equal("New in Quest Three", s.ArcNewHeading);
    }

    [Fact]
    public void Pick_TheArcLensStaysChosenAfterThePickEnds()
    {
        // D12: picking an arc chose the Arc lens; that choice outlives the pick (dropped, or cleared by the automatic option).
        var dropped = At("m2", "s3");
        dropped.PickArc("arc-shadow");
        dropped.SetView("s0");
        Assert.Equal(AtlasLens.Arc, dropped.Lens);
        Assert.Null(dropped.Arc);

        var cleared = At("m2", "s2");
        cleared.PickArc("arc-hold");
        cleared.PickArc(null);
        cleared.SetView("s5");
        Assert.Equal(AtlasLens.Arc, cleared.Lens);
        Assert.Null(cleared.Arc);
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
    public void LensAndPickChangesDismissAPendingRaise()
    {
        var s = At("s2", "s2");
        Assert.Equal(AtlasStateChange.NeedsConfirmation, s.RequestCeiling("s3"));
        s.SetLens(AtlasLens.Changes);
        Assert.Null(s.PendingCeilingId);

        s.RequestCeiling("s3");
        s.PickArc("arc-tie");
        Assert.Null(s.PendingCeilingId);
    }

    [Fact]
    public void ShowWholeCast_DoesNothingOutsideTheArcLens()
    {
        var s = At("m2", "s2", home: "char-bo");
        s.SetLens(AtlasLens.StoryPoint);
        s.ShowWholeCast();
        Assert.Equal("char-bo", s.FocusId);
    }

    [Fact]
    public void ResetHint_InTheArcLensOnlyAfterTheSessionLeftItsResting()
    {
        var s = At("m2", "s2");
        s.SetView("s3");
        Assert.False(s.SelectionWasReset); // the whole cast is the Arc lens's resting view
        s.FocusOn("char-bo");
        s.SetView("s2");
        Assert.True(s.SelectionWasReset);
    }

    [Fact]
    public void WindowPin_StoryPointKeepsV1BehaviourAcrossArcs()
    {
        // AtlasWindow pins Story point until NDL-010; arc data must not change what it sees.
        var s = At("m2", "s0", home: "char-bo");
        s.SetLens(AtlasLens.StoryPoint);
        Assert.Equal("char-bo", s.FocusId);
        Assert.False(s.SelectionWasReset);
        foreach (var view in new[] { "s1", "s2", "s3", "m1", "s5" })
        {
            s.SetView(view);
            Assert.Equal(AtlasLens.StoryPoint, s.Lens);
            Assert.Equal("char-bo", s.FocusId);
            Assert.Equal(AtlasProjector.Project(D, view, AtlasContentView.MainAndOptional).Entities.Count, s.Snapshot.Entities.Count);
            Assert.False(s.SelectionWasReset);
        }

        var atArc = At("m2", "s2", home: "char-bo"); // opens in Arc, then pinned
        atArc.SetLens(AtlasLens.StoryPoint);
        Assert.Equal("char-bo", atArc.FocusId);
        Assert.False(atArc.SelectionWasReset);
    }

    [Fact]
    public void DerivedState_IsCachedUntilSomethingChanges()
    {
        var s = At("m2", "s2");
        s.SetLens(AtlasLens.Changes);
        var groups = s.ChangeGroups;
        Assert.Same(groups, s.ChangeGroups);
        s.SelectChange(groups[0].Rows[0].Key);
        Assert.Same(groups, s.ChangeGroups);
        s.SetView("s3");
        Assert.NotSame(groups, s.ChangeGroups);

        var arc = At("m2", "s3");
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
    public void ArcSurfaces_AreEmptyOutsideTheArcLens()
    {
        var s = At("m2", "s3");
        s.SetLens(AtlasLens.StoryPoint);
        Assert.Empty(s.ArcNewRows);
        Assert.Empty(s.ArcEndedRows);
        Assert.Null(s.ArcNewHeading);
        Assert.Null(s.CastHeading);
    }

    [Fact]
    public void Cast_HeadingCountsMembersAndTheListLeavesOutTheEntry()
    {
        var s = At("m2", "s2"); // arc-hold at s2: ana, bo, cy, foe, dee
        Assert.Equal(AtlasText.CastHeading(5), s.CastHeading);
        Assert.Equal(5, s.SearchResults.Count);
        Assert.DoesNotContain(s.SearchResults, e => e.Id == "evt-hold");
        Assert.True(s.FocusOn("evt-hold")); // the centre node can still be refocused
        s.SetLens(AtlasLens.StoryPoint);
        Assert.Null(s.CastHeading);
    }

    [Fact]
    public void NewRows_LeaveOutParticipation()
    {
        var s = At("m2", "s2");
        Assert.Contains(s.Arc!.New, r => r.Id == "p-dee-hold"); // the core reports the joiner's edge
        Assert.DoesNotContain(s.ArcNewRows, r => r.Relationship!.TypeId == AtlasDataset.ParticipantTypeId);
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
        Assert.Contains(s.ArcNewRows, r => r.Relationship!.Id == "p-ana-tie");
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
        Assert.Equal(AtlasLens.Arc, s.Lens);
        Assert.Equal("The Siege of Saltmere", s.Arc!.Entry.Name);
        Assert.Equal("Story so far, through The Captain's Bargain", s.Arc.RecapLabel);
        Assert.DoesNotContain(s.Snapshot.Entities, e => e.Id == "char-orrin"); // in the story, not in the cast
        Assert.Equal(new[] { "Captain Mira allied with Vessa", "Vessa member of The Drowned Court" }, s.ArcNewRows.Select(r => r.Text));
        Assert.Equal(new[] { "Captain Mira member of The Harbor Watch" }, s.ArcEndedRows.Select(r => r.Text));

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
