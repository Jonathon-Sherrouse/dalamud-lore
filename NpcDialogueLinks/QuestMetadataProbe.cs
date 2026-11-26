using System.Text.Json;
using System.Text.Json.Serialization;
using Dalamud.Game.Addon.Lifecycle;
using Dalamud.Game.Addon.Lifecycle.AddonArgTypes;
using Dalamud.Game.ClientState.Objects.Types;
using Dalamud.Game.NativeWrapper;
using Dalamud.Plugin;
using Dalamud.Plugin.Services;
using Dalamud.Utility;

namespace NpcDialogueLinks;

internal sealed class QuestMetadataProbe : IDisposable
{
    private const int MaxRecentAddonSnapshots = 24;
    private const int MaxAtkValuesPerSnapshot = 48;
    private const int MaxStringLength = 500;

    private static readonly JsonSerializerOptions SerializerOptions = new()
    {
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        WriteIndented = false,
    };

    private readonly IAddonLifecycle addonLifecycle;
    private readonly IClientState clientState;
    private readonly IDataManager dataManager;
    private readonly IDalamudPluginInterface pluginInterface;
    private readonly ITargetManager targetManager;
    private readonly List<TalkAddonEventSnapshot> recentAddonSnapshots = [];
    private QuestProbeRecord? lastLine;
    private CancellationTokenSource? indexCancellation;
    private Task<QuestDialogueIndex?>? indexLoad;

    public QuestMetadataProbe(
        IDalamudPluginInterface pluginInterface,
        IAddonLifecycle addonLifecycle,
        IClientState clientState,
        IDataManager dataManager,
        ITargetManager targetManager)
    {
        this.pluginInterface = pluginInterface;
        this.addonLifecycle = addonLifecycle;
        this.clientState = clientState;
        this.dataManager = dataManager;
        this.targetManager = targetManager;

        this.addonLifecycle.RegisterListener(AddonEvent.PreSetup, "Talk", this.OnTalkAddonEvent);
        this.addonLifecycle.RegisterListener(AddonEvent.PostSetup, "Talk", this.OnTalkAddonEvent);
        this.addonLifecycle.RegisterListener(AddonEvent.PreRefresh, "Talk", this.OnTalkAddonEvent);
        this.addonLifecycle.RegisterListener(AddonEvent.PostRefresh, "Talk", this.OnTalkAddonEvent);
    }

    public bool Enabled { get; private set; }

    public string MatchStatus => this.indexLoad switch
    {
        null => "disabled",
        { IsCompleted: false } => "loading",
        { IsCompletedSuccessfully: true, Result: not null } => "ready",
        _ => "unavailable",
    };

    public string OutputDirectory
        => Path.Combine(this.pluginInterface.ConfigDirectory.FullName, "quest-metadata-probes");

    public void SetEnabled(bool enabled)
    {
        if (this.Enabled == enabled)
        {
            return;
        }

        this.Enabled = enabled;
        if (enabled)
        {
            var path = this.dataManager.GameData.DataPath.FullName;
            var language = this.dataManager.Language.ToLumina();
            this.indexCancellation = new CancellationTokenSource();
            var token = this.indexCancellation.Token;
            this.indexLoad = Task.Run<QuestDialogueIndex?>(() =>
            {
                try
                {
                    return QuestDialogueIndex.Build(path, language, token);
                }
                catch (OperationCanceledException) when (token.IsCancellationRequested)
                {
                    return null;
                }
                catch (Exception exception)
                {
                    Plugin.Log.Warning(exception, "Could not load the quest dialogue scripts.");
                    return null;
                }
            }, token);
        }
        else
        {
            this.indexCancellation?.Cancel();
            this.indexCancellation?.Dispose();
            this.indexCancellation = null;
            this.indexLoad = null;
            this.lastLine = null;
            this.recentAddonSnapshots.Clear();
        }
    }

