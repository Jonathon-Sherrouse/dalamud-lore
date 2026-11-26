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
    /// <summary>The footer under the panes, which describes the content view in use (council round 2).</summary>
    public static string ContentViewHelp(AtlasContentView view) => view == AtlasContentView.MainStory
        ? "Shows main story content only."
        : "Includes optional story content available by the selected story point.";
    public const string ExternalLinkWarning = "External pages may contain later spoilers. The Atlas only filters what it shows itself.";
    public const string EmptyFocus = "Search or pick an entry to see its connections.";
    public const string NoResults = "No matching entries at this point in the story.";
    public const string LoadFailed = "The Lore Atlas could not load its data. Other features are unaffected.";

    /// <summary>The Lore Explain window's single entry point into the Atlas (NDL-010). It opens the window and passes no data.</summary>
    public const string OpenAtlasButton = "Open Atlas";
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
    public const string OptionalTooltip = "Known from optional quests available by this story point.";
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

    /// <summary><see cref="NextStoryStep"/> standing alone as a picker or menu item, so it starts with a capital.</summary>
    public const string NextStoryStepOption = "The next story step";

    /// <summary>Label above an arc's reviewed recap, naming the step it covers. A milestone reads "as of ‹milestone›".</summary>
    public static string RecapThrough(AtlasCheckpoint step) =>
        step.Milestone ? $"Story so far, as of {step.Label}" : $"Story so far, through {step.DisplayTitle}";

    /// <summary>
    /// Marker for an explicitly picked arc viewed after it ended. The recap label already names the arc's last step,
    /// so this only says that the arc is over.
    /// </summary>
    public const string ArcEnded = "This arc has ended.";

    public const string NoArcHere = "No story arc covers this point.";
    public const string FollowBeforeCoverage = "Your completed story is before the points covered here.";
    public const string FollowUnknown = "Progress unavailable.";

    /// <summary>Follow's neutral raise prompt: names no quest, and the view does not move.</summary>
    public const string ConfirmRaiseToProgress = "Allow optional story lore through your completed main-scenario quests? The current view will stay where it is.";

    /// <summary>Only a Follow result is presented as the player's progress.</summary>
    public static string FollowProgress(string questOrPoint) => $"Your progress: through {questOrPoint}";

    // ---- Follow (NDL-017) ----

    public const string FollowToggle = "Follow my progress";
    public const string FollowTooltip = "Moves to your latest completed main-scenario quest. Raises the spoiler limit automatically when no new optional story would be revealed.";
    public const string FollowRefreshButton = "Refresh";
    public const string FollowReading = "Reading your progress…";

    /// <summary>Progress beyond the limit: names no quest past it, and reads sensibly beside the raise offer.</summary>
    public const string FollowBeyondLimit = "Your progress is past your spoiler limit.";
    public const string FollowRaiseButton = "Raise to my progress…";

    /// <summary>The position line when Follow placed the view at the limit because progress is beyond it.</summary>
    public static string FollowAtLimit(AtlasCheckpoint point) => $"{FollowBeyondLimit} {ViewingAt(point)}";

    /// <summary>A default or manually chosen position, never presented as "you are here".</summary>
    public static string ViewingAt(AtlasCheckpoint point) =>
        point.Milestone ? $"Viewing: {point.Label}" : $"Viewing: after {point.DisplayTitle}";

    public static string ContentViewLabel(AtlasContentView view) => view switch
    {
        AtlasContentView.MainStory => "Main story only",
        _ => "Main story + optional",
    };

    // ---- the map (NDL-018) ----

    /// <summary>Between the steps of the trail above the map.</summary>
    public const string TrailSeparator = "›";

    /// <summary>Shared coverage line on slice (non-milestone) steps (v2 plan, "Coverage note").</summary>
    public const string CoverageNote = "This point covers only the characters involved in this part of the story.";

    public const string ArcPickerLabel = "Story arc";

    /// <summary>The arc picker's first option: follow the default selection for the current view.</summary>
    public const string ArcAutomatic = "The arc at this point";

    /// <summary>Under an arc's name in the picker: where it starts. The start is always at or below the view.</summary>
    public static string ArcStartsAt(AtlasCheckpoint firstStep) =>
        firstStep.Milestone ? $"from {firstStep.Label}" : $"from {firstStep.DisplayTitle}";

    /// <summary>
    /// The picker line under an arc's name: where it starts, plus "ended" once the view is past its last step (user
    /// decision, 2026-11-16, NDL-011). Never shown before the end, so it never spoils one.
    /// </summary>
    public static string ArcPickerDetail(string startLabel, bool ended) => ended ? $"{startLabel} · ended" : startLabel;

    /// <summary>
    /// A picker group heading: the patch an arc starts in, from the label of the first milestone at or after its start
    /// ("A Realm Reborn — Patch 2.0 complete" → "A Realm Reborn — Patch 2.0").
    /// </summary>
    public static string ArcGroup(string milestoneLabel) =>
        milestoneLabel.EndsWith(" complete", StringComparison.Ordinal) ? milestoneLabel[..^" complete".Length] : milestoneLabel;

    public static string CastHeading(int count) => $"Cast ({count})";

    public const string ArcNewHeading = "New at this point";

    /// <summary>The "new" heading for a picked arc viewed after it ended: the rows are new at its last quest.</summary>
    public static string ArcNewIn(AtlasCheckpoint lastStep) =>
        lastStep.Milestone ? $"New as of {lastStep.Label}" : $"New in {lastStep.DisplayTitle}";
    public const string ArcEndedHeading = "Ended so far in this arc";
    public const string ArcNothingNew = "Nothing new.";
    public const string ArcNothingEnded = "Nothing has ended yet.";

    /// <summary>When an ended row's relationship ended (a step at or below the view).</summary>
    public static string EndedIn(AtlasCheckpoint step) =>
        step.Milestone ? $"ended by {step.Label}" : $"ended in {step.DisplayTitle}";
}

