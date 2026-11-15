using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// Synthetic schema-v2 timeline for NDL-006. Every v2 rule in docs/atlas/v2-plan.md has a case here:
/// <code>
/// order: 0 s0 (baseline) · 1 s1 · 2 s2 · 3 s3 · 4 m1 (milestone) · 5 s5 (gap step) · 6 s6 (gap step after a slice) · 7 m2 (milestone)
/// arc-hold   = evt-hold,   s1..s3  (cast: ana, bo, cy, foe from s1; dee joins at s2)
/// arc-shadow = evt-shadow, s2..m1  (overlaps arc-hold; ends at a milestone; cast: bo, cy, dee, foe)
/// arc-tie    = evt-tie,    s2..s2  (nested; same start as arc-shadow, authored after it; cast: ana)
/// </code>
/// Relationships: ana is held [s0,s2) with end evidence; bo possessed [s1,s3) (starts and ends inside arc-hold);
/// cy–bo allied [s1,s2) then [s3,…) (ends and restarts); dee–bo knows [s1,s2) and [s3,m1) (ends twice);
/// cy–foe knows split by citation at s2 (no change); dee–ana knows from s0 (mid-arc joiner's prior tie);
/// zed–ana (never in a cast); newbie–bo from m1 (wider cast appearing at a milestone).
/// </summary>
internal static class V2Fx
{
    public const string Json = """
    {
      "schemaVersion": 2,
      "checkpoints": [
        { "id": "s0", "label": "After Baseline Quest", "questTitle": "Baseline Quest", "gameQuestIds": [100] },
        { "id": "s1", "label": "After Quest One", "questTitle": "Quest One", "contiguousWithPrevious": true, "gameQuestIds": [101] },
        { "id": "s2", "label": "After Quest Two", "questTitle": "Quest Two", "contiguousWithPrevious": true, "gameQuestIds": [102] },
        { "id": "s3", "label": "After Quest Three", "questTitle": "Quest Three", "contiguousWithPrevious": true, "gameQuestIds": [103] },
        { "id": "m1", "label": "Patch One complete", "milestone": true, "contiguousWithPrevious": true, "gameQuestIds": [104] },
        { "id": "s5", "label": "After Quest Nine", "questTitle": "Quest Nine", "gameQuestIds": [109] },
        { "id": "s6", "label": "After Quest Twelve", "questTitle": "Quest Twelve", "gameQuestIds": [112] },
        { "id": "m2", "label": "Patch Two complete", "milestone": true, "gameQuestIds": [200] }
      ],
      "relationshipTypes": [
        { "id": "participant-in", "outgoingLabel": "part of", "incomingLabel": "has participant", "symmetric": false },
        { "id": "prisoner-of", "outgoingLabel": "prisoner of", "incomingLabel": "holds prisoner", "symmetric": false },
        { "id": "possessed-by", "outgoingLabel": "possessed by", "incomingLabel": "possesses", "symmetric": false },
        { "id": "allied-with", "outgoingLabel": "allied with", "incomingLabel": "allied with", "symmetric": true },
        { "id": "knows", "outgoingLabel": "knows", "incomingLabel": "knows", "symmetric": true }
      ],
      "entities": [
        { "id": "char-ana", "category": "character", "presentations": [
          { "validFrom": "s0", "validUntil": "s2", "scope": "main", "name": "Ana", "summary": "Ana is held.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" },
          { "validFrom": "s2", "scope": "main", "name": "Ana", "summary": "Ana is free.", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "char-bo", "category": "character", "presentations": [
          { "validFrom": "s0", "scope": "main", "name": "Bo", "summary": "Bo.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "char-cy", "category": "character", "presentations": [
          { "validFrom": "s0", "scope": "main", "name": "Cy", "summary": "Cy.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "char-dee", "category": "character", "presentations": [
          { "validFrom": "s0", "scope": "main", "name": "Dee", "summary": "Dee.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "char-zed", "category": "character", "presentations": [
          { "validFrom": "s0", "scope": "main", "name": "Zed", "summary": "Zed.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "char-newbie", "category": "character", "presentations": [
          { "validFrom": "m1", "scope": "main", "name": "Newbie", "summary": "Newbie.", "citations": [ { "title": "Src m1", "availableAt": "m1", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "org-foe", "category": "organization", "presentations": [
          { "validFrom": "s0", "scope": "main", "name": "The Foe", "summary": "The Foe.", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "evt-hold", "category": "event", "presentations": [
          { "validFrom": "s1", "validUntil": "s3", "scope": "main", "name": "The Hold", "summary": "Recap one.", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
          { "validFrom": "s3", "scope": "main", "name": "The Hold", "summary": "Recap two.", "citations": [ { "title": "Src s3", "availableAt": "s3", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "evt-shadow", "category": "event", "presentations": [
          { "validFrom": "s2", "scope": "main", "name": "The Shadow", "summary": "Shadow recap.", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" } ] },
        { "id": "evt-tie", "category": "event", "presentations": [
          { "validFrom": "s2", "scope": "main", "name": "The Tie", "summary": "Tie recap.", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" } ] }
      ],
      "relationships": [
        { "id": "r-ana-prisoner", "source": "char-ana", "type": "prisoner-of", "target": "org-foe", "validFrom": "s0", "validUntil": "s2", "scope": "main",
          "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ],
          "endCitations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-bo-possessed", "source": "char-bo", "type": "possessed-by", "target": "org-foe", "validFrom": "s1", "validUntil": "s3", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-cy-bo-1", "source": "char-cy", "type": "allied-with", "target": "char-bo", "validFrom": "s1", "validUntil": "s2", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-cy-bo-2", "source": "char-cy", "type": "allied-with", "target": "char-bo", "validFrom": "s3", "scope": "main", "citations": [ { "title": "Src s3", "availableAt": "s3", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-dee-bo-1", "source": "char-dee", "type": "knows", "target": "char-bo", "validFrom": "s1", "validUntil": "s2", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-dee-bo-2", "source": "char-dee", "type": "knows", "target": "char-bo", "validFrom": "s3", "validUntil": "m1", "scope": "main", "citations": [ { "title": "Src s3", "availableAt": "s3", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-cy-foe-a", "source": "char-cy", "type": "knows", "target": "org-foe", "validFrom": "s0", "validUntil": "s2", "scope": "main", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-cy-foe-b", "source": "char-cy", "type": "knows", "target": "org-foe", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-dee-ana", "source": "char-dee", "type": "knows", "target": "char-ana", "validFrom": "s0", "scope": "main", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-zed-ana", "source": "char-zed", "type": "knows", "target": "char-ana", "validFrom": "s0", "scope": "main", "citations": [ { "title": "Src s0", "availableAt": "s0", "scope": "main" } ], "review": "reviewed" },
        { "id": "r-newbie-bo", "source": "char-newbie", "type": "knows", "target": "char-bo", "validFrom": "m1", "scope": "main", "citations": [ { "title": "Src m1", "availableAt": "m1", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-ana-hold", "source": "char-ana", "type": "participant-in", "target": "evt-hold", "validFrom": "s1", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-bo-hold", "source": "char-bo", "type": "participant-in", "target": "evt-hold", "validFrom": "s1", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-cy-hold", "source": "char-cy", "type": "participant-in", "target": "evt-hold", "validFrom": "s1", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-foe-hold", "source": "org-foe", "type": "participant-in", "target": "evt-hold", "validFrom": "s1", "scope": "main", "citations": [ { "title": "Src s1", "availableAt": "s1", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-dee-hold", "source": "char-dee", "type": "participant-in", "target": "evt-hold", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-bo-shadow", "source": "char-bo", "type": "participant-in", "target": "evt-shadow", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-cy-shadow", "source": "char-cy", "type": "participant-in", "target": "evt-shadow", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-dee-shadow", "source": "char-dee", "type": "participant-in", "target": "evt-shadow", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-foe-shadow", "source": "org-foe", "type": "participant-in", "target": "evt-shadow", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" },
        { "id": "p-ana-tie", "source": "char-ana", "type": "participant-in", "target": "evt-tie", "validFrom": "s2", "scope": "main", "citations": [ { "title": "Src s2", "availableAt": "s2", "scope": "main" } ], "review": "reviewed" }
      ],
      "arcs": [
        { "id": "arc-hold", "entityId": "evt-hold", "firstStep": "s1", "lastStep": "s3" },
        { "id": "arc-shadow", "entityId": "evt-shadow", "firstStep": "s2", "lastStep": "m1" },
        { "id": "arc-tie", "entityId": "evt-tie", "firstStep": "s2", "lastStep": "s2" }
      ]
    }
    """;

