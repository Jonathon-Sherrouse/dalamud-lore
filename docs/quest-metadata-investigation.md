# Quest Metadata Investigation

## Answer

Current state: NpcDialogueLinks should not send quest metadata yet.

The plugin can identify broad scene context during `Talk` dialogue, but the current code and locally installed Dalamud/FFXIVClientStructs API surface do not expose a verified "current Talk dialogue belongs to quest X" value through a simple Dalamud service.

## Sources Checked

- `GameContextProvider` currently has `QuestName`, `QuestId`, and `QuestConfidence` fields, but no capture source.
- `LoreExplainClient` now sends quest fields only when `QuestConfidence == "verified"` and either quest id or name is present.
- `LoreExplainWindow` now displays quest context only when that same verified condition is met.
- Local Dalamud XML docs expose target object `DataId`, but not quest ownership for current dialogue.
- Local FFXIVClientStructs XML docs expose `QuestManager`, including accepted/tracked quests and quest sequence lookup.
- Local FFXIVClientStructs XML docs expose `QuestEventHandler`, `EventHandler`, `GameObject.EventId`, and scene-related fields that may be useful for runtime probing.
- Local FFXIVClientStructs XML docs expose `AgentScenarioTree` MSQ/job quest ids, but this represents guide state rather than the source quest for the active Talk line.

## Candidate Sources

`QuestManager`

Reliability for this feature: low by itself.

It can answer whether a known quest is active and what sequence it is on. It does not answer which active quest caused the current `Talk` addon line. Iterating active quests and matching by NPC/zone/objective would become inference, so it should not be sent as verified metadata.

`AgentScenarioTree`

Reliability for this feature: low by itself.

It can expose MSQ/job guide quest ids. This is useful for a future "current guide quest" hint, but it is not proof that the current NPC dialogue belongs to that quest. It also does not cover ordinary sidequests reliably.

Target object `DataId` / `EventId`

Reliability for this feature: unknown until runtime validation.

Dalamud exposes target object data ids, and FFXIVClientStructs documents `GameObject.EventId`. The event id may correlate with a quest or event handler in some cases, but the current plugin does not validate that relationship. This is a promising probe target, not a safe implementation source yet.

`QuestEventHandler` / `EventHandler`

Reliability for this feature: promising but unverified.

FFXIVClientStructs documents quest event handler and scene fields. These may provide the best path to verified context if runtime logging proves that a stable handler, info field, or event id maps directly to a quest row during `Talk`. Accessing these structures should be treated as pointer-sensitive and guarded with runtime validation.

`Talk` addon values

Reliability for this feature: unknown.

The current plugin only reads visible text nodes from `AddonTalk`. The XML docs do not identify a quest row/id field on `AddonTalk`. A debug probe should log `AtkValues` during `PreSetup`, `PostSetup`, `PreRefresh`, and `PostRefresh` across known scenarios before any implementation trusts addon values.

## Runtime Test Matrix

Not completed in this pass because it requires in-game scenarios. Test before enabling quest metadata:

- Normal non-quest NPC talk: expect no quest metadata.
- Active sidequest dialogue: expect one verified quest id/name or omission.
- MSQ dialogue: expect one verified quest id/name or omission.
- Repeatable/non-MSQ dialogue: expect verified id/name only when the event source is unambiguous.

## Current Probe Workflow

The plugin now has an opt-in probe command for gathering user-verifiable samples. It does not promote quest metadata to Lore Explain.

Commands:

```text
/npclinks questprobe on
/npclinks questprobe capture <verified quest name>
/npclinks questprobe off
/npclinks questprobe path
```

When enabled, the probe auto-exports each newly captured `Talk` dialogue line. The manual `capture` command writes another record for the current captured line with the quest name supplied by the user after verifying it in game.

Output path:

```text
<Dalamud plugin config>/quest-metadata-probes/quest-probe-YYYYMMDD.jsonl
```

Each JSONL record contains:

- captured dialogue text
- optional user-verified quest name
- local dictionary terms detected in the dialogue
- zone, territory, map, target, and best-effort speaker context
- target object identifiers, including base id, object ids, object kind, object index, and position
- recent `Talk` addon `PreSetup`, `PostSetup`, `PreRefresh`, and `PostRefresh` `AtkValue` snapshots

Next analysis step: collect samples for the matrix below and compare verified quest names against target identifiers and `AtkValue` values. Only promote a field if it maps directly and consistently to the active `Talk` line's quest.

## Initial Probe Findings

First captured sample set, May 17, 2026:

- `A Father's Grief`: quest dialogue with target `Hunmu Rruk`
- `NO QUEST`: ordinary talk with target `Wuk Duxun`
- `Getting to the Bottom of Things`: quest dialogue with target `Hopeful Swimmer`; this was entered as `RandomQuest` during capture and should be normalized during analysis

The captured `Talk` addon values did not expose an obvious quest id or quest row. Values `[5] = 61` and `[11] = 1080` appeared across quest and non-quest samples, while value `[2]` varied within the same quest sample set. Target base ids identified the NPC/object variant being spoken to, but did not by themselves prove quest ownership.

Conclusion from this sample set: `Talk` addon `AtkValues` are not enough for verified quest metadata. The next probe pass should capture native event/handler ids and active quest candidates, then compare those against user-verified quest names.

## Pickup Later

Status: paused after the first runtime probe sample analysis.

When resuming, do not ask the user to gather more samples with the current probe first. Upgrade the probe to a v2 capture format, then ask for a small second in-game sample pass.

Probe v2 should try to add:

- native target/event id if it can be accessed safely
- safe event-handler identifiers or scene fields, guarded against null pointers and runtime exceptions
- active/tracked quest ids, quest names, and quest sequence values from `QuestManager`
- the existing manual verified quest name, which remains the ground truth for analysis

Recommended second sample pass:

- normal NPC conversation labeled `NO QUEST`
- 2-3 lines from `A Father's Grief`
- 2-3 lines from `Getting to the Bottom of Things`
- one MSQ or unrelated sidequest, if convenient

Important note: `RandomQuest` in the first sample set means `Getting to the Bottom of Things`.

## Recommended Implementation Path

1. Add a debug-only quest probe command or setting that logs, for each new `Talk` line. Initial command/export support is implemented; runtime sample collection is pending.
   - visible dialogue text
   - target name, base id, and native `GameObject.EventId` if safely accessible
   - `Talk` addon `AtkValues` count/types/primitive values during setup and refresh
   - current `QuestManager.TrackedQuests` and active quest sequences
   - current `QuestEventHandler` or `EventHandler` fields only behind null checks and exception-safe guards
2. Run the test matrix and compare logs against known quest names from the in-game journal.
3. Promote a source only if it gives a direct quest row/id for the active dialogue, not just a plausible active quest.
4. Resolve the name from `Lumina.Excel.Sheets.Quest` using `IDataManager`.
5. Set `QuestConfidence = "verified"` only for that direct source.

## Fallback Behavior

Until runtime validation identifies a direct source of truth, omit quest metadata entirely. Continue sending zone, territory, map id, recent dialogue history, dictionary terms, and best-effort speaker/target metadata exactly as before.