/// <summary>One arc-picker row. <see cref="ArcId"/> null is the automatic choice.</summary>
public sealed record AtlasArcPickerOption(string? ArcId, string Label, bool IsCurrent)
{
    /// <summary>"from ‹start quest›", so a player can tell where the arc sits; empty for the automatic option.</summary>
    public string Detail { get; init; } = string.Empty;

    /// <summary>The patch heading the arc is listed under; null for the automatic option.</summary>
    public string? Group { get; init; }
}

/// <summary>
/// One row of the arc panel's lists: a relationship new at the arc's effective step, or one that ended so far in the arc
/// (<see cref="EndedInLabel"/> set). Rows never carry end evidence; no surface shows it (NDL-018).
/// </summary>
public sealed record AtlasArcRow(
    string Key,
    AtlasRelationshipView Relationship,
    AtlasEntityView Source,
    AtlasEntityView Target,
    string? EndedInLabel = null)
{
    /// <summary>"Source label Target".</summary>
    public string Text => $"{Source.Name} {Relationship.OutgoingLabel} {Target.Name}";
}

/// <summary>
/// One step of the trail above the map: the entry that was in the middle, named as it is shown now. The last step is
/// the current centre. An arc entry's step opens that arc's whole cast.
/// </summary>
public sealed record AtlasTrailStep(string EntityId, string Name, bool IsArc, bool IsCurrent);

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
/// UI-agnostic Atlas browser state: spoiler controls, content view, story arc, search, the map's centre and trail, and
/// relationship selection. Every front end (the Dalamud window and the local viewer) renders this object and calls its
/// methods; no front end keeps its own browsing logic. Not thread-safe; callers serialize access.
/// </summary>
/// <remarks>
/// One map (NDL-018): whatever is in the middle decides what shows. A story arc's entry in the middle shows the arc's
/// whole cast at its effective step with the arc panel; anything else shows its one-hop connections in
/// <see cref="Snapshot"/>, the projected view, so search, connections and refocus always cover everyone.
/// </remarks>
public sealed class AtlasSession
{
    private AtlasSnapshot snapshot;
    private string? explicitArcId;
    private string approvedCeilingId;

    // The map's trail: the entries put in the middle, oldest first. The last one is the centre (FocusId).
    private readonly List<string> trail = new();

    // Derived state, built lazily and cleared whenever its inputs change (Reproject for the limit, view and content view;
    // ResolveArc for the story arc). Front ends may read these every frame without re-projecting.
    private IReadOnlyList<AtlasArcPickerOption>? arcPickerOptions;
    private IReadOnlyList<AtlasArcRow>? arcNewRows;
    private IReadOnlyList<AtlasArcRow>? arcEndedRows;
    private IReadOnlyList<AtlasTrailStep>? trailSteps;
    private AtlasGraphLayout? wholeCastLayout;

