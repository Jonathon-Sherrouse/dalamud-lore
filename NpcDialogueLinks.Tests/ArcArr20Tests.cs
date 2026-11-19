using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// NDL-012: the five arcs of A Realm Reborn 2.0 before the Black Wolf's Challenge (MSQ #102–#154), pinned against the
/// worked examples in docs/atlas/ndl-012-discovery.md. "New" and "Ended so far" are checked at every step that moves.
/// </summary>
public class ArcArr20Tests
{
    private const string B1 = "arc-b1-road-to-titan";
    private const string B2 = "arc-b2-fall-of-the-waking-sands";
    private const string B3 = "arc-b3-search-for-the-enterprise";
    private const string B4 = "arc-b4-garudas-barrier";
    private const string B5 = "arc-b5-road-to-castrum-centri";

    private static readonly AtlasDataset D = AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Draft).Dataset!;

    private static AtlasSession At(string view, string? pick = null)
    {
        var session = new AtlasSession(D, new AtlasSpoilerState(D.Checkpoints[^1].Id, view));
        session.SetLens(AtlasLens.Arc);
        Assert.True(session.PickArc(pick));
        return session;
    }

    private static string Step(int msq) => $"cp-msq-{msq}";

    [Fact]
    public void TheDefaultArcFollowsTheStory()
    {
        Assert.Null(At(Step(102)).Arc); // the baseline: no arc has started
        var expected = new Dictionary<string, string>();
        foreach (var n in Enumerable.Range(103, 3)) expected[Step(n)] = B1;
        foreach (var n in Enumerable.Range(106, 5)) expected[Step(n)] = B2; // #110 is shared with B3; the earlier-started arc wins
        foreach (var n in Enumerable.Range(111, 19)) expected[Step(n)] = B3;
        foreach (var n in Enumerable.Range(130, 12)) expected[Step(n)] = B4;
        foreach (var id in new[] { 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154 }.Select(Step).Append("cp-msq-150b")) expected[id] = B5;
        expected["cp-msq-155"] = "arc-a4-black-wolf"; // unchanged: the accepted arc stays the default from #155

        foreach (var (step, arc) in expected)
        {
            Assert.True(At(step).Arc?.ArcId == arc, $"{step}: expected {arc}, got {At(step).Arc?.ArcId}");
        }
    }

    [Fact]
    public void TheSharedStepOffersBothArcs()
    {
        var s = At(Step(110));
        Assert.Contains(s.ArcPickerOptions, o => o.ArcId == B2);
        Assert.Contains(s.ArcPickerOptions, o => o.ArcId == B3);
        Assert.True(s.PickArc(B3));
        Assert.Equal(B3, s.Arc!.ArcId);
        Assert.False(s.Arc.PastEnd);
    }

    public static TheoryData<string, string, string[], string[]> NewAndEnded() => new()
    {
        // arc, step, "New at this point" rows (spokes left out), "Ended so far" in order of ending
        { B1, Step(103), [], [] },
        { B1, Step(105), ["rel-lahabrea-allied-empire"], [] },
        { B2, Step(106), ["rel-iliud-aids-scions", "rel-livia-member-empire", "rel-minfilia-prisoner-livia-arr"], [] },
        { B2, Step(108), [], [] },
        { B2, Step(110), ["rel-alphinaud-member-scions-arr", "rel-marques-revealed-cid"], [] },
        { B3, Step(110), ["rel-garuda-summoned-ixal"], [] },
        { B3, Step(115), ["rel-francel-member-haillenarte"], [] },
        { B3, Step(118), ["rel-haurchefant-aids-francel"], [] },
        { B3, Step(122), ["rel-guillaime-opposes-alphinaud"], [] },
        { B3, Step(127), ["rel-drillemont-aids-alphinaud"], [] },
        { B3, Step(128), [], ["rel-guillaime-opposes-alphinaud"] }, // the impostor is defeated
        { B3, Step(129), [], ["rel-guillaime-opposes-alphinaud"] },
        { B4, Step(130), [], [] },
        { B4, Step(141), ["rel-gaius-member-empire"], [] },
        { B5, Step(142), ["rel-minfilia-held-castrum-centri"], [] },
        { B5, Step(143), [], [] }, // the other captives are held there too, but they are not in the cast
        { B5, Step(147), ["rel-biggs-serves-cid", "rel-wedge-serves-cid"], [] },
        { B5, Step(148), ["rel-glaumunt-aids-scions"], [] },
        { B5, Step(154), [], [] },
    };

    [Theory]
    [MemberData(nameof(NewAndEnded))]
    public void NewAndEndedMatchTheWorkedExamples(string arc, string step, string[] added, string[] ended)
    {
        var s = At(step, arc);
        Assert.Equal(arc, s.Arc!.ArcId);
        Assert.Equal(added, s.ArcNewRows.Select(r => r.Relationship!.Id).Order(StringComparer.Ordinal));
        Assert.Equal(ended, s.ArcEndedRows.Select(r => r.Relationship!.Id));
        Assert.All(s.ArcEndedRows, r => Assert.Empty(r.EndCitations));
    }

    [Fact]
    public void TheImpostorsDefeatCarriesEndEvidenceInChanges()
    {
        var s = At(Step(128));
        s.SetLens(AtlasLens.Changes);
        var ended = s.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Ended).Rows.Single();
        Assert.Equal("rel-guillaime-opposes-alphinaud", ended.Relationship!.Id);
        Assert.Equal("The Heretic among Us — main scenario quest (2.0)", ended.EndCitations.Single().Title);
    }

    [Theory]
    [InlineData(B1, "cp-msq-105", 6)]
    [InlineData(B2, "cp-msq-110", 10)]
    [InlineData(B3, "cp-msq-129", 10)]
    [InlineData(B4, "cp-msq-141", 8)]
    [InlineData(B5, "cp-msq-154", 10)]
    public void EachCastStaysWithinTheCap(string arc, string lastStep, int members)
    {
        Assert.Equal(members, At(lastStep, arc).Arc!.Cast.Entities.Count - 1);
    }

    public static TheoryData<string> ArcSteps()
    {
        var data = new TheoryData<string>();
        foreach (var arc in D.Arcs.Where(a => a.Id != "arc-a4-black-wolf"))
        {
            foreach (var c in D.Checkpoints.Where(c => c.Order >= arc.FirstOrder && c.Order <= arc.LastOrder))
            {
                data.Add($"{arc.Id}|{c.Id}");
            }
        }

        return data;
    }

    [Theory]
    [MemberData(nameof(ArcSteps))]
    public void EveryStepHasItsOwnRecapWithinTheLength(string arcAndStep)
    {
        var (arc, step) = (arcAndStep.Split('|')[0], arcAndStep.Split('|')[1]);
        var recap = At(step, arc).Arc!.Entry.Summary;
        Assert.InRange(recap.Split(' ', StringSplitOptions.RemoveEmptyEntries).Length, 30, 80);
        Assert.InRange(recap.Count(c => c == '.'), 2, 4);
        foreach (var finality in new[] { "at last", "finally", "in the end", "is over", "concludes", "the end of the arc" })
        {
            Assert.DoesNotContain(finality, recap, StringComparison.OrdinalIgnoreCase);
        }

        var previous = D.Checkpoints.Last(c => c.Order < D.Checkpoints.Single(x => x.Id == step).Order);
        if (D.Arcs.Single(a => a.Id == arc).FirstOrder < D.Checkpoints.Single(x => x.Id == step).Order)
        {
            Assert.NotEqual(At(previous.Id, arc).Arc!.Entry.Summary, recap); // a new recap at every step
        }
    }

    [Fact]
    public void MarquesNeverShowsCidsNameOrFaceBeforeTheReveal()
    {
        foreach (var n in Enumerable.Range(106, 4))
        {
            var snapshot = AtlasProjector.Project(D, Step(n), AtlasContentView.MainAndOptional);
            var marques = snapshot.FindEntity("char-marques")!;
            Assert.Null(marques.Portrait);
            Assert.Null(snapshot.FindEntity("char-cid"));
            Assert.DoesNotContain("Cid", marques.Summary, StringComparison.Ordinal);
        }

        var reveal = AtlasProjector.Project(D, Step(110), AtlasContentView.MainStory);
        Assert.Contains("Marques", reveal.FindEntity("char-cid")!.Aliases);
        Assert.Contains(reveal.Relationships, r => r.Id == "rel-marques-revealed-cid");
    }

    [Fact]
    public void TheImpostorIsRenamedOnlyOnceUnmasked()
    {
        Assert.Equal("Guillaime", AtlasProjector.Project(D, Step(125), AtlasContentView.MainStory).FindEntity("char-guillaime")!.Name);
        Assert.Equal("The false Guillaime", AtlasProjector.Project(D, Step(126), AtlasContentView.MainStory).FindEntity("char-guillaime")!.Name);
    }
}
