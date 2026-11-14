using System.Text.Json.Nodes;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

public class ProjectionTests
{
    private static readonly AtlasDataset Sample = Fx.SampleDataset();

    [Theory]
    [InlineData("cp-early", AtlasContentView.MainStory, 10, 8)]
    [InlineData("cp-early", AtlasContentView.MainAndOptional, 10, 10)]
    [InlineData("cp-later", AtlasContentView.MainStory, 12, 10)]
    [InlineData("cp-later", AtlasContentView.MainAndOptional, 12, 13)]
    public void Projection_ExpectedCounts(string checkpoint, AtlasContentView view, int entities, int relationships)
    {
        // Same shape as the council-checked pilot counts: 10 → 12 entities; 8 → 10 main, 10 → 13 full relationships.
        var snapshot = Fx.Project(Sample, checkpoint, view);
        Assert.Equal(entities, snapshot.Entities.Count);
        Assert.Equal(relationships, snapshot.Relationships.Count);
    }

    [Fact]
    public void Projection_ExpectedEntitySets()
    {
        string[] early = { "char-ada", "char-bren", "char-corin", "char-ilse", "char-maren", "char-pell", "char-quill", "char-tobin", "org-lantern-guild", "loc-old-hall" };
        var later = early.Concat(new[] { "org-wardens", "loc-new-hall" }).ToArray();
        foreach (var view in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
        {
            Assert.Equal(early.OrderBy(x => x), Fx.Ids(Fx.Project(Sample, Fx.Early, view).Entities).OrderBy(x => x));
            Assert.Equal(later.OrderBy(x => x), Fx.Ids(Fx.Project(Sample, Fx.Later, view).Entities).OrderBy(x => x));
        }
    }

    [Fact]
    public void Projection_EntitiesOrderedByCategoryThenId()
    {
        var ids = Fx.Ids(Fx.Project(Sample, Fx.Later).Entities);
        Assert.Equal(new[] { "char-ada", "char-bren", "char-corin", "char-ilse", "char-maren", "char-pell", "char-quill", "char-tobin", "org-lantern-guild", "org-wardens", "loc-new-hall", "loc-old-hall" }, ids);
    }

    [Fact]
    public void Projection_EdgeEndsAtExclusiveBound()
    {
        Assert.Contains(Fx.Project(Sample, Fx.Early).Relationships, r => r.Id == "rel-guild-hq-old-hall");
        Assert.DoesNotContain(Fx.Project(Sample, Fx.Later).Relationships, r => r.Id == "rel-guild-hq-old-hall");
    }

    [Fact]
    public void Projection_EntityHiddenBeforeValidFrom()
    {
        var early = Fx.Project(Sample, Fx.Early);
        Assert.Null(early.FindEntity("org-wardens"));
        Assert.Null(early.FindEntity("loc-new-hall"));
        Assert.Null(early.GetNeighborhood("org-wardens"));
        Assert.Empty(early.Search("Wardens"));
        Assert.DoesNotContain(early.Relationships, r => r.SourceId == "org-wardens" || r.TargetId == "loc-new-hall");
    }

    [Fact]
    public void Projection_EdgeBeginsLaterWithVisibleEndpoints()
    {
        // WE-1 R11 (conceals) and WE-3 R13 (Bren's grandparent): both endpoints visible early, edge only later.
        var early = Fx.Project(Sample, Fx.Early);
        Assert.NotNull(early.FindEntity("char-quill"));
        Assert.NotNull(early.FindEntity("loc-old-hall"));
        Assert.DoesNotContain(early.Relationships, r => r.Id is "rel-quill-conceals-old-hall" or "rel-bren-grandchild-corin");
        Assert.Contains(Fx.Project(Sample, Fx.Later).Relationships, r => r.Id == "rel-quill-conceals-old-hall");
    }

    [Fact]
    public void Projection_HiddenCountsNotDisclosed()
    {
        var neighborhood = Fx.Project(Sample, Fx.Early).GetNeighborhood("loc-old-hall")!;
        Assert.Single(neighborhood.Neighbors); // only the guild's base edge; the later "conceals" edge is absent
        Assert.Empty(neighborhood.OverflowEntities);
    }

    [Fact]
    public void Projection_SelectsPresentationForViewCheckpoint()
    {
        Assert.Contains("guiding it from the Old Hall", Fx.Project(Sample, Fx.Early).FindEntity("char-maren")!.Summary);
        Assert.Contains("Whereabouts unknown", Fx.Project(Sample, Fx.Later).FindEntity("char-maren")!.Summary);
    }

    [Fact]
    public void Projection_ReverseViewingDoesNotBackfill()
    {
        // Ceiling at cp-later, view at cp-early: exactly the early text and citations.
        var session = new AtlasSession(Sample, new AtlasSpoilerState(Fx.Later, Fx.Early));
        var hall = session.Snapshot.FindEntity("loc-old-hall")!;
        Assert.Equal("The guild's base, raided once and then reclaimed.", hall.Summary);
        Assert.DoesNotContain(hall.Citations, c => c.Title == "Sample Quest: Shelter in the Snow");
    }

    [Fact]
    public void Projection_CitationWithoutUrlIsAllowed()
    {
        var citations = Fx.Project(Sample, Fx.Early).FindEntity("char-ada")!.Citations;
        Assert.Contains(citations, c => c.Title == "Sample Quest: Two Travelers" && c.Url is null);
    }

    [Fact]
    public void Search_MatchesOnlyVisibleNamesAndAliases()
    {
        Assert.Empty(Fx.Project(Sample, Fx.Early).Search("New"));
        Assert.Equal(new[] { "loc-new-hall" }, Fx.Ids(Fx.Project(Sample, Fx.Later).Search("new")));
        Assert.Equal(new[] { "char-tobin" }, Fx.Ids(Fx.Project(Sample, Fx.Early).Search("lamplighter")));
        Assert.Empty(Fx.Project(Sample, Fx.Early).Search("raided")); // summaries are not searched
        Assert.Equal(10, Fx.Project(Sample, Fx.Early).Search("   ").Count);
    }

    [Fact]
    public void Projection_EdgeVisibleFromFirstCheckpoint()
    {
        foreach (var checkpoint in new[] { Fx.Early, Fx.Later })
        {
            var snapshot = Fx.Project(Sample, checkpoint);
            var fromBren = snapshot.GetNeighborhood("char-bren")!.Neighbors.Single(n => n.Relationship.Id == "rel-bren-twin-ada");
            var fromAda = snapshot.GetNeighborhood("char-ada")!.Neighbors.Single(n => n.Relationship.Id == "rel-bren-twin-ada");
            Assert.Equal(AtlasDirection.Outgoing, fromBren.Direction);
            Assert.Equal(AtlasDirection.Incoming, fromAda.Direction);
            Assert.Equal("twin of", fromBren.Label);
            Assert.Equal("twin of", fromAda.Label);
        }
    }

    [Fact]
    public void Projection_DirectionalLabels()
    {
        var snapshot = Fx.Project(Sample, Fx.Early);
        var fromGuild = snapshot.GetNeighborhood("org-lantern-guild")!.Neighbors.Single(n => n.Relationship.Id == "rel-maren-leads-guild");
        Assert.Equal(AtlasDirection.Incoming, fromGuild.Direction);
        Assert.Equal("led by", fromGuild.Label);
    }

    [Fact]
    public void Projection_NoDerivedEdges()
    {
        // WE-3: early, Bren's twin has a grandparent, but Bren's own grandparent edge only begins later.
        var neighbors = Fx.Project(Sample, Fx.Early).GetNeighborhood("char-bren")!.Neighbors.Select(n => n.Entity.Id).ToArray();
        Assert.Contains("char-ada", neighbors);
        Assert.DoesNotContain("char-corin", neighbors);
    }

    [Fact]
    public void Projection_MainScopeHidesOptionalRecords()
    {
        var main = Fx.Project(Sample, Fx.Early, AtlasContentView.MainStory);
        var full = Fx.Project(Sample, Fx.Early, AtlasContentView.MainAndOptional);
        Assert.DoesNotContain(main.Relationships, r => r.Id == "rel-ada-grandchild-corin");
        Assert.Contains(full.Relationships, r => r.Id == "rel-ada-grandchild-corin");
        Assert.Equal("The figure whose old spell is why no one remembers the newcomer.", main.FindEntity("char-corin")!.Summary);
        Assert.StartsWith("Ada's grandfather", full.FindEntity("char-corin")!.Summary);
    }

    [Fact]
    public void Projection_OptionalPresentationReplacesWholeRecord()
    {
        var corin = Fx.Project(Sample, Fx.Early, AtlasContentView.MainAndOptional).FindEntity("char-corin")!;
        Assert.Equal(new[] { "Sample Quest: The First Lantern", "Sample Side Story: The Elder's Pledge" }, corin.Citations.Select(c => c.Title));
    }

    [Fact]
    public void Projection_OptionalOnlyEntityHiddenInMainStory()
    {
        var doc = Fx.Sample();
        Fx.Entities(doc).Add(new JsonObject { ["id"] = "char-secret", ["category"] = "character", ["presentations"] = new JsonArray(Fx.Pres("Secret", Fx.Early, scope: "optional")) });
        var dataset = Fx.Load(doc);
        Assert.Null(Fx.Project(dataset, Fx.Early, AtlasContentView.MainStory).FindEntity("char-secret"));
        Assert.NotNull(Fx.Project(dataset, Fx.Early, AtlasContentView.MainAndOptional).FindEntity("char-secret"));
    }

    [Fact]
    public void Projection_NoLaterTextReachableFromEarlierSnapshot()
    {
        // Tag every record and citation that should be invisible early, then sweep every early surface for the tag.
        const string Tag = "ZZLATER";
        var doc = Fx.Sample();
        foreach (var entity in Fx.Entities(doc).Select(e => e!.AsObject()))
        {
            foreach (var p in entity["presentations"]!.AsArray().Select(p => p!.AsObject()).Where(p => (string?)p["validFrom"] == Fx.Later))
            {
                p["name"] = $"{p["name"]} {Tag}";
                p["summary"] = $"{p["summary"]} {Tag}";
                p["aliases"] = new JsonArray(p["aliases"]!.AsArray().Select(a => (JsonNode?)JsonValue.Create($"{(string?)a} {Tag}")).ToArray());
            }
        }

        void TagCitations(JsonNode? node)
        {
            foreach (var c in node!["citations"]!.AsArray().Select(c => c!.AsObject()).Where(c => (string?)c["availableAt"] == Fx.Later))
            {
                if (!((string)c["title"]!).EndsWith(Tag, StringComparison.Ordinal))
                {
                    c["title"] = $"{c["title"]} {Tag}";
                }
            }
        }

        foreach (var entity in Fx.Entities(doc))
        {
            foreach (var p in entity!["presentations"]!.AsArray())
            {
                TagCitations(p);
            }
        }

        foreach (var r in Fx.Relationships(doc))
        {
            TagCitations(r);
        }

        foreach (var type in doc["relationshipTypes"]!.AsArray().Select(t => t!.AsObject()).Where(t => (string?)t["id"] is "controls" or "turned-against" or "conceals"))
        {
            type["outgoingLabel"] = $"{type["outgoingLabel"]} {Tag}";
            type["incomingLabel"] = $"{type["incomingLabel"]} {Tag}";
        }

        var dataset = Fx.Load(doc);
        foreach (var view in new[] { AtlasContentView.MainStory, AtlasContentView.MainAndOptional })
        {
            var early = Fx.Project(dataset, Fx.Early, view);
            var text = new List<string?>();
            void Add(AtlasEntityView e)
            {
                text.AddRange(new[] { e.Id, e.Name, e.Summary });
                text.AddRange(e.Aliases);
                text.AddRange(e.Citations.SelectMany(c => new[] { c.Title, c.Url?.ToString() }));
            }

            foreach (var e in early.Entities.Concat(early.Search(Tag)))
            {
                Add(e);
                var n = early.GetNeighborhood(e.Id)!;
                foreach (var neighbor in n.Neighbors)
                {
                    Add(neighbor.Entity);
                    text.AddRange(new[] { neighbor.Label, neighbor.Relationship.OutgoingLabel, neighbor.Relationship.IncomingLabel, neighbor.Relationship.Id });
                    text.AddRange(neighbor.Relationship.Citations.SelectMany(c => new[] { c.Title, c.Url?.ToString() }));
                }

                var layout = AtlasGraphLayout.Compute(n);
                text.AddRange(layout.Edges.Select(x => x.Label));
            }

            Assert.DoesNotContain(text, s => s is not null && s.Contains(Tag, StringComparison.Ordinal));
            Assert.Contains(Fx.Project(dataset, Fx.Later, view).Entities, e => e.Summary.Contains(Tag, StringComparison.Ordinal));
        }
    }

    [Fact]
    public void Neighborhood_CanvasCapsAtEightAndListStaysComplete()
    {
        var doc = Fx.Sample();
        for (var i = 0; i < 4; i++)
        {
            Fx.Entities(doc).Add(new JsonObject { ["id"] = $"char-extra-{i}", ["category"] = "character", ["presentations"] = new JsonArray(Fx.Pres($"Extra {i}", Fx.Early)) });
            Fx.Relationships(doc).Add(Fx.Edge($"rel-extra-{i}", $"char-extra-{i}", "member-of", "org-lantern-guild"));
        }

        var neighborhood = Fx.Project(Fx.Load(doc), Fx.Early).GetNeighborhood("org-lantern-guild")!;
        Assert.Equal(12, neighborhood.Neighbors.Count);
        Assert.Equal(AtlasSnapshot.MaxCanvasNeighbors, neighborhood.CanvasEntities.Count);
        Assert.Equal(12 - AtlasSnapshot.MaxCanvasNeighbors, neighborhood.OverflowEntities.Count);
        var order = neighborhood.Neighbors.Select(n => n.Entity.Id).Distinct().ToArray();
        Assert.Equal(order.OrderBy(id => id.StartsWith("loc-") ? 2 : id.StartsWith("org-") ? 1 : 0).ThenBy(id => id, StringComparer.Ordinal), order);
    }

    [Fact]
    public void Projection_UnknownCheckpointThrows()
    {
        Assert.Throws<ArgumentException>(() => Fx.Project(Sample, "cp-nowhere"));
    }
}