    public AtlasSession(
        AtlasDataset dataset,
        AtlasSpoilerState initialState,
        AtlasContentView contentView = AtlasContentView.MainAndOptional,
        string? homeEntityId = AtlasDefaults.HomeEntityId)
    {
        Dataset = dataset ?? throw new ArgumentNullException(nameof(dataset));
        SpoilerState = AtlasSpoilerPolicy.Restore(dataset, initialState?.CeilingId, initialState?.ViewId);
        approvedCeilingId = SpoilerState.CeilingId;
        ContentView = contentView;
        HomeEntityId = homeEntityId;
        snapshot = Project();
        Reproject(storySettingChanged: false);
    }

    // ---- position ----

    /// <summary>
    /// "Viewing: after ‹quest›", the chosen point, never "you are here" (v2 plan, "Honest positioning"). Only when Follow
    /// placed the view does it read as the player's progress.
    /// </summary>
    public string PositionLabel => !FollowedHere ? AtlasText.ViewingAt(ViewCheckpoint)
        : FollowResult!.BeyondLimit ? AtlasText.FollowAtLimit(ViewCheckpoint)
        : AtlasText.FollowProgress(ViewCheckpoint.DisplayTitle);

    /// <summary>The coverage line on slice steps; null on milestones.</summary>
    public string? CoverageNote => ViewCheckpoint.Milestone ? null : AtlasText.CoverageNote;

    // ---- story arc ----

    /// <summary>
    /// The story arc: the explicit pick while it lasts, otherwise the default (the earliest-started arc containing the
    /// view), or null when neither applies. The map rests on its entry, and the browse list shows its cast.
    /// </summary>
    public AtlasArcView? Arc { get; private set; }

    /// <summary>The arc picker: the automatic choice, then every arc started by the view, named as of its effective step.</summary>
    public IReadOnlyList<AtlasArcPickerOption> ArcPickerOptions => arcPickerOptions ??= BuildArcPickerOptions();

    /// <summary>Whether any arc has started by the view. Without one, front ends leave the picker out.</summary>
    public bool ArcPickerOffered => ArcPickerOptions.Count > 1;

    /// <summary>
    /// Whether the picker shows patch headings: only when its arcs start in more than one patch (user decision,
    /// 2026-11-15), so a single heading over everything never adds clutter.
    /// </summary>
    public bool ArcPickerGrouped => ArcPickerOptions.Where(o => o.ArcId is not null).Select(o => o.Group).Distinct().Count() > 1;

    /// <summary>"No story arc covers this point." under the picker when arcs have started but none applies here.</summary>
    public string? ArcPickerNote => ArcPickerOffered && Arc is null ? AtlasText.NoArcHere : null;

    /// <summary>"Cast (n)" above the cast list while the browse list shows it; null otherwise.</summary>
    public string? CastHeading => ShowsCastList ? AtlasText.CastHeading(CastMembers.Count) : null;

    /// <summary>"New at this point", or "New in ‹last quest›" for a picked arc viewed after it ended. Null outside the arc panel.</summary>
    public string? ArcNewHeading => ShowsWholeCast ? (Arc!.PastEnd ? AtlasText.ArcNewIn(Arc.Effective) : AtlasText.ArcNewHeading) : null;

    /// <summary>True while the story arc's entry is in the middle: the whole-cast chart and the arc panel show.</summary>
    public bool ShowsWholeCast => Arc is not null && FocusId == Arc.Entry.Id;

    /// <summary>
    /// Relationships new at the arc's effective step, as rows (no end evidence). Spokes to the arc entry are left out: a
    /// new member already shows by appearing on the chart, and listing every spoke would bury the real changes (D8).
    /// Empty outside the arc panel.
    /// </summary>
    public IReadOnlyList<AtlasArcRow> ArcNewRows => !ShowsWholeCast ? Array.Empty<AtlasArcRow>() : arcNewRows ??= Arc!.New
        .Where(r => !AtlasArcs.IsSpoke(r, Arc.Entry.Id))
        .Select(r => new AtlasArcRow($"new:{r.Id}", r, Arc.Cast.FindEntity(r.SourceId)!, Arc.Cast.FindEntity(r.TargetId)!))
        .ToList();

