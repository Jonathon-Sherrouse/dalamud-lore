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
    private const string Cp30 = "cp-hw-3-0";
    private const string Cp356 = "cp-hw-3-56";
    private const string Cp40 = "cp-sb-4-0";
    private const string Cp456 = "cp-sb-4-56";
    private const string Cp50 = "cp-shb-5-0";
    private const string Cp555 = "cp-shb-5-55";
    private const string Cp60 = "cp-ew-6-0";
    private const string Cp655 = "cp-ew-6-55";

    private static string RealPath => Path.Combine(AppContext.BaseDirectory, "atlas.json");

    /// <summary>Parsed once: the file is several megabytes, and hundreds of per-checkpoint cases read it.</summary>
    private static readonly Lazy<AtlasLoadResult> Draft = new(() => AtlasLoader.LoadFile(RealPath, AtlasValidationMode.Draft));

    private static AtlasDataset LoadDraft()
    {
        var result = Draft.Value;
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
        // ARR #1–#101 (2026-11-19) come first: the three starting-city chains (one after another), then the shared story
        // to #101 (tools/atlas/timeline_arr_early.py). Everything from #102 on keeps its pinned position, offset by them.
        const int o = 150;
        Assert.Equal(("cp-msq-1", "Close to Home (Gridania)", 65621), (dataset.Checkpoints[0].Id, dataset.Checkpoints[0].QuestTitle, dataset.Checkpoints[0].GameQuestIds.Single()));
        Assert.Equal(("cp-msq-1b", "Close to Home (Limsa Lominsa)"), (dataset.Checkpoints[23].Id, dataset.Checkpoints[23].QuestTitle));
        Assert.Equal(("cp-msq-1c", "Close to Home (Ul'dah)"), (dataset.Checkpoints[45].Id, dataset.Checkpoints[45].QuestTitle));
        Assert.Equal(("cp-msq-25", "It's Probably Pirates"), (dataset.Checkpoints[69].Id, dataset.Checkpoints[69].QuestTitle));
        Assert.Equal(("cp-msq-101", "Battle Scars"), (dataset.Checkpoints[o - 1].Id, dataset.Checkpoints[o - 1].QuestTitle));
        Assert.Equal("cp-msq-102", dataset.Checkpoints[o].Id);
        // NDL-012: MSQ #102–#153, one step per quest, both #150 paths in MSQ-index-then-authored order (no #152).
        // NDL-009: the A4 slice (after MSQ #154, then #155–160), then the two kept milestone ids.
        Assert.Equal(
            new[]
            {
                ("cp-msq-102", "After It Was a Very Good Year", 66386),
                ("cp-msq-103", "After In the Company of Heroes", 66391),
                ("cp-msq-104", "After As You Wish", 66392),
                ("cp-msq-105", "After Lord of Crags", 66393),
                ("cp-msq-106", "After All Good Things", 66053),
                ("cp-msq-107", "After You Can't Take It with You", 69403),
                ("cp-msq-108", "After Bringing out the Dead", 66412),
                ("cp-msq-109", "After Bury Me Not on the Lone Prairie", 66414),
                ("cp-msq-110", "After Eyes on Me", 66054),
                ("cp-msq-111", "After He Who Waited Behind", 66419),
                ("cp-msq-112", "After Cold Reception", 66420),
                ("cp-msq-113", "After The Unending War", 66422),
                ("cp-msq-114", "After Men of Honor", 66423),
                ("cp-msq-115", "After Three for Three", 66425),
                ("cp-msq-116", "After The Rose and the Unicorn", 66426),
                ("cp-msq-117", "After The Talk of Coerthas", 66433),
                ("cp-msq-118", "After Road to Redemption", 66446),
                ("cp-msq-119", "After Following the Evidence", 66447),
                ("cp-msq-120", "After In the Eyes of Gods and Men", 66448),
                ("cp-msq-121", "After The Final Flight of the Enterprise", 69404),
                ("cp-msq-122", "After Ye of Little Faith", 66460),
                ("cp-msq-123", "After Factual Folklore", 66463),
                ("cp-msq-124", "After The Best Inventions", 69405),
                ("cp-msq-125", "After Influencing Inquisitors", 66474),
                ("cp-msq-126", "After By the Lights of Ishgard", 66475),
                ("cp-msq-127", "After Blood for Blood", 66476),
                ("cp-msq-128", "After The Heretic among Us", 66477),
                ("cp-msq-129", "After In Pursuit of the Past", 66488),
                ("cp-msq-130", "After Into the Eye of the Storm", 66489),
                ("cp-msq-131", "After Sealed with Science", 66491),
                ("cp-msq-132", "After With the Utmost Care", 66492),
                ("cp-msq-133", "After A Promising Prospect", 66495),
                ("cp-msq-134", "After It's Probably Not Pirates", 66496),
                ("cp-msq-135", "After Representing the Representative", 66497),
                ("cp-msq-136", "After The Reluctant Researcher", 66498),
                ("cp-msq-137", "After Sweet Somethings", 66499),
                ("cp-msq-138", "After History Repeating", 66503),
                ("cp-msq-139", "After The Curious Case of Giggity", 69406),
                ("cp-msq-140", "After Better Late than Never", 66511),
                ("cp-msq-141", "After Lady of the Vortex", 66055),
                ("cp-msq-142", "After Reclamation", 66056),
                ("cp-msq-143", "After Casing the Castrum", 66514),
                ("cp-msq-144", "After Eyes on the Empire", 66516),
                ("cp-msq-145", "After Footprints in the Snow", 66517),
                ("cp-msq-146", "After Monumental Hopes", 66518),
                ("cp-msq-147", "After Notorious Biggs", 66519),
                ("cp-msq-148", "After Come-Into-My-Castrum", 66520),
                ("cp-msq-149", "After Getting Even with Garlemald", 66522),
                ("cp-msq-150", "After Drowning Out the Voices", 66537),
                ("cp-msq-150b", "After Acting the Part", 66538),
                ("cp-msq-151", "After Dressed for Conquest", 69407),
                ("cp-msq-153", "After Fool Me Twice", 66540),
                ("cp-msq-154", "After Every Little Thing She Does Is Magitek", 66541),
                ("cp-msq-155", "After Escape from Castrum Centri", 66057),
                ("cp-msq-156", "After The Black Wolf's Ultimatum", 66058),
                ("cp-msq-157", "After Operation Archon", 70057),
                ("cp-msq-158", "After A Hero in Need", 66573),
                ("cp-msq-159", "After Hearts on Fire", 69408),
                ("cp-msq-160", "After Rock the Castrum", 69409),
                (Cp20, "A Realm Reborn — Patch 2.0 complete", 70058), // The Ultimate Weapon (#161)
            },
            dataset.Checkpoints.Skip(o).Take(60).Select(c => (c.Id, c.Label, c.GameQuestIds.Single())));

        // After 2.0 (2026-11-19): one step per main-scenario quest of 2.1–3.56, generated from the wiki infoboxes
        // (tools/atlas/timeline_2x_3x.py), with each patch's last quest as a milestone: 2.55, 3.0 and 3.56.
        // Stormblood (2026-11-19): one step per quest of 4.0–4.56 (tools/atlas/timeline_4x.py), with the 4.0 and 4.56 milestones.
        // Shadowbringers (2026-11-19): one step per quest of 5.0–5.55 (tools/atlas/timeline_5x.py), with the 5.0 and 5.55 milestones.
        // Endwalker (2026-11-19): one step per quest of 6.0–6.55 (tools/atlas/timeline_6x.py), with the 6.0 and 6.55 milestones.
        Assert.Equal(902, dataset.Checkpoints.Count);
        Assert.Equal(
            new[] { (Cp20, 59 + o, 70058), (Cp255, 139 + o, 65964), (Cp30, 233 + o, 67205), (Cp356, 277 + o, 67895), (Cp40, 399 + o, 68089), (Cp456, 439 + o, 68721), (Cp50, 545 + o, 69190), (Cp555, 596 + o, 69602), (Cp60, 704 + o, 70000), (Cp655, 751 + o, 70289) },
            dataset.Checkpoints.Where(c => c.Milestone).Select(c => (c.Id, c.Order, c.GameQuestIds.Single())));
        Assert.Equal("A Realm Reborn — Patch 2.55 complete", dataset.Checkpoints[139 + o].Label);
        Assert.Equal("Heavensward — Patch 3.0 complete", dataset.Checkpoints[233 + o].Label);
        Assert.Equal("Heavensward — Patch 3.56 complete", dataset.Checkpoints[277 + o].Label);
        Assert.Equal(("cp-msq-162", "The Price of Principles", 66711), (dataset.Checkpoints[60 + o].Id, dataset.Checkpoints[60 + o].QuestTitle, dataset.Checkpoints[60 + o].GameQuestIds.Single()));
        Assert.Equal(("cp-msq-240", "The Parting Glass"), (dataset.Checkpoints[138 + o].Id, dataset.Checkpoints[138 + o].QuestTitle));
        Assert.Equal(("cp-msq-242", "Coming to Ishgard"), (dataset.Checkpoints[140 + o].Id, dataset.Checkpoints[140 + o].QuestTitle));
        Assert.Equal(("cp-msq-334", "Fetters of Lament"), (dataset.Checkpoints[232 + o].Id, dataset.Checkpoints[232 + o].QuestTitle));
        Assert.Equal(("cp-msq-336", "An Uncertain Future"), (dataset.Checkpoints[234 + o].Id, dataset.Checkpoints[234 + o].QuestTitle));
        Assert.Equal(("cp-msq-378", "Fly Free, My Pretty"), (dataset.Checkpoints[276 + o].Id, dataset.Checkpoints[276 + o].QuestTitle));
        Assert.Equal(("cp-msq-380", "Beyond the Great Wall", 67982), (dataset.Checkpoints[278 + o].Id, dataset.Checkpoints[278 + o].QuestTitle, dataset.Checkpoints[278 + o].GameQuestIds.Single()));
        Assert.Equal(("cp-msq-500", "The Measure of His Reach"), (dataset.Checkpoints[398 + o].Id, dataset.Checkpoints[398 + o].QuestTitle));
        Assert.Equal(("cp-msq-502", "Arenvald's Adventure"), (dataset.Checkpoints[400 + o].Id, dataset.Checkpoints[400 + o].QuestTitle));
        Assert.Equal(("cp-msq-540", "A Brief Reprieve"), (dataset.Checkpoints[438 + o].Id, dataset.Checkpoints[438 + o].QuestTitle));
        Assert.Equal("Stormblood — Patch 4.0 complete", dataset.Checkpoints[399 + o].Label);
        Assert.Equal("Stormblood — Patch 4.56 complete", dataset.Checkpoints[439 + o].Label);
        Assert.Equal(("cp-msq-542", "The Syrcus Trench"), (dataset.Checkpoints[440 + o].Id, dataset.Checkpoints[440 + o].QuestTitle));
        Assert.Equal(("cp-msq-646", "A Greater Purpose"), (dataset.Checkpoints[544 + o].Id, dataset.Checkpoints[544 + o].QuestTitle));
        Assert.Equal(("cp-msq-697", "On Official Business"), (dataset.Checkpoints[595 + o].Id, dataset.Checkpoints[595 + o].QuestTitle));
        Assert.Equal("Shadowbringers — Patch 5.0 complete", dataset.Checkpoints[545 + o].Label);
        Assert.Equal("Shadowbringers — Patch 5.55 complete", dataset.Checkpoints[596 + o].Label);
        Assert.Equal(("cp-msq-699", "The Next Ship to Sail", 69893), (dataset.Checkpoints[597 + o].Id, dataset.Checkpoints[597 + o].QuestTitle, dataset.Checkpoints[597 + o].GameQuestIds.Single()));
        Assert.Equal(("cp-msq-807", "Newfound Adventure"), (dataset.Checkpoints[705 + o].Id, dataset.Checkpoints[705 + o].QuestTitle));
        Assert.Equal(("cp-msq-852", "The Game Is Afoot"), (dataset.Checkpoints[750 + o].Id, dataset.Checkpoints[750 + o].QuestTitle));
        Assert.Equal("Endwalker — Patch 6.0 complete", dataset.Checkpoints[704 + o].Label);
        Assert.Equal("Endwalker — Patch 6.55 complete", dataset.Checkpoints[751 + o].Label);
        Assert.Equal(dataset.Checkpoints.Count, dataset.Checkpoints.Select(c => c.Id).Distinct().Count());
        Assert.All(dataset.Checkpoints.Where(c => !c.Milestone), c => Assert.Equal(c.Label, $"After {c.QuestTitle}"));

        // Not contiguous: the first step, and each step that follows another parallel path (#150, 2.55's pairs, the
        // Artoirel and Emmanellain chains, the moogle trials). Every milestone follows its patch's last quest.
        Assert.Equal(
            new[] { "cp-msq-1", "cp-msq-1b", "cp-msq-1c", "cp-msq-41b", "cp-msq-41c", "cp-msq-80b", "cp-msq-150b", "cp-msq-234b", "cp-msq-245b", "cp-msq-282b", "cp-msq-282c", "cp-msq-385b", "cp-msq-387c", "cp-msq-398b", "cp-msq-398c", "cp-msq-421b", "cp-msq-421c", "cp-msq-545b", "cp-msq-570b", "cp-msq-570c", "cp-msq-701b" },
            dataset.Checkpoints.Where(c => !c.ContiguousWithPrevious).Select(c => c.Id));
    }

    /// <summary>
    /// NDL-006: the accepted pilot content must come through the v1 → v2 upgrade unchanged. These fingerprints were
    /// captured by running this digest on the v1 data and code (origin/main at 23cd3fa). They cover every displayable
    /// field, optional flags included, of the accepted legacy records only, so later content (arc entries, NDL-009)
    /// never moves the pin.
    /// </summary>
    [Theory]
    [InlineData(Cp20, AtlasContentView.MainStory, "FD571B50BDDB29076893F4DDAF61E56161D8A3CE73C764681A335DE4B73B4AFE")]
    [InlineData(Cp20, AtlasContentView.MainAndOptional, "382A24F8D5F7E3A3F39CF6E3F73CA41FA98A5B2586DAE8D64A1BAD497552EE91")]
    [InlineData(Cp255, AtlasContentView.MainStory, "22E72329BEC68619C422404DB74676F9B41C2DD2E3BCB568F7E57F3BD4F45220")]
    [InlineData(Cp255, AtlasContentView.MainAndOptional, "08698C44E3E98A2BD5844D4BA544C40986DB247E9D8667A9CD5D16C147F9584B")]
    public void Real_AcceptedSnapshotsArePinnedAcrossTheV2Upgrade(string checkpoint, AtlasContentView view, string digest)
    {
        var dataset = LoadDraft();
        Assert.All(LegacyRelationships, id => Assert.Contains(dataset.Relationships, r => r.Id == id));
        Assert.Equal(digest, SnapshotDigest.Of(AtlasProjector.Project(dataset, checkpoint, view), AllEntities.ToHashSet(), LegacyRelationships.ToHashSet()));
    }

    /// <summary>The fourteen relationships accepted before schema v2.</summary>
    private static readonly string[] LegacyRelationships =
    [
        "rel-alisaie-grandchild-louisoix", "rel-alisaie-member-scions", "rel-alphinaud-grandchild-louisoix", "rel-alphinaud-member-scions",
        "rel-alphinaud-twin-alisaie", "rel-braves-control-rising-stones", "rel-braves-turned-against-scions", "rel-minfilia-leads-scions",
        "rel-scions-hq-waking-sands", "rel-tataru-member-scions", "rel-thancred-member-scions", "rel-urianger-conceals-waking-sands",
        "rel-urianger-member-scions", "rel-yshtola-member-scions",
    ];

    public static TheoryData<string, AtlasContentView, string[], string[]> ExpectedSnapshots()
    {
        var data = new TheoryData<string, AtlasContentView, string[], string[]>
        {
            { Cp20, AtlasContentView.MainStory, [.. AllEntities.Except(Hidden20Entities), .. ArcEntities, .. ArrEntities], [.. MainEdges20, .. ArcEdgesAtMilestones, .. ArrLasting] },
            { Cp20, AtlasContentView.MainAndOptional, [.. AllEntities.Except(Hidden20Entities), .. ArcEntities, .. ArrEntities], [.. MainEdges20, .. OptionalEdges20, .. ArcEdgesAtMilestones, .. ArrLasting] },
            { Cp255, AtlasContentView.MainStory, [.. AllEntities, .. ArcEntities, .. ArrEntities], [.. MainEdges255, .. ArcEdgesAtMilestones, .. ArrLasting] },
            { Cp255, AtlasContentView.MainAndOptional, [.. AllEntities, .. ArcEntities, .. ArrEntities], [.. MainEdges255, .. OptionalEdges255, .. ArcEdgesAtMilestones, .. ArrLasting] },
        };

        // NDL-009: the A4 slice, now with the NDL-012 records that carry on through it; every slice record is main scope.
        foreach (var (step, entities, relationships) in SliceSnapshots)
        {
            data.Add(step, AtlasContentView.MainStory, entities, relationships);
            data.Add(step, AtlasContentView.MainAndOptional, entities, relationships);
        }

        return data;
    }

    [Theory]
    [MemberData(nameof(ExpectedSnapshots))]
    public void Real_SnapshotsMatchTheReviewedContract(string checkpoint, AtlasContentView view, string[] entities, string[] relationships)
    {
        var snapshot = AtlasProjector.Project(LoadDraft(), checkpoint, view);
        // The lead's earlier entries (2026-11-19): text from #148 names Revenant's Toll, and the #159 recap names Raubahn.
        var at = OrderOf(checkpoint);
        entities = [.. entities, .. LeadBackfills.Where(b => at >= OrderOf(b.From)).Select(b => b.Id)];
        if (checkpoint == Cp255 || OrderOf(checkpoint) >= OrderOf("cp-msq-102"))
        {
            // Every story point now has earlier or later content around it (ARR #1–#101 before the slice, 2.1–2.55 before
            // this milestone), so each shows everything reviewed here plus that content.
            Assert.Subset(snapshot.Entities.Select(e => e.Id).ToHashSet(), entities.ToHashSet());
            Assert.Subset(snapshot.Relationships.Select(r => r.Id).ToHashSet(), relationships.ToHashSet());
            return;
        }

        Assert.Equal(entities.Order(StringComparer.Ordinal), snapshot.Entities.Select(e => e.Id).Order(StringComparer.Ordinal));
        Assert.Equal(relationships.Order(StringComparer.Ordinal), snapshot.Relationships.Select(r => r.Id).Order(StringComparer.Ordinal));
    }

    public static TheoryData<string> AllCheckpoints() => new(SliceSteps.Concat([Cp20, Cp255]));

    /// <summary>NDL-012: every step from #102 to #160, read from the file, so the sweeps cover the whole timeline.</summary>
    private static string[] SliceSteps =>
        Draft.Value.Dataset!.Checkpoints.Where(c => !c.Milestone).Select(c => c.Id).ToArray();

    [Theory]
    [MemberData(nameof(AllCheckpoints))]
    public void Real_OpensOnTheScionsAtEveryCheckpoint(string checkpoint)
    {
        // NDL-005 D5: the Atlas opens on the home entry wherever it is visible. Before the Scions appear (#30, 2026-11-19)
        // there is no home entry yet, so the Story point lens opens with nothing focused rather than naming them early.
        var dataset = LoadDraft();
        var session = new AtlasSession(dataset, new AtlasSpoilerState(dataset.Checkpoints[^1].Id, checkpoint));
        Assert.Equal(checkpoint, session.SpoilerState.ViewId);
        session.SetLens(AtlasLens.StoryPoint);
        if (session.Snapshot.FindEntity(AtlasDefaults.HomeEntityId) is null)
        {
            Assert.Null(session.FocusId);
            return;
        }

        Assert.Equal(AtlasDefaults.HomeEntityId, session.FocusId);
        Assert.NotEmpty(session.Neighborhood!.Neighbors);
    }

    [Fact]
    public void Real_MeetsPilotShape()
    {
        var dataset = LoadDraft();
        // Every entry through NDL-012 is still there; the eras after 2.0 add the rest (438 with ARR #1–#101, 542 through Endwalker).
        Assert.All(AllEntities.Concat(ArcEntities).Concat(ArrEntities), id => Assert.Contains(dataset.Entities, e => e.Id == id));
        Assert.Equal(542, dataset.Entities.Count);

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
        // NDL-009 (arc A4): imperial and engineer surnames, and the 2.0 finale's setups for later content.
        "Garlond", "Baelsar", "Junius", "Scaeva", "Arvina", "Midas", "Nero", "Zodiark", "Nabriales", "Igeyorhm", "Pashtarot",
    ];

    /// <summary>Later-story phrases: case-insensitive.</summary>
    private static readonly string[] BannedPhrases =
    [
        "Oracle of Light", "Word of the Mother", "Warrior of Darkness", "Warriors of Darkness", "Heavensward",
        "Shadowbringers", "Stormblood", "Endwalker", "Bahamut stirs", "the Reckoning", "Dark One", "new primal",
    ];

    /// <summary>
    /// Banned names and phrases that the story itself establishes later: each may appear from the step named here on
    /// (2026-11-19, the timeline through 3.56). Mirrored in tools/atlas/build_pilot_content.py (ALLOWED_FROM).
    /// </summary>
    private static readonly Dictionary<string, string> AllowedFrom = new()
    {
        ["Nabriales"] = "cp-msq-224", // he names himself in An Uninvited Ascian, and is destroyed there
        ["Warriors of Darkness"] = "cp-msq-340", // the band names itself in Against the Dying of the Light
        ["Warrior of Darkness"] = "cp-msq-340",
        ["Word of the Mother"] = "cp-msq-345", // the voice's own name, and that quest's title
        ["Nero"] = "cp-msq-376", // he introduces himself to the Alliance in The Obvious Solution
        ["Lyse"] = "cp-hw-3-56", // Yda is revealed as Lyse in The Far Edge of Fate
        ["Heavensward"] = "cp-hw-3-0", // the 3.0 finale's own quest title
        // Shadowbringers: each from the earliest step any era's pages establish it (mirrors ALLOWED_FROM in the build).
        ["Exarch"] = "cp-msq-542", ["The First"] = "cp-msq-542", ["Oracle of Light"] = "cp-msq-543", ["Lightwarden"] = "cp-msq-563",
        ["Emet-Selch"] = "cp-msq-584", ["Zodiark"] = "cp-msq-603", ["Ryne"] = "cp-msq-620", ["Hythlodaeus"] = "cp-msq-646",
        ["Hades"] = "cp-shb-5-0",
    };

    /// <summary>Terms of the 2.x story that must not surface before the quest that introduces them (case-insensitive).</summary>
    private static readonly (string Term, string From)[] NotBefore =
    [
        ("Rising Stones", "cp-msq-165"), ("Crystal Braves", "cp-msq-199"), ("regicide", "cp-msq-168"), ("banquet", "cp-msq-233"),
    ];

    private static readonly (string Id, string From)[] LeadBackfills = [("loc-revenants-toll", "cp-msq-148"), ("char-raubahn", "cp-msq-159")];

    private static readonly HashSet<string> QuestTitles =
        AtlasLoader.LoadFile(RealPath, AtlasValidationMode.Draft).Dataset!.Checkpoints.Select(c => c.QuestTitle).OfType<string>().ToHashSet();

    private static readonly Dictionary<string, int> Orders =
        AtlasLoader.LoadFile(RealPath, AtlasValidationMode.Draft).Dataset!.Checkpoints.ToDictionary(c => c.Id, c => c.Order);

    private static int OrderOf(string checkpoint) => Orders[checkpoint];

    public static TheoryData<string, AtlasContentView> AllSnapshots()
    {
        var data = new TheoryData<string, AtlasContentView>();
        foreach (var checkpoint in SliceSteps.Concat([Cp20, Cp255]))
        {
            data.Add(checkpoint, AtlasContentView.MainStory);
            data.Add(checkpoint, AtlasContentView.MainAndOptional);
        }

        return data;
    }

    [Theory]
    [MemberData(nameof(AllSnapshots))]
    public void Real_NoDisplayedTextLeaksLaterStory(string checkpoint, AtlasContentView view)
    {
        var snapshot = AtlasProjector.Project(LoadDraft(), checkpoint, view);
        var at = OrderOf(checkpoint);
        bool Allowed(string term) => AllowedFrom.TryGetValue(term, out var from) && at >= OrderOf(from);
        // A citation shows its quest's title, which is public and appears only once that quest is reached (Still
        // Waters, Shadows of the First), so the name lists apply to everything else.
        var citationTexts = snapshot.Entities.SelectMany(e => e.Citations).Concat(snapshot.Relationships.SelectMany(r => r.Citations))
            .SelectMany(c => new[] { c.Title, c.Url is null ? null : Uri.UnescapeDataString(c.Url.ToString()).Replace('_', ' ') }).OfType<string>().ToHashSet();
        foreach (var text in DisplayedText(snapshot).Where(t => !citationTexts.Contains(t)))
        {
            foreach (var name in BannedNames.Where(n => !Allowed(n)))
            {
                Assert.False(Regex.IsMatch(text, $@"(?<![\p{{L}}-]){Regex.Escape(name)}(?![\p{{L}}-])"), $"'{name}' appears in: {text}");
            }

            foreach (var phrase in BannedPhrases.Where(n => !Allowed(n)))
            {
                Assert.False(text.Contains(phrase, StringComparison.OrdinalIgnoreCase), $"'{phrase}' appears in: {text}");
            }

            foreach (var (term, from) in NotBefore.Where(n => at < OrderOf(n.From)))
            {
                Assert.False(text.Contains(term, StringComparison.OrdinalIgnoreCase), $"'{term}' appears before {from} in: {text}");
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
            var quest = page.Replace('_', ' ').Replace(" (Quest)", string.Empty, StringComparison.Ordinal);
            if (!QuestTitles.Contains(quest)) // a quest's own title (such as Shadows of the First) is not a name page
            {
                Assert.DoesNotContain(NeverLink, bad => page.Contains(bad, StringComparison.OrdinalIgnoreCase));
            }

            if (OrderOf(checkpoint) < OrderOf(Cp255))
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

    // ---- NDL-009: arc A4, The Black Wolf's Challenge ----

    private static readonly string[] ArcEntities =
    [
        "evt-black-wolfs-challenge", "evt-operation-archon", "char-cid", "char-gaius", "char-livia", "char-lahabrea", "org-eorzean-alliance",
    ];

    private static readonly string[] ArcSpokes =
    [
        "p-minfilia-a4", "p-thancred-a4", "p-alphinaud-a4", "p-scions-a4", "p-cid-a4", "p-gaius-a4", "p-livia-a4", "p-lahabrea-a4", "p-alliance-a4",
    ];

    private static readonly string[] ArchonEdges = ["rel-alliance-in-archon", "rel-scions-in-archon", "rel-cid-in-archon", "p-archon-a4"];

    /// <summary>What stays at the milestones: the arc's cast edges, which never end.</summary>
    private static readonly string[] ArcEdgesAtMilestones = [.. ArcSpokes, .. ArchonEdges];

    private static readonly string[] Backfill = ["rel-minfilia-leads-scions-a4", "rel-thancred-member-scions-a4", "rel-alphinaud-member-scions-a4"];

    private static readonly string[] BaselineEntities = ["char-minfilia", "char-thancred", "char-alphinaud", "org-scions", "char-cid", "char-gaius", "char-livia", "char-lahabrea"];

    private static readonly string[] ArcCast155 = [.. BaselineEntities, "evt-black-wolfs-challenge", "org-eorzean-alliance"];

    private static readonly string[] During155To159 = [.. Backfill, "rel-thancred-possessed-lahabrea", .. ArcSpokes];

    // ---- NDL-012: A Realm Reborn 2.0, MSQ #102–#154 ----

    /// <summary>The 25 entities NDL-012 adds (5 arc entries and 20 others); each stays visible through both milestones.</summary>
    private static readonly string[] ArrEntities =
    [
        "evt-road-to-titan", "evt-fall-of-the-waking-sands", "evt-search-for-the-enterprise", "evt-garudas-barrier", "evt-road-to-castrum-centri",
        "char-yda", "char-papalymo", "char-titan", "char-rhitahtyn", "char-noraxia", "char-iliud", "char-marques", "char-garuda", "char-francel",
        "char-haurchefant", "char-guillaime", "char-drillemont", "char-biggs", "char-wedge", "char-glaumunt",
        "org-company-of-heroes", "org-garlean-empire", "org-house-haillenarte", "org-ixal", "loc-castrum-centri",
    ];

    /// <summary>Pilot entities that NDL-012 makes visible before 2.0, so they now also show at the A4 steps.</summary>
    private static readonly string[] EarlierPilotEntities = ["char-yshtola", "char-urianger", "char-tataru", "loc-waking-sands"];

    /// <summary>NDL-012 relationships that never end: the five arcs' cast edges and the open-ended relationships.</summary>
    private static readonly string[] ArrLasting =
    [
        "p-yshtola-b1", "p-company-of-heroes-b1", "p-titan-b1", "p-rhitahtyn-b1", "p-lahabrea-b1", "p-garlean-empire-b1", "p-minfilia-b2",
        "p-scions-b2", "p-waking-sands-b2", "p-livia-b2", "p-garlean-empire-b2", "p-noraxia-b2", "p-iliud-b2", "p-marques-b2", "p-alphinaud-b2",
        "p-cid-b2", "p-alphinaud-b3", "p-cid-b3", "p-garuda-b3", "p-ixal-b3", "p-guillaime-b3", "p-francel-b3", "p-house-haillenarte-b3",
        "p-haurchefant-b3", "p-drillemont-b3", "p-lahabrea-b3", "p-cid-b4", "p-alphinaud-b4", "p-garuda-b4", "p-ixal-b4", "p-titan-b4", "p-gaius-b4",
        "p-garlean-empire-b4", "p-scions-b4", "p-alphinaud-b5", "p-cid-b5", "p-yda-b5", "p-yshtola-b5", "p-minfilia-b5", "p-scions-b5",
        "p-castrum-centri-b5", "p-biggs-b5", "p-wedge-b5", "p-glaumunt-b5",
        "rel-yda-member-scions", "rel-papalymo-member-scions", "rel-lahabrea-allied-empire", "rel-iliud-aids-scions", "rel-marques-revealed-cid",
        "rel-garuda-summoned-ixal", "rel-francel-member-haillenarte", "rel-haurchefant-aids-francel", "rel-drillemont-aids-alphinaud",
        "rel-biggs-serves-cid", "rel-wedge-serves-cid", "rel-glaumunt-aids-scions",
    ];

    /// <summary>Backfills of pilot triples (and Gaius's membership) that run through the A4 steps and end at 2.0.</summary>
    private static readonly string[] ArrUntil20 =
    [
        "rel-yshtola-member-scions-arr", "rel-urianger-member-scions-arr", "rel-tataru-member-scions-arr", "rel-scions-hq-waking-sands-arr",
        "rel-gaius-member-empire",
    ];

    private static readonly string[] ArrHeldAtCastrumCentri =
    [
        "rel-minfilia-held-castrum-centri", "rel-urianger-held-castrum-centri", "rel-papalymo-held-castrum-centri", "rel-tataru-held-castrum-centri",
    ];

    private static readonly string[] ArrAtA4 = [.. ArrLasting, .. ArrUntil20];

    private static readonly string[] A4StepEntities = [.. ArrEntities, .. EarlierPilotEntities];

    private static readonly (string Step, string[] Entities, string[] Relationships)[] SliceSnapshots =
    [
        ("cp-msq-154", [.. BaselineEntities, .. A4StepEntities], [.. Backfill, "rel-minfilia-prisoner-livia", .. ArrAtA4, .. ArrHeldAtCastrumCentri, "rel-livia-member-empire", "rel-rhitahtyn-serves-gaius"]),
        ("cp-msq-155", [.. ArcCast155, .. A4StepEntities], [.. During155To159, .. ArrAtA4, "rel-livia-member-empire", "rel-rhitahtyn-serves-gaius"]),
        ("cp-msq-156", [.. ArcCast155, .. A4StepEntities], [.. During155To159, .. ArrAtA4, "rel-livia-member-empire", "rel-rhitahtyn-serves-gaius"]),
        ("cp-msq-157", [.. ArcCast155, "evt-operation-archon", .. A4StepEntities], [.. During155To159, "rel-livia-serves-gaius", .. ArchonEdges, .. ArrAtA4, "rel-livia-member-empire"]),
        ("cp-msq-158", [.. ArcCast155, "evt-operation-archon", .. A4StepEntities], [.. During155To159, "rel-livia-serves-gaius", .. ArchonEdges, .. ArrAtA4, "rel-livia-member-empire"]),
        ("cp-msq-159", [.. ArcCast155, "evt-operation-archon", .. A4StepEntities], [.. During155To159, "rel-livia-serves-gaius", .. ArchonEdges, .. ArrAtA4, "rel-livia-member-empire"]),
        ("cp-msq-160", [.. ArcCast155, "evt-operation-archon", .. A4StepEntities], [.. During155To159, .. ArchonEdges, .. ArrAtA4]),
    ];
}
