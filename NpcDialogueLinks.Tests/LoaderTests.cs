using System.Text;
using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

public class LoaderTests
{
    [Fact]
    public void Sample_PassesStrictValidation()
    {
        var result = AtlasLoader.LoadFile(Fx.SamplePath, AtlasValidationMode.Strict);
        Assert.True(result.Success, string.Join("\n", result.Errors));
    }

    [Fact]
    public void Loader_MissingFileFailsWithoutThrowing()
    {
        var result = AtlasLoader.LoadFile(Path.Combine(Path.GetTempPath(), $"missing-{Guid.NewGuid():N}.json"), AtlasValidationMode.Strict);
        Fx.AssertFails(result, AtlasErrorCode.MissingFile);
    }

    [Theory]
    [InlineData("")]
    [InlineData("not json")]
    [InlineData("[]")]
    [InlineData("{\"schemaVersion\":1,")]
    [InlineData("{\"schemaVersion\":1, /* comment */ \"checkpoints\":[]}")]
    [InlineData("{\"schemaVersion\":1,\"schemaVersion\":1}")]
    public void Loader_MalformedJsonFailsWithoutThrowing(string json)
    {
        var result = AtlasLoader.LoadJson(json, AtlasValidationMode.Strict);
        Assert.False(result.Success);
        Assert.Contains(result.Errors, e => e.Code is AtlasErrorCode.MalformedJson or AtlasErrorCode.UnsupportedSchemaVersion);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(2)]
    public void Loader_RejectsUnsupportedSchemaVersion(int version)
    {
        var doc = Fx.Sample();
        doc["schemaVersion"] = version;
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.UnsupportedSchemaVersion);
    }

    [Fact]
    public void Loader_RejectsUnknownProperty()
    {
        var doc = Fx.Sample();
        Fx.Entity(doc, "char-maren")["portrait"] = "maren.png";
        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.MalformedJson);
    }

    [Fact]
    public void Loader_RejectsOversizedInput()
    {
        var huge = "{\"schemaVersion\":1,\"pad\":\"" + new string('x', AtlasLoader.MaxFileBytes) + "\"}";
        Fx.AssertFails(AtlasLoader.LoadJson(huge, AtlasValidationMode.Strict), AtlasErrorCode.TooLarge);
    }

    [Fact]
    public void Loader_RejectsTooManyEntities()
    {
        var doc = Fx.Sample();
        var entities = Fx.Entities(doc);
        for (var i = 0; entities.Count <= AtlasLoader.MaxEntities; i++)
        {
            entities.Add(new JsonObject { ["id"] = $"char-extra-{i}", ["category"] = "character", ["presentations"] = new JsonArray(Fx.Pres($"Extra {i}", Fx.Early)) });
        }

        Fx.AssertFails(Fx.Try(doc), AtlasErrorCode.BoundsExceeded);
    }

    [Fact]
    public void Loader_NeverThrowsOnArbitraryBytes()
    {
        var random = new Random(1234);
        for (var i = 0; i < 200; i++)
        {
            var bytes = new byte[random.Next(0, 256)];
            random.NextBytes(bytes);
            var result = AtlasLoader.LoadUtf8(bytes, AtlasValidationMode.Strict);
            Assert.False(result.Success);
        }

        // Structurally plausible but semantically broken documents also fail cleanly.
        var doc = Fx.Sample();
        doc["entities"] = new JsonArray(null, 5, "x", new JsonObject());
        Assert.False(Fx.Try(doc).Success);
        Assert.False(AtlasLoader.LoadUtf8(Encoding.UTF8.GetBytes("{\"schemaVersion\":1}"), AtlasValidationMode.Strict).Success);
    }

    [Fact]
    public void ReviewModes_DraftAllowsPendingStrictRejects()
    {
        var doc = Fx.Sample();
        Fx.Presentation(doc, "char-maren", 0)["review"] = "pending";
        Fx.Rel(doc, "rel-maren-leads-guild")["review"] = "pending";

        Assert.True(Fx.Try(doc, AtlasValidationMode.Draft).Success);
        var strict = Fx.Try(doc, AtlasValidationMode.Strict);
        Fx.AssertFails(strict, AtlasErrorCode.UnreviewedRecord);
        Assert.Equal(2, strict.Errors.Count(e => e.Code == AtlasErrorCode.UnreviewedRecord));
    }

    [Fact]
    public void Loader_AbsentOptionalFieldsEqualNull()
    {
        var doc = Fx.Sample();
        var presentation = Fx.Presentation(doc, "char-maren", 1);
        presentation.Remove("validUntil");
        presentation.Remove("aliases");
        var dataset = Fx.Load(doc);
        Assert.Empty(Fx.Project(dataset, Fx.Later).FindEntity("char-maren")!.Aliases);
    }

    [Fact]
    public void Errors_DoNotEmbedEntityIds()
    {
        // Structured errors go to the log only, but they still avoid echoing ids such as hidden entity names.
        var doc = Fx.Sample();
        Fx.Relationships(doc).Add(Fx.Edge("rel-bad", "org-wardens", "controls", "loc-old-hall"));
        var result = Fx.Try(doc);
        Assert.False(result.Success);
        Assert.DoesNotContain(result.Errors, e => e.Message.Contains("wardens", StringComparison.OrdinalIgnoreCase));
    }
}
