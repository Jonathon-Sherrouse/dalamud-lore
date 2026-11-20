using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>Portraits (NDL-011): the schema field, its validation and review, the shared crop, and the real data.</summary>
public class PortraitTests
{
    private static JsonObject Portrait(uint icon = 87046, double x = 0.5, double y = 0.4, double size = 0.75, string review = "reviewed") =>
        new()
        {
            ["gameIcon"] = icon,
            ["crop"] = new JsonObject { ["x"] = x, ["y"] = y, ["size"] = size },
            ["review"] = review,
        };

    private static JsonObject WithPortrait(JsonObject portrait, string entityId = "char-maren")
    {
        var doc = Fx.Sample();
        Fx.Entity(doc, entityId)["portrait"] = portrait;
        return doc;
    }

    [Fact]
    public void Portrait_IsOptionalAndLoads()
    {
        var dataset = Fx.Load(WithPortrait(Portrait()));
        var view = Fx.Project(dataset, Fx.Early).Entities.Single(e => e.Id == "char-maren");
        Assert.Equal(new AtlasPortrait(87046, 0.5, 0.4, 0.75, AtlasReviewStatus.Reviewed), view.Portrait);
        Assert.All(Fx.Project(dataset, Fx.Early).Entities.Where(e => e.Id != "char-maren"), e => Assert.Null(e.Portrait));
    }

