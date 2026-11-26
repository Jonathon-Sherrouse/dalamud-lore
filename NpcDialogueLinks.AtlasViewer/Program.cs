using System.Net;
using System.Text.Json;
using System.Text.Json.Serialization;
using NpcDialogueLinks;
using NpcDialogueLinks.Atlas;

// Local Atlas viewer. Usage:
//   dotnet run --project NpcDialogueLinks.AtlasViewer -- [--data <atlas.json> | --arc-sample] [--draft] [--port 5219] [--portraits <dir>]
// Defaults: the synthetic sample, Strict validation (same as the runtime), port 5219, bound to 127.0.0.1 only.
// Portraits (NDL-011) are read from a local cache filled from your own game install by tools/atlas/PortraitCache;
// without it the viewer draws category shapes, as the game does before an icon loads.

var options = ViewerOptions.Parse(args);
var host = new ViewerHost(options);
host.Reload();

var builder = WebApplication.CreateBuilder(new WebApplicationOptions
{
    ContentRootPath = AppContext.BaseDirectory,
    WebRootPath = Path.Combine(AppContext.BaseDirectory, "wwwroot"),
});
builder.WebHost.ConfigureKestrel(k => k.Listen(IPAddress.Loopback, options.Port));
builder.Logging.SetMinimumLevel(LogLevel.Warning);
var app = builder.Build();

var json = new JsonSerializerOptions
{
    PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
    Converters = { new JsonStringEnumConverter(JsonNamingPolicy.CamelCase) },
};

app.UseDefaultFiles();
app.UseStaticFiles();
app.MapGet("/api/state", () => Results.Json(host.State(), json));
app.MapPost("/api/action", async (HttpRequest request) =>
{
    var action = await JsonSerializer.DeserializeAsync<ViewerAction>(request.Body, json);
    return Results.Json(host.Apply(action), json);
});
app.MapPost("/api/reload", () => Results.Json(host.Reload(), json));
app.MapGet("/portraits/{icon}.png", (uint icon) =>
    host.PortraitFile(icon) is { } file ? Results.File(file, "image/png") : Results.NotFound());

Console.WriteLine($"Lore Atlas local viewer: http://127.0.0.1:{options.Port}/");
Console.WriteLine($"Data: {options.DataPath} ({(options.Draft ? "Draft" : "Strict")} validation). State: {options.StatePath}");
Console.WriteLine($"Portraits: {options.PortraitDir} ({(Directory.Exists(options.PortraitDir) ? "found" : "missing; run tools/atlas/PortraitCache to fill it")})");
app.Run();

internal sealed record ViewerOptions(string DataPath, bool Draft, int Port, string StatePath, string PortraitDir, string UserTermsPath)
{
    public static ViewerOptions Parse(string[] args)
    {
        var data = Path.Combine(AppContext.BaseDirectory, "sample-atlas.json");
        var draft = false;
        var port = 5219;
        string? state = null;
        string? portraits = null;
        string? userTerms = null;
        for (var i = 0; i < args.Length; i++)
        {
            switch (args[i])
            {
                case "--data" when i + 1 < args.Length: data = Path.GetFullPath(args[++i]); break;
                case "--arc-sample": data = Path.Combine(AppContext.BaseDirectory, "sample-arc-atlas.json"); break;
                case "--draft": draft = true; break;
                case "--port" when i + 1 < args.Length && int.TryParse(args[i + 1], out var p): port = p; i++; break;
                case "--state" when i + 1 < args.Length: state = Path.GetFullPath(args[++i]); break;
                case "--user-terms" when i + 1 < args.Length: userTerms = Path.GetFullPath(args[++i]); break;
                case "--portraits" when i + 1 < args.Length: portraits = Path.GetFullPath(args[++i]); break;
            }
        }

        // Mirrors the plugin persisting both controls in its configuration; kept outside the repository.
        state ??= Path.Combine(DefaultFolder, "viewer-state.json");

        // Game images never enter the repository: the cache lives beside the viewer's state, outside it.
        portraits ??= Path.Combine(DefaultFolder, "portraits");
        return new ViewerOptions(data, draft, port, state, portraits, userTerms ?? Path.Combine(DefaultFolder, "user-terms.json"));
    }