    public QuestProbeWriteResult CaptureDialogue(
        string dialogue,
        Func<LoreContextMetadata> captureContext,
        IReadOnlyList<string> knownTerms)
    {
        // A failure on a new line must never leave the previous line available for labeling.
        this.lastLine = null;
        try
        {
            var loggedIn = this.clientState.IsLoggedIn;
            var target = loggedIn ? this.targetManager.Target : null;
            if (target is not null && !target.IsValid())
            {
                target = null;
            }
            var status = this.MatchStatus;
            var match = status == "ready"
                ? this.indexLoad!.Result!.Match(dialogue)
                : new QuestDialogueMatch(status, null, null);
            var record = new QuestProbeRecord(
                SchemaVersion: 3,
                LineId: Guid.NewGuid(),
                CreatedAt: DateTimeOffset.Now,
                Source: "auto-dialogue",
                Dialogue: dialogue,
                UserVerifiedQuestName: string.Empty,
                KnownTerms: knownTerms,
                Context: loggedIn ? captureContext() : LoreContextMetadata.Empty,
                Target: this.CaptureTarget(target),
                AddonEvents: this.GetRecentAddonSnapshots(),
                Runtime: loggedIn ? QuestProbeRuntime.Capture(this.dataManager, target) : null,
                AutomaticMatch: match);
            var result = this.Write(record);
            if (result.Succeeded)
            {
                this.lastLine = record;
                var message = match.Status switch
                {
                    "unique" => $"Quest: {match.QuestName}",
                    "ambiguous" => "Quest: Unknown (shared line).",
                    "unknown" => "Quest: Unknown.",
                    "loading" => "Quest matching is still loading.",
                    _ => "Quest matching unavailable.",
                };
                return result with { Message = message };
            }

            return result;
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Failed to capture quest metadata probe.");
            return new QuestProbeWriteResult(false, string.Empty, $"Failed to capture quest probe: {exception.Message}");
        }
    }

    public QuestProbeWriteResult LabelLastDialogue(string label)
    {
        if (this.lastLine is null)
        {
            return new QuestProbeWriteResult(false, string.Empty, "Enable the quest probe and talk to an NPC before labeling a line.");
        }

        if (string.IsNullOrWhiteSpace(label))
        {
            return new QuestProbeWriteResult(false, string.Empty, "Enter the journal quest name, or NO QUEST for ordinary NPC dialogue.");
        }

        var marked = this.lastLine with { Source = "manual-capture", UserVerifiedQuestName = label.Trim() };
        var result = this.Write(marked);
        if (!result.Succeeded)
        {
            return result;
        }

        var excerpt = marked.Dialogue.Length <= 100 ? marked.Dialogue : marked.Dialogue[..100] + "…";
        return result with { Message = $"Labeled “{excerpt}” as {marked.UserVerifiedQuestName}." };
    }

    private QuestProbeWriteResult Write(QuestProbeRecord record)
    {
        try
        {
            Directory.CreateDirectory(this.OutputDirectory);
            var path = Path.Combine(this.OutputDirectory, $"quest-probe-{record.CreatedAt:yyyyMMdd}.jsonl");
            File.AppendAllText(path, JsonSerializer.Serialize(record, SerializerOptions) + Environment.NewLine);
            return new QuestProbeWriteResult(true, path, $"Quest probe captured: {path}");
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Failed to write quest metadata probe.");
            return new QuestProbeWriteResult(false, string.Empty, $"Failed to write quest probe: {exception.Message}");
        }
    }

    public void Dispose()
    {
        this.SetEnabled(false);
        this.addonLifecycle.UnregisterListener(this.OnTalkAddonEvent);
    }

    private void OnTalkAddonEvent(AddonEvent eventType, AddonArgs args)
    {
        if (!this.Enabled)
        {
            return;
        }

        try
        {
            this.recentAddonSnapshots.Add(CaptureAddonSnapshot(eventType, args));
            if (this.recentAddonSnapshots.Count > MaxRecentAddonSnapshots)
            {
                this.recentAddonSnapshots.RemoveRange(0, this.recentAddonSnapshots.Count - MaxRecentAddonSnapshots);
            }
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Failed to capture Talk addon quest probe snapshot.");
        }
    }

    private IReadOnlyList<TalkAddonEventSnapshot> GetRecentAddonSnapshots()
        => this.recentAddonSnapshots.ToArray();

    private QuestProbeTargetSnapshot CaptureTarget(IGameObject? target)
    {
        if (target is null)
        {
            return QuestProbeTargetSnapshot.Empty;
        }

        return new QuestProbeTargetSnapshot(
            Name: Normalize(target.Name.ToString()),
            ObjectKind: target.ObjectKind.ToString(),
            SubKind: target.SubKind,
            BaseId: target.BaseId,
            GameObjectId: target.GameObjectId.ToString(),
            EntityId: target.EntityId.ToString(),
            OwnerId: target.OwnerId.ToString(),
            ObjectIndex: target.ObjectIndex,
            TargetObjectId: target.TargetObjectId.ToString(),
            Address: FormatPointer(target.Address),
            Position: new QuestProbePosition(target.Position.X, target.Position.Y, target.Position.Z),
            TerritoryType: this.clientState.TerritoryType,
            MapId: this.clientState.MapId);
    }