    /// <summary>"Ended so far in this arc", as rows. Never carries sources of any kind (v2 plan, "Arc lens"). Empty outside the arc panel.</summary>
    public IReadOnlyList<AtlasArcRow> ArcEndedRows => !ShowsWholeCast ? Array.Empty<AtlasArcRow>() : arcEndedRows ??= Arc!.EndedSoFar
        .Select(e => new AtlasArcRow($"ended:{e.Relationship.Id}", e.Relationship, e.Source, e.Target, EndedInFor(e.EndedAtCheckpointId)))
        .ToList();

    /// <summary>
    /// Pick an arc, or null for the automatic choice, and put it in the middle with a fresh trail. Only arcs started by
    /// the view can be picked. The pick holds while the view moves, until the view drops below the arc's first step.
    /// </summary>
    public bool PickArc(string? arcId)
    {
        if (arcId is not null && AtlasArcs.Eligible(Dataset, SpoilerState.ViewId, ContentView).All(a => a.ArcId != arcId))
        {
            return false;
        }

        explicitArcId = arcId;
        PendingCeiling = null;
        ResolveArc();
        Rest();
        SelectionWasReset = false;
        return true;
    }

    // ---- the map's centre and trail ----

    /// <summary>The most steps the trail keeps. Past it, the oldest step after the first is dropped.</summary>
    public const int MaxTrailSteps = 6;

    /// <summary>
    /// The trail above the map, oldest first; the last step is the centre. Empty only when nothing can be shown. It
    /// starts again at the resting centre whenever the limit, view, content view or picked arc changes. Arc entries are
    /// named as the picker names them, as of their effective step; everything else as the view shows it.
    /// </summary>
    public IReadOnlyList<AtlasTrailStep> Trail => trailSteps ??= trail.Select((id, i) =>
            ArcByEntry(id) is { } arc
                ? new AtlasTrailStep(id, ArcPickerOptions.First(o => o.ArcId == arc.Id).Label, true, i == trail.Count - 1)
                : new AtlasTrailStep(id, snapshot.FindEntity(id)?.Name ?? string.Empty, false, i == trail.Count - 1))
        .ToList();

    /// <summary>Go back to an earlier step of the trail, dropping the steps after it.</summary>
    public bool ReturnTo(int index)
    {
        if (index < 0 || index >= trail.Count - 1)
        {
            return false;
        }

        return FocusOn(trail[index]);
    }

    /// <summary>The started arc whose entry is <paramref name="entityId"/>, or null.</summary>
    private AtlasArc? ArcByEntry(string? entityId) =>
        entityId is null ? null
        : ArcPickerOptions.Where(o => o.ArcId is not null).Select(o => Dataset.Arcs.First(a => a.Id == o.ArcId)).FirstOrDefault(a => a.EntityId == entityId);

    private IReadOnlyList<AtlasArcPickerOption> BuildArcPickerOptions()
    {
        var options = new List<AtlasArcPickerOption> { new(null, AtlasText.ArcAutomatic, explicitArcId is null) };
        options.AddRange(AtlasArcs.Eligible(Dataset, SpoilerState.ViewId, ContentView)
            .Select(a => new AtlasArcPickerOption(a.ArcId, a.Name, a.ArcId == explicitArcId) { Detail = AtlasText.ArcPickerDetail(a.StartLabel, a.Ended), Group = a.Group }));
        return options;
    }

    private AtlasCheckpoint ViewCheckpoint
    {
        get
        {
            Dataset.TryGetCheckpoint(SpoilerState.ViewId, out var view);
            return view;
        }
    }

    private string EndedInFor(string checkpointId)
    {
        Dataset.TryGetCheckpoint(checkpointId, out var ended);
        return AtlasText.EndedIn(ended);
    }

    /// <summary>The entry in the middle when no story arc applies, if visible. See <see cref="AtlasDefaults"/>.</summary>
    public string? HomeEntityId { get; }

    /// <summary>
    /// True after a story-setting change (limit, view or content view) reset a search, trail or selection the player
    /// had made, until their next browsing action. Front ends show <see cref="AtlasText.SelectionReset"/>.
    /// </summary>
    public bool SelectionWasReset { get; private set; }

    public AtlasDataset Dataset { get; }

    public AtlasSpoilerState SpoilerState { get; private set; }

    public AtlasContentView ContentView { get; private set; }

    /// <summary>The projected view at the view checkpoint: what search, connections and refocus work over.</summary>
    public AtlasSnapshot Snapshot => snapshot;

