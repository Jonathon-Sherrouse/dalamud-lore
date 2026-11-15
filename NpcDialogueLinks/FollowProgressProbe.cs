#if DEBUG
using System.Security.Cryptography;
using System.Text;
using Dalamud.Plugin;
using Dalamud.Plugin.Services;
using FFXIVClientStructs.FFXIV.Client.Game;
using Lumina.Excel.Sheets;
using NpcDialogueLinks.Progress;

namespace NpcDialogueLinks;

/// <summary>
/// NDL-007 DEBUG-ONLY investigation probe for Follow's progress source (<c>/npclinks followprobe</c>).
/// Compiled into Debug builds only. Reads go through <see cref="AtlasProgressSource"/>; the only extra
/// reads are labelled "raw" diagnostics of the completed-quest bitfield, taken on the framework thread,
/// used to show why the gate exists, and never used by Follow. Logs stay local and never include the
/// character's name or content ID (only a short one-way tag).
/// </summary>
internal sealed unsafe class FollowProgressProbe : IDisposable
{
    private const string Tag = "NPC Links";
    private const int MaxLoggedFlips = 12;

    // Authored (row, title) pairs, taken offline from the local game data with Lumina on 2026-11-14.
    // Retired rows are the pre-streamlining ARR versions that the game keeps under a hidden category.
    private static readonly (uint Row, string Title, string Note)[] Anchors =
    [
        (65621, "Close to Home", "starting-city variant"),
        (65644, "Close to Home", "starting-city variant"),
        (65645, "Close to Home", "starting-city variant"),
        (65659, "Close to Home", "starting-city variant"),
        (65660, "Close to Home", "starting-city variant"),
        (66104, "Close to Home", "starting-city variant"),
        (66105, "Close to Home", "starting-city variant"),
        (66106, "Close to Home", "starting-city variant"),
        (66572, "Operation Archon", "retired row"),
        (70057, "Operation Archon", "current row"),
        (66060, "The Ultimate Weapon", "retired row"),
        (70058, "The Ultimate Weapon", "current row, 2.0 finale"),
        (65615, "Chasing Ivy", "retired row"),
        (69422, "Chasing Ivy", "current row"),
        (65955, "The Steps of Faith", "retired row"),
        (70127, "The Steps of Faith", "current row"),
        (65964, "Before the Dawn", "2.55 finale"),
        (67205, "Heavensward", "3.0 finale"),
        (67895, "The Far Edge of Fate", "3.3 finale"),
        (68089, "Stormblood", "4.0 finale"),
        (69190, "Shadowbringers", "5.0 finale"),
        (70000, "Endwalker", "6.0 finale"),
        (70495, "Dawntrail", "7.0 finale"),
    ];

    // Deliberate negatives for the title cross-check and the row guard.
    private static readonly (uint Row, string? Title, string Expect)[] Negatives =
    [
        (70058, "Before the Dawn", "TitleMismatch"),
        (65536, null, "InvalidQuestRow"),
        (0, null, "InvalidQuestRow"),
        (200000, null, "InvalidQuestRow"),
    ];

    private readonly AtlasProgressSource source;
    private readonly IDalamudPluginInterface pluginInterface;
    private readonly IFramework framework;
    private readonly IChatGui chatGui;
    private readonly IDataManager dataManager;
    private readonly object logLock = new();

    private bool watching;
    private string? lastGateSignature;
    private byte[]? lastBits;
    private bool lastBitsTrusted;
    private bool drawCheckPending;

    public FollowProgressProbe(
        AtlasProgressSource source,
        IDalamudPluginInterface pluginInterface,
        IFramework framework,
        IChatGui chatGui,
        IDataManager dataManager)
    {
        this.source = source;
        this.pluginInterface = pluginInterface;
        this.framework = framework;
        this.chatGui = chatGui;
        this.dataManager = dataManager;
        this.source.CharacterInvalidated += this.OnCharacterInvalidated;
    }

    public string OutputDirectory => Path.Combine(this.pluginInterface.ConfigDirectory.FullName, "follow-progress-probe");

    private string LogPath => Path.Combine(this.OutputDirectory, $"followprobe-{DateTimeOffset.Now:yyyyMMdd}.log");

    public void Dispose()
    {
        this.SetWatching(false);
        this.source.CharacterInvalidated -= this.OnCharacterInvalidated;
        this.pluginInterface.UiBuilder.Draw -= this.OnDrawCheck;
    }

