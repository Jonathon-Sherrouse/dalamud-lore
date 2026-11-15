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

    /// <summary>The player has not completed the first covered step.</summary>
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
    /// The last step of the contiguous completed prefix among covered steps (those with game quest ids), clamped to the
    /// limit. A step is complete when all its quests are complete.
    /// </summary>
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

        var states = covered.Select(c => c.GameQuestIds.Select(progress).ToList()).ToList();
        if (states.Any(s => s.Contains(AtlasQuestProgress.Unknown)))
        {
            return AtlasFollowResult.Unknown;
        }

        var prefix = -1;
        while (prefix + 1 < covered.Count && states[prefix + 1].All(p => p == AtlasQuestProgress.Complete))
        {
            prefix++;
        }

        if (prefix < 0)
        {
            return AtlasFollowResult.BeforeCoverage;
        }

        var reached = covered[prefix];
        return reached.Order > ceiling.Order
            ? new AtlasFollowResult(AtlasFollowKind.Position, ceiling.Id, true, reached.Id)
            : new AtlasFollowResult(AtlasFollowKind.Position, reached.Id, false, reached.Id);
    }
}
