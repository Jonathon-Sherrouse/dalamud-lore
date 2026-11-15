using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>Player-facing copy shared by every Atlas front end, so the in-game window and the local viewer stay identical.</summary>
public static class AtlasText
{
    public const string WindowTitle = "Lore Atlas";
    public const string CeilingLabel = "Spoiler limit";
    public const string ViewLabel = "Viewing as of";
    public const string ContentViewHelp = "Includes optional story content available by the selected patch.";
    public const string ExternalLinkWarning = "External pages may contain later spoilers. The Atlas only filters what it shows itself.";
    public const string EmptyFocus = "Search or pick an entry to see its connections.";
    public const string NoResults = "No matching entries at this point in the story.";
    public const string LoadFailed = "The Lore Atlas could not load its data. Other features are unaffected.";
    public const string ConfirmRaiseButton = "Show";
    public const string CancelRaiseButton = "Cancel";
    public const string RaiseButton = "Raise…";
    public const string ContentLabel = "Content";
    public const string SearchPlaceholder = "Search names…";
    public const string ConnectionsHeading = "Connections";
    public const string NoConnections = "None at this point.";
    public const string CloseConnectionButton = "Close";
    public const string SelectedConnectionHeading = "Selected connection";
    public const string ListOnlyMarker = "(list only)";
    public const string SelectionReset = "Selection reset because the story settings changed.";

    /// <summary>Tag on records known only from optional quests (user decision, 2026-11-14).</summary>
    public const string OptionalTag = "optional";
    public const string OptionalTooltip = "Known from optional quests available by this patch.";
    public const string OptionalSummaryNote = "Includes optional quests.";

    /// <summary>Neutral confirmation: names only the checkpoint label, never what lies beyond it.</summary>
    public static string ConfirmRaise(string checkpointLabel) =>
        $"Allow story knowledge through \"{checkpointLabel}\"? The current view will not change.";

    public static string CategoryLabel(AtlasCategory category) => category switch
    {
        AtlasCategory.Character => "Character",
        AtlasCategory.Organization => "Organization",
        AtlasCategory.Location => "Location",
        AtlasCategory.Event => "Event",
        _ => "Entry",
    };

    /// <summary>Authored category glyph (no portraits or external art): every front end draws this shape.</summary>
    public static AtlasGlyph CategoryGlyph(AtlasCategory category) => category switch
    {
        AtlasCategory.Character => AtlasGlyph.Circle,
        AtlasCategory.Organization => AtlasGlyph.Square,
        AtlasCategory.Location => AtlasGlyph.Diamond,
        AtlasCategory.Event => AtlasGlyph.Hexagon,
        _ => AtlasGlyph.Circle,
    };

    /// <summary>A checkpoint beyond the spoiler limit, shown greyed in the "Viewing as of" picker.</summary>
    public static string LockedCheckpoint(string checkpointLabel) => $"{checkpointLabel} (locked)";

    /// <summary>Label of the collapsible sources section, with its count (e.g. "Sources (3)").</summary>
    public static string SourcesToggle(int count) => $"Sources ({count})";

    /// <summary>Browse-list group heading (user decision, 2026-11-14: group by category).</summary>
    public static string CategoryGroupLabel(AtlasCategory category) => category switch
    {
        AtlasCategory.Character => "Characters",
        AtlasCategory.Organization => "Organizations",
        AtlasCategory.Location => "Locations",
        AtlasCategory.Event => "Events",
        _ => "Entries",
    };

    /// <summary>The one step just beyond the spoiler limit, offered without its quest title (v2 spoiler rule 1).</summary>
    public const string NextStoryStep = "the next story step";

    /// <summary>Changes-lens heading for a step contiguous with the previous one.</summary>
    public const string ChangesThisQuest = "What this quest changed";

    /// <summary>Changes-lens heading across a gap in the covered steps.</summary>
    public static string ChangesSince(string previousPoint) => $"Changes since {previousPoint}";

