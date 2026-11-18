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

    [Fact]
    public void Real_EveryEntryButTheWakingSandsHasAReviewedPortrait()
    {
        // The 19 entries NDL-011 covered. NDL-012's 25 new entries have no portraits yet; they keep their shapes.
        var portraits = RealPortraits.Where(p => NdlElevenEntries.Contains(p.Key)).ToDictionary(p => p.Key, p => p.Value);
        Assert.Equal(19, portraits.Count);
        Assert.All(RealPortraits.Where(p => !NdlElevenEntries.Contains(p.Key)), p => Assert.Null(p.Value));
        Assert.Null(portraits["loc-waking-sands"]);
        Assert.All(portraits.Where(p => p.Key != "loc-waking-sands"), p =>
        {
            Assert.NotNull(p.Value);
            Assert.Equal(AtlasReviewStatus.Reviewed, p.Value!.Review);
        });
    }

    [Fact]
    public void Real_CharactersUseTripleTriadCardsAndTheTwinsShareOne()
    {
        var portraits = RealPortraits.Where(p => p.Value is not null).ToDictionary(p => p.Key, p => p.Value);
        foreach (var (id, portrait) in portraits.Where(p => p.Key.StartsWith("char-", StringComparison.Ordinal)))
        {
            Assert.InRange(portrait!.GameIcon, 87001u, 87999u);
        }

        Assert.Equal(portraits["char-alphinaud"]!.GameIcon, portraits["char-alisaie"]!.GameIcon);
        Assert.True(portraits["char-alphinaud"]!.CropX < 0.5 && portraits["char-alisaie"]!.CropX > 0.5, "Alphinaud is the card's left half, Alisaie its right.");
        Assert.Equal(17, portraits.Values.Where(p => p is not null).Select(p => p!.GameIcon).Distinct().Count());
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
