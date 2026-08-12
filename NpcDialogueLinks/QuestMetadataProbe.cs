using System.Text.Json;
using System.Text.Json.Serialization;
using Dalamud.Game.Addon.Lifecycle;
using Dalamud.Game.Addon.Lifecycle.AddonArgTypes;
using Dalamud.Game.ClientState.Objects.Types;
using Dalamud.Game.NativeWrapper;
using Dalamud.Plugin;
using Dalamud.Plugin.Services;

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

    public string OutputDirectory
        => Path.Combine(this.pluginInterface.ConfigDirectory.FullName, "quest-metadata-probes");

    public void SetEnabled(bool enabled)
    {
        this.Enabled = enabled;
        if (!enabled)
        {
            this.recentAddonSnapshots.Clear();
        }
    }

    public QuestProbeWriteResult CaptureDialogue(
        string source,
        string dialogue,
        string userVerifiedQuestName,
        LoreContextMetadata context,
        IReadOnlyList<string> knownTerms)
    {
        if (string.IsNullOrWhiteSpace(dialogue))
        {
            return new QuestProbeWriteResult(false, string.Empty, "No dialogue has been captured yet.");
        }

        try
        {
            Directory.CreateDirectory(this.OutputDirectory);
            var path = Path.Combine(this.OutputDirectory, $"quest-probe-{DateTimeOffset.Now:yyyyMMdd}.jsonl");
            var record = new QuestProbeRecord(
                CreatedAt: DateTimeOffset.Now,
                Source: source,
                Dialogue: dialogue,
                UserVerifiedQuestName: userVerifiedQuestName.Trim(),
                KnownTerms: knownTerms,
                Context: context,
                Target: this.CaptureTarget(),
                AddonEvents: this.GetRecentAddonSnapshots());

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

    private QuestProbeTargetSnapshot CaptureTarget()
    {
        var target = this.targetManager.Target;
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
    DateTimeOffset CreatedAt,
    string Source,
    string Dialogue,
    string UserVerifiedQuestName,
    IReadOnlyList<string> KnownTerms,
    LoreContextMetadata Context,
    QuestProbeTargetSnapshot Target,
    IReadOnlyList<TalkAddonEventSnapshot> AddonEvents);

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
