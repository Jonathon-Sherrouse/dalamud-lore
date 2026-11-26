# Quest Metadata Investigation

## Current status

Probe v3 (`NDL-015`) compares new `Talk` lines with local quest scripts in the client language. It reports a quest title when the normalized text matches exactly one quest across the scripts. Lines with zero or multiple matching quests have an unknown quest. Live validation of this build and quest identification for Lore Explain are pending.

## Checking automatic matches

1. Open `/xlplugins` → **Dev Tools** → **Installed Dev Plugins** and click **Reload** for **NPC Dialogue Links**.
2. Run `/npclinks questprobe on`. Wait for **Quest matching ready.** in chat before starting the conversation.
3. Talk to an ordinary NPC and check chat for **Quest: Unknown**. Then start a new line for a known quest objective or turn-in. Compare the title after **Quest:** with your journal. For an unexpected title or **Unknown** on a quest line, note the NPC, the expected journal title and the chat result.
4. Run `/npclinks questprobe off`. Use `/npclinks questprobe path` to locate the dated JSONL file. Each line is written as it is captured.

In a v3 record, `automaticMatch.status` gives the lookup result. A unique match carries `automaticMatch.questRowId` and `automaticMatch.questName`. To add an optional journal-verified label, use `/npclinks questprobe capture` followed by the exact journal title before advancing to the next line. For an ordinary NPC, use `NO QUEST`. The labeled copy carries your label in `userVerifiedQuestName` and shares its `lineId` and automatic match with the original record.

### Evidence from saved dialogue

During the v2 test, *One Step Behind* was tracked in both Oswold's ordinary greeting and Backrix's turn-in. Both lines had a target event ID of zero, two framework event IDs of zero, and a scene of `-1`. Those fields could not distinguish the two conversations.

An offline comparison checked the saved lines against 5,532 English quest scripts in the player's install. All 19 lines from *A Father's Grief*, three from *Getting to the Bottom of Things*, and one from *One Step Behind* matched their expected quest uniquely after trimming surrounding whitespace. The two labeled ordinary conversations had no matches. The live check above tests whether newly displayed lines give the same result in chat.

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

The plugin reads the dialogue from visible text nodes on `AddonTalk`. The probe also logs available `AtkValues` during `PreSetup`, `PostSetup`, `PreRefresh`, and `PostRefresh`. The first sample set below explains why v2 also looks at event and journal data.

## Second in-game sample pass

This was the manual-label workflow for v2. Use [Checking automatic matches](#checking-automatic-matches) for v3.

1. Load the v2 DLL and reload **NPC Dialogue Links** in `/xlplugins` → **Dev Tools** → **Installed Dev Plugins**. Run `/npclinks questprobe status` and confirm chat reports v2 with the probe disabled. The [dev plugin setup](atlas/README.md#loading-a-development-build) covers adding a new DLL location.
2. Run `/npclinks questprobe on`. As you talk to NPCs, each newly captured `Talk` line gets an automatic record.
3. Label samples while the probe is enabled, following the table below. A manual capture writes a labeled copy of the most recent recorded line with its original evidence. You can close the dialogue box or consult the journal first. Enter the label before the next dialogue line is captured.
4. Once you have labeled the final line, run `/npclinks questprobe off`. This clears the line available for labeling. Use `/npclinks questprobe path` to find `quest-probe-YYYYMMDD.jsonl`. Look for records with `schemaVersion` equal to `2`. Each labeled copy shares its `lineId` with its automatic record. Check the dialogue and the label on that pair.

| Sample | What to enter |
|---|---|
| Ordinary conversation with a non-quest NPC | `/npclinks questprobe capture NO QUEST` |
| Two or three lines from an active sidequest | After each line, enter `/npclinks questprobe capture` followed by a space and the exact journal title. For example, use `/npclinks questprobe capture A Father's Grief` if that is the quest you played. |
| A different sidequest or MSQ | Use its exact journal title. Any accessible quest works. Capturing *Getting to the Bottom of Things* would also allow comparison with the first pass. |
| Repeatable quest or cutscene-adjacent conversation, if available | Use the quest title only for a line you can independently associate with it. Leave uncertain lines unlabeled. |

The local records include the dialogue, matched dictionary terms, zone and target context, recent addon events, and available event and journal evidence at capture time. The output supports offline comparison.

| V2 field under `runtime` | What to compare |
|---|---|
| `targetEvent` | The selected object's event ID and its handler's event ID and scene when available. |
| `eventFramework` | The two event-state IDs and scene number. These values may persist between scenes. |
| `journal.activeNormalQuests` | The active normal quest slots, short quest IDs, full sheet row IDs, available names, sequences and tracked flags. |
| `journal.trackedSlots` | Occupied tracking slots with their raw type and index, including other quest types. |

An omitted section was unavailable. A present journal with empty lists means the probe read the slots and found no entries. Older records in the same file can be recognized by the absence of `schemaVersion`.

## Initial Probe Findings

First captured sample set, May 17, 2026:

- `A Father's Grief`: quest dialogue with target `Hunmu Rruk`
- `NO QUEST`: ordinary talk with target `Wuk Duxun`
- `Getting to the Bottom of Things`: quest dialogue with target `Hopeful Swimmer`; this was entered as `RandomQuest` during capture and should be normalized during analysis

The captured `Talk` addon values did not expose an obvious quest id or quest row. Values `[5] = 61` and `[11] = 1080` appeared across quest and non-quest samples, while value `[2]` varied within the same quest sample set. Target base ids identified the NPC/object variant being spoken to, but did not by themselves prove quest ownership.

These samples showed why the next pass needs event identifiers and active quest data alongside the existing addon values.

## Interpreting v2 captures

Compare event identifiers on the labeled quest lines with their independently verified journal titles and quest rows. The same quest should be identifiable across multiple lines, and an ordinary conversation should remain unassigned even when a quest is tracked. Keep observations with missing fields in the sample set so the coverage gap is visible.

Active or tracked quest membership alone only tells us what was in the journal. Before exposing a quest in Lore Explain, identify a field that directly maps the active line to a quest row, verify it across the sample types above, and resolve its name from `Lumina.Excel.Sheets.Quest`. Only a validated source can set `QuestConfidence` to `"verified"`.

## Fallback Behavior

Until runtime validation identifies a direct source of truth, omit quest metadata entirely. Continue sending zone, territory, map id, recent dialogue history, dictionary terms, and best-effort speaker/target metadata exactly as before.