    public static string DefaultFolder =>
        Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "NpcDialogueLinks.AtlasViewer");
}

internal sealed record ViewerAction(string Type, string? Value);

internal sealed record SavedState(string? CeilingId, string? ViewId, AtlasDictionaryPreference DictionaryPreviews);

/// <summary>Hosts one AtlasSession, the same way the plugin window will: load, guard, persist, render.</summary>
internal sealed class ViewerHost(ViewerOptions options)
{
    private readonly object gate = new();
    private readonly Dictionary<uint, (int Width, int Height)?> portraitSizes = new();
    private readonly TermDictionary dictionary = new(Path.Combine(AppContext.BaseDirectory, "terms.json"),
        options.UserTermsPath, (ex, message) => Console.Error.WriteLine($"[atlas] {message}: {ex.Message}"));
    private AtlasDictionaryPreference dictionaryPreviews;
    private bool dictionaryWarningOpen;
    private AtlasSession? session;
    private string? loadError;

    public object Reload()
    {
        lock (gate)
        {
            // Same boundary as the plugin: the loader never throws; failure yields a generic message, details to the log.
            var result = AtlasLoader.LoadFile(options.DataPath, options.Draft ? AtlasValidationMode.Draft : AtlasValidationMode.Strict);
            if (!result.Success)
            {
                session = null;
                loadError = AtlasText.LoadFailed;
                Console.Error.WriteLine($"[atlas] load failed with {result.Errors.Count} error(s):");
                foreach (var error in result.Errors)
                {
                    Console.Error.WriteLine($"[atlas]   {error.Code} at {error.Path}: {error.Message}");
                }

                return StateCore();
            }

            var contentView = session?.ContentView ?? AtlasContentView.MainAndOptional;
            var saved = ReadSaved();
            dictionaryPreviews = saved?.DictionaryPreviews ?? AtlasDictionaryPreference.Unacknowledged;
            dictionaryWarningOpen = false;
            dictionary.Reload();
            session = new AtlasSession(result.Dataset!, new AtlasSpoilerState(saved?.CeilingId ?? string.Empty, saved?.ViewId ?? string.Empty), contentView);
            session.SpoilerStateChanged += Save;
            Save(session.SpoilerState); // persist the revalidated state, as the plugin will after content updates
            loadError = null;
            return StateCore();
        }
    }

    public object State()
    {
        lock (gate)
        {
            return StateCore();
        }
    }

    public object Apply(ViewerAction? action)
    {
        lock (gate)
        {
            if (session is not null && action is not null)
            {
                switch (action.Type)
                {
                    case "toggleDictionary":
                        dictionaryPreviews = AtlasDictionaryOptions.Toggle(dictionaryPreviews);
                        dictionaryWarningOpen = dictionaryPreviews == AtlasDictionaryPreference.Unacknowledged;
                        Save(session.SpoilerState);
                        break;
                    case "confirmDictionary":
                        dictionaryPreviews = AtlasDictionaryOptions.Confirm(dictionaryPreviews, dictionaryWarningOpen);
                        dictionaryWarningOpen = false;
                        Save(session.SpoilerState);
                        break;
                    case "cancelDictionary": dictionaryWarningOpen = false; break;
                    case "search": session.SetSearch(action.Value); break;
                    case "focus": session.FocusOn(action.Value); break;
                    case "selectRelationship": session.SelectRelationship(action.Value); break;
                    case "clearSelection": session.ClearSelection(); break;
                    case "requestCeiling": session.RequestCeiling(action.Value); break;
                    case "confirmCeiling": session.ConfirmPendingCeiling(); break;
                    case "cancelCeiling": session.CancelPendingCeiling(); break;
                    case "setView": session.SetView(action.Value); break;
                    case "setSourcesExpanded": session.SetSourcesExpanded(action.Value == "true"); break;
                    case "setContentView":
                        session.SetContentView(action.Value == "mainStory" ? AtlasContentView.MainStory : AtlasContentView.MainAndOptional);
                        break;
                    case "setLens":
                        if (Enum.TryParse<AtlasLens>(action.Value, ignoreCase: true, out var lens))
                        {
                            session.SetLens(lens);
                        }

                        break;
                    case "pickArc": session.PickArc(string.IsNullOrEmpty(action.Value) ? null : action.Value); break;
                    case "showWholeCast": session.ShowWholeCast(); break;
                    case "selectChange": session.SelectChange(action.Value); break;
                }
            }

            return StateCore();
        }
    }

