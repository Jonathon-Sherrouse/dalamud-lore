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

    /// <summary>Changes-lens heading for a step contiguous with the previous one.</summary>
    public const string ChangesThisQuest = "What this quest changed";

    /// <summary>Changes-lens heading across a gap in the covered steps.</summary>
    public static string ChangesSince(string previousPoint) => $"Changes since {previousPoint}";

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
    public const string ConfirmRaiseToProgress = "Allow story knowledge through your completed quests? The current view will not change.";

    /// <summary>Only a Follow result is presented as the player's progress.</summary>
    public static string FollowProgress(string questOrPoint) => $"Your progress: through {questOrPoint}";

    // ---- Follow (NDL-017) ----

    public const string FollowToggle = "Follow my progress";
    public const string FollowTooltip = "Moves the view to the latest main-scenario quest you have completed, never past your spoiler limit. Reads your completed quests only.";
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

    public const string WholeCastButton = "Whole cast";

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

    /// <summary>
    /// What a picked Changes row did at the view, shown at the top of its details so an ended relationship never reads
    /// as current. Front ends put the row's mark (+, −, ~) before it.
    /// </summary>
    public static string ChangeStatus(AtlasChangeKind kind, AtlasCheckpoint view)
    {
        var at = view.Milestone ? $"by {view.Label}" : $"in {view.DisplayTitle}";
        return kind switch
        {
            AtlasChangeKind.Added => $"Added {at}",
            AtlasChangeKind.Ended => $"Ended {at}",
            _ => $"Description updated {at}",
        };
    }

    public const string ChangesAdded = "Added";
    public const string ChangesEnded = "Ended";
    public const string ChangesUpdated = "Description updated";
    public const string NoChanges = "Nothing changed at this point.";
    public const string ChangesNotOffered = "Nothing to compare here. Changes compares a quest step with the one before it, or a milestone with the previous milestone.";
    public const string ChangesPickHint = "Pick a change to see its details.";

    /// <summary>Label of the collapsible end-evidence section, shown only on a Changes "ended" row.</summary>
    public static string EndSourcesToggle(int count) => $"Sources for the ending ({count})";
}

/// <summary>What the window shows (v2 plan, "Product shape"). Follow is a toggle beside the lenses, not a lens.</summary>
public enum AtlasLens
{
    Arc,
    StoryPoint,
    Changes,
}

public sealed record AtlasLensOption(AtlasLens Lens, string Label, bool IsCurrent);

/// <summary>One arc-picker row. <see cref="ArcId"/> null is the automatic choice.</summary>
public sealed record AtlasArcPickerOption(string? ArcId, string Label, bool IsCurrent)
{
    /// <summary>"from ‹start quest›", so a player can tell where the arc sits; empty for the automatic option.</summary>
    public string Detail { get; init; } = string.Empty;