    /// <summary>Label above an arc's reviewed recap, naming the step it covers.</summary>
    public static string RecapThrough(string questOrPoint) => $"Story so far, through {questOrPoint}";

    /// <summary>Marker for an explicitly picked arc viewed after it ended.</summary>
    public static string ArcAsOf(string lastQuest) => $"As of {lastQuest}";

    public const string NoArcHere = "No story arc covers this point.";
    public const string FollowBeforeCoverage = "Your completed story is before the points covered here.";
    public const string FollowUnknown = "Progress unavailable.";

    /// <summary>Follow's neutral raise prompt: names no quest, and the view does not move.</summary>
    public const string ConfirmRaiseToProgress = "Allow story knowledge through your completed quests? The current view will not change.";

    /// <summary>Only a Follow result is presented as the player's progress.</summary>
    public static string FollowProgress(string questOrPoint) => $"Your progress: through {questOrPoint}";

    /// <summary>A default or manually chosen position, never presented as "you are here".</summary>
    public static string ViewingAfter(string questOrPoint) => $"Viewing: after {questOrPoint}";

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

    /// <summary>Events and arc entries (schema v2). NDL-008 finalizes its look.</summary>
    Hexagon,
}

/// <summary>Pilot-wide browsing defaults shared by every front end.</summary>
public static class AtlasDefaults
{
    /// <summary>
    /// The entry the Atlas opens on and returns to when story settings clear the focus (user decision,
    /// 2026-11-14). Ignored when it is absent or not visible. A later schema version could carry this in the data.
    /// </summary>
    public const string HomeEntityId = "org-scions";
}

/// <summary>One browse-list group: a category heading and its visible entries, in category-then-id order.</summary>
public sealed record AtlasResultGroup(AtlasCategory Category, string Label, IReadOnlyList<AtlasEntityView> Entries);

public sealed record AtlasCheckpointOption(string Id, string Label, bool IsCeiling, bool IsView, bool ViewSelectable);

/// <summary>
/// UI-agnostic Atlas browser state: spoiler controls, content view, search, focus and relationship selection.
/// Every front end (the Dalamud window and the local viewer) renders this object and calls its methods;
/// no front end keeps its own browsing logic. Not thread-safe; callers serialize access.
/// </summary>
public sealed class AtlasSession
{
    private AtlasSnapshot snapshot;

    public AtlasSession(
        AtlasDataset dataset,
        AtlasSpoilerState initialState,
        AtlasContentView contentView = AtlasContentView.MainAndOptional,
        string? homeEntityId = AtlasDefaults.HomeEntityId)
    {
        Dataset = dataset ?? throw new ArgumentNullException(nameof(dataset));
        SpoilerState = AtlasSpoilerPolicy.Restore(dataset, initialState?.CeilingId, initialState?.ViewId);
        ContentView = contentView;
        HomeEntityId = homeEntityId;
        snapshot = Project();
        FocusHome();
    }

    /// <summary>The entry focused on open and after story-setting changes, when visible. See <see cref="AtlasDefaults"/>.</summary>
    public string? HomeEntityId { get; }

    /// <summary>
    /// True after a story-setting change (limit, view or content view) reset a search, focus or selection the
    /// player had made, until their next browsing action. Front ends show <see cref="AtlasText.SelectionReset"/>.
    /// </summary>
    public bool SelectionWasReset { get; private set; }

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

    /// <summary>The neutral confirmation for <see cref="PendingCeiling"/>; it never names a quest beyond the limit.</summary>
    public string? PendingCeilingPrompt => PendingCeiling is { } pending ? AtlasText.ConfirmRaise(RaiseLabel(pending)) : null;

    /// <summary>A checkpoint's label as shown in pickers and prompts: real at or below the limit or for milestones.</summary>
    private string RaiseLabel(AtlasCheckpoint checkpoint)
    {
        Dataset.TryGetCheckpoint(SpoilerState.CeilingId, out var ceiling);
        return checkpoint.Order <= ceiling.Order || checkpoint.Milestone ? checkpoint.Label : AtlasText.NextStoryStep;
    }

