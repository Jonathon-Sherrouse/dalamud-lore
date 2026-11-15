# Lore Atlas v2 plan: arc context

> **Status: approved planning contract.** The user approved this plan on 2026-11-14 after eight council rounds; the final round was unanimous ([council record](#council-record)). It is a plan, not delivered work. Each story below has its own acceptance gate.

## Goal and priority

**Goal (user, 2026-11-14).** A player at any point in the story, lost in the beat they're playing, can open the Atlas and understand what is going on, with no spoilers.

The answer is a researched **story arc**: a run of consecutive main-scenario quests. Inside an arc, the Atlas shows a reviewed "story so far" recap and a relationship chart of the arc's whole cast, built up quest by quest.

The plan also delivers the five parked quest-scoped ideas, A–E, as switchable views:

| Idea | Delivered as |
|---|---|
| A | Quest-level story points across the covered slice |
| B | The Changes lens |
| C | Arc and event entries |
| D | Quest-bounded relationships that appear, persist and end step by step |
| E | Follow, driven by verified **completed** story progress |

**Priority (user decision, 2026-11-14).** Atlas v2 goes ahead of the roadmap's `Pre-Ship` and `Next Polish Pass` work. Those items stay open.

**Follow narrowed (accepted with plan approval).** The parked idea E said "current quest". This plan delivers completed progress, because a snapshot of an in-progress quest would spoil its ending.

**Scope.** v2 proves the experience **within one researched arc**.
- It does not deliver "at any point in the story" across the game. How to extend coverage is decided after the slice is evaluated.
- It does not explain the scene currently playing. Confusion about the current line of dialogue belongs to **Lore Explain**, whose prompt-level spoiler caution is *not* the Atlas's reviewed checkpoint guarantee.
- The Atlas gives reviewed context through the last completed quest.

## Product shape

There are three **lenses**, which pick *what* is shown, and a **Follow** toggle, which picks *where* on the timeline you are. The existing content toggle (main story only, or main + optional) is orthogonal to both.

| Lens | What it shows |
|---|---|
| **Arc** (core) | The selected arc's **story-so-far recap** and its **whole-cast chart**, as of the arc's effective step. See [Arc lens](#arc-lens). |
| **Story point** | The cumulative, unfiltered snapshot after a chosen timeline step: today's view, with quest-level steps across the covered slice. |
| **Changes** | A semantic diff between the previous step and the current one: **added**, **ended**, **description updated**. See [Changes lens](#changes-lens). |
| **Follow** (toggle) | Moves the view to the player's verified completed story progress. See [Follow](#follow-completed-story-progress). |

**Default lens.** The window opens in the Arc lens when an arc contains the view, and in Story point otherwise. Whenever Follow moves the view into an arc, the window switches to the Arc lens, unless the user has picked a lens explicitly. An explicit lens choice lasts for the session.

**Honest positioning.**
- Only a Follow result is presented as the player's progress: "Your progress: through ‹quest›". When that result is clamped to the limit, word it so it reads sensibly beside the raise offer.
- A default, manual or stale position is labelled as the chosen point ("Viewing: after ‹quest›"), never as "you are here".

**Coverage note.** On slice steps (non-milestone steps), one shared `AtlasText` line says the point covers only the characters involved in that part of the story.

**Entry points.** The window opens from `/npclinks atlas` and from one **Open Atlas** button in the Lore Explain window (`NDL-010`). The button only opens the window; no data passes between the two features.

## Timeline and data model (schema v2)

The core keeps today's model: one checkpoint `Order`, half-open intervals, `Project(dataset, checkpointId, view)`, the spoiler policy and the validator. It adds a few fields.

### Timeline

- **Timeline steps are checkpoints.** There is one step per main-scenario quest, and it means **"after this quest"**. There is no "during" position.
- A fact that begins and ends inside one quest stays summary text, as in v1. Adding a "during" position would need a flagged amendment.
- **Main scenario only.** Optional records keep record-level `scope` and the existing available-content rule. In practice they attach at the milestones.
- **New optional checkpoint fields:**

  | Field | Purpose |
  |---|---|
  | `milestone` | True for patch milestones |
  | `questTitle` | Reviewed, spoiler-checked display title |
  | `contiguousWithPrevious` | Whether the previous step is the quest immediately before this one |
  | `gameQuestIds` | Lumina Quest rows, used only by Follow. Milestones carry them too. |

- **Kept IDs.** `cp-arr-2-0` and `cp-arr-2-55` stay as the milestone step IDs, so saved settings survive. `cp-arr-2-0` has `contiguousWithPrevious` false unless discovery shows the arc's last step is directly before *The Ultimate Weapon*.
- **Bounds are unchanged.** The slice (at most 10 steps) plus two milestones fits the 16-checkpoint cap. Later content stories raise bounds with a justification.

### Arcs and events

- **Category `event`.** Added with a fourth glyph and color, ordered last.
- **Relationship types.** The vocabulary stays closed: `participant-in`, plus at most two other new types.
- **The top-level `arcs` collection.** Each arc has an `id`, an `entityId` (its **arc entry**, which must be an `event` entity), a `firstStep` and a `lastStep`. Arcs may **overlap or nest**.
- **Validation:**
  - `firstStep` is at or before `lastStep`, and both are main-scenario steps.
  - `firstStep` is **never the first timeline step**; there is always a baseline before it.
  - The entry's **first presentation starts exactly at `firstStep`**, so its name never appears earlier, and the entry stays visible through `lastStep`.
  - The entry and every `participant-in` edge to it are main scope.
  - Each such edge starts at or after `firstStep` and has **no `validUntil`**, so the cast never shrinks.
  - The cast has **at most 10 members** at any step. If the real cast is larger, discovery flags it and the user chooses a justified raise or an editorial cast; members are never trimmed silently.
- **The recap.** At every covered step of an arc, the arc entry's effective summary is a reviewed **"story so far in this arc"** recap:
  - 2–4 sentences, about 80 words at most, within the 1,200-character cap;
  - it covers the current situation, the immediate objective, and the relevant causes and stakes, using only established knowledge;
  - no teasers or finality wording; at `lastStep` it must not read as a conclusion;
  - an unchanged presentation may span steps while the review sheet marks each step "unchanged, still accurate".

### Citations and migration

- **`endCitations`.** An optional list (at most 8) on relationships, holding reviewed evidence for why or when a relationship ended.
  - Each citation's `availableAt` is after `validFrom` and at or before `validUntil`.
  - They follow the existing scope rule (a main record cites only main sources) and the same-title consistency rule.
  - They are shown **only** in the Changes row for that ending.
- **No citation `questId`.** Changes and the Arc lens are computed from snapshots instead.
- **Migration.** The loader accepts v2 only, with no runtime converter. The generator emits v2.
  - Tests pin the accepted milestone snapshots (legacy entity and relationship IDs and presentations) in both content views. New slice and arc records are asserted separately.
  - Arc records that cite the same quests as accepted records move those citations' `availableAt` earlier. That is a permitted mechanical change: `availableAt` is never displayed, and the pinned milestone snapshots stay identical.
- **Authoring tool.** `build_pilot_content.py` moves to per-record review status, so accepted records stay `reviewed` while new ones are `pending`.

### Defaults and saved state

Absent **or** invalid saved state resets both controls to the **earliest checkpoint**, which is the pre-arc baseline.
- This means a first-time player is never shown an arc's outcome.
- Follow's neutral raise offer, or one Raise… milestone, brings later players forward.
- Valid saved IDs restore exactly.

## Spoiler rules

These add to the v1 invariants.

1. **Raising the limit never reveals a title.**
   - Above the limit, pickers show only neutral milestone labels plus one unnamed "next story step".
   - Raise prompts name a milestone, "the next story step", or (in Follow) "your completed quests".
   - Lowering may choose any step at or below the limit.
2. **Endings never appear in advance.** No active relationship is marked "temporary", "until" or "ends". Endings appear only in diff-derived views (Changes, and the Arc lens's "Ended so far"), once the selected step establishes them. `endCitations` appear in Changes only.
3. **Quest titles, event and arc names, recaps and new type labels** are reviewed metadata. They appear only at or below the limit, and counts never include locked steps.
4. **Diff rows come from snapshots at or below the view.** An ended row uses its endpoints' presentations at the step before it ended.
5. **The per-step leak sweep** covers every surface, including option lists, prompts and recaps.
6. **Arc names and recaps are reviewed for what they reveal at their own start step.** Pickers use the name as of the arc's effective step.
7. **Nothing reveals an arc's length or end.** There is no "step 2 of 5", end marker or "arc complete" badge until V is **after** `lastStep`. At V = `lastStep`, the lens looks exactly like a mid-arc step.
8. **The cast comes only from `participant-in` edges visible at the effective step.**
9. **Coverage boundaries.** The Arc lens filters every snapshot to its cast, so the wider cast first appearing at a milestone never shows as "added". Any cast-internal relationship that starts at a milestone must either be backfilled under the [baseline rule](#content-slice) or be reviewed as a genuine start.

## Arc lens

For a selected arc **X** whose `firstStep` is at or before the view **V**, the effective step is **T = min(V, X.lastStep)**. Steps after T are **never** consulted.

**What it shows.**
- **Cast C:** the arc entry plus every entity with a `participant-in` edge to it visible at T. The cast only grows.
- **Filtering.** Every snapshot the lens uses is projected, then filtered to C: only C's entities, and only relationships with both endpoints in C. The filter applies to search, counts, connections, refocus and marks.
- **New:** triples present at T but not at the step before T.
- **Ended so far in this arc:** the union of the semantic "ended" results from each consecutive pair of steps, from the step before `firstStep` up to T.
  - A relationship that starts and ends inside the arc is listed.
  - A triple present again at T is dropped.
  - A triple that ended more than once uses its latest ending.
  - Rows show no sources.
- **Default view:** the arc's name and **recap**, labelled "Story so far, through ‹quest at T›", shown alongside or above a **whole-cast chart** (all of C and all cast-to-cast relationships), without selecting or refocusing anything. Refocusing a character shows today's one-hop view inside the filter.

**Selection.**
- **Default rule:** among the arcs that contain V, pick the **earliest-started**, so you stay with the ongoing arc until it ends. Ties break by authored arc order, never by span or `lastStep`.
- **Picker:** lists only arcs whose `firstStep` is at or before V, sorted by `firstStep` and then authored order, each with its name as of its effective step. It never shows a span.
- **A default selection** is recomputed whenever V changes. If no arc contains V, the lens shows a neutral empty state.
- **An explicit pick** lasts until the user picks again or clears it, Follow moves the view, or its `firstStep` becomes later than V. A picked arc that has already ended stays viewable at its `lastStep`, labelled "as of ‹last quest›".
- **With Follow on,** if no arc contains the followed step, the lens says "No story arc covers this point". It never keeps a previous arc on screen as if followed.

## Changes lens

- **How it compares.** It diffs two projected snapshots by the triple `(source, type, target)`, so a citation split is not a change. An entity counts as "description updated" only if its name, aliases or summary differ.
- **When it's offered.** From the second step onward, and only between steps of the same kind: slice step → slice step, or milestone → milestone. It is never offered across a slice → milestone boundary.
- **Its label.** "What this quest changed" when the step is `contiguousWithPrevious`; otherwise "Changes since ‹previous point›".
- **Known side effect.** It will list the arc entry as "description updated" at most arc steps. That is truthful.
- **Not in v2:** "~ changed type" pairing, or distinguishing "revealed" from "began".

## Content slice

**Discovery** happens in `NDL-006`, before the schema freezes. It produces:
- a verified inventory of quest order;
- 2–3 worked examples with passages;
- a **proposed arc map**: candidate arcs with first and last quests, the evidence for each boundary, any overlaps, and the rationale for judgment calls.

Arc boundaries are **editorial decisions backed by evidence**, and the user reviews them like content.

**Scope.** At least **one complete arc**; the candidate is the 2.0 raid → rescue. A second, overlapping arc is included only if it fits within the caps; the candidate is the possession storyline from *Escape from Castrum Centri* to *The Ultimate Weapon*. If only one fits, overlap is proven with synthetic fixtures.

**Caps.**

| Item | Cap |
|---|---|
| Slice steps, including the baseline | 10 |
| Arcs | 2 |
| New non-event entities | 4 |
| `event` entities, arc entries included | 4 |
| New relationship types | 3 |
| Cast per arc | 10 |

**An arc is never truncated.** If it doesn't fit, discovery stops and proposes a justified cap raise or steps only at the quests that change the chart (`contiguousWithPrevious` false). The user decides.

**Baseline rule.** An entity the player knows before the arc is covered from the **baseline** step, together with its existing relationships to other covered entities. Only what the arc introduces may start mid-arc. Arc-introduced entities and events keep presentations through the milestones. A pinned test checks that "added" rows match the worked examples at every slice step and every milestone step.

**Fresh research.** Earlier presentations are researched from scratch; the accepted 2.0 summaries narrate the whole arc, so they are never reused. Extending an accepted record's start counts as a factual change and needs review.

**The review sheet** gains an Arcs section: each arc's boundaries and evidence, its name and recap per step ("new recap" or "unchanged, still accurate"), and its cast.

## Follow: completed story progress

> **Deferred (user decision, 2026-11-14).** The user deferred Follow before the `NDL-007` in-game run, so v2 ships without it. That is the explicitly accepted reduced scope under the failure path below. The investigation is parked in the [backlog](../backlog.md#deferred-follow-ndl-007).

**The source.**
- Client completed-quest flags for authored `gameQuestIds`, for example FFXIVClientStructs `QuestManager` / `UIState` quest completion.
- A small adapter outside the pure core returns **complete**, **incomplete** or **unknown**.
- These flags are the only permitted progress source. The adapter never touches `QuestMetadataProbe`.

**`NDL-007` exit criteria.** Follow ships only if all of these hold:
1. The flag is false before and true after completion for known pairs, on at least two characters at different progress.
2. Lumina row → client ID conversion is verified, and a title cross-check disables Follow on any mismatch.
3. Reads happen only on the framework thread while logged in. A logged-out or loading state reads as **unknown**, never as incomplete.
4. A character switch invalidates the result and re-reads.
5. Story-skip behavior is documented.

**Behavior.**
- **The function.** `FollowPosition` returns exactly one of:
  - **a position:** the last step of the contiguous completed prefix among covered steps, clamped to the limit;
  - **before coverage:** the player hasn't completed the baseline step;
  - **unknown:** any covered step's flag reads unknown, or the player isn't logged in. If both "unknown" and "before coverage" apply, it returns unknown.
- **No fallback.** For "before coverage" and "unknown", the view doesn't move and a status line explains why.
- **Timing.** Follow runs on window open and on an explicit Refresh. It is not continuous.
- **The limit.** Follow never raises the limit. If progress is beyond it, Follow offers one neutral raise per session; confirming raises only the limit.
- **Character switch.** It clears the previous result and any pending raise.
- **Turning off.** A manual view change turns Follow off. The position is never persisted.

**Failure path.** If `NDL-007` fails, Follow is reported as **blocked or deferred**, and the user explicitly accepts the reduced scope. Manual picking or viewer simulation does not count as delivering it.

## Delivery

| Card | Story | Depends on |
|---|---|---|
| `NDL-006` | Arc discovery, schema v2 and core | This planning publication |
| `NDL-007` | Completed-progress investigation for Follow | This planning publication. Runs in parallel, and must conclude before `NDL-008` is accepted. |
| `NDL-008` | Lens and Arc UX design, as a viewer-only prototype (an explicit exception) | `NDL-006` accepted; `NDL-007` concluded |
| `NDL-009` | Arc content and review | `NDL-006` schema frozen |
| `NDL-010` | Window and viewer integration, Follow if `NDL-007` passed, the Open Atlas button, and the in-game test | `NDL-008`, `NDL-009` |

`NDL-006` must keep the existing window, viewer and bundled data working throughout. Its synthetic fixtures cover:
- **Records and diffs:** a citation split; a sparse step; the first step; locked titles; the slice → milestone boundary.
- **Arcs:** overlapping and nested arcs; an arc ending at a milestone; a mid-arc joiner whose existing relationships don't show as "New"; a view after an arc ends; no arc at the view.
- **Arc selection:** default vs explicit lifetime; ties broken by authored order; re-selection when V drops below an arc's start.
- **Ended so far:** a relationship that starts and ends inside the arc; one that ends and restarts; one that ends twice.
- **Spoilers:** V = `lastStep` looks identical to mid-arc; no arc length or future cast leaks.
- **Follow:** position, before coverage, unknown, character switch, and precedence.
- **State and layout:** absent and invalid saved state; the whole-cast layout at the cast cap.

## Council record

Delegates: Claude Opus 5.5, Claude Fable 5.2, GPT Sol and GPT Astra, all at high effort, reviewing read-only.

| Rounds | Topic | Outcome |
|---|---|---|
| 1–3 | The base plan: lenses, timeline, Changes, Follow, the slice | All agreed in round 3 |
| 4–6 | Arcs as the unit of context: the cumulative cast, "Ended so far", selection and lifetime, the whole-cast chart | All agreed in round 6 |
| 7 | Arcs vs expansion granularity for "what's going on here?" | Consensus: arcs plus milestones; a required recap |
| 8 | The recap, the default lens, earliest-checkpoint defaults, positioning, the Open Atlas button, the scope statement | All agreed |
