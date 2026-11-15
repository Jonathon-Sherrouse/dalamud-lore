using System.Text.RegularExpressions;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// Tests over the real pilot file, NpcDialogueLinks/atlas.json (NDL-003). The expected snapshots below are the
/// reviewed visibility contract from docs/atlas/content-review.md; change them only together with that sheet.
/// </summary>
public class RealDataTests
{
    private const string Cp20 = "cp-arr-2-0";
    private const string Cp255 = "cp-arr-2-55";

    private static string RealPath => Path.Combine(AppContext.BaseDirectory, "atlas.json");

    private static AtlasDataset LoadDraft()
    {
        var result = AtlasLoader.LoadFile(RealPath, AtlasValidationMode.Draft);
        Assert.True(result.Success, "atlas.json failed Draft validation:\n" + string.Join("\n", result.Errors));
        return result.Dataset!;
    }

    [Fact]
    public void Real_PassesStructuralValidation()
    {
        LoadDraft();
    }

    [Fact]
    public void Real_StrictIsBlockedOnlyByReviewMarkers()
    {
        // Before human acceptance every record is pending, so Strict reports only UnreviewedRecord.
        // After the mechanical reviewed-marker commit, Strict must pass with no errors at all.
        var result = AtlasLoader.LoadFile(RealPath, AtlasValidationMode.Strict);
        Assert.All(result.Errors, e => Assert.Equal(AtlasErrorCode.UnreviewedRecord, e.Code));
        var pending = File.ReadAllText(RealPath).Contains("\"pending\"", StringComparison.Ordinal);
        Assert.Equal(!pending, result.Success);
    }

    [Fact]
    public void Real_HasExactlyTheApprovedCheckpoints()
    {
        var dataset = LoadDraft();
        Assert.Equal(
            new[] { (Cp20, "A Realm Reborn — Patch 2.0 complete"), (Cp255, "A Realm Reborn — Patch 2.55 complete") },
            dataset.Checkpoints.Select(c => (c.Id, c.Label)));
    }

    public static TheoryData<string, AtlasContentView, string[], string[]> ExpectedSnapshots() => new()
    {
        { Cp20, AtlasContentView.MainStory, [.. AllEntities.Except(Hidden20Entities)], [.. MainEdges20] },
        { Cp20, AtlasContentView.MainAndOptional, [.. AllEntities.Except(Hidden20Entities)], [.. MainEdges20, .. OptionalEdges20] },
        { Cp255, AtlasContentView.MainStory, AllEntities, [.. MainEdges255] },
        { Cp255, AtlasContentView.MainAndOptional, AllEntities, [.. MainEdges255, .. OptionalEdges255] },
    };

    [Theory]
    [MemberData(nameof(ExpectedSnapshots))]
    public void Real_SnapshotsMatchTheReviewedContract(string checkpoint, AtlasContentView view, string[] entities, string[] relationships)
    {
        var snapshot = AtlasProjector.Project(LoadDraft(), checkpoint, view);
        Assert.Equal(entities.Order(StringComparer.Ordinal), snapshot.Entities.Select(e => e.Id).Order(StringComparer.Ordinal));
        Assert.Equal(relationships.Order(StringComparer.Ordinal), snapshot.Relationships.Select(r => r.Id).Order(StringComparer.Ordinal));
    }

    [Theory]
    [InlineData(Cp20)]
    [InlineData(Cp255)]
    public void Real_OpensOnTheScionsAtEveryCheckpoint(string checkpoint)
    {
        // NDL-005 D5: the pilot home entry exists and is visible wherever the Atlas can open.
        var session = new AtlasSession(LoadDraft(), new AtlasSpoilerState(Cp255, checkpoint));
        Assert.Equal(AtlasDefaults.HomeEntityId, session.FocusId);
        Assert.NotEmpty(session.Neighborhood!.Neighbors);
    }

    [Fact]
    public void Real_MeetsPilotShape()
    {
        var dataset = LoadDraft();
        Assert.InRange(dataset.Entities.Count, 8, 12);

        var early = AtlasProjector.Project(dataset, Cp20, AtlasContentView.MainStory);
        var late = AtlasProjector.Project(dataset, Cp255, AtlasContentView.MainStory);

        // At least one description change in the main story alone…
        Assert.Contains(early.Entities, e => late.FindEntity(e.Id) is { } l && l.Summary != e.Summary);

        // …and at least one relationship that ends and one that begins.
        var earlyIds = early.Relationships.Select(r => r.Id).ToHashSet();
        var lateIds = late.Relationships.Select(r => r.Id).ToHashSet();
        Assert.NotEmpty(earlyIds.Except(lateIds));
        Assert.NotEmpty(lateIds.Except(earlyIds));
    }

    /// <summary>Surnames and later identities: case-sensitive whole words (so "Tataru" never matches "Taru").</summary>
    private static readonly string[] BannedNames =
    [
        "Warde", "Waters", "Rhul", "Augurelt", "Leveilleur", "Taru", "Totolymo", "Hext", "Ascilia", "Ascilla",
        "Lyse", "Ryne", "Exarch", "Emet-Selch", "Hythlodaeus", "Hades", "Lightwarden", "Wyrmblood", "The First",
    ];

    /// <summary>Later-story phrases: case-insensitive.</summary>
    private static readonly string[] BannedPhrases =
    [
        "Oracle of Light", "Word of the Mother", "Warrior of Darkness", "Warriors of Darkness", "Heavensward",
        "Shadowbringers", "Stormblood", "Endwalker",
    ];

