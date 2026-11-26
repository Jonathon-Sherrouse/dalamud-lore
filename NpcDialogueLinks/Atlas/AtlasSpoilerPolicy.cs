using System;

namespace NpcDialogueLinks.Atlas;

/// <summary>The two persisted spoiler controls. <see cref="ViewId"/> never exceeds <see cref="CeilingId"/>.</summary>
public sealed record AtlasSpoilerState(string CeilingId, string ViewId);

public enum AtlasStateChange
{
    /// <summary>The request matched the current state.</summary>
    None,

    /// <summary>State changed; the UI must clear search, focus, selection, and details.</summary>
    Changed,

    /// <summary>Raising the ceiling needs explicit confirmation; state is unchanged.</summary>
    NeedsConfirmation,

    /// <summary>Unknown checkpoint, or a view above the ceiling; state is unchanged.</summary>
    Rejected,
}

public sealed record AtlasStateResult(AtlasSpoilerState State, AtlasStateChange Change);

/// <summary>
/// Pure rules for the ceiling ("spoiler limit") and view ("viewing as of") controls. Absent or invalid saved state
/// resets to the earliest checkpoint, the pre-arc baseline in v2, so a reset never raises the limit (v2 plan).
/// </summary>
public static class AtlasSpoilerPolicy
{
    /// <summary>Both controls at the earliest checkpoint.</summary>
    public static AtlasSpoilerState Default(AtlasDataset dataset)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        var earliest = dataset.EarliestCheckpoint.Id;
        return new AtlasSpoilerState(earliest, earliest);
    }

    /// <summary>
    /// Revalidates saved state against the current dataset. Missing or unknown IDs, or a saved view above
    /// the saved ceiling, reset both controls to the earliest checkpoint.
    /// </summary>
    public static AtlasSpoilerState Restore(AtlasDataset dataset, string? savedCeilingId, string? savedViewId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        if (!dataset.TryGetCheckpoint(savedCeilingId, out var ceiling)
            || !dataset.TryGetCheckpoint(savedViewId, out var view)
            || view.Order > ceiling.Order)
        {
            return Default(dataset);
        }

        return new AtlasSpoilerState(ceiling.Id, view.Id);
    }

    /// <summary>
    /// Raising the ceiling requires <paramref name="confirmed"/> and never moves the view. Lowering it clamps the view.
    /// </summary>
    public static AtlasStateResult SetCeiling(AtlasDataset dataset, AtlasSpoilerState state, string? ceilingId, bool confirmed)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        ArgumentNullException.ThrowIfNull(state);
        if (!dataset.TryGetCheckpoint(ceilingId, out var requested)
            || !dataset.TryGetCheckpoint(state.CeilingId, out var current)
            || !dataset.TryGetCheckpoint(state.ViewId, out var view))
        {
            return new AtlasStateResult(state, AtlasStateChange.Rejected);
        }

        if (requested.Order == current.Order)
        {
            return new AtlasStateResult(state, AtlasStateChange.None);
        }

        if (requested.Order > current.Order)
        {
            // v2 spoiler rule 1: the limit rises only to a milestone or to the single next step, so raising can never
            // require naming a quest further ahead.
            if (!requested.Milestone && requested.Order != current.Order + 1)
            {
                return new AtlasStateResult(state, AtlasStateChange.Rejected);
            }

            return confirmed
                ? new AtlasStateResult(state with { CeilingId = requested.Id }, AtlasStateChange.Changed)
                : new AtlasStateResult(state, AtlasStateChange.NeedsConfirmation);
        }

        var clampedView = view.Order > requested.Order ? requested.Id : view.Id;
        return new AtlasStateResult(new AtlasSpoilerState(requested.Id, clampedView), AtlasStateChange.Changed);
    }

    /// <summary>
    /// Follow's neutral "your completed quests" raise. Progress is read here, against the current limit, so the raise is
    /// verified by construction and a stale or hand-built Follow result can never be applied. The limit rises to exactly
    /// the reached step, only with <paramref name="confirmed"/>, and the view never moves. Anything else is rejected.
    /// </summary>
    public static AtlasStateResult SetCeilingToFollowed(AtlasDataset dataset, AtlasSpoilerState state, Func<int, AtlasQuestProgress> progress, bool confirmed)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        ArgumentNullException.ThrowIfNull(state);
        ArgumentNullException.ThrowIfNull(progress);
        var follow = AtlasFollow.Position(dataset, progress, state.CeilingId);
        if (follow.Kind != AtlasFollowKind.Position || !follow.BeyondLimit || !dataset.TryGetCheckpoint(follow.ReachedCheckpointId, out var reached))
        {
            return new AtlasStateResult(state, AtlasStateChange.Rejected);
        }

        return confirmed
            ? new AtlasStateResult(state with { CeilingId = reached.Id }, AtlasStateChange.Changed)
            : new AtlasStateResult(state, AtlasStateChange.NeedsConfirmation);
    }

    /// <summary>The view may move anywhere at or below the ceiling; it can never raise the ceiling.</summary>
    public static AtlasStateResult SetView(AtlasDataset dataset, AtlasSpoilerState state, string? viewId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        ArgumentNullException.ThrowIfNull(state);
        if (!dataset.TryGetCheckpoint(viewId, out var requested)
            || !dataset.TryGetCheckpoint(state.CeilingId, out var ceiling)
            || requested.Order > ceiling.Order)
        {
            return new AtlasStateResult(state, AtlasStateChange.Rejected);
        }

        return requested.Id == state.ViewId
            ? new AtlasStateResult(state, AtlasStateChange.None)
            : new AtlasStateResult(state with { ViewId = requested.Id }, AtlasStateChange.Changed);
    }
}
