using Dalamud.Game.ClientState.Objects.Types;
using Dalamud.Plugin.Services;
using FFXIVClientStructs.FFXIV.Client.Game;
using FFXIVClientStructs.FFXIV.Client.Game.Event;
using FFXIVClientStructs.FFXIV.Client.Game.UI;
using Lumina.Excel.Sheets;
using NativeGameObject = FFXIVClientStructs.FFXIV.Client.Game.Object.GameObject;

namespace NpcDialogueLinks;

internal static class QuestProbeRuntime
{
    // Called synchronously while processing the Talk line. Only managed values leave this method.
    public static QuestProbeRuntimeSnapshot Capture(IDataManager dataManager, IGameObject? target)
        => new(
            TryRead("target event", () => ReadTargetEvent(target)),
            TryRead("event framework", ReadEventFramework),
            TryRead("quest journal", () => ReadJournal(dataManager)));

    private static unsafe QuestProbeTargetEvent? ReadTargetEvent(IGameObject? target)
    {
        if (target is null || !target.IsValid() || target.Address == 0)
        {
            return null;
        }

        var gameObject = (NativeGameObject*)target.Address;
        var handler = gameObject->EventHandler;
        return new QuestProbeTargetEvent(
            gameObject->EventId.Id,
            handler == null ? null : handler->Info.EventId.Id,
            handler == null ? null : handler->Scene);
    }

    private static unsafe QuestProbeEventFramework? ReadEventFramework()
    {
        var framework = EventFramework.Instance();
        if (framework == null)
        {
            return null;
        }

        // The framework can retain values between scenes. Keep the two sources distinct for comparison.
        return new QuestProbeEventFramework(
            framework->EventState1.EventId.Id,
            framework->EventState2.EventId.Id,
            framework->Scene);
    }

    private static unsafe QuestProbeJournal? ReadJournal(IDataManager dataManager)
    {
        var manager = QuestManager.Instance();
        if (manager == null)
        {
            return null;
        }

        var trackedSlots = new List<QuestProbeTrackedSlot>();
        var trackedNormalSlots = new HashSet<int>();
        var tracking = manager->TrackedQuests;
        for (var slot = 0; slot < tracking.Length; slot++)
        {
            var entry = tracking[slot];
            if (entry.QuestType == 0)
            {
                continue;
            }

            trackedSlots.Add(new QuestProbeTrackedSlot(slot, entry.QuestType, entry.Index));
            if (entry.QuestType == (byte)Journal.QuestType.NormalQuest)
            {
                trackedNormalSlots.Add(entry.Index);
            }
        }

        var activeQuests = new List<QuestProbeActiveQuest>();
        var normalQuests = manager->NormalQuests;
        for (var slot = 0; slot < normalQuests.Length; slot++)
        {
            var quest = normalQuests[slot];
            if (quest.QuestId == 0)
            {
                continue;
            }

            var rowId = new EventId { ContentId = EventHandlerContent.Quest, EntryId = quest.QuestId }.Id;
            var name = TryRead("quest name", () => dataManager.GetExcelSheet<Quest>().GetRowOrDefault(rowId)?.Name.ExtractText());
            activeQuests.Add(new QuestProbeActiveQuest(
                slot, quest.QuestId, rowId, name, quest.Sequence, trackedNormalSlots.Contains(slot)));
        }

        return new QuestProbeJournal(activeQuests, trackedSlots);
    }

    private static T? TryRead<T>(string source, Func<T?> read) where T : class
    {
        try
        {
            return read();
        }
        catch (Exception exception)
        {
            Plugin.Log.Debug(exception, "Quest probe could not read {Source}.", source);
            return null;
        }
    }
}

internal sealed record QuestProbeRuntimeSnapshot(
    QuestProbeTargetEvent? TargetEvent,
    QuestProbeEventFramework? EventFramework,
    QuestProbeJournal? Journal);

internal sealed record QuestProbeTargetEvent(uint EventId, uint? HandlerEventId, short? HandlerScene);

internal sealed record QuestProbeEventFramework(uint EventState1Id, uint EventState2Id, short Scene);

internal sealed record QuestProbeJournal(
    IReadOnlyList<QuestProbeActiveQuest> ActiveNormalQuests,
    IReadOnlyList<QuestProbeTrackedSlot> TrackedSlots);

internal sealed record QuestProbeActiveQuest(int Slot, ushort QuestId, uint RowId, string? Name, byte Sequence, bool Tracked);

internal sealed record QuestProbeTrackedSlot(int Slot, byte QuestType, byte Index);