    public static JsonObject Doc() => JsonNode.Parse(Json)!.AsObject();

    public static AtlasDataset Load() => Fx.Load(Doc());

    public static JsonObject Rel(JsonObject doc, string id) => Fx.Rel(doc, id);

    public static JsonObject Arc(JsonObject doc, string id) =>
        doc["arcs"]!.AsArray().Select(a => a!.AsObject()).First(a => (string?)a["id"] == id);

    public static JsonObject Checkpoint(JsonObject doc, string id) =>
        doc["checkpoints"]!.AsArray().Select(c => c!.AsObject()).First(c => (string?)c["id"] == id);

    public static JsonObject Cite(string title, string availableAt, string scope = "main") =>
        new() { ["title"] = title, ["availableAt"] = availableAt, ["scope"] = scope };

    /// <summary>A minimal valid document with one arc whose cast is <paramref name="castSize"/> characters.</summary>
    public static JsonObject WithCast(int castSize)
    {
        var entities = new JsonArray(new JsonObject
        {
            ["id"] = "evt-big", ["category"] = "event",
            ["presentations"] = new JsonArray(Pres("s1", "The Big Event")),
        });
        var relationships = new JsonArray();
        for (var i = 1; i <= castSize; i++)
        {
            entities.Add(new JsonObject { ["id"] = $"char-m{i:00}", ["category"] = "character", ["presentations"] = new JsonArray(Pres("s0", $"Member {i:00}")) });
            relationships.Add(Edge($"p-m{i:00}", $"char-m{i:00}", "participant-in", "evt-big", "s1"));
        }

        // Two relationships between the same pair, to exercise separate lanes.
        relationships.Add(Edge("r-m01-m02-knows", "char-m01", "knows", "char-m02", "s1"));
        relationships.Add(Edge("r-m01-m02-allied", "char-m01", "allied-with", "char-m02", "s1"));
        return new JsonObject
        {
            ["schemaVersion"] = 2,
            ["checkpoints"] = new JsonArray(
                new JsonObject { ["id"] = "s0", ["label"] = "Before" },
                new JsonObject { ["id"] = "s1", ["label"] = "During", ["contiguousWithPrevious"] = true }),
            ["relationshipTypes"] = Doc()["relationshipTypes"]!.DeepClone(),
            ["entities"] = entities,
            ["relationships"] = relationships,
            ["arcs"] = new JsonArray(new JsonObject { ["id"] = "arc-big", ["entityId"] = "evt-big", ["firstStep"] = "s1", ["lastStep"] = "s1" }),
        };

        static JsonObject Pres(string from, string name) => new()
        {
            ["validFrom"] = from, ["scope"] = "main", ["name"] = name, ["summary"] = $"{name}.",
            ["citations"] = new JsonArray(Cite($"Src {from}", from)), ["review"] = "reviewed",
        };

        static JsonObject Edge(string id, string source, string type, string target, string from) => new()
        {
            ["id"] = id, ["source"] = source, ["type"] = type, ["target"] = target, ["validFrom"] = from, ["scope"] = "main",
            ["citations"] = new JsonArray(Cite($"Src {from}", from)), ["review"] = "reviewed",
        };
    }

    public static IReadOnlyList<string> Ids(IEnumerable<AtlasRelationshipView> relationships) => relationships.Select(r => r.Id).Order(StringComparer.Ordinal).ToList();

    public static IReadOnlyList<string> Ids(IEnumerable<AtlasEndedRelationship> ended) => ended.Select(e => e.Relationship.Id).ToList();
}
