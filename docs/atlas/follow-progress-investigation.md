# Follow progress investigation (`NDL-007`)

The user accepted the investigation for merge on November 26, 2026. The two-character in-game checks below are pending. **`NDL-017` (2026-11-26) builds Atlas Follow on this adapter**; see the [plan's amendments](v2-plan.md#ndl-017-amendments).

This investigation asks whether the client's completed-quest flags can safely drive the Atlas **Follow** toggle. The [Follow plan](v2-plan.md#follow-completed-story-progress) defines its criteria. The separate [quest dialogue investigation](../quest-metadata-investigation.md) covers matching NPC lines to quest scripts.

## Short answer so far

The source looks sound **if** it's read through a strict gate, and **if** NDL-006 authors every alternative row for a story step. The in-game run decides the rest.

| # | Exit criterion | Agent evidence | In-game | Verdict |
|---|---|---|---|---|
| 1 | Flag false before, true after, for known pairs, on two characters at different progress | The probe logs live flips and per-character anchor reads | Pending | **Pending** |
| 2 | Lumina row → client ID verified, plus a title cross-check that disables Follow on mismatch | Verified in decompiled ClientStructs and Dalamud code and against the local game data; host-tested | Pending (anchor titles and negatives live) | **Pending** |
| 3 | Framework thread and logged in only; logged out or loading reads unknown | Gate implemented and host-tested; the probe tests off-thread and logs every transition | Pending | **Pending** |
| 4 | A character switch invalidates and re-reads | Character generation implemented and host-tested | Pending (logout → other character) | **Pending** |
| 5 | Story-skip behaviour documented | See [Story skips](#story-skips) | Not applicable (no skip used) | See section |

## The source

`NpcDialogueLinks/AtlasProgressSource.cs` (adapter, outside `Atlas/`), and `NpcDialogueLinks/Progress/QuestProgress.cs` (pure rules, host-tested).

- **Read:** FFXIVClientStructs `QuestManager.IsQuestComplete(ushort clientId)`, the game's own completion check. Nothing else feeds Follow.
- **Dalamud's `IUnlockState.IsQuestCompleted(Quest)`, only behind the gate.** `NDL-007` didn't use it. Since `NDL-017` it supplies the flag, but only after the gate below has passed. The decompiled Dalamud shows it returns `false` whenever `PlayerState` isn't loaded:

  ```csharp
  public bool IsQuestCompleted(Quest row)
  {
      if (!IsLoaded) return false;            // logged out reads as "incomplete"
      return QuestManager.IsQuestComplete(row.RowId);
  }
  ```

  Called on its own, that's exactly the unknown-as-incomplete mistake the contract forbids. Behind the gate, which already requires a loaded player, it's the same `QuestManager.IsQuestComplete` read.
- **Read-only.** No hooks, no network, no game-state writes. No active-quest, journal or `QuestMetadataProbe` input.

## Criterion 2: row → client ID

**Conversion rule:** `clientId = rowId − 0x10000`.
- **Rejected rows:**
  - rows outside `0x10001..0x1FFFF`;
  - client ID 0;
  - IDs past the end of the completed-quest bitfield.
- **Each rejected row** reads `unknown(InvalidQuestRow)`. A bare `& 0xFFFF` would wrap them silently instead.

**Evidence:**
- **ClientStructs** (decompiled from the user's installed `FFXIVClientStructs.dll`) applies the same `& 0xFFFF` mask:

  ```csharp
  public static bool IsQuestComplete(uint questId) => IsQuestComplete((ushort)(questId & 0xFFFF));
  ```

- **Dalamud** passes the Lumina `row.RowId` straight into that overload (see above). So the two projects agree on the mapping.
- **The completed-quest bitfield** is `QuestManager._completedQuests`: 751 bytes, exposed as a 6,008-bit array. Bits are read least-significant first, as in `ptr[i/8] & (1 << i%8)`.
- **Local game data** (the Lumina Quest sheet, read offline from the user's install on 2026-11-14) has 5,533 rows, `65536..71068`. That's client IDs `0..5532`, all inside the bitfield.
- **In game,** the probe compares the native check with the raw bit for every anchor (`rawBit=` in the log). Agreement confirms the bit order; disagreement fails this criterion.

**Title cross-check.** The adapter compares the authored title with the game's title for that row. A mismatch reads `unknown(TitleMismatch)`, and `CombineAlternatives` makes the whole step unknown, so Follow can't move.

Normalisation is limited to harmless differences:
- Unicode form;
- curly vs straight quotes;
- non-breaking and repeated spaces.

Case and wording stay strict. The probe runs a deliberate mismatch (row 70058 authored as "Before the Dawn") and three invalid rows.

### Finding: one title, several rows

The title cross-check **can't** catch everything, because the quest sheet reuses titles:

- **Starting-city variants** (legitimate): "Close to Home" has 8 current MSQ rows (65621, 65644, 65645, 65659, 65660, 66104, 66105, 66106). "Call of the Sea" and "On Track" also repeat.
- **Retired rows and their replacements.** 180 rows sit in a hidden category ("Sephiroth Missions", no journal genre). 79 of them carry old ARR main-scenario-style IDs (`Gai…`/`Man…`); the rest are mostly old class and side quests. Their replacements are new rows with the same title:
  - 37 `Xxa…` rows from the **patch 5.3** ARR abridgement (Aug 2020), for example "Chasing Ivy" 65615 → 69422 and "Moving On" 66712 → 69410;
  - 3 `Xxc…` rows: "Operation Archon" 66572 → 70057 and "The Ultimate Weapon" 66060 → 70058 (**patch 6.1**, Apr 2022), plus "The Steps of Faith" 65955 → 70127 (**patch 6.2**).

So a title match can still point at the wrong (retired) row.

**Open in-game question:** for a veteran who finished ARR before the rows were replaced, which bits are set, the old row, the new row, or both?

- **What the patch notes say:**
  - The 6.1 notes say players who "have completed the main scenario quest 'The Ultimate Weapon' as of Patch 6.08" keep access to what follows. They never say the completion was copied to the new row ([Patch 6.1 notes](https://na.finalfantasyxiv.com/lodestone/topics/detail/808eb196b065ebd1b6ec130fac1402d99f7f90a4)).
  - The 5.3 notes (seen only through a [third-party mirror](https://www.diffchecker.com/9K9y45IM)) say journal entries for removed quests disappear "even if they are quests you have already completed".
- **A hint from other plugins:** the Questionable plugin remaps old row 524 to new 4522 when it reads prerequisites ([QuestInfo.cs](https://github.com/PunishXIV/Questionable/blob/HEAD/Questionable/Domain/QuestInfo.cs)). So old rows still matter in the game data.
- **Undocumented:** nobody documents what the bits hold. The probe reads both rows of each pair on whatever characters the user has.
- **If a veteran has only the old bit set,** a step authored with only the new row reads incomplete. Follow would then stop early. That direction is safe for spoilers, but it's wrong.

**Recommendations for `NDL-006`** (its schema, not changed here):
- `gameQuestIds` means **alternatives**. A step is complete if any listed row is complete. `ProgressRules.CombineAlternatives` implements and tests that rule: a data error on any row makes the step unknown.
- The generator should refuse rows in the retired category, unless a retired row is deliberately listed beside its replacement as an alternative, after the in-game veteran read shows whether that's needed.
- Author all 8 "Close to Home" rows (and the other starting-city variants) if any such step is covered.

## Criterion 3: threads, login and loading

Every read samples one gate and evaluates it in this order (`ProgressRules.Evaluate`). The first failure decides the reason, and every failure is unknown.

| Order | Condition | Unknown reason |
|---|---|---|
| 1 | `IFramework.IsInFrameworkUpdateThread` | `NotFrameworkThread`. Nothing else is sampled. |
| 2 | Gate sampling didn't throw | `ReadFailed` |
| 3 | `IClientState.IsLoggedIn` | `LoggedOut` |
| 4 | `IPlayerState.IsLoaded` | `PlayerNotLoaded` |
| 5 | `IPlayerState.ContentId != 0` | `NoCharacter` |
| 6 | Not `BetweenAreas`/`BetweenAreas51`, and a local player object exists | `Loading` |
| 7 | `QuestManager.Instance()` non-null | `QuestDataUnavailable` |
| 8 | At least one completed quest | `QuestDataEmpty`. A logged-in character with zero completions can't be told apart from "the list hasn't arrived". The cost is that a brand-new character sees "unknown" instead of "before coverage", and the view doesn't move in either case. |

Notes:
- **`IsInFrameworkUpdateThread` is a thread-identity check** (`Thread.CurrentThread == BoundThread`), not "inside the Update callback". Chat commands and Update both qualify.
- **Whether `UiBuilder.Draw` qualifies** is unconfirmed. The probe's `thread` command logs it. **For `NDL-010`:** if it logs `false`, the Atlas window must marshal reads with `IFramework.RunOnFrameworkThread`. Otherwise every read from the window reads unknown, which is safe but useless.
- **Dalamud's `Login` event** fires on the first framework tick where conditions exist and the local player object is present. The gate doesn't rely on it.
- **Watch mode** logs every gate transition with a guarded read beside a raw (ungated, diagnostic-only) bit and the bit count. That shows what the raw flags hold at character select and during loading, which is the reason the gate exists.

## Criterion 4: character switch

`CharacterTracker` (host-tested) holds the content ID of the last trustworthy read and a **generation** number.

- **Login and logout** each forget the character and bump the generation.
- **A read that sees a different content ID** without a logout in between also bumps it, and raises `CharacterInvalidated`.
- **Consumers tag** a Follow result, or a pending raise offer, with the generation. When it changes, they drop the result and re-read, which matches the plan's "clears the previous result and any pending raise".
- **Privacy:** logs never record names or content IDs, only a short one-way tag (`char-xxxx`).

## Story skips

Researched on the web on 2026-11-14 (sources below). No skip item was used in the in-game run.

**What a skip does** ([Tales of Adventure](https://na.finalfantasyxiv.com/tales_of_adventure/), official):
- **Completion:** the items "flag the corresponding title as completed, and take you to the start of the subsequent storyline". For A Realm Reborn: "All main scenario quests within A Realm Reborn will be completed automatically."
- **Variants:** "Completed quests will be associated with the player's starting city and class." So only one starting-city variant of each opening quest is flagged. That's the same as a normal player, which is why steps combine alternatives with "any".
- **Limits:**
  - Not usable on a Free Trial account.
  - Not usable past the item's end quest (A Realm Reborn: "Before the Dawn").
  - Usable only in a sanctuary, and using one logs the character out.
  - It doesn't raise level.
- **No automatic skips:** no source describes one for new or Free Trial characters.
- **Side content isn't covered:** the page doesn't mention Crystal Tower, side quests or feature quests. Whether a skip flags them is undocumented.

**What that means for Follow:**
- **A skipped character reads as having completed every skipped main-story quest,** and Follow places them there. That's correct by the contract's own definition ("completed story progress"), even though they never saw that story. The spoiler **limit** still governs what's shown, because Follow never raises it.
- **Optional steps** (the "main + optional" content view) might read incomplete on a skipped character even when the main story around them reads complete. Follow's position comes from covered **main-story** steps only, so this doesn't affect it. Don't extend Follow to optional content without new evidence.
- **The logout matters.** Using a skip logs the character out, and the adapter invalidates the character on every logout (criterion 4), so no pre-skip result survives.
- **Not verified in game.** Nobody used a skip during this investigation; only the documentation above backs these points.

**Rejected alternative:** the `ScenarioTree` sheet with `AgentScenarioTree`, which some plugins use for an overall main-story position. `AgentScenarioTree` is the game's main-story guide, which is journal/guide state, and the contract allows only completion flags. Recorded here so it isn't reproposed without a contract change.

## Probe reference

`/npclinks followprobe …` exists only in **Debug** builds. It isn't in the help text and isn't in Release.

| Command | What it does |
|---|---|
| `status` | The gate, its verdict, the character tag and the generation |
| `anchors` | Reads 23 authored (row, title) anchors from 2.0 to 7.0, including retired/current pairs, then combines alternatives per step and runs the negative checks |
| `read <row or exact title>[; …]` | Reads arbitrary rows; a title expands to every row with that title |
| `thread` | The same read on and off the framework thread, plus a one-shot check of whether Draw is on the framework thread |
| `watch on` / `watch off` | Logs gate transitions and character invalidations, and prints quest-completion flips as they happen |
| `path` | The log path: `pluginConfigs/NpcDialogueLinks/follow-progress-probe/followprobe-YYYYMMDD.log` |

## In-game evidence

*Pending the user's run.* Record the date, the build, how many characters were tested and at what progress, and the result for each criterion. Missing evidence stays pending, never passed.
