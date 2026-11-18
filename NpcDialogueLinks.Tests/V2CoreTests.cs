using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>Schema-v2 validation rules (docs/atlas/v2-plan.md, "Timeline and data model").</summary>
public class V2ValidationTests
{
    [Fact]
    public void V2_FixtureLoadsStrict()
    {
        var dataset = V2Fx.Load();
        Assert.Equal(8, dataset.Checkpoints.Count);
        Assert.Equal(3, dataset.Arcs.Count);
        Assert.True(dataset.Checkpoints[4].Milestone);
        Assert.Equal("Quest One", dataset.Checkpoints[1].QuestTitle);
        Assert.True(dataset.Checkpoints[1].ContiguousWithPrevious);
        Assert.Equal(new[] { 101 }, dataset.Checkpoints[1].GameQuestIds);
    }

    [Fact]
    public void V2_FirstCheckpointCannotBeContiguous()
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s0")["contiguousWithPrevious"] = true;
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
    }

    [Theory]
    [InlineData("[0]")]
    [InlineData("[-5]")]
    [InlineData("[100, 100]")]
    public void V2_GameQuestIdsMustBePositiveAndUnique(string ids)
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s0")["gameQuestIds"] = JsonNode.Parse(ids);
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
    }

    [Fact]
    public void V2_EndCitationsNeedAnEndingRelationship()
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-dee-ana")["endCitations"] = new JsonArray(V2Fx.Cite("Src s2", "s2"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.EndCitationOutOfRange);
    }

    [Theory]
    [InlineData("End too early", "s0")] // at validFrom: the ending is not yet knowable
    [InlineData("End too late", "s3")]  // after validUntil
    public void V2_EndCitationsMustFallInsideTheInterval(string title, string availableAt)
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-ana-prisoner")["endCitations"] = new JsonArray(V2Fx.Cite(title, availableAt));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.EndCitationOutOfRange);
    }

    [Fact]
    public void V2_MainRelationshipCannotCiteOptionalEndEvidence()
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-ana-prisoner")["endCitations"] = new JsonArray(V2Fx.Cite("Optional end src", "s2", "optional"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.CitationScopeMismatch);
    }

    [Fact]
    public void V2_EndCitationsShareTheTitleRegistry()
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-ana-prisoner")["endCitations"] = new JsonArray(V2Fx.Cite("Src s1", "s2")); // "Src s1" is s1 elsewhere
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InconsistentCitation);
    }

    [Fact]
    public void V2_ArcsNeedTheParticipantType()
    {
        var doc = V2Fx.Doc();
        Fx.Entities(doc); // no-op; keeps helpers in use
        foreach (var type in doc["relationshipTypes"]!.AsArray().Select(t => t!.AsObject()).Where(t => (string?)t["id"] == "participant-in"))
        {
            type["id"] = "joins";
        }

        foreach (var rel in Fx.Relationships(doc).Select(r => r!.AsObject()).Where(r => (string?)r["type"] == "participant-in"))
        {
            rel["type"] = "joins";
        }

        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcEntryMustBeAnEvent()
    {
        var doc = V2Fx.Doc();
        Fx.Entity(doc, "evt-tie")["category"] = "character";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcCannotStartOnTheFirstStep()
    {
        var doc = V2Fx.Doc();
        V2Fx.Arc(doc, "arc-tie")["firstStep"] = "s0";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcEntryMustFirstAppearExactlyAtFirstStep()
    {
        var doc = V2Fx.Doc();
        V2Fx.Arc(doc, "arc-tie")["firstStep"] = "s3";
        V2Fx.Arc(doc, "arc-tie")["lastStep"] = "s3";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcEntryMustStayVisibleThroughLastStep()
    {
        var doc = V2Fx.Doc();
        Fx.Presentation(doc, "evt-tie", 0)["validUntil"] = "s3";
        V2Fx.Arc(doc, "arc-tie")["lastStep"] = "m1";
        Fx.Relationships(doc).Remove(V2Fx.Rel(doc, "p-ana-tie")); // keep endpoints valid so the arc rule is what fails
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_MembershipNeverEnds()
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "p-ana-tie")["validUntil"] = "m1";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_MembershipIsMainScope()
    {
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "p-ana-tie")["scope"] = "optional";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcStepsMustBeOrdered()
    {
        var doc = V2Fx.Doc();
        V2Fx.Arc(doc, "arc-shadow")["lastStep"] = "s1";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_EachArcHasItsOwnEntry()
    {
        var doc = V2Fx.Doc();
        V2Fx.Arc(doc, "arc-tie")["entityId"] = "evt-shadow";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidArc);
    }

    [Fact]
    public void V2_ArcStepsMustExist()
    {
        var doc = V2Fx.Doc();
        V2Fx.Arc(doc, "arc-tie")["lastStep"] = "s99";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.UnknownReference);
    }

    [Fact]
    public void V2_CastCapIsTenParticipants()
    {
        Assert.True(Fx.Try(V2Fx.WithCast(10)).Success);
        Fx.AssertFails(Fx.Try(V2Fx.WithCast(11)), AtlasErrorCode.CastTooLarge);
    }
}

/// <summary>The Changes lens: semantic diff, offering rule and labels.</summary>
/// <summary>Round-1 council fixes to validation.</summary>
public class V2ValidationFixTests
{
    [Fact]
    public void V2_GameQuestIdsAreAllOrNone()
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s3").Remove("gameQuestIds");
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.InvalidField);
        Assert.Contains(result.Errors, e => e.Path == "$.checkpoints[3].gameQuestIds");
    }

    [Fact]
    public void V2_GameQuestIdNeverMarksTwoSteps()
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s2")["gameQuestIds"] = new JsonArray(101);
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.InvalidField);
        Assert.Contains(result.Errors, e => e.Path == "$.checkpoints[2].gameQuestIds" && e.Message.Contains("101"));
    }

    [Fact]
    public void V2_NoQuestIdsAnywhereIsFine()
    {
        var doc = V2Fx.Doc();
        foreach (var checkpoint in doc["checkpoints"]!.AsArray())
        {
            checkpoint!.AsObject().Remove("gameQuestIds");
        }

        Assert.True(Fx.Try(doc).Success);
    }

    [Fact]
    public void V2_EndCitationsCannotEndAcrossASliceMilestoneBoundary()
    {
        // r-dee-bo-2 ends at m1 (slice s3 → milestone m1), where Changes is never offered, so the evidence could never show.
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-dee-bo-2")["endCitations"] = new JsonArray(V2Fx.Cite("Src m1", "m1"));
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.EndCitationOutOfRange);
        Assert.All(result.Errors, e => Assert.Equal(AtlasErrorCode.EndCitationOutOfRange, e.Code));
    }

    [Fact]
    public void V2_ParticipantTypeCannotBeSymmetric()
    {
        var doc = V2Fx.Doc();
        var type = doc["relationshipTypes"]!.AsArray().Select(t => t!.AsObject()).First(t => (string?)t["id"] == "participant-in");
        type["symmetric"] = true;
        type["incomingLabel"] = "part of";
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.InvalidArc);
        Assert.Contains(result.Errors, e => e.Path == "$.relationshipTypes");
    }

    [Fact]
    public void V2_EndCitationsNeedARealEnding()
    {
        // r-cy-foe-a ends at s2 only to split citations: r-cy-foe-b carries the same triple on, so no ended row ever shows.
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-cy-foe-a")["endCitations"] = new JsonArray(V2Fx.Cite("Src s2", "s2"));
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.EndCitationOutOfRange);
        Assert.Contains(result.Errors, e => e.Path.EndsWith(".endCitations") && e.Message.Contains("continues"));
    }

    [Fact]
    public void V2_MainEndingContinuedOnlyByOptionalContentKeepsItsEvidence()
    {
        // The main-story view still shows the ending, so the evidence is displayable there.
        var doc = V2Fx.Doc();
        V2Fx.Rel(doc, "r-cy-foe-a")["endCitations"] = new JsonArray(V2Fx.Cite("Src s2", "s2"));
        V2Fx.Rel(doc, "r-cy-foe-b")["scope"] = "optional";
        V2Fx.Rel(doc, "r-cy-foe-b")["citations"] = new JsonArray(V2Fx.Cite("Opt s2", "s2", "optional"));
        Assert.True(Fx.Try(doc).Success, string.Join("; ", Fx.Try(doc).Errors.Select(e => $"{e.Code} {e.Path} {e.Message}")));
    }

    [Fact]
    public void V2_CoverageErrorsPointAtTheAuthoredCheckpoint()
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s1")["label"] = "";
        V2Fx.Checkpoint(doc, "s2").Remove("gameQuestIds");
        Assert.Contains(Fx.Try(doc).Errors, e => e.Path == "$.checkpoints[2].gameQuestIds");
    }

    [Fact]
    public void V2_ArcEntryPresentationsAreAllMainScope()
    {
        var doc = V2Fx.Doc();
        var entry = Fx.Entities(doc).Select(e => e!.AsObject()).First(e => (string?)e["id"] == "evt-shadow");
        entry["presentations"]!.AsArray().Add(new JsonObject
        {
            ["validFrom"] = "s2", ["scope"] = "optional", ["name"] = "The Shadow", ["summary"] = "Side detail.",
            ["citations"] = new JsonArray(V2Fx.Cite("Opt s2", "s2", "optional")), ["review"] = "reviewed",
        });
        var result = Fx.Try(doc);
        Fx.AssertFails(result, AtlasErrorCode.InvalidArc);
        Assert.All(result.Errors, e => Assert.Equal(AtlasErrorCode.InvalidArc, e.Code));
    }
}