    /// <summary>
    /// A requested ceiling awaiting confirmation, or null. Internal: the checkpoint carries its label and quest title,
    /// which may lie above the limit; front ends use <see cref="PendingCeilingId"/> and <see cref="PendingCeilingPrompt"/>.
    /// </summary>
    private AtlasCheckpoint? PendingCeiling { get; set; }

    /// <summary>The id of the ceiling awaiting confirmation, or null.</summary>
    public string? PendingCeilingId => PendingCeiling?.Id;

    /// <summary>Raised when persisted spoiler state changes, so the host can save it.</summary>
    public event Action<AtlasSpoilerState>? SpoilerStateChanged;

    public IReadOnlyList<AtlasCheckpointOption> CheckpointOptions
    {
        get
        {
            // v2 spoiler rule 1: above the limit, only neutral milestones and one unnamed "next story step" are listed,
            // so no quest title beyond the limit ever reaches a picker.
            Dataset.TryGetCheckpoint(SpoilerState.CeilingId, out var ceiling);
            return Dataset.Checkpoints
                .Where(c => c.Order <= ceiling.Order || c.Milestone || c.Order == ceiling.Order + 1)
                .Select(c => new AtlasCheckpointOption(c.Id, RaiseLabel(c), c.Id == SpoilerState.CeilingId, c.Id == SpoilerState.ViewId, c.Order <= ceiling.Order))
                .ToList();
        }
    }

    public IReadOnlyList<AtlasEntityView> SearchResults => snapshot.Search(SearchQuery);

    /// <summary>Search results grouped by category, omitting empty groups (user decision, 2026-11-14).</summary>
    public IReadOnlyList<AtlasResultGroup> SearchResultGroups =>
        SearchResults
            .GroupBy(e => e.Category)
            .Select(g => new AtlasResultGroup(g.Key, AtlasText.CategoryGroupLabel(g.Key), g.ToList()))
            .ToList();

    public AtlasEntityView? Focus => snapshot.FindEntity(FocusId);

    public AtlasNeighborhood? Neighborhood => snapshot.GetNeighborhood(FocusId);

    public AtlasGraphLayout? Layout => Neighborhood is { } neighborhood ? AtlasGraphLayout.Compute(neighborhood) : null;

    public AtlasRelationshipView? SelectedRelationship =>
        Neighborhood?.Neighbors.FirstOrDefault(n => n.Relationship.Id == SelectedRelationshipId)?.Relationship;

    public void SetSourcesExpanded(bool expanded) => SourcesExpanded = expanded;

    public void SetSearch(string? query)
    {
        SelectionWasReset = false;
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
        SelectionWasReset = false;
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
        SelectionWasReset = false;
        return true;
    }

    public void ClearSelection()
    {
        SelectedRelationshipId = null;
        SelectionWasReset = false;
    }

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
        Reproject();
    }

    private void Apply(AtlasStateResult result)
    {
        if (result.Change != AtlasStateChange.Changed)
        {
            return;
        }

        SpoilerState = result.State;
        Reproject();
        SpoilerStateChanged?.Invoke(SpoilerState);
    }

    /// <summary>Re-project after a story-setting change: clear transient state, then return to the home entry.</summary>
    private void Reproject()
    {
        var hadPlayerState = SearchQuery.Length > 0
            || (FocusId is not null && FocusId != HomeEntityId)
            || SelectedRelationshipId is not null;
        SearchQuery = string.Empty;
        FocusId = null;
        SelectedRelationshipId = null;
        PendingCeiling = null;
        snapshot = Project();
        FocusHome();
        SelectionWasReset = hadPlayerState;
    }

    private void FocusHome()
    {
        if (snapshot.FindEntity(HomeEntityId) is not null)
        {
            FocusId = HomeEntityId;
        }
    }

    private AtlasSnapshot Project() => AtlasProjector.Project(Dataset, SpoilerState.ViewId, ContentView);
}
