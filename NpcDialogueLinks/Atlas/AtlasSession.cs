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

    // ---- v2 lenses (NDL-008) ----

    public const string LensLabelHeading = "Lens";

    public static string LensLabel(AtlasLens lens) => lens switch
    {
        AtlasLens.Arc => "Arc",
        AtlasLens.Changes => "Changes",
        _ => "Story point",
    };

    /// <summary>Shared coverage line on slice (non-milestone) steps (v2 plan, "Coverage note").</summary>
    public const string CoverageNote = "This point covers only the characters involved in this part of the story.";

    public const string ArcPickerLabel = "Story arc";

    /// <summary>The arc picker's first option: follow the default selection for the current view.</summary>
    public const string ArcAutomatic = "The arc at this point";

    public const string WholeCastButton = "Whole cast";

    public static string CastHeading(int count) => $"Cast ({count})";

    public const string ArcNewHeading = "New at this point";
    public const string ArcEndedHeading = "Ended so far in this arc";
    public const string ArcNothingNew = "Nothing new at this point.";
    public const string ArcNothingEnded = "Nothing has ended yet.";

    /// <summary>When an ended row's relationship ended (a step at or below the view).</summary>
    public static string EndedIn(string questOrPoint) => $"ended in {questOrPoint}";

    public const string ChangesAdded = "Added";
    public const string ChangesEnded = "Ended";
    public const string ChangesUpdated = "Description updated";
    public const string NoChanges = "Nothing changed at this point.";
    public const string ChangesNotOffered = "Changes compare one quest step with the one before it, or one milestone with the previous milestone. There is no comparison for this point.";
    public const string ChangesPickHint = "Pick a change to see its details.";

    /// <summary>Label of the collapsible end-evidence section, shown only on a Changes "ended" row.</summary>
    public static string EndSourcesToggle(int count) => $"Sources for the ending ({count})";
}

/// <summary>What the window shows (v2 plan, "Product shape"). Follow is deferred (user decision, 2026-11-14).</summary>
public enum AtlasLens
{
    Arc,
    StoryPoint,
    Changes,
}

public sealed record AtlasLensOption(AtlasLens Lens, string Label, bool IsCurrent);

/// <summary>One arc-picker row. <see cref="ArcId"/> null is the automatic choice.</summary>
public sealed record AtlasArcPickerOption(string? ArcId, string Label, bool IsCurrent);

public enum AtlasChangeKind
{
    Added,
    Ended,
    Updated,
}

/// <summary>
/// One row of the Changes lens or the Arc lens's lists. A relationship row has <see cref="Relationship"/> with its
/// endpoints; an updated-description row has <see cref="Entity"/>. <see cref="EndCitations"/> is non-empty only on a
/// Changes "ended" row, the one surface allowed to show end evidence (v2 spoiler rule 2).
/// </summary>
public sealed record AtlasChangeRow(
    string Key,
    AtlasChangeKind Kind,
    AtlasRelationshipView? Relationship,
    AtlasEntityView? Source,
    AtlasEntityView? Target,
    AtlasEntityView? Entity,
    IReadOnlyList<AtlasCitationView> EndCitations,
    string? EndedInLabel = null)
{
    /// <summary>"Source label Target" for relationship rows; the entity's name otherwise.</summary>
    public string Text => Relationship is { } r ? $"{Source!.Name} {r.OutgoingLabel} {Target!.Name}" : Entity!.Name;
}

public sealed record AtlasChangeGroup(AtlasChangeKind Kind, string Label, IReadOnlyList<AtlasChangeRow> Rows);

public enum AtlasGlyph
{
    Circle,
    Square,
    Diamond,