public class V2ChangesTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    [Theory]
    [InlineData("s0", false)] // first step
    [InlineData("s1", true)]
    [InlineData("s2", true)]
    [InlineData("m1", false)] // slice → milestone boundary
    [InlineData("s5", false)] // milestone → slice
    [InlineData("s6", true)]  // slice → slice across a gap
    [InlineData("m2", false)] // slice → milestone
    public void Changes_OfferedOnlyBetweenStepsOfTheSameKind(string checkpoint, bool offered)
    {
        Assert.Equal(offered, AtlasChanges.IsOffered(D, checkpoint));
        Assert.Equal(offered, AtlasChanges.At(D, checkpoint, AtlasContentView.MainAndOptional) is not null);
    }

    [Fact]
    public void Changes_LabelsContiguousStepsAsThisQuest()
    {
        Assert.Equal(AtlasText.ChangesThisQuest, AtlasChanges.Label(D, "s2"));
        Assert.Null(AtlasChanges.Label(D, "m1"));
    }

    [Fact]
    public void Changes_SlicesAcrossAGapSayChangesSince()
    {
        Assert.Equal(AtlasText.ChangesSince("Quest Nine"), AtlasChanges.Label(D, "s6"));
    }

    [Fact]
    public void Changes_MilestonesAcrossAGapSayChangesSince()
    {
        var sample = Fx.SampleDataset();
        Assert.True(AtlasChanges.IsOffered(sample, Fx.Later));
        Assert.Equal(AtlasText.ChangesSince(sample.Checkpoints[0].Label), AtlasChanges.Label(sample, Fx.Later));
    }

    [Fact]
    public void Changes_DiffsByTripleSoCitationSplitsAreNotChanges()
    {
        var diff = AtlasChanges.At(D, "s2", AtlasContentView.MainAndOptional)!;
        Assert.Equal(new[] { "r-ana-prisoner", "r-cy-bo-1", "r-dee-bo-1" }, V2Fx.Ids(diff.Ended).Order(StringComparer.Ordinal));
        Assert.DoesNotContain(diff.Ended, e => e.Relationship.Id.StartsWith("r-cy-foe"));
        Assert.DoesNotContain(diff.Added, r => r.Id.StartsWith("r-cy-foe"));
        Assert.Contains(diff.DescriptionUpdated, e => e.Id == "char-ana");
    }

    [Fact]
    public void Changes_EndEvidenceAppearsOnlyOnTheEndedRow()
    {
        var diff = AtlasChanges.At(D, "s2", AtlasContentView.MainAndOptional)!;
        var ended = diff.Ended.Single(e => e.Relationship.Id == "r-ana-prisoner");
        Assert.Equal("Src s2", ended.EndCitations.Single().Title);
        Assert.Equal("Ana is held.", ended.Source.Summary); // endpoints as they were before the ending

        // The record itself never carries its end evidence into a normal snapshot.
        var before = AtlasProjector.Project(D, "s1", AtlasContentView.MainAndOptional);
        Assert.DoesNotContain(before.Relationships.Single(r => r.Id == "r-ana-prisoner").Citations, c => c.Title == "Src s2");
    }
}