    /// <summary>The patch heading the arc is listed under; null for the automatic option.</summary>
    public string? Group { get; init; }
}

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

    // Derived lens state, built lazily and cleared by Reproject, which every input (limit, view, content view, lens,
    // arc pick) passes through. Front ends may read these every frame without re-projecting.
    private IReadOnlyList<AtlasChangeGroup>? changeGroups;
    private IReadOnlyList<AtlasArcPickerOption>? arcPickerOptions;
    private IReadOnlyList<AtlasChangeRow>? arcNewRows;
    private IReadOnlyList<AtlasChangeRow>? arcEndedRows;
    private AtlasGraphLayout? wholeCastLayout;

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

    /// <summary>
    /// "Viewing: after ‹quest›", the chosen point, never "you are here" (v2 plan, "Honest positioning"). Only when Follow
    /// placed the view does it read as the player's progress.
    /// </summary>
    public string PositionLabel => !FollowedHere ? AtlasText.ViewingAt(ViewCheckpoint)
        : FollowResult!.BeyondLimit ? AtlasText.FollowAtLimit(ViewCheckpoint)
        : AtlasText.FollowProgress(ViewCheckpoint.DisplayTitle);

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
    public IReadOnlyList<AtlasArcPickerOption> ArcPickerOptions => arcPickerOptions ??= BuildArcPickerOptions();

    /// <summary>
    /// Whether the picker shows patch headings: only when its arcs start in more than one patch (user decision,
    /// 2026-11-15), so a single heading over everything never adds clutter.
    /// </summary>
    public bool ArcPickerGrouped => ArcPickerOptions.Where(o => o.ArcId is not null).Select(o => o.Group).Distinct().Count() > 1;

    /// <summary>"Cast (n)" above the cast list: the arc's members, not counting the arc entry. Null outside an arc view.</summary>
    public string? CastHeading => ArcView is { } arc ? AtlasText.CastHeading(arc.Cast.Entities.Count - 1) : null;

    /// <summary>"New at this point", or "New in ‹last quest›" for a picked arc viewed after it ended. Null outside an arc view.</summary>
    public string? ArcNewHeading => ArcView is { } arc ? (arc.PastEnd ? AtlasText.ArcNewIn(arc.Effective) : AtlasText.ArcNewHeading) : null;

    /// <summary><see cref="Arc"/> while the Arc lens shows it; null in the other lenses, so Arc-only surfaces stay empty there.</summary>
    private AtlasArcView? ArcView => Lens == AtlasLens.Arc ? Arc : null;

    /// <summary>True in the Arc lens while no entity is focused: the whole-cast chart and the arc panel show.</summary>
    public bool ShowsWholeCast => Lens == AtlasLens.Arc && Arc is not null && FocusId is null;

    /// <summary>
    /// Relationships new at the arc's effective step, as rows (no end evidence). Spokes to the arc entry are left out: a
    /// new member already shows by appearing on the chart, and listing every spoke would bury the real changes (D8).
    /// </summary>
    public IReadOnlyList<AtlasChangeRow> ArcNewRows => arcNewRows ??= ArcView is { } arc
        ? arc.New.Where(r => !AtlasArcs.IsSpoke(r, arc.Entry.Id)).Select(r => RelationshipRow(AtlasChangeKind.Added, r, arc.Cast)).ToList()
        : Array.Empty<AtlasChangeRow>();

    /// <summary>"Ended so far in this arc", as rows. Never carries sources of any kind (v2 plan, "Arc lens").</summary>
    public IReadOnlyList<AtlasChangeRow> ArcEndedRows => arcEndedRows ??= ArcView is { } arc
        ? arc.EndedSoFar.Select(e => new AtlasChangeRow(
            $"ended:{e.Relationship.Id}", AtlasChangeKind.Ended, e.Relationship, e.Source, e.Target, null,
            Array.Empty<AtlasCitationView>(), EndedInFor(e.EndedAtCheckpointId))).ToList()
        : Array.Empty<AtlasChangeRow>();

    /// <summary>
    /// Pick an arc, or null for the automatic choice. Only arcs started by the view can be picked. Picking an arc is
    /// choosing the Arc lens, so the default lens rule can no longer hide the pick when the view moves past its end.
    /// </summary>
    public bool PickArc(string? arcId)
    {
        if (arcId is not null && AtlasArcs.Eligible(Dataset, SpoilerState.ViewId, ContentView).All(a => a.ArcId != arcId))
        {
            return false;
        }

        explicitArcId = arcId;
        if (arcId is not null)
        {
            LensIsExplicit = true;
            Lens = AtlasLens.Arc;
        }

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
    public IReadOnlyList<AtlasChangeGroup> ChangeGroups => changeGroups ??= BuildChangeGroups();

    private IReadOnlyList<AtlasChangeGroup> BuildChangeGroups()
    {
        if (AtlasChanges.At(Dataset, SpoilerState.ViewId, ContentView) is not { } diff)
        {
            return Array.Empty<AtlasChangeGroup>();
        }

        var after = Lens == AtlasLens.Arc ? Project() : snapshot;
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

    public string? SelectedChangeKey { get; private set; }

    /// <summary>"Added in ‹quest›", "Ended by ‹milestone›"… for the picked Changes row; null when none is picked.</summary>
    public string? SelectedChangeStatus => SelectedChange is { } row ? AtlasText.ChangeStatus(row.Kind, ViewCheckpoint) : null;

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

    private static AtlasChangeRow RelationshipRow(AtlasChangeKind kind, AtlasRelationshipView r, AtlasSnapshot endpoints) =>
        new($"{kind.ToString().ToLowerInvariant()}:{r.Id}", kind, r, endpoints.FindEntity(r.SourceId), endpoints.FindEntity(r.TargetId), null, Array.Empty<AtlasCitationView>());

    private string EndedInFor(string checkpointId)
    {
        Dataset.TryGetCheckpoint(checkpointId, out var ended);
        return AtlasText.EndedIn(ended);
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
    /// Visible entries matching the search. In the Arc lens with an empty search, the cast members without the arc entry,
    /// which is the panel's subject and the chart's centre; a search can still find the entry by name.
    /// </summary>
    public IReadOnlyList<AtlasEntityView> SearchResults =>
        ArcView is { } arc && SearchQuery.Trim().Length == 0
            ? snapshot.Entities.Where(e => e.Id != arc.Entry.Id).ToList()
            : snapshot.Search(SearchQuery);

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
        ShowsWholeCast ? wholeCastLayout ??= AtlasGraphLayout.ComputeWholeCast(snapshot, Arc!.Entry.Id)
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
        // Participation spokes are not click targets on the whole-cast chart (D8).
        var onChart = ShowsWholeCast
            ? snapshot.Relationships.Any(r => r.Id == relationshipId && !AtlasArcs.IsSpoke(r, Arc!.Entry.Id))
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
    /// Apply a fresh progress read (on window open, Refresh, or a completed quest). A position moves the view, clamped to
    /// the limit, and ends an explicit arc pick; "before coverage" and "unknown" leave the view alone. Returns true when
    /// the view moved. <paramref name="progress"/> must be a snapshot: it is kept for the raise confirmation.
    /// </summary>
    public bool ApplyFollow(Func<int, AtlasQuestProgress> progress)
    {
        ArgumentNullException.ThrowIfNull(progress);
        if (!FollowEnabled)
        {
            return false;
        }

        followProgress = progress;
        Evaluate(offerRaise: true);
        if (FollowResult is not { Kind: AtlasFollowKind.Position } result || result.CheckpointId == SpoilerState.ViewId)
        {
            return false;
        }

        var change = AtlasSpoilerPolicy.SetView(Dataset, SpoilerState, result.CheckpointId);
        if (change.Change != AtlasStateChange.Changed)
        {
            return false;
        }

        explicitArcId = null; // Follow moving the view ends an explicit arc pick (v2 plan, "Arc lens").
        Apply(change);
        return true;
    }

    /// <summary>A different character (or a logout): drop the result and any raise offer until the next read.</summary>
    public void ResetFollowForCharacter()
    {
        FollowResult = null;
        followProgress = null;
        FollowRaiseOffered = false;
        FollowRaisePending = false;
        followRaiseOffered = false;
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
        Apply(result);
        return result.Change;
    }

    /// <summary>Decline the offered raise. It is not offered again this session for this character.</summary>
    public void CancelFollowRaise()
    {
        FollowRaisePending = false;
        FollowRaiseOffered = false;
    }

    /// <summary>Recompute the Follow result from the last read against the current limit, without moving the view.</summary>
    private void Evaluate(bool offerRaise)
    {
        if (!FollowEnabled || followProgress is null)
        {
            return;
        }

        FollowResult = AtlasFollow.Position(Dataset, followProgress, SpoilerState.CeilingId);
        if (!FollowResult.BeyondLimit)
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
        Reproject(storySettingChanged: true);
    }

    private void Apply(AtlasStateResult result)
    {
        if (result.Change != AtlasStateChange.Changed)
        {
            return;
        }

        var ceilingChanged = result.State.CeilingId != SpoilerState.CeilingId;
        SpoilerState = result.State;
        if (ceilingChanged)
        {
            // The Follow result is clamped to the limit, so re-clamp it; a limit change never moves the view for Follow.
            Evaluate(offerRaise: false);
        }

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
        changeGroups = null;
        arcPickerOptions = null;
        arcNewRows = null;
        arcEndedRows = null;
        wholeCastLayout = null;

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
