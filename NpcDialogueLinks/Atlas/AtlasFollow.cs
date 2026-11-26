using System;
using System.Collections.Generic;
using System.Linq;

namespace NpcDialogueLinks.Atlas;

/// <summary>A game quest's completion as read by the runtime adapter. Unknown is never treated as incomplete.</summary>
public enum AtlasQuestProgress
{
    Complete,
    Incomplete,
    Unknown,
}

public enum AtlasFollowKind
{
    /// <summary>A covered step the view can follow to.</summary>
    Position,

    /// <summary>The player has completed no covered step.</summary>
    BeforeCoverage,

    /// <summary>Any covered step reads unknown, or the player is not logged in. Takes precedence.</summary>
    Unknown,
}

/// <summary>
/// The result of <see cref="AtlasFollow.Position"/>. For <see cref="AtlasFollowKind.Position"/>, <see cref="CheckpointId"/>
/// is where the view goes (clamped to the limit) and <see cref="ReachedCheckpointId"/> is the real progress step;
/// <see cref="BeyondLimit"/> means they differ, so a front end may offer the neutral "your completed quests" raise.
/// </summary>
public sealed record AtlasFollowResult(AtlasFollowKind Kind, string? CheckpointId, bool BeyondLimit, string? ReachedCheckpointId = null)
{
    public static readonly AtlasFollowResult Unknown = new(AtlasFollowKind.Unknown, null, false);
    public static readonly AtlasFollowResult BeforeCoverage = new(AtlasFollowKind.BeforeCoverage, null, false);
}

/// <summary>
/// Pure Follow positioning (docs/atlas/v2-plan.md, "Follow"). Completed-quest flags for authored game quest ids are the
/// only progress source. The result never raises the spoiler limit and never falls back to a default step.
/// </summary>
public static class AtlasFollow
{
    /// <summary>
    /// The latest covered step (one with game quest ids) that the player has completed, clamped to the limit. A step's
    /// quest ids are alternatives: any completed one completes it.
    /// </summary>
    /// <remarks>
    /// NDL-017 amendment: the timeline lays mutually exclusive paths end to end (the three starting-city chains, the
    /// Grand Company pairs) and lists parallel quests one after another, so most players never complete some earlier
    /// steps. A contiguous completed prefix would stop every Limsa Lominsa or Ul'dah starter at "before coverage", so
    /// Follow takes the latest completed step instead. Main-scenario quests unlock in order, so completing a step means
    /// the player finished the story before it on their own path.
    /// </remarks>
    public static AtlasFollowResult Position(AtlasDataset dataset, Func<int, AtlasQuestProgress> progress, string ceilingId)
    {
        ArgumentNullException.ThrowIfNull(dataset);
        ArgumentNullException.ThrowIfNull(progress);
        if (!dataset.TryGetCheckpoint(ceilingId, out var ceiling))
        {
            return AtlasFollowResult.Unknown;
        }

        var covered = dataset.Checkpoints.Where(c => c.GameQuestIds.Count > 0).ToList();
        if (covered.Count == 0)
        {
            return AtlasFollowResult.Unknown;
        }

        AtlasCheckpoint? reached = null;
        foreach (var checkpoint in covered)
        {
            var states = checkpoint.GameQuestIds.Select(progress).ToList();
            if (states.Contains(AtlasQuestProgress.Unknown))
            {
                return AtlasFollowResult.Unknown;
            }

            if (states.Contains(AtlasQuestProgress.Complete) && (reached is null || checkpoint.Order > reached.Order))
            {
                reached = checkpoint;
            }
        }

        if (reached is null)
        {
            return AtlasFollowResult.BeforeCoverage;
        }

        return reached.Order > ceiling.Order
            ? new AtlasFollowResult(AtlasFollowKind.Position, ceiling.Id, true, reached.Id)
            : new AtlasFollowResult(AtlasFollowKind.Position, reached.Id, false, reached.Id);
    }

    /// <summary>MSQ completion covers the main story. Optional records need the player's approval before they are revealed.</summary>
    internal static bool CanRaiseAutomatically(
        AtlasDataset dataset,
        AtlasContentView contentView,
        string approvedCeilingId,
        string reachedId)
    {
        if (contentView == AtlasContentView.MainStory)
        {
            return true;
        }

        if (!dataset.TryGetCheckpoint(approvedCeilingId, out var approved)
            || !dataset.TryGetCheckpoint(reachedId, out var reached))
        {
            return false;
        }

        bool NewlyVisible(int order) => order > approved.Order && order <= reached.Order;

        // Players can browse every unlocked step. Include records introduced along the way and relationship endings
        // exposed by Changes, even when the destination no longer shows those records.
        return !dataset.Entities.Any(entity => entity.Presentations.Any(presentation =>
                   presentation.Scope == AtlasScope.Optional && NewlyVisible(presentation.Interval.FromOrder)))
            && !dataset.Relationships.Any(relationship => relationship.Scope == AtlasScope.Optional
                && (NewlyVisible(relationship.Interval.FromOrder)
                    || relationship.Interval.UntilOrder is int end && NewlyVisible(end)));
    }
}