/// <summary>The Arc lens: cumulative cast, New, Ended so far, selection and rule 7.</summary>
public class V2ArcTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static AtlasArcView Arc(string arc, string view) => AtlasArcs.Project(D, arc, view, AtlasContentView.MainAndOptional)!;

    [Fact]
    public void Arc_IsNullBeforeItStarts()
    {
        Assert.Null(AtlasArcs.Project(D, "arc-hold", "s0", AtlasContentView.MainAndOptional));
        Assert.Null(AtlasArcs.Project(D, "arc-shadow", "s1", AtlasContentView.MainAndOptional));
    }

    [Fact]
    public void Arc_CastGrowsAndNeverShowsFutureMembers()
    {
        Assert.Equal(new[] { "char-ana", "char-bo", "char-cy", "org-foe", "evt-hold" }, Arc("arc-hold", "s1").Cast.Entities.Select(e => e.Id));
        Assert.Empty(Arc("arc-hold", "s1").Cast.Search("Dee")); // dee joins at s2
        Assert.Contains(Arc("arc-hold", "s2").Cast.Entities, e => e.Id == "char-dee");
        Assert.DoesNotContain(Arc("arc-hold", "s3").Cast.Entities, e => e.Id == "char-zed"); // never a participant
        Assert.DoesNotContain(Arc("arc-hold", "s3").Cast.Relationships, r => r.Id == "r-zed-ana");
    }

    [Fact]
    public void Arc_MidArcJoinersExistingTiesAreNotNew()
    {
        var atS2 = Arc("arc-hold", "s2");
        Assert.Contains(atS2.New, r => r.Id == "p-dee-hold");
        Assert.DoesNotContain(atS2.New, r => r.Id == "r-dee-ana");
    }

    [Fact]
    public void Arc_NewComparesWithTheStepBefore()
    {
        Assert.Equal(new[] { "r-cy-bo-2", "r-dee-bo-2" }, V2Fx.Ids(Arc("arc-hold", "s3").New));
    }

    [Fact]
    public void Arc_EndedSoFarCatchesStartAndEndInsideTheArc()
    {
        var ended = Arc("arc-hold", "s3").EndedSoFar;
        Assert.Equal(new[] { "r-ana-prisoner", "r-bo-possessed" }, V2Fx.Ids(ended));
        Assert.Equal("s2", ended[0].EndedAtCheckpointId);
        Assert.Equal("s3", ended[1].EndedAtCheckpointId);
        Assert.NotEmpty(AtlasChanges.At(D, "s2", AtlasContentView.MainAndOptional)!.Ended.Single(e => e.Relationship.Id == "r-ana-prisoner").EndCitations);
        Assert.All(ended, e =>
        {
            // Arc-lens ended rows show no sources: no end evidence, and no citations on the row or its endpoints.
            Assert.Empty(e.EndCitations);
            Assert.Empty(e.Relationship.Citations);
            Assert.Empty(e.Source.Citations);
            Assert.Empty(e.Target.Citations);
        });
    }

    [Fact]
    public void Arc_EndedThenRestartedIsNotListed()
    {
        Assert.DoesNotContain(Arc("arc-hold", "s3").EndedSoFar, e => e.Relationship.SourceId == "char-cy" && e.Relationship.TargetId == "char-bo");
        Assert.Contains(Arc("arc-hold", "s2").EndedSoFar, e => e.Relationship.Id == "r-cy-bo-1"); // before it restarts
    }

    [Fact]
    public void Arc_EndedTwiceUsesTheLatestEnding()
    {
        var ended = Arc("arc-shadow", "m1").EndedSoFar.Single(e => e.Relationship.SourceId == "char-dee" && e.Relationship.TargetId == "char-bo");
        Assert.Equal("m1", ended.EndedAtCheckpointId);
        Assert.Equal("r-dee-bo-2", ended.Relationship.Id);
    }

    [Fact]
    public void Arc_EndingAtAMilestoneIgnoresTheWiderCast()
    {
        var atMilestone = Arc("arc-shadow", "m1");
        Assert.Empty(atMilestone.New); // newbie appears at m1 but is not in the cast
        Assert.DoesNotContain(atMilestone.Cast.Entities, e => e.Id == "char-newbie");
        Assert.False(AtlasChanges.IsOffered(D, "m1")); // and Changes never compares across the boundary
    }

    [Fact]
    public void Arc_LastStepLooksExactlyLikeMidArc()
    {
        var atLast = Arc("arc-hold", "s3");
        var pastEnd = Arc("arc-hold", "m1");
        Assert.False(atLast.PastEnd);
        Assert.Null(atLast.AsOfLabel);
        Assert.True(pastEnd.PastEnd);
        Assert.Equal(AtlasText.ArcEnded, pastEnd.AsOfLabel);
        Assert.Equal(SnapshotDigest.Of(atLast.Cast), SnapshotDigest.Of(pastEnd.Cast));
        Assert.Equal(V2Fx.Ids(atLast.New), V2Fx.Ids(pastEnd.New));
        Assert.Equal(V2Fx.Ids(atLast.EndedSoFar), V2Fx.Ids(pastEnd.EndedSoFar));
        Assert.Equal(atLast.RecapLabel, pastEnd.RecapLabel);
    }

    [Fact]
    public void Arc_RecapIsTheEntrySummaryAtTheEffectiveStep()
    {
        Assert.Equal("Recap one.", Arc("arc-hold", "s2").Entry.Summary);
        Assert.Equal("Story so far, through Quest Two", Arc("arc-hold", "s2").RecapLabel);
        Assert.Equal("Recap two.", Arc("arc-hold", "s5").Entry.Summary); // past the end: as of s3
    }

    [Theory]
    [InlineData("s0", null)]
    [InlineData("s1", "arc-hold")]
    [InlineData("s2", "arc-hold")] // three arcs contain s2; the earliest-started wins
    [InlineData("m1", "arc-shadow")]
    [InlineData("s5", null)]
    public void Arc_DefaultIsTheEarliestStartedContainingArc(string view, string? expected)
    {
        Assert.Equal(expected, AtlasArcs.Default(D, view));
    }

    [Fact]
    public void Arc_TiesBreakByAuthoredOrderNeverBySpan()
    {
        var doc = V2Fx.Doc();
        doc["arcs"]!.AsArray().Remove(V2Fx.Arc(doc, "arc-hold"));
        var withoutHold = Fx.Load(doc);
        Assert.Equal("arc-shadow", AtlasArcs.Default(withoutHold, "s2")); // shadow (longer) and tie (shorter) start together

        // Reverse the authored order: now the tie wins, proving span plays no part.
        var arcs = doc["arcs"]!.AsArray();
        var shadow = V2Fx.Arc(doc, "arc-shadow");
        arcs.Remove(shadow);
        arcs.Add(shadow);
        Assert.Equal("arc-tie", AtlasArcs.Default(Fx.Load(doc), "s2"));
    }

    [Fact]
    public void Arc_PickerListsStartedArcsInOrderWithoutSpans()
    {
        Assert.Equal(new[] { "arc-hold", "arc-shadow", "arc-tie" }, AtlasArcs.Eligible(D, "s2", AtlasContentView.MainAndOptional).Select(o => o.ArcId));
        Assert.Equal(new[] { "arc-hold" }, AtlasArcs.Eligible(D, "s1", AtlasContentView.MainAndOptional).Select(o => o.ArcId));
        Assert.Equal("The Hold", AtlasArcs.Eligible(D, "m2", AtlasContentView.MainAndOptional)[0].Name);
    }

    [Fact]
    public void Arc_ExplicitPickHoldsUntilViewDropsBelowItsStart()
    {
        Assert.Equal(new AtlasArcResolution("arc-shadow", false), AtlasArcs.Resolve(D, "s3", "arc-shadow")); // default would be arc-hold
        Assert.Equal(new AtlasArcResolution("arc-hold", false), AtlasArcs.Resolve(D, "s5", "arc-hold"));     // ended arc stays viewable
        Assert.Equal(new AtlasArcResolution("arc-hold", true), AtlasArcs.Resolve(D, "s1", "arc-shadow"));    // view below its start: back to default
        Assert.Equal(new AtlasArcResolution(null, true), AtlasArcs.Resolve(D, "s0", "arc-hold"));
        Assert.Equal(new AtlasArcResolution("arc-hold", false), AtlasArcs.Resolve(D, "s2", null));
    }

    [Fact]
    public void Arc_DroppedPickContractForTheSession()
    {
        // Documents the session contract only: PickDropped tells the session to clear the pick, after which rising to s3
        // shows the default. The session itself (and a real lifetime test) is NDL-008.
        var pick = (string?)"arc-shadow";
        var atS1 = AtlasArcs.Resolve(D, "s1", pick);
        Assert.True(atS1.PickDropped);
        if (atS1.PickDropped)
        {
            pick = null;
        }

        Assert.Equal("arc-hold", AtlasArcs.Resolve(D, "s3", pick).ArcId);
    }

    [Fact]
    public void Arc_UnknownPickFallsBackAndIsDropped()
    {
        Assert.Equal(new AtlasArcResolution("arc-hold", true), AtlasArcs.Resolve(D, "s2", "arc-nope"));
    }

    [Fact]
    public void Arc_NothingOutsideTheCastReachesAnySurface()
    {
        var view = Arc("arc-shadow", "m1");
        var castIds = view.Cast.Entities.Select(e => e.Id).ToHashSet();
        Assert.All(view.Cast.Relationships, r => Assert.True(castIds.Contains(r.SourceId) && castIds.Contains(r.TargetId)));
        Assert.All(view.EndedSoFar, e => Assert.True(castIds.Contains(e.Source.Id) && castIds.Contains(e.Target.Id)));
        Assert.Empty(view.Cast.Search("Newbie"));
    }
}