    /// <summary>Things that exist only from 2.1 onward and must never surface in a 2.0 snapshot.</summary>
    private static readonly string[] NotYetAt20 = ["Crystal Braves", "Rising Stones", "banquet", "regicide"];

    public static TheoryData<string, AtlasContentView> AllSnapshots() => new()
    {
        { Cp20, AtlasContentView.MainStory },
        { Cp20, AtlasContentView.MainAndOptional },
        { Cp255, AtlasContentView.MainStory },
        { Cp255, AtlasContentView.MainAndOptional },
    };

    [Theory]
    [MemberData(nameof(AllSnapshots))]
    public void Real_NoDisplayedTextLeaksLaterStory(string checkpoint, AtlasContentView view)
    {
        var snapshot = AtlasProjector.Project(LoadDraft(), checkpoint, view);
        foreach (var text in DisplayedText(snapshot))
        {
            foreach (var name in BannedNames)
            {
                Assert.False(Regex.IsMatch(text, $@"(?<![\p{{L}}-]){Regex.Escape(name)}(?![\p{{L}}-])"), $"'{name}' appears in: {text}");
            }

            foreach (var phrase in BannedPhrases)
            {
                Assert.False(text.Contains(phrase, StringComparison.OrdinalIgnoreCase), $"'{phrase}' appears in: {text}");
            }

            if (checkpoint == Cp20)
            {
                foreach (var phrase in NotYetAt20)
                {
                    Assert.False(text.Contains(phrase, StringComparison.OrdinalIgnoreCase), $"2.55 term '{phrase}' appears at 2.0 in: {text}");
                }
            }
        }
    }

    /// <summary>Wiki pages that the citation-safety audit ruled unsafe to link at any checkpoint.</summary>
    private static readonly string[] NeverLink =
    [
        "Minfilia", "Ryne", "Oracle_of_Light", "The_First", "Lyse", "The_Unending_Codex", "Ascilla", "Leveilleur",
    ];

    [Theory]
    [MemberData(nameof(AllSnapshots))]
    public void Real_CitationLinksAreSafe(string checkpoint, AtlasContentView view)
    {
        var snapshot = AtlasProjector.Project(LoadDraft(), checkpoint, view);
        var citations = snapshot.Entities.SelectMany(e => e.Citations).Concat(snapshot.Relationships.SelectMany(r => r.Citations));
        foreach (var url in citations.Select(c => c.Url).OfType<Uri>())
        {
            Assert.Equal("https", url.Scheme);
            Assert.Equal("ffxiv.consolegameswiki.com", url.Host);
            Assert.StartsWith("/wiki/", url.AbsolutePath, StringComparison.Ordinal);
            Assert.Empty(url.Query);
            var page = Uri.UnescapeDataString(url.AbsolutePath["/wiki/".Length..]);
            Assert.DoesNotContain(NeverLink, bad => page.Contains(bad, StringComparison.OrdinalIgnoreCase));
            if (checkpoint == Cp20)
            {
                Assert.DoesNotContain("Louisoix", page, StringComparison.OrdinalIgnoreCase);
            }
        }
    }

    private static IEnumerable<string> DisplayedText(AtlasSnapshot snapshot)
    {
        foreach (var e in snapshot.Entities)
        {
            yield return e.Name;
            yield return e.Summary;
            foreach (var a in e.Aliases)
            {
                yield return a;
            }

            foreach (var c in e.Citations)
            {
                yield return c.Title;
                if (c.Url is not null)
                {
                    yield return Uri.UnescapeDataString(c.Url.ToString()).Replace('_', ' ');
                }
            }
        }

        foreach (var r in snapshot.Relationships)
        {
            yield return r.OutgoingLabel;
            yield return r.IncomingLabel;
            foreach (var c in r.Citations)
            {
                yield return c.Title;
                if (c.Url is not null)
                {
                    yield return Uri.UnescapeDataString(c.Url.ToString()).Replace('_', ' ');
                }
            }
        }
    }

    private static readonly string[] AllEntities =
    [
        "char-alisaie", "char-alphinaud", "char-louisoix", "char-minfilia", "char-tataru", "char-thancred",
        "char-urianger", "char-yshtola", "org-crystal-braves", "org-scions", "loc-rising-stones", "loc-waking-sands",
    ];

    private static readonly string[] Hidden20Entities = ["org-crystal-braves", "loc-rising-stones"];

    private static readonly string[] MembersAndTwins =
    [
        "rel-minfilia-leads-scions", "rel-thancred-member-scions", "rel-yshtola-member-scions", "rel-urianger-member-scions",
        "rel-alphinaud-member-scions", "rel-tataru-member-scions", "rel-alphinaud-twin-alisaie",
    ];

    private static readonly string[] MainEdges20 = [.. MembersAndTwins, "rel-scions-hq-waking-sands"];

    private static readonly string[] OptionalEdges20 = ["rel-alisaie-grandchild-louisoix", "rel-alisaie-member-scions"];

    private static readonly string[] MainEdges255 =
    [
        .. MembersAndTwins, "rel-braves-control-rising-stones", "rel-braves-turned-against-scions", "rel-urianger-conceals-waking-sands",
    ];

    private static readonly string[] OptionalEdges255 = [.. OptionalEdges20, "rel-alphinaud-grandchild-louisoix"];
}