    /// <summary>The snapshot the chart and the selected connection are drawn from: the arc's cast in the whole-cast chart.</summary>
    public AtlasSnapshot ChartSnapshot => ShowsWholeCast ? Arc!.Cast : snapshot;

    public string SearchQuery { get; private set; } = string.Empty;

    /// <summary>The entry in the middle of the map (the trail's last step), or null when nothing can be shown.</summary>
    public string? FocusId => trail.Count > 0 ? trail[^1] : null;

    public string? SelectedRelationshipId { get; private set; }

    /// <summary>
    /// Whether the details' sources sections are open. Collapsed by default (user decision, 2026-11-14), so
    /// sources stay out of the way until asked for. One setting covers entity and connection sources; it lasts
    /// for the session and is never persisted, so every new session starts collapsed.
    /// </summary>
    public bool SourcesExpanded { get; private set; }

    /// <summary>The neutral confirmation for <see cref="PendingCeiling"/>; it never names a quest beyond the limit.</summary>
    public string? PendingCeilingPrompt => PendingCeiling is { } pending ? AtlasText.ConfirmRaise(RaiseLabel(pending, inSentence: true)) : null;

    /// <summary>A checkpoint's label as shown in pickers and prompts: real at or below the limit or for milestones.</summary>
    private string RaiseLabel(AtlasCheckpoint checkpoint, bool inSentence = false)
    {
        Dataset.TryGetCheckpoint(SpoilerState.CeilingId, out var ceiling);
        return checkpoint.Order <= ceiling.Order || checkpoint.Milestone ? checkpoint.Label
            : inSentence ? AtlasText.NextStoryStep : AtlasText.NextStoryStepOption;
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

    /// <summary>
    /// Visible entries matching the search, from everyone. With an empty search and a story arc, the arc's cast members
    /// instead (without the arc entry, which the trail and the picker already name); a search can still find anyone.
    /// </summary>
    public IReadOnlyList<AtlasEntityView> SearchResults => ShowsCastList ? CastMembers : snapshot.Search(SearchQuery);

    private bool ShowsCastList => Arc is not null && SearchQuery.Trim().Length == 0;

    /// <summary>The story arc's members visible at the view, as the view names them, so every one can be put in the middle.</summary>
    private IReadOnlyList<AtlasEntityView> CastMembers => Arc is { } arc
        ? arc.Cast.Entities.Where(e => e.Id != arc.Entry.Id).Select(e => snapshot.FindEntity(e.Id)).OfType<AtlasEntityView>().ToList()
        : Array.Empty<AtlasEntityView>();

    /// <summary>Search results grouped by category, omitting empty groups (user decision, 2026-11-14).</summary>
    public IReadOnlyList<AtlasResultGroup> SearchResultGroups =>
        SearchResults
            .GroupBy(e => e.Category)
            .Select(g => new AtlasResultGroup(g.Key, AtlasText.CategoryGroupLabel(g.Key), g.ToList()))
            .ToList();

    /// <summary>The entry in the middle, as shown (the arc entry as of its effective step in the whole-cast chart).</summary>
    public AtlasEntityView? Focus => ShowsWholeCast ? Arc!.Entry : snapshot.FindEntity(FocusId);

    /// <summary>The centre's one-hop connections; null in the whole-cast chart, which has the arc panel instead.</summary>
    public AtlasNeighborhood? Neighborhood => ShowsWholeCast ? null : snapshot.GetNeighborhood(FocusId);

    /// <summary>The whole-cast chart while the story arc's entry is in the middle; otherwise the centre's one-hop graph.</summary>
    public AtlasGraphLayout? Layout =>
        ShowsWholeCast ? wholeCastLayout ??= AtlasGraphLayout.ComputeWholeCast(Arc!.Cast, Arc.Entry.Id)
        : Neighborhood is { } neighborhood ? AtlasGraphLayout.Compute(neighborhood)
        : null;

    public AtlasRelationshipView? SelectedRelationship =>
        SelectedRelationshipId is null ? null
        : ShowsWholeCast ? Arc!.Cast.Relationships.FirstOrDefault(r => r.Id == SelectedRelationshipId)
        : Neighborhood?.Neighbors.FirstOrDefault(n => n.Relationship.Id == SelectedRelationshipId)?.Relationship;

    public void SetSourcesExpanded(bool expanded) => SourcesExpanded = expanded;

    public void SetSearch(string? query)
    {
        SelectionWasReset = false;
        SearchQuery = (query ?? string.Empty).Length > AtlasSnapshot.MaxSearchQueryLength
            ? query![..AtlasSnapshot.MaxSearchQueryLength]
            : query ?? string.Empty;
    }

    /// <summary>
    /// Put a visible entry in the middle and add it to the trail; an entry already on the trail cuts the trail back to
    /// it. A started arc's entry becomes the story arc, so its whole cast shows and the browse list shows its cast.
    /// Returns false and changes nothing if the entry is not visible.
    /// </summary>
    public bool FocusOn(string? entityId)
    {
        var arc = ArcByEntry(entityId);
        if (entityId is null || (arc is null && snapshot.FindEntity(entityId) is null))
        {
            return false;
        }

        if (arc is not null && arc.Id != Arc?.ArcId)
        {
            // The pick lasts like one made in the picker. Its trail is kept, so the way back stays on screen.
            explicitArcId = arc.Id;
            ResolveArc();
        }

        var existing = trail.IndexOf(entityId);
        if (existing >= 0)
        {
            trail.RemoveRange(existing + 1, trail.Count - existing - 1);
        }
        else
        {
            trail.Add(entityId);
            if (trail.Count > MaxTrailSteps)
            {
                trail.RemoveAt(1);
            }
        }

        trailSteps = null;
        SelectedRelationshipId = null;
        SelectionWasReset = false;
        return true;
    }

    /// <summary>Select a relationship on the current chart (the neighborhood, or the whole cast) to show its details and sources.</summary>
    public bool SelectRelationship(string? relationshipId)
    {
        // Participation spokes are not click targets on the whole-cast chart (D8).
        var onChart = ShowsWholeCast
            ? Arc!.Cast.Relationships.Any(r => r.Id == relationshipId && !AtlasArcs.IsSpoke(r, Arc.Entry.Id))
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

        return ApplyCeilingSelection(result, confirmed: false);
    }

    public AtlasStateChange ConfirmPendingCeiling()
    {
        if (PendingCeiling is null)
        {
            return AtlasStateChange.None;
        }

        var result = AtlasSpoilerPolicy.SetCeiling(Dataset, SpoilerState, PendingCeiling.Id, confirmed: true);
        PendingCeiling = null;
        return ApplyCeilingSelection(result, confirmed: true);
    }

    public void CancelPendingCeiling() => PendingCeiling = null;

    /// <summary>A manual view change. It turns Follow off (v2 plan, "Follow").</summary>
    public AtlasStateChange SetView(string? checkpointId)
    {
        PendingCeiling = null;
        var result = AtlasSpoilerPolicy.SetView(Dataset, SpoilerState, checkpointId);
        Apply(result);
        if (result.Change == AtlasStateChange.Changed)
        {
            SetFollow(false);
        }

        return result.Change;
    }

    // ---- Follow (NDL-017) ----

    private Func<int, AtlasQuestProgress>? followProgress;
    private bool followRaiseOffered;

    /// <summary>The Follow toggle. Only the host persists it; a Follow position is never persisted as progress.</summary>
    public bool FollowEnabled { get; private set; }

    /// <summary>The latest Follow result, or null while Follow is off or nothing has been read for this character.</summary>
    public AtlasFollowResult? FollowResult { get; private set; }

    /// <summary>The one neutral "your completed quests" raise is on offer (once per session and character).</summary>
    public bool FollowRaiseOffered { get; private set; }

    /// <summary>The offered raise awaits confirmation.</summary>
    public bool FollowRaisePending { get; private set; }

    /// <summary>The neutral confirmation for the Follow raise. It never names a quest.</summary>
    public string? FollowRaisePrompt => FollowRaisePending ? AtlasText.ConfirmRaiseToProgress : null;

    /// <summary>Follow placed the current view (the position line then reads as the player's progress).</summary>
    public bool FollowedHere => FollowEnabled && FollowResult is { Kind: AtlasFollowKind.Position } result && result.CheckpointId == SpoilerState.ViewId;

    /// <summary>
    /// The Follow status line, or null when there is nothing to add to the position line. It never names a quest beyond
    /// the limit: a clamped result names only the limit's own step.
    /// </summary>
    public string? FollowStatus => !FollowEnabled ? null
        : FollowResult is not { } result ? AtlasText.FollowReading
        : result.Kind == AtlasFollowKind.Unknown ? AtlasText.FollowUnknown
        : result.Kind == AtlasFollowKind.BeforeCoverage ? AtlasText.FollowBeforeCoverage
        : FollowedHere ? null
        : result.BeyondLimit ? AtlasText.FollowBeyondLimit
        : Dataset.TryGetCheckpoint(result.CheckpointId, out var point) ? AtlasText.FollowProgress(point.DisplayTitle)
        : null;

    /// <summary>Turn Follow on or off. Turning it off forgets the result and any raise offer; the view stays where it is.</summary>
    public void SetFollow(bool enabled)
    {
        if (enabled == FollowEnabled)
        {
            return;
        }

        FollowEnabled = enabled;
        if (!enabled)
        {
            FollowResult = null;
            followProgress = null;
            FollowRaiseOffered = false;
            FollowRaisePending = false;
        }
    }

    /// <summary>
    /// Apply a fresh progress snapshot. Raise the session's limit when the completed step is safe to reveal, then move
    /// the view. Unknown progress leaves the view alone. Returns true when the view moved.
    /// </summary>
    public bool ApplyFollow(Func<int, AtlasQuestProgress> progress)
    {
        ArgumentNullException.ThrowIfNull(progress);
        if (!FollowEnabled)
        {
            return false;
        }

        followProgress = progress;
        var result = AtlasFollow.Position(Dataset, progress, approvedCeilingId);
        var ceilingId = approvedCeilingId;
        if (result.BeyondLimit
            && result.ReachedCheckpointId is { } reachedId
            && AtlasFollow.CanRaiseAutomatically(Dataset, ContentView, approvedCeilingId, reachedId))
        {
            ceilingId = reachedId;
            result = result with { CheckpointId = reachedId, BeyondLimit = false };
        }

        SetFollowResult(result, offerRaise: true);
        if (result.Kind != AtlasFollowKind.Position)
        {
            if (result.Kind == AtlasFollowKind.BeforeCoverage)
            {
                RestoreApprovedCeiling();
            }

            return false;
        }

        var state = new AtlasSpoilerState(ceilingId, result.CheckpointId!);
        var viewMoved = state.ViewId != SpoilerState.ViewId;
        if (viewMoved)
        {
            explicitArcId = null;
        }

        if (state != SpoilerState)
        {
            if (state.CeilingId != SpoilerState.CeilingId)
            {
                PendingCeiling = null;
            }

            Apply(new AtlasStateResult(state, AtlasStateChange.Changed));
        }

        return viewMoved;
    }

    /// <summary>A different character (or a logout): drop the result and any raise offer until the next read.</summary>
    public void ResetFollowForCharacter()
    {
        FollowResult = null;
        followProgress = null;
        FollowRaiseOffered = false;
        FollowRaisePending = false;
        followRaiseOffered = false;
        PendingCeiling = null;
        RestoreApprovedCeiling();
    }

    /// <summary>Ask to confirm the offered raise. Returns false when nothing is on offer.</summary>
    public bool RequestFollowRaise()
    {
        FollowRaisePending = FollowRaiseOffered;
        return FollowRaisePending;
    }

    /// <summary>Confirm the offered raise: the limit rises to the player's progress and the view does not move.</summary>
    public AtlasStateChange ConfirmFollowRaise()
    {
        if (!FollowRaisePending || followProgress is null)
        {
            FollowRaisePending = false;
            return AtlasStateChange.None;
        }

        var result = AtlasSpoilerPolicy.SetCeilingToFollowed(Dataset, SpoilerState, followProgress, confirmed: true);
        FollowRaisePending = false;
        FollowRaiseOffered = false;
        return ApplyCeilingSelection(result, confirmed: true);
    }

    /// <summary>Decline the offered raise. It is not offered again this session for this character.</summary>
    public void CancelFollowRaise()
    {
        FollowRaisePending = false;
        FollowRaiseOffered = false;
    }

    private void SetFollowResult(AtlasFollowResult result, bool offerRaise)
    {
        FollowResult = result;
        if (!result.BeyondLimit)
        {
            FollowRaiseOffered = false;
            FollowRaisePending = false;
        }
        else if (offerRaise && !followRaiseOffered)
        {
            followRaiseOffered = true;
            FollowRaiseOffered = true;
        }
    }

    /// <summary>Switch between main-story-only and main-plus-optional records. Clears transient state like a checkpoint change.</summary>
    public void SetContentView(AtlasContentView view)
    {
        if (view == ContentView)
        {
            return;
        }

        ContentView = view;
        if (SpoilerState.CeilingId != approvedCeilingId
            && !AtlasFollow.CanRaiseAutomatically(Dataset, view, approvedCeilingId, SpoilerState.CeilingId))
        {
            PendingCeiling = null;
            RestoreApprovedCeiling();
        }
        else
        {
            Reproject(storySettingChanged: true);
        }
    }

    private AtlasStateChange ApplyCeilingSelection(AtlasStateResult result, bool confirmed)
    {
        if (result.Change == AtlasStateChange.Changed)
        {
            // Lowering an automatic limit to a point above the approved limit does not approve that point globally.
            if (confirmed || CheckpointOrder(result.State.CeilingId) <= CheckpointOrder(approvedCeilingId))
            {
                approvedCeilingId = result.State.CeilingId;
            }

            RecheckFollowAtCeiling(result.State.CeilingId);
            Apply(result);
        }

        return result.Change;
    }

    private int CheckpointOrder(string checkpointId)
        => Dataset.TryGetCheckpoint(checkpointId, out var checkpoint) ? checkpoint.Order : -1;

    private void RecheckFollowAtCeiling(string ceilingId)
    {
        if (FollowEnabled && followProgress is { } progress)
        {
            SetFollowResult(AtlasFollow.Position(Dataset, progress, ceilingId), offerRaise: false);
        }
    }

    private void RestoreApprovedCeiling()
    {
        if (SpoilerState.CeilingId == approvedCeilingId)
        {
            return;
        }

        RecheckFollowAtCeiling(approvedCeilingId);
        Apply(AtlasSpoilerPolicy.SetCeiling(Dataset, SpoilerState, approvedCeilingId, confirmed: false));
    }

    private void Apply(AtlasStateResult result)
    {
        if (result.Change != AtlasStateChange.Changed)
        {
            return;
        }

        SpoilerState = result.State;
        Reproject(storySettingChanged: true);
        // Automatic raises belong to the character whose progress was read. Save only the approved limit and a view
        // valid at that limit, so reopening or changing characters cannot inherit the automatic raise.
        var savedState = SpoilerState.CeilingId == approvedCeilingId
            ? SpoilerState
            : AtlasSpoilerPolicy.SetCeiling(Dataset, SpoilerState, approvedCeilingId, confirmed: false).State;
        SpoilerStateChanged?.Invoke(savedState);
    }

    /// <summary>
    /// Re-project after a story-setting change (limit, view, content view): resolve the story arc (ending an explicit pick
    /// whose first step is now after the view), rebuild the snapshot, clear transient state, and start the trail again at
    /// the resting centre.
    /// </summary>
    private void Reproject(bool storySettingChanged)
    {
        var hadPlayerState = SearchQuery.Length > 0
            || trail.Count > 1
            || (FocusId is not null && FocusId != RestingFocus())
            || SelectedRelationshipId is not null;
        PendingCeiling = null;
        snapshot = Project();
        ResolveArc();
        Rest();
        SelectionWasReset = storySettingChanged && hadPlayerState;
    }

    /// <summary>Resolve and project the story arc, clearing the state derived from it.</summary>
    private void ResolveArc()
    {
        arcPickerOptions = null;
        var resolution = AtlasArcs.Resolve(Dataset, SpoilerState.ViewId, explicitArcId);
        if (resolution.PickDropped)
        {
            explicitArcId = null;
        }

        Arc = resolution.ArcId is { } arcId ? AtlasArcs.Project(Dataset, arcId, SpoilerState.ViewId, ContentView) : null;
        arcPickerOptions = null;
        arcNewRows = null;
        arcEndedRows = null;
        trailSteps = null;
        wholeCastLayout = null;
    }

    /// <summary>Start the trail again at the resting centre, with no search or selection.</summary>
    private void Rest()
    {
        SearchQuery = string.Empty;
        SelectedRelationshipId = null;
        trail.Clear();
        trailSteps = null;
        if (RestingFocus() is { } rest)
        {
            trail.Add(rest);
        }
    }

    /// <summary>Where the map rests: the story arc's entry, else the home entry when visible, else nothing.</summary>
    private string? RestingFocus() =>
        Arc is { } arc ? arc.Entry.Id
        : snapshot.FindEntity(HomeEntityId) is not null ? HomeEntityId
        : null;

    private AtlasSnapshot Project() => AtlasProjector.Project(Dataset, SpoilerState.ViewId, ContentView);
}
