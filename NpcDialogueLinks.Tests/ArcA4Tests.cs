using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// NDL-009: arc A4, The Black Wolf's Challenge (MSQ #155–161), pinned against the worked examples in
/// docs/atlas/v2-discovery.md. "New" and "Ended so far" are checked at every slice step and at the milestone.
/// </summary>
public class ArcA4Tests
{
    private const string Arc = "arc-a4-black-wolf";
    private const string Milestone = "cp-arr-2-0";

    private static readonly AtlasDataset D = AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Draft).Dataset!;

    private static AtlasSession At(string view)
    {
        var session = new AtlasSession(D, new AtlasSpoilerState("cp-arr-2-55", view));
        session.SetLens(AtlasLens.Arc);
        return session;
    }

    public static TheoryData<string, string[], string[]> NewAndEnded() => new()
    {
        // step, "New at this point" rows (spokes left out, D8), "Ended so far" in order of ending
        { "cp-msq-155", ["rel-thancred-possessed-lahabrea"], ["rel-minfilia-prisoner-livia"] },                       // WE-2: captives freed
        { "cp-msq-156", [], ["rel-minfilia-prisoner-livia"] },
        { "cp-msq-157", ["rel-alliance-in-archon", "rel-cid-in-archon", "rel-livia-serves-gaius", "rel-scions-in-archon"], ["rel-minfilia-prisoner-livia"] }, // WE-3
        { "cp-msq-158", [], ["rel-minfilia-prisoner-livia"] },
        { "cp-msq-159", [], ["rel-minfilia-prisoner-livia"] },
        { "cp-msq-160", [], ["rel-minfilia-prisoner-livia", "rel-livia-serves-gaius"] },
        { Milestone, [], ["rel-minfilia-prisoner-livia", "rel-livia-serves-gaius", "rel-thancred-possessed-lahabrea"] }, // WE-1, at the milestone
    };

    [Theory]
    [MemberData(nameof(NewAndEnded))]
    public void A4_NewAndEndedMatchTheWorkedExamples(string step, string[] added, string[] ended)
    {
        var s = At(step);
        Assert.Equal(Arc, s.Arc!.ArcId);
        Assert.Equal(added, s.ArcNewRows.Select(r => r.Relationship!.Id).Order(StringComparer.Ordinal));
        Assert.Equal(ended, s.ArcEndedRows.Select(r => r.Relationship!.Id));
        Assert.All(s.ArcEndedRows, r => Assert.Empty(r.EndCitations));
    }

    [Fact]
    public void A4_IsNotOpenBeforeItsFirstStep()
    {
        // NDL-012: #154 is the last step of the rescue arc that precedes A4, so an arc is open, but never A4 or its name.
        var s = At("cp-msq-154");
        Assert.Equal("arc-b5-road-to-castrum-centri", s.Arc!.ArcId);
        Assert.DoesNotContain(s.ArcPickerOptions, o => o.ArcId == Arc);
        Assert.DoesNotContain(s.ArcPickerOptions, o => o.Label.Contains("Black Wolf", StringComparison.Ordinal));
    }

    [Fact]
    public void A4_TheCastGrowsToTenWithOperationArchonMidArc()
    {
        Assert.Equal(9, At("cp-msq-155").Arc!.Cast.Entities.Count - 1);
        var later = At("cp-msq-157").Arc!;
        Assert.Equal(10, later.Cast.Entities.Count - 1);
        Assert.Contains(later.Cast.Entities, e => e.Id == "evt-operation-archon");
        Assert.DoesNotContain(later.Cast.Entities, e => e.Id is "char-yshtola" or "char-urianger"); // in the story, not in the cast
    }

    [Fact]
    public void A4_TheLastStepLooksLikeMidArcAndHasARecap()
    {
        var atLast = At(Milestone);
        Assert.False(atLast.Arc!.PastEnd);
        Assert.Null(atLast.Arc.AsOfLabel);
        Assert.Equal("Story so far, as of A Realm Reborn — Patch 2.0 complete", atLast.Arc.RecapLabel);

        var after = At("cp-arr-2-55");
        Assert.Equal("arc-d5-royal-banquet", after.Arc!.ArcId); // the automatic choice: 2.55's own arc (2026-11-19)
        Assert.True(after.PickArc(Arc));
        Assert.True(after.Arc!.PastEnd);
    }

    [Theory]
    [InlineData("cp-msq-155")]
    [InlineData("cp-msq-156")]
    [InlineData("cp-msq-157")]
    [InlineData("cp-msq-158")]
    [InlineData("cp-msq-159")]
    [InlineData("cp-msq-160")]
    [InlineData(Milestone)]
    public void A4_EveryStepHasItsOwnReviewedRecapWithinTheLength(string step)
    {
        var recap = At(step).Arc!.Entry.Summary;
        var words = recap.Split(' ', StringSplitOptions.RemoveEmptyEntries).Length;
        Assert.InRange(words, 30, 80);
        var sentences = recap.Count(c => c == '.');
        Assert.InRange(sentences, 2, 4);
        foreach (var finality in new[] { "at last", "finally", "in the end", "is over", "concludes", "the end of the arc" })
        {
            Assert.DoesNotContain(finality, recap, StringComparison.OrdinalIgnoreCase);
        }
    }

    [Fact]
    public void A4_RecapsChangeAtEveryStep()
    {
        var recaps = new[] { "cp-msq-155", "cp-msq-156", "cp-msq-157", "cp-msq-158", "cp-msq-159", "cp-msq-160", Milestone }
            .Select(step => At(step).Arc!.Entry.Summary).ToList();
        Assert.Equal(recaps.Count, recaps.Distinct().Count());
    }

    [Fact]
    public void A4_EndEvidenceShowsOnlyInTheChangesRowsWhereItCanShow()
    {
        // The rescue (#154 → #155) and Livia's fall (#159 → #160) end between slice steps, so Changes shows their evidence.
        var rescue = At("cp-msq-155");
        rescue.SetLens(AtlasLens.Changes);
        Assert.Equal(AtlasText.ChangesThisQuest, rescue.ChangesLabel);
        // NDL-012 adds the four "held at Castrum Centri" edges, which end with the same rescue and the same evidence.
        var endedAtRescue = rescue.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Ended).Rows;
        Assert.Equal(5, endedAtRescue.Count);
        Assert.All(endedAtRescue, r => Assert.Equal("Escape from Castrum Centri — main scenario quest (2.0)", r.EndCitations.Single().Title));
        var freed = endedAtRescue.Single(r => r.Relationship!.Id == "rel-minfilia-prisoner-livia");
        Assert.Equal("rel-minfilia-prisoner-livia", freed.Relationship!.Id);
        Assert.Equal("Escape from Castrum Centri — main scenario quest (2.0)", freed.EndCitations.Single().Title);

        var fall = At("cp-msq-160");
        fall.SetLens(AtlasLens.Changes);
        // NDL-012: Livia's fall also ends her membership of the Empire, with the same evidence.
        var fallen = fall.ChangeGroups.Single(g => g.Kind == AtlasChangeKind.Ended).Rows;
        Assert.Equal(new[] { "rel-livia-member-empire", "rel-livia-serves-gaius" }, fallen.Select(r => r.Relationship!.Id).Order(StringComparer.Ordinal));
        Assert.All(fallen, r => Assert.Equal("Rock the Castrum — main scenario quest (2.0)", r.EndCitations.Single().Title));

        // The possession ends across the slice → milestone boundary, where Changes is never offered (WE-1).
        var finale = At(Milestone);
        finale.SetLens(AtlasLens.Changes);
        Assert.False(finale.ChangesOffered);
    }

    [Fact]
    public void A4_TheBaselineHoldsTheCaptivityTheRescueEnds()
    {
        var baseline = AtlasProjector.Project(D, "cp-msq-154", AtlasContentView.MainStory);
        Assert.Contains(baseline.Relationships, r => r.Id == "rel-minfilia-prisoner-livia");
        Assert.DoesNotContain(baseline.Entities, e => e.Id == "evt-black-wolfs-challenge"); // the arc's name never shows before #155
    }

    [Fact]
    public void Picker_PlacesTheArcInTheStory()
    {
        var s = new AtlasSession(D, new AtlasSpoilerState("cp-arr-2-0", "cp-msq-160"));
        var arc = s.ArcPickerOptions.Single(o => o.ArcId == "arc-a4-black-wolf");
        Assert.Equal("from Escape from Castrum Centri", arc.Detail);
        Assert.Equal("A Realm Reborn — Patch 2.0", arc.Group);
        Assert.False(s.ArcPickerGrouped);
    }
}