    [Fact]
    public void Portrait_FollowsTheEntityAcrossCheckpointsAndViews()
    {
        var dataset = Fx.Load(WithPortrait(Portrait()));
        foreach (var checkpoint in new[] { Fx.Early, Fx.Later })
        {
            foreach (var view in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
            {
                var maren = Fx.Project(dataset, checkpoint, view).Entities.SingleOrDefault(e => e.Id == "char-maren");
                if (maren is not null)
                {
                    Assert.Equal(87046u, maren.Portrait?.GameIcon);
                }
            }
        }
    }

    [Theory]
    [InlineData(0u, 0.5, 0.5, 0.5)]
    [InlineData(1_000_000u, 0.5, 0.5, 0.5)]
    [InlineData(87046u, -0.1, 0.5, 0.5)]
    [InlineData(87046u, 0.5, 1.1, 0.5)]
    [InlineData(87046u, 0.5, 0.5, 0.05)]
    [InlineData(87046u, 0.5, 0.5, 1.5)]
    public void Portrait_RejectsBadIconsAndCrops(uint icon, double x, double y, double size)
    {
        Fx.AssertFails(Fx.Try(WithPortrait(Portrait(icon, x, y, size))), AtlasErrorCode.InvalidField);
    }

    [Fact]
    public void Portrait_RejectsAMissingCropOrUnknownField()
    {
        var noCrop = Portrait();
        noCrop.Remove("crop");
        Fx.AssertFails(Fx.Try(WithPortrait(noCrop)), AtlasErrorCode.InvalidField);

        // An image file or URL is not part of the schema: portraits only ever name a game icon.
        var withFile = Portrait();
        withFile["image"] = "thancred.png";
        Fx.AssertFails(Fx.Try(WithPortrait(withFile)), AtlasErrorCode.MalformedJson);
    }

    [Fact]
    public void Portrait_PendingReviewBlocksStrictButNotDraft()
    {
        var doc = WithPortrait(Portrait(review: "pending"));
        var strict = Fx.Try(doc, AtlasValidationMode.Strict);
        Fx.AssertFails(strict, AtlasErrorCode.UnreviewedRecord);
        Assert.Contains(strict.Errors, e => e.Path.EndsWith(".portrait.review", StringComparison.Ordinal));
        Assert.True(Fx.Try(doc, AtlasValidationMode.Draft).Success);
    }

    [Fact]
    public void Uv_CentresTheSquareOnTheCrop()
    {
        // A 208 x 256 card: the side is 0.75 of the width, 156 px, centred at (104, 102.4).
        var (u0, v0, u1, v1) = new AtlasPortrait(1, 0.5, 0.4, 0.75, AtlasReviewStatus.Reviewed).Uv(208, 256);
        Assert.Equal(26.0 / 208, u0, 9);
        Assert.Equal(182.0 / 208, u1, 9);
        Assert.Equal((102.4 - 78) / 256, v0, 9);
        Assert.Equal((102.4 + 78) / 256, v1, 9);
        Assert.Equal((u1 - u0) * 208, (v1 - v0) * 256, 9); // square in pixels
    }

    [Fact]
    public void Uv_MovesTheSquareInsideTheImageWithoutShrinkingIt()
    {
        // A 1128 x 360 banner with the crop centred at the far left edge: the full-height square slides right.
        var (u0, v0, u1, v1) = new AtlasPortrait(1, 0.0, 0.5, 1.0, AtlasReviewStatus.Reviewed).Uv(1128, 360);
        Assert.Equal(0, u0, 9);
        Assert.Equal(360.0 / 1128, u1, 9);
        Assert.Equal(0, v0, 9);
        Assert.Equal(1, v1, 9);

        var right = new AtlasPortrait(1, 1.0, 0.5, 1.0, AtlasReviewStatus.Reviewed).Uv(1128, 360);
        Assert.Equal(1, right.U1, 9);
    }

    [Fact]
    public void Uv_HandlesAnUnknownSize()
    {
        Assert.Equal((0d, 0d, 1d, 1d), new AtlasPortrait(1, 0.5, 0.5, 0.5, AtlasReviewStatus.Reviewed).Uv(0, 0));
    }

    // ---- real data ----

    private static readonly AtlasDataset Real =
        AtlasLoader.LoadFile(Path.Combine(AppContext.BaseDirectory, "atlas.json"), AtlasValidationMode.Strict).Dataset!;

    private static IReadOnlyDictionary<string, AtlasPortrait?> RealPortraits =>
        Real.Entities.ToDictionary(e => e.Id, e => e.Portrait);

    private static readonly HashSet<string> NdlElevenEntries =
    [
        "char-minfilia", "char-thancred", "char-yshtola", "char-urianger", "char-alphinaud", "char-alisaie", "char-louisoix", "char-tataru",
        "org-scions", "org-crystal-braves", "loc-waking-sands", "loc-rising-stones", "evt-black-wolfs-challenge", "evt-operation-archon",
        "char-cid", "char-gaius", "char-livia", "char-lahabrea", "org-eorzean-alliance",
    ];

    /// <summary>
    /// Entries without a portrait (2026-11-19): the Waking Sands (no usable image), entries with no faithful image in the
    /// game data, Hydaelyn (her only card shows a later form), and two disguise identities whose faces would give them away.
    /// </summary>
    private static readonly HashSet<string> NoPortrait =
    [
        "loc-waking-sands", "char-glaumunt", "char-slafborn", "char-teledji", "char-nabriales", "char-yuyuhase", "char-alianne",
        "char-wilred", "char-grinnaux", "char-zephirin", "char-dewlala", "char-guillaime", "char-iliud", "char-eline", "char-hydaelyn",
        "org-students-of-baldesion", "org-masks", "char-ivy", "char-masked-man", "char-marques",
        // Stormblood: no faithful image, or a face would give away a disguise (Shadowhunter, the enigmatic figure).
        "char-aulus", "char-bunchin", "char-curtis", "char-enigmatic-figure", "char-hakuro", "char-isse", "char-kaien", "char-maxima",
        "char-meffrid", "char-sarisha", "char-shadowhunter", "char-shanti", "char-shiosai", "char-solus", "char-soroban", "char-stark",
        "char-temulun", "char-theodoric", "char-tsuranuki", "char-wiscar", "evt-the-siege-of-specula-imperatoris", "loc-ala-ghiri",
        "loc-castellum-velodyna", "loc-castrum-oriens", "loc-house-of-the-fierce", "loc-namai", "loc-specula-imperatoris",
        "org-confederacy", "org-doman-liberation-front", "org-dotharl", "org-ferae-domitae", "org-oronir", "org-populares", "org-raen",
        "org-sekiseigumi",
        // A Realm Reborn #1–#101: minor characters and groups with no faithful image, and the masked mage (a disguise).
        "char-ahtbyrm", "char-ahtzapfyn", "char-aideen", "char-amandine", "char-baldewyn", "char-brayflox", "char-byrglaent",
        "char-dadanen", "char-drest", "char-fufulupa", "char-galfrid", "char-gegeruju", "char-ghimthota", "char-haribehrt",
        "char-hihibaru", "char-isembard", "char-ivaurault", "char-komuxio", "char-landenel", "char-laurentius", "char-leofric",
        "char-lewin", "char-lilira", "char-masked-mage", "char-medrod", "char-ourcen", "char-owyne", "char-papashan",
        "char-reyner", "char-sevrin", "char-shamani", "char-swift", "char-trachtoum", "char-ungust", "char-uodh-nunh",
        "char-ursandel", "char-vorsaile", "char-wystan", "evt-a-feast-at-costa-del-sol", "loc-gridania", "loc-limsa-lominsa",
        "loc-little-ala-mhigo", "loc-summerford-farms", "loc-uldah", "org-adventurers-guild", "org-brass-blades",
        "org-lambs-of-dalamud", "org-sultansworn", "org-twin-adder", "org-wood-wailers", "org-yellowjackets",
        // Shadowbringers: no faithful image, a later-expansion card only, or a face that would give away a reveal.
        "char-almet", "char-crystal-exarch", "char-fandaniel", "char-halric", "char-hyllfyr", "char-kai-shirr", "char-korutt",
        "char-sicard", "char-tesleen", "char-tristol", "char-vauthry", "char-venat", "char-white-robed-figure", "char-wrenden",
        "char-za-da", "char-zodiark", "evt-homeward-bound", "evt-the-missing-mayor", "loc-amaurot", "loc-the-first",
        "loc-the-tempest", "org-bloody-executioners", "org-children-of-the-everlasting-dark", "org-convocation-of-fourteen",
        "org-kobolds", "org-lightwardens", "org-telophoroi",
        // Endwalker: no faithful image, or a face or later form that would give a reveal away (Zero, Azdaja, Azem, the
        // watcher, Al End, Stigma-1, M-017, the knight in black).
        "char-ahewann", "char-al-end", "char-ameliance", "char-azdaja", "char-azem", "char-bloewyda", "char-doros", "char-erenville",
        "char-galuf", "char-gnaeus", "char-growingway", "char-khalzahl", "char-knight-in-black", "char-koana", "char-kokkol-dankkol",
        "char-licinia", "char-livingway", "char-m-017", "char-matsya", "char-mettius", "char-montichaigne", "char-nidhana",
        "char-stigma-1", "char-vergilia", "char-watcher", "char-wilfsunn", "char-zero", "loc-bestways-burrow", "loc-ktisis-hyperboreia",
        "loc-red-moon", "loc-tertium", "loc-the-thirteenth", "loc-tower-of-zot", "loc-tuliyollal", "loc-tural", "loc-ultima-thule",
        "org-archfiends", "org-bureau-of-the-architect", "org-iiird-legion", "org-ilsabard-contingent", "org-ist-legion", "org-meteia",
        "org-radiant-host", "org-xth-legion",
    ];

    [Fact]
    public void Real_EveryEntryButTheListedOnesHasAReviewedPortrait()
    {
        Assert.All(NdlElevenEntries.Where(id => id != "loc-waking-sands"), id => Assert.NotNull(RealPortraits[id])); // NDL-011's picks stay
        Assert.All(RealPortraits, p =>
        {
            if (NoPortrait.Contains(p.Key))
            {
                Assert.Null(p.Value);
            }
            else
            {
                Assert.NotNull(p.Value);
                Assert.Equal(AtlasReviewStatus.Reviewed, p.Value!.Review);
            }
        });
    }

    [Fact]
    public void Real_PortraitsAreCardsQuestArtOrDutyArtAndTheTwinsShareOne()
    {
        var portraits = RealPortraits.Where(p => p.Value is not null).ToDictionary(p => p.Key, p => p.Value!);
        foreach (var (id, portrait) in portraits)
        {
            // Triple Triad cards (87xxx), quest illustrations (100xxx) and duty art (112xxx): nothing else.
            Assert.True(portrait.GameIcon is (>= 87001 and <= 87999) or (>= 100000 and <= 101999) or (>= 112000 and <= 112999), $"{id}: {portrait.GameIcon}");
        }

        Assert.Equal(portraits["char-alphinaud"].GameIcon, portraits["char-alisaie"].GameIcon);
        Assert.True(portraits["char-alphinaud"].CropX < 0.5 && portraits["char-alisaie"].CropX > 0.5, "Alphinaud is the card's left half, Alisaie its right.");
    }

    [Fact]
    public void Real_PortraitsShowWhereverTheirEntityDoes()
    {
        foreach (var checkpoint in Real.Checkpoints)
        {
            foreach (var view in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
            {
                foreach (var entity in AtlasProjector.Project(Real, checkpoint.Id, view).Entities)
                {
                    Assert.Equal(RealPortraits[entity.Id], entity.Portrait);
                }
            }
        }
    }
}