    /// <summary>Events and arc entries (schema v2): a flat-topped hexagon in violet (NDL-008).</summary>
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
/// UI-agnostic Atlas browser state: spoiler controls, content view, lens, arc selection, search, focus and
/// relationship or change selection. Every front end (the Dalamud window and the local viewer) renders this object
/// and calls its methods; no front end keeps its own browsing logic. Not thread-safe; callers serialize access.
/// </summary>
/// <remarks>
/// <see cref="Snapshot"/> is what browsing works over: the projected view in Story point and Changes, and the arc's
/// cast-filtered snapshot at its effective step in the Arc lens, so search, counts, connections and refocus never
/// leave the cast (v2 plan, "Arc lens").
/// </remarks>
public sealed class AtlasSession
{
    private AtlasSnapshot snapshot;
    private string? explicitArcId;

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
        Reproject(storySettingChanged: false);
    }

    // ---- lenses ----

    /// <summary>
    /// The current lens. Until the player picks one, it follows the default rule for the current view: Arc when an arc
    /// contains the view, Story point otherwise. An explicit pick lasts for the session and is never persisted.
    /// </summary>
    public AtlasLens Lens { get; private set; }

    /// <summary>True once the player picked a lens; the default rule then no longer applies this session.</summary>
    public bool LensIsExplicit { get; private set; }

    public IReadOnlyList<AtlasLensOption> LensOptions =>
        new[] { AtlasLens.Arc, AtlasLens.StoryPoint, AtlasLens.Changes }
            .Select(l => new AtlasLensOption(l, AtlasText.LensLabel(l), l == Lens))
            .ToList();

    /// <summary>"Viewing: after ‹quest›": the chosen point, never "you are here" (v2 plan, "Honest positioning").</summary>
    public string PositionLabel => AtlasText.ViewingAfter(ViewCheckpoint.DisplayTitle);

    /// <summary>The coverage line on slice steps; null on milestones.</summary>
    public string? CoverageNote => ViewCheckpoint.Milestone ? null : AtlasText.CoverageNote;

    /// <summary>Pick a lens explicitly. It clears search, focus and selection, like any change of what is shown.</summary>
    public void SetLens(AtlasLens lens)
    {
        LensIsExplicit = true;
        if (lens == Lens)
        {
            return;
        }

        Lens = lens;
        Reproject(storySettingChanged: false);
    }

    // ---- Arc lens ----

    /// <summary>The arc shown by the Arc lens (the explicit pick, else the default), or null when none applies.</summary>
    public AtlasArcView? Arc { get; private set; }

    /// <summary>The arc picker: the automatic choice, then every arc started by the view, named as of its effective step.</summary>
    public IReadOnlyList<AtlasArcPickerOption> ArcPickerOptions
    {
        get
        {
            var options = new List<AtlasArcPickerOption> { new(null, AtlasText.ArcAutomatic, explicitArcId is null) };
            options.AddRange(AtlasArcs.Eligible(Dataset, SpoilerState.ViewId, ContentView)
                .Select(a => new AtlasArcPickerOption(a.ArcId, a.Name, a.ArcId == explicitArcId)));
            return options;
        }
    }

    /// <summary>True in the Arc lens while no entity is focused: the whole-cast chart and the arc panel show.</summary>
    public bool ShowsWholeCast => Lens == AtlasLens.Arc && Arc is not null && FocusId is null;

    /// <summary>Relationships new at the arc's effective step, as rows (no end evidence).</summary>
    public IReadOnlyList<AtlasChangeRow> ArcNewRows =>
        Arc is { } arc ? arc.New.Select(r => RelationshipRow(AtlasChangeKind.Added, r, arc.Cast)).ToList() : Array.Empty<AtlasChangeRow>();

    /// <summary>"Ended so far in this arc", as rows. Never carries sources of any kind (v2 plan, "Arc lens").</summary>
    public IReadOnlyList<AtlasChangeRow> ArcEndedRows =>
        Arc is { } arc
            ? arc.EndedSoFar.Select(e => new AtlasChangeRow(
                $"ended:{e.Relationship.Id}", AtlasChangeKind.Ended, e.Relationship, e.Source, e.Target, null,
                Array.Empty<AtlasCitationView>(), EndedInFor(e.EndedAtCheckpointId))).ToList()
            : Array.Empty<AtlasChangeRow>();

