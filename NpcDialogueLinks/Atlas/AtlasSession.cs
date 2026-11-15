using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>Player-facing copy shared by every Atlas front end, so the in-game window and the local viewer stay identical.</summary>
public static class AtlasText
{
    public const string WindowTitle = "Lore Atlas";
    public const string CeilingLabel = "Knowledge approved through";
    public const string ViewLabel = "Viewing as of";
    public const string ContentViewHelp = "Includes optional story content available by the selected patch.";
    public const string ExternalLinkWarning = "External pages may contain later spoilers. The Atlas only filters what it shows itself.";
    public const string EmptyFocus = "Search or pick an entry to see its connections.";
    public const string NoResults = "No matching entries at this point in the story.";
    public const string LoadFailed = "The Lore Atlas could not load its data. Other features are unaffected.";
    public const string ConfirmRaiseButton = "Show";
    public const string CancelRaiseButton = "Cancel";

    /// <summary>Neutral confirmation: names only the checkpoint label, never what lies beyond it.</summary>
    public static string ConfirmRaise(string checkpointLabel) =>
        $"Allow story knowledge through \"{checkpointLabel}\"? The current view will not change.";

    public static string CategoryLabel(AtlasCategory category) => category switch
    {
        AtlasCategory.Character => "Character",
        AtlasCategory.Organization => "Organization",
        AtlasCategory.Location => "Location",
        _ => "Entry",
    };

    /// <summary>Authored category glyph (no portraits or external art): every front end draws this shape.</summary>
    public static AtlasGlyph CategoryGlyph(AtlasCategory category) => category switch
    {
        AtlasCategory.Character => AtlasGlyph.Circle,
        AtlasCategory.Organization => AtlasGlyph.Square,
        AtlasCategory.Location => AtlasGlyph.Diamond,
        _ => AtlasGlyph.Circle,
    };

    /// <summary>Label of the collapsible sources section, with its count (e.g. "Sources (3)").</summary>
    public static string SourcesToggle(int count) => $"Sources ({count})";

    public static string ContentViewLabel(AtlasContentView view) => view switch
    {
        AtlasContentView.MainStory => "Main story only",
        _ => "Main story + optional",
    };
}

public enum AtlasGlyph
{
    Circle,
    Square,
    Diamond,
}

public sealed record AtlasCheckpointOption(string Id, string Label, bool IsCeiling, bool IsView, bool ViewSelectable);

/// <summary>
/// UI-agnostic Atlas browser state: spoiler controls, content view, search, focus and relationship selection.
/// Every front end (the Dalamud window and the local viewer) renders this object and calls its methods;
/// no front end keeps its own browsing logic. Not thread-safe; callers serialize access.
/// </summary>
public sealed class AtlasSession
{
    private AtlasSnapshot snapshot;

    public AtlasSession(AtlasDataset dataset, AtlasSpoilerState initialState, AtlasContentView contentView = AtlasContentView.MainAndOptional)
    {
        Dataset = dataset ?? throw new ArgumentNullException(nameof(dataset));
        SpoilerState = AtlasSpoilerPolicy.Restore(dataset, initialState?.CeilingId, initialState?.ViewId);
        ContentView = contentView;
        snapshot = Project();
    }

    public AtlasDataset Dataset { get; }

    public AtlasSpoilerState SpoilerState { get; private set; }

    public AtlasContentView ContentView { get; private set; }

    public AtlasSnapshot Snapshot => snapshot;

    public string SearchQuery { get; private set; } = string.Empty;

    public string? FocusId { get; private set; }

    public string? SelectedRelationshipId { get; private set; }

    /// <summary>
    /// Whether the details' sources sections are open. Collapsed by default (user decision, 2026-11-14), so
    /// sources stay out of the way until asked for. One setting covers entity and connection sources; it lasts
    /// for the session and is never persisted, so every new session starts collapsed.
    /// </summary>
    public bool SourcesExpanded { get; private set; }

    /// <summary>A requested ceiling awaiting confirmation, or null.</summary>
    public AtlasCheckpoint? PendingCeiling { get; private set; }

    /// <summary>Raised when persisted spoiler state changes, so the host can save it.</summary>
    public event Action<AtlasSpoilerState>? SpoilerStateChanged;