    private object StateCore()
    {
        var mode = options.Draft ? "draft" : "strict";
        if (session is null)
        {
            return new { ok = false, mode, error = loadError ?? AtlasText.LoadFailed };
        }

        var s = session;
        return new
        {
            ok = true,
            mode,
            dictionaryEnabled = dictionaryPreviews == AtlasDictionaryPreference.Enabled,
            dictionaryWarningOpen,
            portraitStyle = new
            {
                nodeRadius = AtlasPortraitStyle.NodeRadius,
                focusRadius = AtlasPortraitStyle.FocusRadius,
                ringWidth = AtlasPortraitStyle.RingWidth,
                badgeRadius = AtlasPortraitStyle.BadgeRadius,
                badgeOffset = AtlasPortraitStyle.BadgeOffset,
                headerSize = AtlasPortraitStyle.HeaderSize,
                minNodePixels = AtlasPortraitStyle.MinNodePixels,
                minFocusPixels = AtlasPortraitStyle.MinFocusPixels,
            },
            chartStyle = new
            {
                ringFraction = AtlasChartStyle.RingFraction,
                labelPositions = AtlasChartStyle.LabelPositions,
                nameMaxWidth = AtlasChartStyle.NameMaxWidth,
                centreNameMaxWidth = AtlasChartStyle.CentreNameMaxWidth,
                centreNameRingWidth = AtlasChartStyle.CentreNameRingWidth,
                clearance = AtlasChartStyle.Clearance,
                labelOffsets = AtlasChartStyle.LabelOffsets,
                nameOverlapWeight = AtlasChartStyle.NameOverlapWeight,
                nodeOverlapWeight = AtlasChartStyle.NodeOverlapWeight,
                labelOverlapWeight = AtlasChartStyle.LabelOverlapWeight,
                portraitObstacleScale = AtlasChartStyle.PortraitObstacleScale,
                diamondExtent = AtlasChartStyle.DiamondExtent,
                hexagonExtent = AtlasChartStyle.HexagonExtent,
                centreNameMinWidth = AtlasChartStyle.CentreNameMinWidth,
                fewNodesNameMaxWidth = AtlasChartStyle.FewNodesNameMaxWidth,
                fewNodesThreshold = AtlasChartStyle.FewNodesThreshold,
                browseFraction = AtlasChartStyle.BrowseFraction,
                browseMin = AtlasChartStyle.BrowseMin,
                browseMax = AtlasChartStyle.BrowseMax,
                detailsFraction = AtlasChartStyle.DetailsFraction,
                detailsMin = AtlasChartStyle.DetailsMin,
                detailsMax = AtlasChartStyle.DetailsMax,
            },
            text = new
            {
                title = AtlasText.WindowTitle,
                dictionaryLabel = AtlasDictionaryOptions.Label,
                dictionaryWarning = AtlasDictionaryOptions.Warning,
                dictionaryEnable = AtlasDictionaryOptions.Enable,
                dictionaryCancel = AtlasDictionaryOptions.Cancel,
                dictionaryClose = AtlasDictionaryOptions.CloseEntry,
                ceilingLabel = AtlasText.CeilingLabel,
                viewLabel = AtlasText.ViewLabel,
                contentViewHelp = AtlasText.ContentViewHelp(s.ContentView),
                externalLinkWarning = AtlasText.ExternalLinkWarning,
                emptyFocus = AtlasText.EmptyFocus,
                noResults = AtlasText.NoResults,
                confirmButton = AtlasText.ConfirmRaiseButton,
                cancelButton = AtlasText.CancelRaiseButton,
                raiseButton = AtlasText.RaiseButton,
                contentLabel = AtlasText.ContentLabel,
                searchPlaceholder = AtlasText.SearchPlaceholder,
                connectionsHeading = AtlasText.ConnectionsHeading,
                noConnections = AtlasText.NoConnections,
                closeConnection = AtlasText.CloseConnectionButton,
                selectedConnectionHeading = AtlasText.SelectedConnectionHeading,
                listOnly = AtlasText.ListOnlyMarker,
                selectionReset = AtlasText.SelectionReset,
                optionalTag = AtlasText.OptionalTag,
                optionalTooltip = AtlasText.OptionalTooltip,
                optionalSummaryNote = AtlasText.OptionalSummaryNote,
                lensHeading = AtlasText.LensLabelHeading,
                arcPickerLabel = AtlasText.ArcPickerLabel,
                wholeCast = AtlasText.WholeCastButton,
                noArc = AtlasText.NoArcHere,
                arcEnded = AtlasText.ArcEndedHeading,
                arcNothingNew = AtlasText.ArcNothingNew,
                arcNothingEnded = AtlasText.ArcNothingEnded,
                noChanges = AtlasText.NoChanges,
                changesNotOffered = AtlasText.ChangesNotOffered,
                changesPickHint = AtlasText.ChangesPickHint,
                eventCategory = AtlasText.CategoryLabel(AtlasCategory.Event),
            },
            lens = s.Lens,
            lenses = s.LensOptions.Select(l => new { id = l.Lens, l.Label, l.IsCurrent }),
            position = s.PositionLabel,
            coverage = s.CoverageNote,
            arc = s.Lens == AtlasLens.Arc
                ? new
                {
                    picker = s.ArcPickerOptions.Select(o => new { id = o.ArcId, o.Label, o.IsCurrent, o.Detail, o.Group }),
                    pickerGrouped = s.ArcPickerGrouped,
                    wholeCast = s.ShowsWholeCast,
                    castHeading = s.CastHeading,
                    view = s.Arc is { } a
                        ? new
                        {
                            a.ArcId,
                            entry = EntityDetails(a.Entry),
                            recapLabel = a.RecapLabel,
                            asOf = a.AsOfLabel,
                            newHeading = s.ArcNewHeading,
                            newRows = s.ArcNewRows.Select(Row),
                            endedRows = s.ArcEndedRows.Select(Row),
                        }
                        : null,
                }
                : null,
            changes = s.Lens == AtlasLens.Changes
                ? new
                {
                    offered = s.ChangesOffered,
                    label = s.ChangesLabel,
                    groups = s.ChangeGroups.Select(g => new { g.Kind, g.Label, rows = g.Rows.Select(Row) }),
                    selected = s.SelectedChange is { } c ? Row(c) : null,
                    selectedStatus = s.SelectedChangeStatus,
                }
                : null,
            checkpoints = s.CheckpointOptions.Select(c => new
            {
                c.Id,
                c.Label,
                c.IsCeiling,
                c.IsView,
                c.ViewSelectable,
                lockedLabel = AtlasText.LockedCheckpoint(c.Label),
            }),
            contentView = s.ContentView,
            contentViews = new[] { AtlasContentView.MainAndOptional, AtlasContentView.MainStory }
                .Select(v => new { id = v, label = AtlasText.ContentViewLabel(v) }),
            pendingCeiling = s.PendingCeilingId is { } pendingId ? new { Id = pendingId, prompt = s.PendingCeilingPrompt } : null,
            sourcesExpanded = s.SourcesExpanded,
            selectionWasReset = s.SelectionWasReset,
            search = s.SearchQuery,
            groups = s.SearchResultGroups.Select(g => new
            {
                g.Label,
                entries = g.Entries.Select(e => new { e.Id, e.Name, glyph = AtlasText.CategoryGlyph(e.Category), portrait = Portrait(e.Portrait) }),
            }),
            focus = s.Focus is { } focus ? EntityDetails(focus) : null,
            neighbors = s.Neighborhood?.Neighbors.Select(n => new
            {
                entityId = n.Entity.Id,
                entityName = n.Entity.Name,
                category = AtlasText.CategoryLabel(n.Entity.Category),
                relationshipId = n.Relationship.Id,
                label = n.Label,
                direction = n.Direction,
                symmetric = n.Relationship.Symmetric,
                optional = n.Relationship.IsOptional,
                onCanvas = s.Neighborhood!.CanvasEntities.Any(c => c.Id == n.Entity.Id),
            }),
            layout = s.Layout is { } layout
                ? new
                {
                    nodes = layout.Nodes.Select(n => new { id = n.Entity.Id, name = n.Entity.Name, glyph = AtlasText.CategoryGlyph(n.Entity.Category), n.X, n.Y, n.IsFocus, hasPortrait = n.Entity.Portrait is not null, portrait = Portrait(n.Entity.Portrait) }),
                    edges = layout.Edges.Select(e => new { relationshipId = e.Relationship.Id, e.FromId, e.ToId, e.Label, e.Symmetric, e.LaneIndex, e.LaneCount, optional = e.Relationship.IsOptional, participation = e.IsParticipation }),
                }
                : null,
            selectedRelationship = s.SelectedRelationship is { } r
                ? new { r.Id, source = s.Snapshot.FindEntity(r.SourceId)!.Name, target = s.Snapshot.FindEntity(r.TargetId)!.Name, label = r.OutgoingLabel, optional = r.IsOptional, citations = Citations(r.Citations), sourcesLabel = AtlasText.SourcesToggle(r.Citations.Count) }
                : null,
        };
    }

