using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

public class ValidationTests
{
    [Fact]
    public void Validation_RejectsDuplicateEntityId()
    {
        var doc = Fx.Sample();
        Fx.Entities(doc).Add(Fx.Entity(doc, "char-maren").DeepClone());
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.DuplicateId);
    }

    [Fact]
    public void Validation_RejectsUnknownReference()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-tobin-member")["target"] = "org-nowhere";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.UnknownReference);
    }

    [Fact]
    public void Validation_RejectsUnknownRelationshipType()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-tobin-member")["type"] = "rivals";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.UnknownReference);
    }

    [Theory]
    [InlineData("cp-early", "cp-early")]
    [InlineData("cp-later", "cp-early")]
    public void Validation_RejectsEmptyOrInvertedInterval(string from, string until)
    {
        var doc = Fx.Sample();
        var rel = Fx.Rel(doc, "rel-tobin-member");
        rel["validFrom"] = from;
        rel["validUntil"] = until;
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidInterval);
    }

    [Fact]
    public void Validation_RejectsEdgeWhoseEndpointIsHidden()
    {
        // WE-1: the New Hall is not visible at cp-early.
        var doc = Fx.Sample();
        Fx.Relationships(doc).Add(Fx.Edge("rel-early-new-hall", "org-lantern-guild", "headquartered-at", "loc-new-hall"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.EndpointNotVisible);
    }

    [Fact]
    public void Validation_RejectsMainEdgeToOptionalOnlyEntity()
    {
        var doc = Fx.Sample();
        Fx.Entities(doc).Add(new JsonObject
        {
            ["id"] = "char-secret",
            ["category"] = "character",
            ["presentations"] = new JsonArray(Fx.Pres("Secret", Fx.Early, scope: "optional")),
        });
        Fx.Relationships(doc).Add(Fx.Edge("rel-secret", "char-secret", "member-of", "org-lantern-guild"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.EndpointNotVisible);

        // The same edge is legal as optional.
        Fx.Rel(doc, "rel-secret")["scope"] = "optional";
        Fx.Rel(doc, "rel-secret")["citations"] = new JsonArray(Fx.DefaultCite(Fx.Early, "optional"));
        Assert.True(Fx.Try(doc).Success);
    }

    [Fact]
    public void Validation_RejectsOverlappingPresentations()
    {
        // WE-2: two main presentations covering cp-later. A main and an optional one may coexist (Corin).
        var doc = Fx.Sample();
        Fx.Presentation(doc, "char-maren", 0)["validUntil"] = null;
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.OverlappingPresentation);
    }

    [Fact]
    public void Validation_RejectsGapInVisibility()
    {
        var doc = Fx.ThreeCheckpoints();
        var a = Fx.Entity(doc, "char-a");
        a["presentations"] = new JsonArray(
            Fx.Pres("A", "cp-1", "cp-2", citation: Fx.Cite("Src 1", "cp-1")),
            Fx.Pres("A", "cp-3", citation: Fx.Cite("Src 1", "cp-1")));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.VisibilityGap);

        // Ending early, or starting late, is not a gap.
        a["presentations"] = new JsonArray(Fx.Pres("A", "cp-1", "cp-3", citation: Fx.Cite("Src 1", "cp-1")));
        Assert.True(Fx.Try(doc).Success);
        a["presentations"] = new JsonArray(Fx.Pres("A", "cp-2", citation: Fx.Cite("Src 1", "cp-1")));
        Assert.True(Fx.Try(doc).Success);
    }

    [Fact]
    public void Validation_RejectsReverseDuplicateOfSymmetricEdge()
    {
        var doc = Fx.Sample();
        Fx.Relationships(doc).Add(Fx.Edge("rel-ada-twin-bren", "char-ada", "twin-of", "char-bren", citation: Fx.Cite("Sample Quest: Two Travelers")));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.ReverseSymmetricDuplicate);
    }

    [Fact]
    public void Validation_RejectsReversedSymmetricEvenWithoutOverlap()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-bren-twin-ada")["validUntil"] = Fx.Later;
        Fx.Relationships(doc).Add(Fx.Edge("rel-ada-twin-bren", "char-ada", "twin-of", "char-bren", from: Fx.Later, citation: Fx.DefaultCite(Fx.Later)));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.ReverseSymmetricDuplicate);
    }

    [Fact]
    public void Validation_AllowsAdjacentSplitOfSameTriple()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-bren-twin-ada")["validUntil"] = Fx.Later;
        Fx.Relationships(doc).Add(Fx.Edge("rel-bren-twin-ada-2", "char-bren", "twin-of", "char-ada", from: Fx.Later, citation: Fx.DefaultCite(Fx.Later)));
        Assert.True(Fx.Try(doc).Success);
    }

    [Fact]
    public void Validation_RejectsCrossScopeDuplicateTriple()
    {
        var doc = Fx.Sample();
        Fx.Relationships(doc).Add(Fx.Edge("rel-ada-grandchild-main", "char-ada", "grandchild-of", "char-corin"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.DuplicateRelationship);
    }

    [Fact]
    public void Validation_RejectsCitationNewerThanRecord()
    {
        // WE-1 / R08: the evidence that the base relationship ends must not be cited on it.
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-guild-hq-old-hall")["citations"]!.AsArray().Add(Fx.Cite("Sample Quest: A New Hall", Fx.Later));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.CitationTooNew);
    }

    [Fact]
    public void Validation_RejectsMainRecordCitingOptional()
    {
        var doc = Fx.Sample();
        Fx.Presentation(doc, "char-corin", 0)["citations"]!.AsArray().Add(Fx.Cite("Sample Side Story: The Elder's Pledge", scope: "optional"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.CitationScopeMismatch);
    }

    [Fact]
    public void Validation_RejectsUnknownCitationCheckpoint()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-tobin-member")["citations"] = new JsonArray(Fx.Cite("Sample Quest: The First Lantern", "cp-someday"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.UnknownReference);
    }

    [Fact]
    public void Validation_RejectsInconsistentCitationTitles()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-maren-leads-guild")["citations"] = new JsonArray(Fx.Cite("Sample Quest: The Banquet", Fx.Early));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InconsistentCitation);
    }

    [Theory]
    [InlineData("https://example.invalid/page#later-section")]
    [InlineData("https://user:pass@example.invalid/page")]
    [InlineData("javascript:alert(1)")]
    [InlineData("file:///etc/passwd")]
    [InlineData("example.invalid/relative")]
    public void Validation_RejectsUnsafeUrls(string url)
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-tobin-member")["citations"] = new JsonArray(Fx.Cite("Unique Url Source", url: url));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
    }

    [Fact]
    public void Validation_RejectsOptionalSpanningMainBoundary()
    {
        // Maren's main presentations change at cp-later; one optional presentation may not straddle that change.
        var doc = Fx.Sample();
        Fx.Entity(doc, "char-maren")["presentations"]!.AsArray().Add(Fx.Pres("Maren", Fx.Early, scope: "optional"));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.OptionalSpansMainBoundary);
    }

    [Fact]
    public void Validation_RejectsOptionalStraddlingMainCoverage()
    {
        var doc = Fx.ThreeCheckpoints();
        Fx.Entity(doc, "char-a")["presentations"] = new JsonArray(
            Fx.Pres("A", "cp-2", citation: Fx.Cite("Src 1", "cp-1")),
            Fx.Pres("A+", "cp-1", scope: "optional", citation: Fx.Cite("Src 1", "cp-1")));
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.OptionalSpansMainBoundary);
    }

    [Fact]
    public void Validation_RejectsOptionalEndingEarly()
    {
        var doc = Fx.Sample();
        var presentations = Fx.Entity(doc, "char-corin")["presentations"]!.AsArray();
        presentations.RemoveAt(2); // drop Corin's cp-later optional presentation
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.OptionalEndsEarly);
    }

    [Fact]
    public void Validation_RejectsSymmetricTypeWithDifferentLabels()
    {
        var doc = Fx.Sample();
        var twin = doc["relationshipTypes"]!.AsArray().Select(t => t!.AsObject()).First(t => (string?)t["id"] == "twin-of");
        twin["incomingLabel"] = "twin sibling of";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
    }

    [Fact]
    public void Validation_RejectsSelfRelationship()
    {
        var doc = Fx.Sample();
        Fx.Rel(doc, "rel-tobin-member")["target"] = "char-tobin";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
    }
}
