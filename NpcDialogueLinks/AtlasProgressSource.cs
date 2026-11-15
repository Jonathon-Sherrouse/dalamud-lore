using Dalamud.Game.ClientState.Conditions;
using Dalamud.Plugin.Services;
using FFXIVClientStructs.FFXIV.Client.Game;
using Lumina.Excel.Sheets;
using NpcDialogueLinks.Progress;

namespace NpcDialogueLinks;

/// <summary>
/// NDL-007: the read-only source Follow may use. It reads the client's completed-quest flags for authored
/// Lumina Quest rows and answers complete, incomplete or unknown. It never writes game state, never hooks,
/// never touches the network, never looks at active quests or the journal, and never uses QuestMetadataProbe.
/// Every read is gated (framework thread, logged in, player loaded, not loading, quest data present) and every
/// failure reads as unknown.
/// </summary>
/// <remarks>
/// Dalamud's <c>IUnlockState.IsQuestCompleted</c> is deliberately not used: it returns <c>false</c> when the
/// player state isn't loaded, which would turn "unknown" into "incomplete".
/// </remarks>
internal sealed unsafe class AtlasProgressSource : IDisposable
{
    private readonly IFramework framework;
    private readonly IClientState clientState;
    private readonly IPlayerState playerState;
    private readonly ICondition condition;
    private readonly IObjectTable objectTable;
    private readonly IDataManager dataManager;
    private readonly CharacterTracker characters = new();

    public AtlasProgressSource(
        IFramework framework,
        IClientState clientState,
        IPlayerState playerState,
        ICondition condition,
        IObjectTable objectTable,
        IDataManager dataManager)
    {
        this.framework = framework;
        this.clientState = clientState;
        this.playerState = playerState;
        this.condition = condition;
        this.objectTable = objectTable;
        this.dataManager = dataManager;
        this.clientState.Login += this.OnLogin;
        this.clientState.Logout += this.OnLogout;
    }

    /// <summary>Raised on the framework thread whenever earlier results stop belonging to the current character.</summary>
    public event Action<string>? CharacterInvalidated;

    /// <summary>Tag results with this; when it changes, drop them (and any pending raise offer) and re-read.</summary>
    public int CharacterGeneration => this.characters.Generation;

    public bool HasCharacter => this.characters.Current.HasValue;

    public void Dispose()
    {
        this.clientState.Login -= this.OnLogin;
        this.clientState.Logout -= this.OnLogout;
    }

    /// <summary>Sample the gate. Off the framework thread nothing else is touched.</summary>
    public ProgressGate SampleGate()
    {
        if (!this.framework.IsInFrameworkUpdateThread)
        {
            return ProgressGate.OffThread;
        }

        try
        {
            var loggedIn = this.clientState.IsLoggedIn;
            var playerLoaded = loggedIn && this.playerState.IsLoaded;
            var contentId = playerLoaded ? this.playerState.ContentId : 0UL;
            var betweenAreas = this.condition[ConditionFlag.BetweenAreas] || this.condition[ConditionFlag.BetweenAreas51];
            var localPlayerPresent = this.objectTable.LocalPlayer is not null;
            var questManager = QuestManager.Instance();
            var completedCount = questManager is null ? 0 : questManager->CompletedQuestsBitArray.PopCount;

            return new ProgressGate(
                OnFrameworkThread: true,
                IsLoggedIn: loggedIn,
                PlayerLoaded: playerLoaded,
                ContentId: contentId,
                LocalPlayerPresent: localPlayerPresent,
                BetweenAreas: betweenAreas,
                QuestDataAvailable: questManager is not null,
                CompletedQuestCount: completedCount);
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Follow progress gate sampling failed; treating progress as unknown.");
            return ProgressGate.Failed;
        }
    }

    /// <summary>Read one quest. <paramref name="expectedTitle"/> is the authored title; a mismatch reads unknown.</summary>
    public QuestCompletionRead Read(uint questRowId, string? expectedTitle)
        => this.ReadMany([(questRowId, expectedTitle)])[0];

    /// <summary>Read several quests under one gate sample, so a batch can never mix states from two frames.</summary>
    public IReadOnlyList<QuestCompletionRead> ReadMany(IReadOnlyList<(uint QuestRowId, string? ExpectedTitle)> quests)
    {
        var gate = this.SampleGate();
        var reason = ProgressRules.Evaluate(gate);
        if (reason != ProgressUnknownReason.None)
        {
            return quests.Select(quest => QuestCompletionRead.Unknown(quest.QuestRowId, reason)).ToArray();
        }

        if (this.characters.Observe(gate.ContentId))
        {
            this.RaiseInvalidated("character changed between reads");
        }

        var questManager = QuestManager.Instance();
        if (questManager is null)
        {
            return quests.Select(quest => QuestCompletionRead.Unknown(quest.QuestRowId, ProgressUnknownReason.QuestDataUnavailable)).ToArray();
        }

        var bitCount = questManager->CompletedQuestsBitArray.BitCount;
        var results = new QuestCompletionRead[quests.Count];
        for (var index = 0; index < quests.Count; index++)
        {
            results[index] = this.ReadOne(quests[index].QuestRowId, quests[index].ExpectedTitle, bitCount);
        }

        return results;
    }

    /// <summary>The game's title for a quest row, or null when the row doesn't exist. Static data; safe anywhere.</summary>
    public string? GetQuestTitle(uint questRowId)
    {
        try
        {
            return this.dataManager.GetExcelSheet<Quest>().TryGetRow(questRowId, out var row)
                ? row.Name.ExtractText()
                : null;
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Failed to resolve quest row {QuestRowId}.", questRowId);
            return null;
        }
    }

    private QuestCompletionRead ReadOne(uint questRowId, string? expectedTitle, int bitCount)
    {
        if (!QuestIdMapping.TryToClientId(questRowId, bitCount, out var clientId))
        {
            return QuestCompletionRead.Unknown(questRowId, ProgressUnknownReason.InvalidQuestRow);
        }

        var title = this.GetQuestTitle(questRowId);
        if (string.IsNullOrWhiteSpace(title))
        {
            return QuestCompletionRead.Unknown(questRowId, ProgressUnknownReason.InvalidQuestRow);
        }

        if (expectedTitle is not null && !QuestTitles.Matches(expectedTitle, title))
        {
            return QuestCompletionRead.Unknown(questRowId, ProgressUnknownReason.TitleMismatch);
        }

        try
        {
            return QuestCompletionRead.Known(questRowId, QuestManager.IsQuestComplete(clientId));
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Completed-quest read failed for row {QuestRowId}.", questRowId);
            return QuestCompletionRead.Unknown(questRowId, ProgressUnknownReason.ReadFailed);
        }
    }

    private void OnLogin()
    {
        this.characters.Invalidate();
        this.RaiseInvalidated("login");
    }

    private void OnLogout(int type, int code)
    {
        _ = type;
        _ = code;
        this.characters.Invalidate();
        this.RaiseInvalidated("logout");
    }

    private void RaiseInvalidated(string cause)
    {
        try
        {
            this.CharacterInvalidated?.Invoke(cause);
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "A Follow progress invalidation handler failed.");
        }
    }
}