    private object EntityDetails(AtlasEntityView entity) => new
    {
        entity.Id,
        portrait = Portrait(entity.Portrait),
        entity.Name,
        category = AtlasText.CategoryLabel(entity.Category),
        aliases = entity.Aliases,
        entity.Summary,
        summaryLinks = dictionaryPreviews == AtlasDictionaryPreference.Enabled ? dictionary.FindAtlasLinks(entity.Summary) : null,
        glyph = AtlasText.CategoryGlyph(entity.Category),
        includesOptional = entity.IncludesOptional,
        citations = Citations(entity.Citations),
        sourcesLabel = AtlasText.SourcesToggle(entity.Citations.Count),
    };

    /// <summary>A Changes or Arc-lens row. End evidence is present only on a Changes "ended" row (the core enforces it).</summary>
    private object Row(AtlasChangeRow row) => new
    {
        row.Key,
        row.Kind,
        row.Text,
        sourceId = row.Source?.Id,
        sourceName = row.Source?.Name,
        label = row.Relationship?.OutgoingLabel,
        targetId = row.Target?.Id,
        targetName = row.Target?.Name,
        optional = row.Relationship?.IsOptional ?? false,
        endedIn = row.EndedInLabel,
        citations = row.Relationship is { } r ? Citations(r.Citations) : null,
        sourcesLabel = row.Relationship is { } r2 ? AtlasText.SourcesToggle(r2.Citations.Count) : null,
        endCitations = Citations(row.EndCitations),
        endSourcesLabel = AtlasText.EndSourcesToggle(row.EndCitations.Count),
        entity = row.Entity is { } e ? EntityDetails(e) : null,
    };