    public void HandleCommand(string arguments)
    {
        var trimmed = arguments.Trim();
        var parts = trimmed.Split(' ', 2, StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        var action = parts.Length > 0 ? parts[0].ToLowerInvariant() : "status";
        var rest = parts.Length > 1 ? parts[1] : string.Empty;

        // Commands arrive on the framework thread; marshal anyway so every read is gated the same way.
        _ = this.framework.RunOnFrameworkThread(() =>
        {
            try
            {
                switch (action)
                {
                    case "status":
                        this.PrintStatus();
                        break;
                    case "anchors":
                        this.RunAnchors();
                        break;
                    case "read":
                        this.RunRead(rest);
                        break;
                    case "thread":
                        this.RunThreadCheck();
                        break;
                    case "watch":
                        this.SetWatching(!string.Equals(rest, "off", StringComparison.OrdinalIgnoreCase));
                        this.Say(this.watching
                            ? "Follow probe watch ON: logging logout, loading, login, character switches and quest completions."
                            : "Follow probe watch OFF.");
                        break;
                    case "path":
                        this.Say($"Follow probe log: {this.LogPath}");
                        break;
                    default:
                        this.Say("Follow probe (debug): /npclinks followprobe status | anchors | read <row or title>[; ...] | thread | watch on|off | path");
                        break;
                }
            }
            catch (Exception exception)
            {
                Plugin.Log.Warning(exception, "Follow probe command failed.");
                this.Say("Follow probe command failed; see the Dalamud log.");
            }
        });
    }

    private void PrintStatus()
    {
        var gate = this.source.SampleGate();
        var reason = ProgressRules.Evaluate(gate);
        var line = $"status: {DescribeGate(gate)} => {(reason == ProgressUnknownReason.None ? "READY" : "unknown:" + reason)}; character={CharacterTag(gate.ContentId)}; generation={this.source.CharacterGeneration}; watch={(this.watching ? "on" : "off")}";
        this.Log(line);
        this.Say(line);
        this.Say($"Log: {this.LogPath}");
    }

    private void RunAnchors()
    {
        var gate = this.source.SampleGate();
        var reason = ProgressRules.Evaluate(gate);
        this.Log($"--- anchors: {DescribeGate(gate)} => {(reason == ProgressUnknownReason.None ? "READY" : "unknown:" + reason)}; character={CharacterTag(gate.ContentId)}; generation={this.source.CharacterGeneration}");

        var reads = this.source.ReadMany(Anchors.Select(anchor => (anchor.Row, (string?)anchor.Title)).ToArray());
        var summary = new List<string>();
        for (var index = 0; index < Anchors.Length; index++)
        {
            var anchor = Anchors[index];
            var read = reads[index];
            var raw = this.RawBit(anchor.Row);
            var gameTitle = this.source.GetQuestTitle(anchor.Row) ?? "(no row)";
            this.Log($"anchor row={anchor.Row} client={anchor.Row - QuestIdMapping.QuestRowBase} authored=\"{anchor.Title}\" game=\"{gameTitle}\" note={anchor.Note} => {Describe(read)}; rawBit={raw}");
            if (read.State == QuestCompletion.Complete)
            {
                summary.Add($"{anchor.Title} [{anchor.Row}]");
            }
        }

        var steps = Anchors
            .Select((anchor, index) => (anchor.Title, Read: reads[index]))
            .GroupBy(item => item.Title)
            .Select(group => $"{group.Key}={ProgressRules.CombineAlternatives(group.Select(item => item.Read).ToArray())}")
            .ToArray();
        this.Log("steps (alternatives combined): " + string.Join("; ", steps));

        foreach (var negative in Negatives)
        {
            var read = this.source.Read(negative.Row, negative.Title);
            var ok = read.State == QuestCompletion.Unknown && read.Reason.ToString() == negative.Expect;
            this.Log($"negative row={negative.Row} authored=\"{negative.Title ?? "(none)"}\" expect={negative.Expect} => {Describe(read)} [{(ok ? "PASS" : "FAIL")}]");
            if (reason == ProgressUnknownReason.None)
            {
                this.Say($"check {negative.Expect} on row {negative.Row}: {(ok ? "PASS" : "FAIL")}");
            }
        }

        if (reason != ProgressUnknownReason.None)
        {
            this.Say($"Progress is unknown ({reason}); nothing was treated as incomplete. Details in the log.");
            return;
        }

        this.Say($"Completed quests on this character: {gate.CompletedQuestCount}. Character {CharacterTag(gate.ContentId)}.");
        this.Say(summary.Count == 0 ? "No anchor quest reads complete." : "Complete: " + string.Join(", ", summary));
        this.Say("Steps: " + string.Join("; ", steps));
    }

    private void RunRead(string arguments)
    {
        var tokens = arguments.Split(';', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        if (tokens.Length == 0)
        {
            this.Say("Usage: /npclinks followprobe read <row or exact title>[; <row or title> ...]");
            return;
        }

        var gate = this.source.SampleGate();
        this.Log($"--- read: {DescribeGate(gate)}; character={CharacterTag(gate.ContentId)}");
        foreach (var token in tokens)
        {
            var rows = uint.TryParse(token, out var row) ? [row] : this.FindRowsByTitle(token);
            if (rows.Count == 0)
            {
                this.Say($"No quest row titled \"{token}\".");
                continue;
            }

            foreach (var questRow in rows)
            {
                var gameTitle = this.source.GetQuestTitle(questRow);
                var read = this.source.Read(questRow, gameTitle);
                var line = $"row {questRow} (client {(questRow > QuestIdMapping.QuestRowBase ? questRow - QuestIdMapping.QuestRowBase : 0)}) \"{gameTitle ?? "(no row)"}\" => {Describe(read)}; rawBit={this.RawBit(questRow)}";
                this.Log("read " + line);
                this.Say(line);
            }
        }
    }

    private void RunThreadCheck()
    {
        var anchor = Anchors[11];
        var onThread = this.source.Read(anchor.Row, anchor.Title);
        this.Log($"thread check: framework thread => {Describe(onThread)}");
        this.Say($"On the framework thread: {Describe(onThread)}");

        _ = Task.Run(() =>
        {
            var offThread = this.source.Read(anchor.Row, anchor.Title);
            var ok = offThread.State == QuestCompletion.Unknown && offThread.Reason == ProgressUnknownReason.NotFrameworkThread;
            this.Log($"thread check: background thread => {Describe(offThread)} [{(ok ? "PASS" : "FAIL")}]");
            _ = this.framework.RunOnFrameworkThread(() => this.Say($"From a background thread: {Describe(offThread)} [{(ok ? "PASS" : "FAIL")}]"));
        });

        // One-shot: is a window's Draw callback on the framework thread? (Matters for the Atlas window in NDL-010.)
        if (!this.drawCheckPending)
        {
            this.drawCheckPending = true;
            this.pluginInterface.UiBuilder.Draw += this.OnDrawCheck;
        }
    }

    private void OnDrawCheck()
    {
        this.pluginInterface.UiBuilder.Draw -= this.OnDrawCheck;
        this.drawCheckPending = false;
        var inDraw = this.framework.IsInFrameworkUpdateThread;
        this.Log($"thread check: UiBuilder.Draw IsInFrameworkUpdateThread={inDraw}");
        _ = this.framework.RunOnFrameworkThread(() => this.Say($"Inside a window draw, framework thread = {inDraw}"));
    }

    private void SetWatching(bool enabled)
    {
        if (enabled == this.watching)
        {
            return;
        }

        this.watching = enabled;
        this.lastGateSignature = null;
        this.lastBits = null;
        this.lastBitsTrusted = false;
        if (enabled)
        {
            this.framework.Update += this.OnFrameworkUpdate;
            this.Log("--- watch on");
        }
        else
        {
            this.framework.Update -= this.OnFrameworkUpdate;
            this.Log("--- watch off");
        }
    }

    private void OnFrameworkUpdate(IFramework _)
    {
        try
        {
            var gate = this.source.SampleGate();
            var reason = ProgressRules.Evaluate(gate);
            var bits = this.SnapshotBits();
            var signature = $"{reason}|{CharacterTag(gate.ContentId)}|{gate.IsLoggedIn}|{gate.PlayerLoaded}|{gate.BetweenAreas}|{gate.LocalPlayerPresent}|{(gate.CompletedQuestCount > 0)}";

            if (signature != this.lastGateSignature)
            {
                var anchor = Anchors[11];
                var read = this.source.Read(anchor.Row, anchor.Title);
                this.Log($"transition: {DescribeGate(gate)} => {(reason == ProgressUnknownReason.None ? "READY" : "unknown:" + reason)}; character={CharacterTag(gate.ContentId)}; generation={this.source.CharacterGeneration}; guarded {anchor.Title}[{anchor.Row}] => {Describe(read)}; rawBit={this.RawBit(anchor.Row)}; rawPopCount={(bits is null ? "n/a" : PopCount(bits).ToString())}");
                this.lastGateSignature = signature;
            }

            var trusted = reason == ProgressUnknownReason.None;
            if (bits is not null && this.lastBits is not null && trusted && this.lastBitsTrusted)
            {
                this.LogFlips(this.lastBits, bits);
            }

            this.lastBits = bits;
            this.lastBitsTrusted = trusted;
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Follow probe watch tick failed; turning watch off.");
            this.SetWatching(false);
        }
    }

    private void LogFlips(byte[] before, byte[] after)
    {
        var flips = 0;
        for (var byteIndex = 0; byteIndex < before.Length && byteIndex < after.Length; byteIndex++)
        {
            var changed = before[byteIndex] ^ after[byteIndex];
            if (changed == 0)
            {
                continue;
            }

            for (var bit = 0; bit < 8; bit++)
            {
                if ((changed & (1 << bit)) == 0)
                {
                    continue;
                }

                if (++flips > MaxLoggedFlips)
                {
                    this.Log("flip: (more changes truncated)");
                    return;
                }

                var clientId = (uint)((byteIndex * 8) + bit);
                var row = clientId + QuestIdMapping.QuestRowBase;
                var nowSet = (after[byteIndex] & (1 << bit)) != 0;
                var guarded = this.source.Read(row, this.source.GetQuestTitle(row));
                var line = $"flip: row {row} \"{this.source.GetQuestTitle(row) ?? "(no row)"}\" raw {(nowSet ? "false -> true" : "true -> false")}; guarded now => {Describe(guarded)}";
                this.Log(line);
                this.Say(line);
            }
        }
    }

    private void OnCharacterInvalidated(string cause)
        => this.Log($"invalidated: cause={cause}; generation={this.source.CharacterGeneration}");

    private byte[]? SnapshotBits()
    {
        var questManager = QuestManager.Instance();
        if (questManager is null)
        {
            return null;
        }

        var bitArray = questManager->CompletedQuestsBitArray;
        return new ReadOnlySpan<byte>(bitArray.Pointer, bitArray.ByteLength).ToArray();
    }

    // Raw diagnostic: the bitfield bit for a row, with no gate. Framework thread only; never used by Follow.
    private string RawBit(uint questRow)
    {
        if (!this.framework.IsInFrameworkUpdateThread)
        {
            return "n/a(off-thread)";
        }

        var questManager = QuestManager.Instance();
        if (questManager is null)
        {
            return "n/a(no-quest-manager)";
        }

        var bitArray = questManager->CompletedQuestsBitArray;
        return QuestIdMapping.TryToClientId(questRow, bitArray.BitCount, out var clientId) && bitArray.TryGet(clientId, out var value)
            ? value.ToString().ToLowerInvariant()
            : "n/a(invalid-row)";
    }

    private IReadOnlyList<uint> FindRowsByTitle(string title)
    {
        try
        {
            return this.dataManager.GetExcelSheet<Quest>()
                .Where(row => QuestTitles.Matches(title, row.Name.ExtractText()))
                .Select(row => row.RowId)
                .ToArray();
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Quest title lookup failed for {Title}.", title);
            return [];
        }
    }

    private void Say(string message)
    {
        if (this.framework.IsInFrameworkUpdateThread)
        {
            this.chatGui.Print($"[followprobe] {message}", Tag);
        }
    }

    private void Log(string line)
    {
        var stamped = $"{DateTimeOffset.Now:yyyy-MM-dd HH:mm:ss.fff} {line}";
        Plugin.Log.Information("[followprobe] {Line}", line);
        try
        {
            lock (this.logLock)
            {
                Directory.CreateDirectory(this.OutputDirectory);
                File.AppendAllText(this.LogPath, stamped + Environment.NewLine);
            }
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Failed to append to the Follow probe log.");
        }
    }

    private static string Describe(QuestCompletionRead read)
        => read.Reason == ProgressUnknownReason.None ? read.State.ToString().ToLowerInvariant() : $"unknown({read.Reason})";

    private static string DescribeGate(ProgressGate gate)
        => $"thread={gate.OnFrameworkThread} loggedIn={gate.IsLoggedIn} playerLoaded={gate.PlayerLoaded} hasCharacter={gate.ContentId != 0} localPlayer={gate.LocalPlayerPresent} betweenAreas={gate.BetweenAreas} questData={gate.QuestDataAvailable} completed={gate.CompletedQuestCount}";

    // One-way short tag so logs can tell characters apart without recording who they are.
    private static string CharacterTag(ulong contentId)
    {
        if (contentId == 0)
        {
            return "none";
        }

        var hash = SHA256.HashData(Encoding.UTF8.GetBytes($"npclinks-followprobe:{contentId}"));
        return "char-" + Convert.ToHexString(hash, 0, 2).ToLowerInvariant();
    }

    private static int PopCount(byte[] bytes)
        => bytes.Sum(value => System.Numerics.BitOperations.PopCount(value));
}
#endif
