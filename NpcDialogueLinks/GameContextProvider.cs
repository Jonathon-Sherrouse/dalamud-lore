using Dalamud.Plugin.Services;
using Lumina.Excel.Sheets;

namespace NpcDialogueLinks;

internal sealed class GameContextProvider
{
    private readonly IClientState clientState;
    private readonly IDataManager dataManager;
    private readonly ITargetManager targetManager;

    public GameContextProvider(IClientState clientState, IDataManager dataManager, ITargetManager targetManager)
    {
        this.clientState = clientState;
        this.dataManager = dataManager;
        this.targetManager = targetManager;
    }

    public LoreContextMetadata Capture()
    {
        var territoryType = this.clientState.TerritoryType;
        var mapId = this.clientState.MapId;
        var zoneName = this.ResolveZoneName(territoryType);
        var targetName = Normalize(this.targetManager.Target?.Name.ToString() ?? string.Empty);

        return new LoreContextMetadata(
            ZoneName: zoneName,
            TerritoryType: territoryType,
            MapId: mapId,
            TargetName: targetName,
            SpeakerName: targetName,
            SpeakerConfidence: string.IsNullOrWhiteSpace(targetName) ? "unavailable" : "target-name-best-effort",
            QuestName: string.Empty,
            QuestId: null,
            QuestConfidence: string.Empty);
    }

    private string ResolveZoneName(uint territoryType)
    {
        if (territoryType == 0)
        {
            return string.Empty;
        }

        try
        {
            var sheet = this.dataManager.GetExcelSheet<TerritoryType>();
            var row = sheet.GetRow(territoryType);
            return Normalize(row.PlaceName.Value.Name.ToString());
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Failed to resolve territory {TerritoryType} to a zone name.", territoryType);
            return string.Empty;
        }
    }

    private static string Normalize(string value)
        => value.Trim();
}

internal sealed record LoreContextMetadata(
    string ZoneName,
    uint TerritoryType,
    uint MapId,
    string TargetName,
    string SpeakerName,
    string SpeakerConfidence,
    string QuestName,
    uint? QuestId,
    string QuestConfidence)
{
    public static LoreContextMetadata Empty { get; } = new(
        ZoneName: string.Empty,
        TerritoryType: 0,
        MapId: 0,
        TargetName: string.Empty,
        SpeakerName: string.Empty,
        SpeakerConfidence: "unavailable",
        QuestName: string.Empty,
        QuestId: null,
        QuestConfidence: string.Empty);

    public bool HasAnyContext
        => !string.IsNullOrWhiteSpace(this.ZoneName) ||
           this.TerritoryType != 0 ||
           this.MapId != 0 ||
           !string.IsNullOrWhiteSpace(this.TargetName) ||
           !string.IsNullOrWhiteSpace(this.SpeakerName) ||
           !string.IsNullOrWhiteSpace(this.QuestName) ||
           this.QuestId.HasValue;

    public bool HasVerifiedQuestContext
        => (!string.IsNullOrWhiteSpace(this.QuestName) || this.QuestId.HasValue) &&
           string.Equals(this.QuestConfidence, "verified", StringComparison.OrdinalIgnoreCase);
}