    /// <summary>Pick an arc, or null for the automatic choice. Only arcs started by the view can be picked.</summary>
    public bool PickArc(string? arcId)
    {
        if (arcId is not null && AtlasArcs.Eligible(Dataset, SpoilerState.ViewId, ContentView).All(a => a.ArcId != arcId))
        {
            return false;
        }

        explicitArcId = arcId;
        Reproject(storySettingChanged: false);
        return true;
    }

    /// <summary>Back to the whole-cast chart after refocusing a character in the Arc lens.</summary>
    public void ShowWholeCast()
    {
        if (Lens != AtlasLens.Arc)
        {
            return;
        }

        FocusId = null;
        SelectedRelationshipId = null;
        SelectionWasReset = false;
    }

    // ---- Changes lens ----

    /// <summary>Whether the Changes lens has a comparison at the view (same-kind steps, from the second step on).</summary>
    public bool ChangesOffered => AtlasChanges.IsOffered(Dataset, SpoilerState.ViewId);

    /// <summary>"What this quest changed" or "Changes since ‹previous point›"; null where Changes is not offered.</summary>
    public string? ChangesLabel => AtlasChanges.Label(Dataset, SpoilerState.ViewId);

    /// <summary>The Changes lens rows, grouped Added / Ended / Description updated, omitting empty groups.</summary>
    public IReadOnlyList<AtlasChangeGroup> ChangeGroups
    {
        get
        {
            if (AtlasChanges.At(Dataset, SpoilerState.ViewId, ContentView) is not { } diff)
            {
                return Array.Empty<AtlasChangeGroup>();
            }

            var after = Project();
            var groups = new List<AtlasChangeGroup>
            {
                new(AtlasChangeKind.Added, AtlasText.ChangesAdded, diff.Added.Select(r => RelationshipRow(AtlasChangeKind.Added, r, after)).ToList()),
                new(AtlasChangeKind.Ended, AtlasText.ChangesEnded, diff.Ended.Select(e => new AtlasChangeRow(
                    $"ended:{e.Relationship.Id}", AtlasChangeKind.Ended, e.Relationship, e.Source, e.Target, null, e.EndCitations)).ToList()),
                new(AtlasChangeKind.Updated, AtlasText.ChangesUpdated, diff.DescriptionUpdated.Select(e => new AtlasChangeRow(
                    $"updated:{e.Id}", AtlasChangeKind.Updated, null, null, null, e, Array.Empty<AtlasCitationView>())).ToList()),
            };
            return groups.Where(g => g.Rows.Count > 0).ToList();
        }
    }

    public string? SelectedChangeKey { get; private set; }

    public AtlasChangeRow? SelectedChange =>
        SelectedChangeKey is null ? null : ChangeGroups.SelectMany(g => g.Rows).FirstOrDefault(r => r.Key == SelectedChangeKey);

    public bool SelectChange(string? key)
    {
        if (Lens != AtlasLens.Changes || key is null || ChangeGroups.SelectMany(g => g.Rows).All(r => r.Key != key))
        {
            return false;
        }

        SelectedChangeKey = key;
        SelectionWasReset = false;
        return true;
    }

    private AtlasCheckpoint ViewCheckpoint
    {
        get
        {
            Dataset.TryGetCheckpoint(SpoilerState.ViewId, out var view);
            return view;
        }
    }

    private static AtlasChangeRow RelationshipRow(AtlasChangeKind kind, AtlasRelationshipView r, AtlasSnapshot endpoints) =>
        new($"{kind.ToString().ToLowerInvariant()}:{r.Id}", kind, r, endpoints.FindEntity(r.SourceId), endpoints.FindEntity(r.TargetId), null, Array.Empty<AtlasCitationView>());