/// <summary>Follow positioning from completed-quest flags (docs/atlas/v2-plan.md, "Follow").</summary>
public class V2FollowTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    private static Func<int, AtlasQuestProgress> Progress(int completeThrough, int? unknown = null) =>
        id => id == unknown ? AtlasQuestProgress.Unknown : id <= completeThrough ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete;

    [Fact]
    public void Follow_LandsOnTheLastStepOfTheCompletedPrefix()
    {
        Assert.Equal(new AtlasFollowResult(AtlasFollowKind.Position, "s2", false, "s2"), AtlasFollow.Position(D, Progress(102), "m2"));
        Assert.Equal("m2", AtlasFollow.Position(D, Progress(999), "m2").CheckpointId);
    }

    [Fact]
    public void Follow_ClampsToTheLimitAndSaysSo()
    {
        Assert.Equal(new AtlasFollowResult(AtlasFollowKind.Position, "s1", true, "s2"), AtlasFollow.Position(D, Progress(102), "s1"));
    }

    [Fact]
    public void Follow_PrefixStopsAtTheFirstIncompleteStep()
    {
        // 100 and 101 done, 102 not, 103 done (out-of-order completion): the prefix ends at s1, never jumps to s3.
        AtlasQuestProgress Gap(int id) => id is 100 or 101 or 103 ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete;
        Assert.Equal(new AtlasFollowResult(AtlasFollowKind.Position, "s1", false, "s1"), AtlasFollow.Position(D, Gap, "m2"));
    }

    [Fact]
    public void Follow_AStepNeedsAllItsQuests()
    {
        var doc = V2Fx.Doc();
        V2Fx.Checkpoint(doc, "s2")["gameQuestIds"] = new JsonArray(102, 150);
        var dataset = Fx.Load(doc);
        AtlasQuestProgress Partial(int id) => id is 150 || id > 103 ? AtlasQuestProgress.Incomplete : AtlasQuestProgress.Complete;
        Assert.Equal("s1", AtlasFollow.Position(dataset, Partial, "m2").CheckpointId);
    }

    [Fact]
    public void Follow_RaiseGoesExactlyToTheReachedStepAndNeedsConfirmation()
    {
        var state = AtlasSpoilerPolicy.Restore(D, "s1", "s0");
        var follow = AtlasFollow.Position(D, Progress(103), state.CeilingId); // reached s3, limit s1
        Assert.Equal(("s1", "s3"), (follow.CheckpointId, follow.ReachedCheckpointId));

        var ask = AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(103), confirmed: false);
        Assert.Equal(AtlasStateChange.NeedsConfirmation, ask.Change);
        Assert.Equal(state, ask.State);

        var done = AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(103), confirmed: true);
        Assert.Equal(AtlasStateChange.Changed, done.Change);
        Assert.Equal(new AtlasSpoilerState("s3", "s0"), done.State); // the view is left alone
    }

    [Fact]
    public void Follow_RaiseIsRejectedUnlessProgressIsBeyondTheLimit()
    {
        var state = AtlasSpoilerPolicy.Restore(D, "m1", "s0");
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(102), confirmed: true).Change);    // below the limit
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(104), confirmed: true).Change);    // exactly at it
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(99, 103), confirmed: true).Change); // unknown
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetCeilingToFollowed(D, state, Progress(99), confirmed: true).Change);     // before coverage
    }

    [Fact]
    public void Follow_RaiseCannotApplyAStaleResult()
    {
        // Follow ran with the limit at s1 (reached s3); the user then raised the limit to m1 by hand. Progress is re-read
        // against the current limit, so the old "beyond the limit" can never lower it back to s3.
        var stale = AtlasFollow.Position(D, Progress(103), "s1");
        Assert.True(stale.BeyondLimit);
        var raised = AtlasSpoilerPolicy.Restore(D, "m1", "s0");
        var result = AtlasSpoilerPolicy.SetCeilingToFollowed(D, raised, Progress(103), confirmed: true);
        Assert.Equal(AtlasStateChange.Rejected, result.Change);
        Assert.Equal(raised, result.State);
    }

    [Fact]
    public void Follow_BeforeCoverageNeverFallsBack()
    {
        Assert.Equal(AtlasFollowResult.BeforeCoverage, AtlasFollow.Position(D, Progress(99), "m2"));
    }

    [Fact]
    public void Follow_UnknownWinsOverBeforeCoverage()
    {
        Assert.Equal(AtlasFollowResult.Unknown, AtlasFollow.Position(D, Progress(99, unknown: 103), "m2"));
        Assert.Equal(AtlasFollowResult.Unknown, AtlasFollow.Position(D, Progress(102, unknown: 200), "m2"));
        Assert.Equal(AtlasFollowResult.Unknown, AtlasFollow.Position(D, _ => AtlasQuestProgress.Unknown, "m2")); // logged out
    }

    [Fact]
    public void Follow_IsStatelessSoACharacterSwitchStartsFresh()
    {
        Assert.Equal("s3", AtlasFollow.Position(D, Progress(103), "m2").CheckpointId);
        Assert.Equal(AtlasFollowKind.BeforeCoverage, AtlasFollow.Position(D, Progress(0), "m2").Kind); // next character
    }

    [Fact]
    public void Follow_UsesTheRealMilestoneQuestIds()
    {
        var real = AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Draft).Dataset!;
        // NDL-012: the timeline now starts at MSQ #102, so every quest from there through The Ultimate Weapon is done.
        var throughUltimateWeapon = real.Checkpoints.Where(c => c.Id != "cp-arr-2-55").SelectMany(c => c.GameQuestIds).Select(id => (int)id).ToHashSet();
        Assert.Contains(70058, throughUltimateWeapon);
        AtlasQuestProgress Done(int id) => throughUltimateWeapon.Contains(id) ? AtlasQuestProgress.Complete : AtlasQuestProgress.Incomplete;
        Assert.Equal("cp-arr-2-0", AtlasFollow.Position(real, Done, "cp-arr-2-55").CheckpointId);
    }
}