    /// <summary>The cached image for a portrait's icon, if the cache has it. Only icons named in the loaded data are served.</summary>
    public string? PortraitFile(uint icon)
    {
        lock (gate)
        {
            // The core files are compiled into the viewer, so it can see every entity, not only the visible ones.
            if (session is null || !session.Dataset.Entities.Any(e => e.Portrait?.GameIcon == icon))
            {
                return null;
            }
        }

        var file = Path.Combine(options.PortraitDir, $"{icon}.png");
        return File.Exists(file) ? file : null;
    }

    /// <summary>
    /// A portrait as the page draws it: the cached image and the crop as texture coordinates, from the same
    /// <see cref="AtlasPortrait.Uv"/> the window uses. Null without a portrait or a cached image, so the page draws the shape.
    /// </summary>
    private object? Portrait(AtlasPortrait? portrait)
    {
        if (portrait?.Asset is { } asset)
        {
            var file = Path.Combine(AppContext.BaseDirectory, "wwwroot", "atlas-portraits", $"{asset}.png");
            if (!File.Exists(file))
            {
                return null;
            }

            // Bundled assets are already squared at authoring time.
            var (left, top, right, bottom) = portrait.Uv(1, 1);
            return new { url = $"/atlas-portraits/{asset}.png", u0 = left, v0 = top, u1 = right, v1 = bottom };
        }