    private string EndedInFor(string checkpointId)
    {
        Dataset.TryGetCheckpoint(checkpointId, out var ended);
        return AtlasText.EndedIn(ended.DisplayTitle);
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

    /// <summary>The whole-cast chart in the Arc lens with nothing focused; otherwise the focus's one-hop graph.</summary>
    public AtlasGraphLayout? Layout =>
        ShowsWholeCast ? AtlasGraphLayout.ComputeWholeCast(snapshot, Arc!.Entry.Id)
        : Neighborhood is { } neighborhood ? AtlasGraphLayout.Compute(neighborhood)
        : null;

    public AtlasRelationshipView? SelectedRelationship =>
        SelectedRelationshipId is null ? null
        : ShowsWholeCast ? snapshot.Relationships.FirstOrDefault(r => r.Id == SelectedRelationshipId)
        : Neighborhood?.Neighbors.FirstOrDefault(n => n.Relationship.Id == SelectedRelationshipId)?.Relationship;

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

    /// <summary>Select a relationship on the current chart (the neighborhood, or the whole cast) to show its details and sources.</summary>
    public bool SelectRelationship(string? relationshipId)
    {
        var onChart = ShowsWholeCast
            ? snapshot.Relationships.Any(r => r.Id == relationshipId)
            : Neighborhood?.Neighbors.Any(n => n.Relationship.Id == relationshipId) == true;
        if (!onChart)
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
        Reproject(storySettingChanged: true);
    }

    private void Apply(AtlasStateResult result)
    {
        if (result.Change != AtlasStateChange.Changed)
        {
            return;
        }

        SpoilerState = result.State;
        Reproject(storySettingChanged: true);
        SpoilerStateChanged?.Invoke(SpoilerState);
    }

    /// <summary>
    /// Re-project after anything changes what is shown: apply the default lens rule, resolve the arc (ending an explicit
    /// pick whose first step is now after the view), rebuild the browsing snapshot, clear transient state, and return to
    /// the lens's resting focus. Only a story-setting change (limit, view, content view) raises the reset hint.
    /// </summary>
    private void Reproject(bool storySettingChanged)
    {
        var hadPlayerState = SearchQuery.Length > 0
            || (FocusId is not null && FocusId != RestingFocus())
            || SelectedRelationshipId is not null
            || SelectedChangeKey is not null;
        SearchQuery = string.Empty;
        FocusId = null;
        SelectedRelationshipId = null;
        SelectedChangeKey = null;
        PendingCeiling = null;

        if (!LensIsExplicit)
        {
            Lens = AtlasArcs.Default(Dataset, SpoilerState.ViewId) is not null ? AtlasLens.Arc : AtlasLens.StoryPoint;
        }

        var resolution = AtlasArcs.Resolve(Dataset, SpoilerState.ViewId, explicitArcId);
        if (resolution.PickDropped)
        {
            explicitArcId = null;
        }

        Arc = resolution.ArcId is { } arcId ? AtlasArcs.Project(Dataset, arcId, SpoilerState.ViewId, ContentView) : null;
        snapshot = Lens != AtlasLens.Arc ? Project()
            : Arc is { } arc ? arc.Cast
            : Project().Filter(new HashSet<string>(StringComparer.Ordinal));
        FocusId = RestingFocus();
        SelectionWasReset = storySettingChanged && hadPlayerState;
    }

    /// <summary>Where each lens rests: the home entry in Story point (when visible); nothing in Arc (the whole cast) and Changes.</summary>
    private string? RestingFocus() =>
        Lens == AtlasLens.StoryPoint && snapshot.FindEntity(HomeEntityId) is not null ? HomeEntityId : null;

    private AtlasSnapshot Project() => AtlasProjector.Project(Dataset, SpoilerState.ViewId, ContentView);
}