/// <summary>v2 spoiler rule 1 and the reset rule (docs/atlas/v2-plan.md, "Spoiler rules", "Defaults").</summary>
public class V2SpoilerTests
{
    private static readonly AtlasDataset D = V2Fx.Load();

    [Theory]
    [InlineData(null, null)]
    [InlineData("", "")]
    [InlineData("m1", "nope")]
    [InlineData("s1", "s3")]
    public void Spoiler_AbsentOrInvalidStateResetsToTheEarliestCheckpoint(string? ceiling, string? view)
    {
        Assert.Equal(new AtlasSpoilerState("s0", "s0"), AtlasSpoilerPolicy.Restore(D, ceiling, view));
    }

    [Fact]
    public void Spoiler_ValidStateRestoresExactly()
    {
        Assert.Equal(new AtlasSpoilerState("m1", "s2"), AtlasSpoilerPolicy.Restore(D, "m1", "s2"));
    }

    [Fact]
    public void Spoiler_PickersAboveTheLimitShowOnlyMilestonesAndTheUnnamedNextStep()
    {
        var session = new AtlasSession(D, AtlasSpoilerPolicy.Default(D));
        var options = session.CheckpointOptions;
        Assert.Equal(new[] { "s0", "s1", "m1", "m2" }, options.Select(o => o.Id));
        Assert.Equal(AtlasText.NextStoryStepOption, options.Single(o => o.Id == "s1").Label);
        Assert.All(options, o => Assert.DoesNotContain("Quest", o.Label.Replace("Baseline Quest", string.Empty)));
    }