    public IReadOnlyList<AtlasCheckpointOption> CheckpointOptions
    {
        get
        {
            Dataset.TryGetCheckpoint(SpoilerState.CeilingId, out var ceiling);
            return Dataset.Checkpoints
                .Select(c => new AtlasCheckpointOption(c.Id, c.Label, c.Id == SpoilerState.CeilingId, c.Id == SpoilerState.ViewId, c.Order <= ceiling.Order))
                .ToList();
        }
    }

    public IReadOnlyList<AtlasEntityView> SearchResults => snapshot.Search(SearchQuery);

    public AtlasEntityView? Focus => snapshot.FindEntity(FocusId);

    public AtlasNeighborhood? Neighborhood => snapshot.GetNeighborhood(FocusId);

    public AtlasGraphLayout? Layout => Neighborhood is { } neighborhood ? AtlasGraphLayout.Compute(neighborhood) : null;

    public AtlasRelationshipView? SelectedRelationship =>
        Neighborhood?.Neighbors.FirstOrDefault(n => n.Relationship.Id == SelectedRelationshipId)?.Relationship;

    public void SetSourcesExpanded(bool expanded) => SourcesExpanded = expanded;

    public void SetSearch(string? query)
    {
        SearchQuery = (query ?? string.Empty).Length > AtlasSnapshot.MaxSearchQueryLength
            ? query![..AtlasSnapshot.MaxSearchQueryLength]
            : query ?? string.Empty;
    }

    /// <summary>Focus (or refocus) a visible entity. Returns false and changes nothing if it is not visible.</summary>
    public bool FocusOn(string? entityId)
    {
        if (snapshot.FindEntity(entityId) is null)
        {
            return false;
        }

        FocusId = entityId;
        SelectedRelationshipId = null;
        return true;
    }

    /// <summary>Select a relationship in the current neighborhood to show its details and sources.</summary>
    public bool SelectRelationship(string? relationshipId)
    {
        if (Neighborhood?.Neighbors.Any(n => n.Relationship.Id == relationshipId) != true)
        {
            return false;
        }

        SelectedRelationshipId = relationshipId;
        return true;
    }

    public void ClearSelection() => SelectedRelationshipId = null;

    /// <summary>Request a new ceiling. Raising it sets <see cref="PendingCeiling"/> until confirmed or cancelled.</summary>
    public AtlasStateChange RequestCeiling(string? checkpointId)
    {
        PendingCeiling = null;
        var result = AtlasSpoilerPolicy.SetCeiling(Dataset, SpoilerState, checkpointId, confirmed: false);
        if (result.Change == AtlasStateChange.NeedsConfirmation)
        {
            Dataset.TryGetCheckpoint(checkpointId, out var pending);
            PendingCeiling = pending;
        }

        Apply(result);
        return result.Change;
    }

    public AtlasStateChange ConfirmPendingCeiling()
    {
        if (PendingCeiling is null)
        {
            return AtlasStateChange.None;
        }

        var result = AtlasSpoilerPolicy.SetCeiling(Dataset, SpoilerState, PendingCeiling.Id, confirmed: true);
        PendingCeiling = null;
        Apply(result);
        return result.Change;
    }

    public void CancelPendingCeiling() => PendingCeiling = null;

    public AtlasStateChange SetView(string? checkpointId)
    {
        PendingCeiling = null;
        var result = AtlasSpoilerPolicy.SetView(Dataset, SpoilerState, checkpointId);
        Apply(result);
        return result.Change;
    }

    /// <summary>Switch between main-story-only and main-plus-optional records. Clears transient state like a checkpoint change.</summary>
    public void SetContentView(AtlasContentView view)
    {
        if (view == ContentView)
        {
            return;
        }

        ContentView = view;
        ResetTransient();
        snapshot = Project();
    }

    private void Apply(AtlasStateResult result)
    {
        if (result.Change != AtlasStateChange.Changed)
        {
            return;
        }

        SpoilerState = result.State;
        ResetTransient();
        snapshot = Project();
        SpoilerStateChanged?.Invoke(SpoilerState);
    }

    private void ResetTransient()
    {
        SearchQuery = string.Empty;
        FocusId = null;
        SelectedRelationshipId = null;
        PendingCeiling = null;
    }

    private AtlasSnapshot Project() => AtlasProjector.Project(Dataset, SpoilerState.ViewId, ContentView);
}