        if (portrait is null || PortraitSize(portrait.GameIcon) is not { } size)
        {
            return null;
        }

        var (u0, v0, u1, v1) = portrait.Uv(size.Width, size.Height);
        return new { url = $"/portraits/{portrait.GameIcon}.png", u0, v0, u1, v1 };
    }

    /// <summary>The cached PNG's pixel size, read from its header once.</summary>
    private (int Width, int Height)? PortraitSize(uint icon)
    {
        if (portraitSizes.TryGetValue(icon, out var known))
        {
            return known;
        }

        (int, int)? size = null;
        try
        {
            var file = Path.Combine(options.PortraitDir, $"{icon}.png");
            if (File.Exists(file))
            {
                using var stream = File.OpenRead(file);
                var header = new byte[24];
                if (stream.Read(header, 0, 24) == 24 && header[12] == (byte)'I' && header[13] == (byte)'H')
                {
                    size = (System.Buffers.Binary.BinaryPrimitives.ReadInt32BigEndian(header.AsSpan(16)), System.Buffers.Binary.BinaryPrimitives.ReadInt32BigEndian(header.AsSpan(20)));
                }
            }
        }
        catch (IOException)
        {
        }

        // Only a found image is remembered, so filling the cache while the viewer runs takes effect on the next request.
        if (size is not null)
        {
            portraitSizes[icon] = size;
        }

        return size;
    }

    private static object Citations(IReadOnlyList<AtlasCitationView> citations) =>
        citations.Select(c => new { c.Title, url = c.Url?.AbsoluteUri });

    private SavedState? ReadSaved()
    {
        try
        {
            return File.Exists(options.StatePath)
                ? JsonSerializer.Deserialize<SavedState>(File.ReadAllText(options.StatePath))
                : null;
        }
        catch (Exception ex) when (ex is IOException or JsonException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine($"[atlas] saved viewer state unreadable ({ex.GetType().Name}); using defaults.");
            return null;
        }
    }

    private void Save(AtlasSpoilerState state)
    {
        try
        {
            Directory.CreateDirectory(Path.GetDirectoryName(options.StatePath)!);
            File.WriteAllText(options.StatePath, JsonSerializer.Serialize(new SavedState(state.CeilingId, state.ViewId, dictionaryPreviews)));
        }
        catch (Exception ex) when (ex is IOException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine($"[atlas] could not save viewer state ({ex.GetType().Name}).");
        }
    }
}
