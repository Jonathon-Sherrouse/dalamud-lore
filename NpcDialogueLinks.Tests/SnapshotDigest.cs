using System.Security.Cryptography;
using System.Text;
using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

/// <summary>
/// A stable fingerprint of everything a snapshot can display: entity names, aliases, summaries and citations, plus
/// relationship endpoints, labels and citations. Pins the accepted pilot content across the v1 → v2 upgrade.
/// </summary>
internal static class SnapshotDigest
{
    public static string Of(AtlasSnapshot snapshot) => Of(snapshot, null, null);

    /// <summary>
    /// Fingerprint restricted to fixed entity and relationship id sets, so records added later (for example arc entries
    /// that stay visible at the milestones) never move the pin of the accepted legacy records.
    /// </summary>
    public static string Of(AtlasSnapshot snapshot, IReadOnlySet<string>? entityIds, IReadOnlySet<string>? relationshipIds)
    {
        var text = new StringBuilder();
        foreach (var e in snapshot.Entities.Where(e => entityIds is null || entityIds.Contains(e.Id)))
        {
            text.Append("E|").Append(e.Id).Append('|').Append(e.Category).Append('|').Append(e.IncludesOptional).Append('|').Append(e.Name).Append('|')
                .Append(string.Join("¦", e.Aliases)).Append('|').Append(e.Summary).Append('|')
                .Append(string.Join("¦", e.Citations.Select(c => c.Title + "→" + c.Url))).Append('\n');
        }

        foreach (var r in snapshot.Relationships.Where(r => relationshipIds is null || relationshipIds.Contains(r.Id)))
        {
            text.Append("R|").Append(r.Id).Append('|').Append(r.IsOptional).Append('|').Append(r.SourceId).Append('|').Append(r.TypeId).Append('|').Append(r.TargetId).Append('|')
                .Append(r.OutgoingLabel).Append('|').Append(r.IncomingLabel).Append('|').Append(r.Symmetric).Append('|')
                .Append(string.Join("¦", r.Citations.Select(c => c.Title + "→" + c.Url))).Append('\n');
        }

        return Convert.ToHexString(SHA256.HashData(Encoding.UTF8.GetBytes(text.ToString())));
    }
}
