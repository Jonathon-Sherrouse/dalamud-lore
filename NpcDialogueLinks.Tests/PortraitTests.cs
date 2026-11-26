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

        // The schema accepts a bundled asset key or game icon, with no arbitrary file or URL.
        var withFile = Portrait();
        withFile["image"] = "thancred.png";
        Fx.AssertFails(Fx.Try(WithPortrait(withFile)), AtlasErrorCode.MalformedJson);
    }

    [Theory]
    [InlineData("char-maren", false, true)]
    [InlineData("../maren", false, false)]
    [InlineData("char-maren", true, false)]
    public void Portrait_AssetRequiresASafeKeyAndNoGameIcon(string asset, bool keepIcon, bool valid)
    {
        var portrait = Portrait();
        if (!keepIcon)
            portrait.Remove("gameIcon");
        portrait["asset"] = asset;

        var doc = WithPortrait(portrait);
        if (valid)
            Assert.Equal(asset, Fx.Project(Fx.Load(doc), Fx.Early).Entities.Single(e => e.Id == "char-maren").Portrait?.Asset);
        else
            Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.InvalidField);
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

    private static readonly HashSet<string> NoPortrait =
    [
        "loc-waking-sands", "org-students-of-baldesion", "org-masks", "evt-the-siege-of-specula-imperatoris",
        "loc-ala-ghiri", "loc-castellum-velodyna", "loc-castrum-oriens", "loc-house-of-the-fierce",
        "loc-namai", "loc-specula-imperatoris", "org-confederacy", "org-doman-liberation-front",
        "org-dotharl", "org-ferae-domitae", "org-oronir", "org-populares",
        "org-raen", "org-sekiseigumi", "evt-a-feast-at-costa-del-sol", "loc-gridania",
        "loc-limsa-lominsa", "loc-little-ala-mhigo", "loc-summerford-farms", "loc-uldah",
        "org-adventurers-guild", "org-brass-blades", "org-lambs-of-dalamud", "org-sultansworn",
        "org-twin-adder", "org-wood-wailers", "org-yellowjackets", "evt-homeward-bound",
        "evt-the-missing-mayor", "loc-amaurot", "loc-the-first", "loc-the-tempest",
        "org-bloody-executioners", "org-children-of-the-everlasting-dark", "org-convocation-of-fourteen", "org-kobolds",
        "org-lightwardens", "org-telophoroi", "loc-bestways-burrow", "loc-ktisis-hyperboreia",
        "loc-red-moon", "loc-tertium", "loc-the-thirteenth", "loc-tower-of-zot",
        "loc-tuliyollal", "loc-tural", "loc-ultima-thule", "org-archfiends",
        "org-bureau-of-the-architect", "org-iiird-legion", "org-ilsabard-contingent", "org-ist-legion",
        "org-meteia", "org-radiant-host", "org-xth-legion", "evt-the-third-promise-taken",
        "loc-brightploom-post", "loc-earthenshire", "loc-everkeep", "loc-gladr",
        "loc-mist-continent", "loc-naglfar", "loc-ok-hanu", "loc-wachunpelo",
        "loc-xak-tural", "loc-yak-tel", "loc-yyasulani", "org-daybreakers",
        "org-dustwatch", "org-endless", "org-hhetsarro", "org-jotnar",
        "org-landsguard", "org-mamool-ja", "org-milalla", "org-oblivion",
        "org-preservation", "org-winterers", "org-xbraal", "org-yok-huy",
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
        var portraits = RealPortraits.Where(p => p.Value is { Asset: null }).ToDictionary(p => p.Key, p => p.Value!);
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