    [Fact]
    public void Spoiler_RaisingReachesOnlyMilestonesOrTheNextStep()
    {
        var state = AtlasSpoilerPolicy.Default(D);
        Assert.Equal(AtlasStateChange.Rejected, AtlasSpoilerPolicy.SetCeiling(D, state, "s2", confirmed: true).Change);
        Assert.Equal(AtlasStateChange.NeedsConfirmation, AtlasSpoilerPolicy.SetCeiling(D, state, "s1", confirmed: false).Change);
        Assert.Equal(AtlasStateChange.NeedsConfirmation, AtlasSpoilerPolicy.SetCeiling(D, state, "m2", confirmed: false).Change);
    }

    [Fact]
    public void Spoiler_RaisePromptNeverNamesALaterQuest()
    {
        var session = new AtlasSession(D, AtlasSpoilerPolicy.Default(D));
        Assert.Equal(AtlasStateChange.NeedsConfirmation, session.RequestCeiling("s1"));
        Assert.Contains(AtlasText.NextStoryStep, session.PendingCeilingPrompt);
        Assert.DoesNotContain("Quest One", session.PendingCeilingPrompt);

        session.CancelPendingCeiling();
        session.RequestCeiling("m1");
        Assert.Contains("Patch One complete", session.PendingCeilingPrompt);
        session.ConfirmPendingCeiling();
        Assert.Contains(session.CheckpointOptions, o => o.Id == "s3" && o.Label == "After Quest Three"); // now at or below the limit
        Assert.Equal(AtlasText.NextStoryStepOption, session.CheckpointOptions.Single(o => o.Id == "s5").Label);
    }
}

