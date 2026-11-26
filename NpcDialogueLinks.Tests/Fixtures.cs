using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// Synthetic fixtures. The sample (sample-atlas.json, shared with the local viewer) mirrors the pilot's shape from
/// docs/atlas/worked-examples.md with invented names: cp-early ≈ cp-arr-2-0, cp-later ≈ cp-arr-2-55.
/// </summary>
internal static class Fx
{
    public const string Early = "cp-early";
    public const string Later = "cp-later";

    public static string SamplePath => Path.Combine(AppContext.BaseDirectory, "sample-atlas.json");

    public static JsonObject Sample() => JsonNode.Parse(File.ReadAllText(SamplePath))!.AsObject();

    public static AtlasLoadResult Try(JsonObject doc, AtlasValidationMode mode = AtlasValidationMode.Strict) =>
        AtlasLoader.LoadJson(doc.ToJsonString(), mode);

    public static AtlasDataset Load(JsonObject doc, AtlasValidationMode mode = AtlasValidationMode.Strict)
    {
        var result = Try(doc, mode);
        Assert.True(result.Success, "Expected a valid dataset but got:\n" + string.Join("\n", result.Errors));
        return result.Dataset!;
    }

    public static AtlasDataset SampleDataset() => Load(Sample());

    public static void AssertFails(AtlasLoadResult result, AtlasErrorCode code)
    {
        Assert.False(result.Success, $"Expected {code} but the dataset loaded.");
        Assert.Null(result.Dataset);
        Assert.Contains(result.Errors, e => e.Code == code);
    }

    public static JsonArray Entities(JsonObject doc) => doc["entities"]!.AsArray();

    public static JsonArray Relationships(JsonObject doc) => doc["relationships"]!.AsArray();

    public static JsonObject Entity(JsonObject doc, string id) =>
        Entities(doc).Select(e => e!.AsObject()).First(e => (string?)e["id"] == id);

    public static JsonObject Rel(JsonObject doc, string id) =>
        Relationships(doc).Select(r => r!.AsObject()).First(r => (string?)r["id"] == id);

    public static JsonObject Presentation(JsonObject doc, string entityId, int index) =>
        Entity(doc, entityId)["presentations"]!.AsArray()[index]!.AsObject();

    public static JsonObject Cite(string title, string availableAt = Early, string scope = "main", string? url = null) =>
        new() { ["title"] = title, ["url"] = url, ["availableAt"] = availableAt, ["scope"] = scope };

    public static JsonObject Pres(string name, string from, string? until = null, string scope = "main", string review = "reviewed", JsonObject? citation = null) =>
        new()
        {
            ["validFrom"] = from,
            ["validUntil"] = until,
            ["scope"] = scope,
            ["name"] = name,
            ["aliases"] = new JsonArray(),
            ["summary"] = $"Summary for {name}.",
            ["citations"] = new JsonArray(citation ?? DefaultCite(from, scope)),
            ["review"] = review,
        };

    public static JsonObject Edge(string id, string source, string type, string target, string from = Early, string? until = null, string scope = "main", JsonObject? citation = null) =>
        new()
        {
            ["id"] = id,
            ["source"] = source,
            ["type"] = type,
            ["target"] = target,
            ["validFrom"] = from,
            ["validUntil"] = until,
            ["scope"] = scope,
            ["citations"] = new JsonArray(citation ?? DefaultCite(from, scope)),
            ["review"] = "reviewed",
        };

    /// <summary>A citation available exactly at <paramref name="from"/>; titles are unique per (checkpoint, scope).</summary>
    public static JsonObject DefaultCite(string from, string scope = "main") => Cite($"Fixture Source {from} {scope}", from, scope);

    /// <summary>A minimal three-checkpoint document for rules that two checkpoints cannot exercise.</summary>
    public static JsonObject ThreeCheckpoints() => new()
    {
        ["schemaVersion"] = 2,
        ["checkpoints"] = new JsonArray(
            new JsonObject { ["id"] = "cp-1", ["label"] = "One" },
            new JsonObject { ["id"] = "cp-2", ["label"] = "Two" },
            new JsonObject { ["id"] = "cp-3", ["label"] = "Three" }),
        ["relationshipTypes"] = new JsonArray(new JsonObject { ["id"] = "knows", ["outgoingLabel"] = "knows", ["incomingLabel"] = "known by", ["symmetric"] = false }),
        ["entities"] = new JsonArray(
            new JsonObject { ["id"] = "char-a", ["category"] = "character", ["presentations"] = new JsonArray(Pres("A", "cp-1", citation: Cite("Src 1", "cp-1"))) },
            new JsonObject { ["id"] = "char-b", ["category"] = "character", ["presentations"] = new JsonArray(Pres("B", "cp-1", citation: Cite("Src 1", "cp-1"))) }),
        ["relationships"] = new JsonArray(),
    };

    public static AtlasSnapshot Project(AtlasDataset dataset, string checkpoint, AtlasContentView view = AtlasContentView.MainAndOptional) =>
        AtlasProjector.Project(dataset, checkpoint, view);

    public static string[] Ids(IEnumerable<AtlasEntityView> entities) => entities.Select(e => e.Id).ToArray();
}