    private static TalkAddonEventSnapshot CaptureAddonSnapshot(AddonEvent eventType, AddonArgs args)
    {
        return new TalkAddonEventSnapshot(
            CapturedAt: DateTimeOffset.Now,
            EventType: eventType.ToString(),
            AddonAddress: args.Addon.IsNull ? string.Empty : FormatPointer(args.Addon.Address),
            AtkValueCount: GetAtkValueCount(args),
            AtkValues: CaptureAtkValues(args));
    }

    private static uint GetAtkValueCount(AddonArgs args)
        => args switch
        {
            AddonSetupArgs setupArgs => setupArgs.AtkValueCount,
            AddonRefreshArgs refreshArgs => refreshArgs.AtkValueCount,
            _ => 0u,
        };

    private static IReadOnlyList<QuestProbeAtkValue> CaptureAtkValues(AddonArgs args)
    {
        IEnumerable<AtkValuePtr> values = args switch
        {
            AddonSetupArgs setupArgs => setupArgs.AtkValueEnumerable,
            AddonRefreshArgs refreshArgs => refreshArgs.AtkValueEnumerable,
            _ => Array.Empty<AtkValuePtr>(),
        };

        var snapshots = new List<QuestProbeAtkValue>();
        var index = 0;
        foreach (var value in values.Take(MaxAtkValuesPerSnapshot))
        {
            snapshots.Add(CaptureAtkValue(index, value));
            index++;
        }

        return snapshots;
    }

    private static QuestProbeAtkValue CaptureAtkValue(int index, AtkValuePtr value)
    {
        object? rawValue = null;
        string? error = null;

        try
        {
            rawValue = value.GetValue();
        }
        catch (Exception exception)
        {
            error = exception.GetType().Name;
        }

        return new QuestProbeAtkValue(
            Index: index,
            Address: value.IsNull ? string.Empty : FormatPointer(value.Address),
            Type: value.IsNull ? "Null" : value.ValueType.ToString(),
            Value: NormalizeValue(rawValue),
            Error: error);
    }

    private static string NormalizeValue(object? value)
    {
        if (value is null)
        {
            return string.Empty;
        }

        return Truncate(Normalize(value.ToString() ?? string.Empty));
    }

    private static string Normalize(string value)
        => value.ReplaceLineEndings(" ").Trim();

    private static string Truncate(string value)
        => value.Length <= MaxStringLength ? value : value[..MaxStringLength];

    private static string FormatPointer(IntPtr pointer)
        => pointer == IntPtr.Zero ? string.Empty : $"0x{pointer.ToInt64():X}";
}

internal sealed record QuestProbeWriteResult(bool Succeeded, string Path, string Message);

internal sealed record QuestProbeRecord(
    int SchemaVersion,
    Guid LineId,
    DateTimeOffset CreatedAt,
    string Source,
    string Dialogue,
    string UserVerifiedQuestName,
    IReadOnlyList<string> KnownTerms,
    LoreContextMetadata Context,
    QuestProbeTargetSnapshot Target,
    IReadOnlyList<TalkAddonEventSnapshot> AddonEvents,
    QuestProbeRuntimeSnapshot? Runtime,
    QuestDialogueMatch AutomaticMatch);

internal sealed record QuestProbeTargetSnapshot(
    string Name,
    string ObjectKind,
    byte SubKind,
    uint BaseId,
    string GameObjectId,
    string EntityId,
    string OwnerId,
    ushort ObjectIndex,
    string TargetObjectId,
    string Address,
    QuestProbePosition Position,
    uint TerritoryType,
    uint MapId)
{
    public static QuestProbeTargetSnapshot Empty { get; } = new(
        Name: string.Empty,
        ObjectKind: string.Empty,
        SubKind: 0,
        BaseId: 0,
        GameObjectId: string.Empty,
        EntityId: string.Empty,
        OwnerId: string.Empty,
        ObjectIndex: 0,
        TargetObjectId: string.Empty,
        Address: string.Empty,
        Position: new QuestProbePosition(0, 0, 0),
        TerritoryType: 0,
        MapId: 0);
}

internal sealed record QuestProbePosition(float X, float Y, float Z);

internal sealed record TalkAddonEventSnapshot(
    DateTimeOffset CapturedAt,
    string EventType,
    string AddonAddress,
    uint AtkValueCount,
    IReadOnlyList<QuestProbeAtkValue> AtkValues);

internal sealed record QuestProbeAtkValue(
    int Index,
    string Address,
    string Type,
    string Value,
    string? Error);