/// <summary>The whole-cast layout for the Arc lens.</summary>
public class V2LayoutTests
{
    [Fact]
    public void Layout_WholeCastAtTheCapIsDeterministicAndComplete()
    {
        var dataset = Fx.Load(V2Fx.WithCast(10));
        var view = AtlasArcs.Project(dataset, "arc-big", "s1", AtlasContentView.MainAndOptional)!;
        var a = AtlasGraphLayout.ComputeWholeCast(view.Cast, view.Entry.Id);
        var b = AtlasGraphLayout.ComputeWholeCast(view.Cast, view.Entry.Id);
        Assert.Equal(11, a.Nodes.Count);
        Assert.Equal(a.Nodes.Select(n => (n.Entity.Id, n.X, n.Y)), b.Nodes.Select(n => (n.Entity.Id, n.X, n.Y)));
        Assert.Equal((0d, 0d), (a.Nodes[0].X, a.Nodes[0].Y));
        Assert.Equal((0d, -1d), (a.Nodes[1].X, a.Nodes[1].Y));
        Assert.Equal(view.Cast.Relationships.Count, a.Edges.Count); // every cast-to-cast relationship is drawn
        var pair = a.Edges.Where(e => e.FromId == "char-m01" && e.ToId == "char-m02").ToList();
        Assert.Equal(2, pair.Count);
        Assert.Equal(new[] { 0, 1 }, pair.Select(e => e.LaneIndex).Order());
        Assert.All(pair, e => Assert.Equal(2, e.LaneCount));
    }
}
