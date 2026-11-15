using System.Net;
using System.Text.Json;
using System.Text.Json.Serialization;
using NpcDialogueLinks.Atlas;

// Local Atlas viewer. Usage:
//   dotnet run --project NpcDialogueLinks.AtlasViewer -- [--data <atlas.json> | --arc-sample] [--draft] [--port 5219]
// Defaults: the synthetic sample, Strict validation (same as the runtime), port 5219, bound to 127.0.0.1 only.

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

Console.WriteLine($"Lore Atlas local viewer: http://127.0.0.1:{options.Port}/");
Console.WriteLine($"Data: {options.DataPath} ({(options.Draft ? "Draft" : "Strict")} validation). State: {options.StatePath}");
app.Run();

internal sealed record ViewerOptions(string DataPath, bool Draft, int Port, string StatePath)
{
    public static ViewerOptions Parse(string[] args)
    {
        var data = Path.Combine(AppContext.BaseDirectory, "sample-atlas.json");
        var draft = false;
        var port = 5219;
        string? state = null;
        for (var i = 0; i < args.Length; i++)
        {
            switch (args[i])
            {
                case "--data" when i + 1 < args.Length: data = Path.GetFullPath(args[++i]); break;
                case "--arc-sample": data = Path.Combine(AppContext.BaseDirectory, "sample-arc-atlas.json"); break;
                case "--draft": draft = true; break;
                case "--port" when i + 1 < args.Length && int.TryParse(args[i + 1], out var p): port = p; i++; break;
                case "--state" when i + 1 < args.Length: state = Path.GetFullPath(args[++i]); break;
            }
        }

        // Mirrors the plugin persisting both controls in its configuration; kept outside the repository.
        state ??= Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "NpcDialogueLinks.AtlasViewer", "viewer-state.json");
        return new ViewerOptions(data, draft, port, state);
    }
}

internal sealed record ViewerAction(string Type, string? Value);

internal sealed record SavedState(string? CeilingId, string? ViewId);

/// <summary>Hosts one AtlasSession, the same way the plugin window will: load, guard, persist, render.</summary>
internal sealed class ViewerHost(ViewerOptions options)
{
    private readonly object gate = new();
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
            text = new
            {
                title = AtlasText.WindowTitle,
                ceilingLabel = AtlasText.CeilingLabel,
                viewLabel = AtlasText.ViewLabel,
                contentViewHelp = AtlasText.ContentViewHelp,
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
                arcNew = AtlasText.ArcNewHeading,
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
                    picker = s.ArcPickerOptions.Select(o => new { id = o.ArcId, o.Label, o.IsCurrent }),
                    wholeCast = s.ShowsWholeCast,
                    castHeading = AtlasText.CastHeading(Math.Max(0, s.Snapshot.Entities.Count - 1)),
                    view = s.Arc is { } a
                        ? new
                        {
                            a.ArcId,
                            entry = EntityDetails(a.Entry),
                            recapLabel = a.RecapLabel,
                            asOf = a.AsOfLabel,
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
                entries = g.Entries.Select(e => new { e.Id, e.Name, glyph = AtlasText.CategoryGlyph(e.Category) }),
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
                    nodes = layout.Nodes.Select(n => new { id = n.Entity.Id, name = n.Entity.Name, glyph = AtlasText.CategoryGlyph(n.Entity.Category), n.X, n.Y, n.IsFocus }),
                    edges = layout.Edges.Select(e => new { relationshipId = e.Relationship.Id, e.FromId, e.ToId, e.Label, e.Symmetric, e.LaneIndex, e.LaneCount, optional = e.Relationship.IsOptional, participation = e.IsParticipation }),
                }
                : null,
            selectedRelationship = s.SelectedRelationship is { } r
                ? new { r.Id, source = s.Snapshot.FindEntity(r.SourceId)!.Name, target = s.Snapshot.FindEntity(r.TargetId)!.Name, label = r.OutgoingLabel, optional = r.IsOptional, citations = Citations(r.Citations), sourcesLabel = AtlasText.SourcesToggle(r.Citations.Count) }
                : null,
        };
    }

    private static object EntityDetails(AtlasEntityView entity) => new
    {
        entity.Id,
        entity.Name,
        category = AtlasText.CategoryLabel(entity.Category),
        aliases = entity.Aliases,
        entity.Summary,
        glyph = AtlasText.CategoryGlyph(entity.Category),
        includesOptional = entity.IncludesOptional,
        citations = Citations(entity.Citations),
        sourcesLabel = AtlasText.SourcesToggle(entity.Citations.Count),
    };

    /// <summary>A Changes or Arc-lens row. End evidence is present only on a Changes "ended" row (the core enforces it).</summary>
    private static object Row(AtlasChangeRow row) => new
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
            File.WriteAllText(options.StatePath, JsonSerializer.Serialize(new SavedState(state.CeilingId, state.ViewId)));
        }
        catch (Exception ex) when (ex is IOException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine($"[atlas] could not save viewer state ({ex.GetType().Name}).");
        }
    }
}
