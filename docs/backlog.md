# Backlog

This is the executable acceptance queue used by the [GitHub workflow](github-workflow.md). For feature and polish candidates, see [enhancement-roadmap.md](enhancement-roadmap.md).

Only stable `NDL-###` story cards in the three workflow states below are executable. The legacy inventory is retained for grooming context and is not blanket implementation approval.

## To Do

The user approved [Atlas v2: arc context](atlas/v2-plan.md) on 2026-11-14 and made it the priority ahead of `Pre-Ship`. Follow covers completed story progress only; the user accepted that with the plan. The complete contract is in the plan. **Follow is deferred (user decision, 2026-11-14):** `NDL-007` moved to the [parking lot](#deferred-follow-ndl-007), and v2 ships without Follow.

The user approved publication of the bounded Atlas pilot plan and priority exception on 2026-11-14. Part 1 publishes these cards; it does not start research or implementation. On 2026-11-14 the user also approved a dedicated UX design story, `NDL-005`, which the window story implements. Execute in the order below (`NDL-005` may run alongside `NDL-003`); the complete contract is in [lore-relationship-atlas.md](lore-relationship-atlas.md).

## In Review

## User Accepted

The user approved `NDL-011` on 2026-11-15 as the polish piece for a strong Atlas vertical slice, with the condition that the local viewer looks like the in-game window.

- [x] `NDL-011` **Atlas portraits, in game and in the local viewer**
  - Owner: `ui` (rendering) and `content` (picking and review)
  - Outcome: Every Atlas entry with a suitable, spoiler-safe image in the game's own data shows it as a portrait, in the in-game window and identically in the local viewer. The rest keep their category shape.
  - Acceptance:
    - **Art comes only from the player's own game install, at runtime.** `atlas.json` stores game icon numbers, never image files. Nothing comes from the wiki or other sites, and no game image is committed or packaged.
    - **Every entry gets a candidate search.** All 19 current entries (12 characters, 3 organizations, 2 locations, 2 events) are searched in the game data. The candidates go on one review page for the user, who approves, swaps or vetoes each one.
    - **Spoiler-safe from first appearance.** A portrait must not show a later look, outfit, name or identity than the entry's earliest story point. An entry without an approved portrait keeps its shape.
    - **Schema.** An optional, reviewed `portrait` on an entity, holding the game icon number. It is covered by the generator's per-record fingerprint review and by validator rules. Strict passes.
    - **Rendering.** Portraits appear:
      - on chart nodes, round, inside a ring in the category colour;
      - large in the details and arc-panel headers;
      - small in the browse list.
      
      The category shape and colour stay visible, so meaning never rests on the picture. A missing or failed texture falls back to the shape and never raises an error.
    - **The local viewer looks like the in-game window.** A repository tool extracts the approved images from the user's install into a git-ignored cache outside the repository. The viewer serves them and draws them with the same crop, ring and sizes. Without the cache, the viewer falls back to shapes, as the game would.
    - No network calls and no new hooks.
  - Evidence (report each lane separately):
    - the candidate review page and the user's picks;
    - host tests for the schema, validator, fallback and fingerprints;
    - locked builds and packaging, with no images in the zip;
    - a side-by-side of the viewer and the window;
    - one in-game look by the user.
  - Dependencies: Atlas v2 (`NDL-006`, `NDL-008`–`NDL-010`) accepted; branch `codex/ndl-011-atlas-portraits`.
  - Acceptance record: the user approved all 18 portrait picks and accepted on 2026-11-16. A four-delegate council review of the viewer reached 9/10 from every delegate. The user also asked for the story arc picker to show where each arc starts, patch headings across patches, and "· ended" once the view is past an arc; that shipped in this story. The in-game look was not reported, so that lane is untested; the table is in the [Atlas guide](atlas/README.md#in-game-look-ndl-011).

- [x] `NDL-010` **Ship v2 in game**
  - Owner: `ui`
  - Outcome: The in-game Atlas window and the viewer render the accepted v2 design over the accepted arc content.
  - Acceptance:
    - The ImGui window has the Arc, Story point and Changes lenses at parity with the viewer.
    - No Follow: the user deferred it on 2026-11-14, which is the formally accepted reduced scope.
    - One "Open Atlas" button in the Lore Explain window, with no data flow.
    - Spoiler and positioning rules hold.
    - The scope statement is in the guide and handoff.
  - Evidence: Host tests; locked builds and packaging; an in-game do/expect test by the user; viewer parity. Report the lanes separately.
  - Dependencies: Accepted `NDL-008` and `NDL-009`; branch `codex/ndl-010-atlas-v2-window`. Lead owns `Plugin.cs` and Lore Explain integration.
  - Acceptance record: the user accepted on 2026-11-15 without running the in-game test ("i wont be testing this but i trust you"). The in-game lane is untested; the 11-row table is in the [Atlas guide](atlas/README.md#in-game-test-ndl-010).

- [x] `NDL-009` **Research and review the first arc's content**
  - Owner: `content`
  - Outcome: At least one complete, human-reviewed arc (the candidate is the 2.0 raid → rescue), with a story-so-far recap at every step and its cast's relationships, ships in `atlas.json`.
  - Acceptance:
    - The approved arc map is authored within the caps and never truncated.
    - Baseline coverage for pre-known entities; fresh arc-era presentations, never reused from the 2.0 summaries; reviewed quest titles, arc names and recaps.
    - The review sheet has an Arcs section with one row per step.
    - Pinned "added" rows match the worked examples.
    - Human acceptance precedes the per-record reviewed marking and the strict recheck.
    - The handoff reports the authoring cost per arc step.
  - Evidence: Research lanes with claim/passage/boundary traceability; real-data tests, including the per-step leak sweep; human content review, then strict validation. In-game: not applicable.
  - Dependencies: `NDL-006` schema frozen; branch `codex/ndl-009-atlas-arc-content`. Finalization needs accepted `NDL-006`.
  - Notes from `NDL-006`:
    - The user chose arc A4, *The Black Wolf's challenge* (MSQ #155–161), with an editorial cast of 10 ([v2-discovery.md](atlas/v2-discovery.md)).
    - End evidence (`endCitations`) loads only on an ending the Changes lens can show: both sides of the ending must be slices (or both milestones), and the same relationship must not carry straight on. The possession that ends at the slice → `cp-arr-2-0` boundary therefore carries none.

- [x] `NDL-008` **Design the v2 lenses in the local viewer**
  - Owner: `ui`
  - Outcome: The user accepts the v2 interaction design, prototyped in the viewer: the Arc, Story point and Changes lenses.
  - Acceptance:
    - The Arc lens's default view shows the arc name and the "Story so far, through ‹quest›" recap alongside a whole-cast chart, without refocusing.
    - Default and switch-to-Arc lens rules; arc picker and selection lifetime; Changes rows; honest positioning labels; no-title raise options; the event glyph; the coverage note.
    - No Follow toggle or status lines: Follow is deferred.
    - Updated `ux-design.md` with ImGui feasibility notes.
    - A viewer-only prototype is allowed; production parity comes in `NDL-010`.
  - Evidence: Design doc, viewer walkthrough on synthetic or real data, host tests for any core text or state, locked builds. In-game: not applicable. User design acceptance.
  - Dependencies: Accepted `NDL-006`; `NDL-007` concluded by the user's deferral (2026-11-14); branch `codex/ndl-008-atlas-v2-ux`.

- [x] `NDL-006` **Arc discovery, schema v2 and core**
  - Owner: `lead`
  - Outcome: A research-verified arc map and worked examples freeze a v2 data model and pure core that support arcs, quest-level steps, the Arc, Story point and Changes lenses, and Follow positioning, without breaking the shipped Atlas.
  - Acceptance:
    - Discovery comes first: a verified quest-order inventory, 2–3 worked examples with passages, and a proposed arc map with evidence for each boundary and its overlaps, flagging any cap overflow.
    - Then schema v2 per the plan: timeline-step fields, the `event` category, `arcs`, and `endCitations`.
    - The validator, the v2 spoiler rules, the triple-based snapshot diff, the Arc-lens projection (cumulative cast, "Ended so far", selection and lifetime), a pure whole-cast layout, and a pure `FollowPosition`.
    - Per-record review in the generator, regenerated v2 data with pinned milestone snapshots, earliest-checkpoint defaults, and every synthetic fixture the plan lists.
    - The window, viewer and bundled data keep working.
  - Evidence: Discovery documents with passages; host tests for the core and fixtures; real-data pinned-snapshot tests; locked restore and builds; viewer parity smoke. In-game: not applicable. User acceptance of the arc map and the core is recorded separately.
  - Dependencies: Atlas v2 planning publication; branch `codex/ndl-006-atlas-v2-core`, PR base `main`.

- [x] `NDL-004` **Deliver the standalone Atlas window and validate it in game**
  - Owner: `ui`
  - Outcome: `/npclinks atlas` opens a readable offline relationship browser over the accepted pilot data.
  - Acceptance: Visible-only search, focus/refocus, directed incoming/outgoing one-hop graph with at most eight canvas neighbors and a complete neighbor list, original details/safe sources, two persisted manual controls, declared minimum window size, and Atlas-only failure recovery. The local viewer stays at parity with the window, both rendering the shared `AtlasSession` (see the Atlas local-viewer guide). Lead owns Plugin.cs command/help/window lifecycle, configuration, and project packaging. No new Talk hooks, quest/progression inference, bridge, or API dependency. README changes deliberately deferred while unrelated local edits remain; document the command in the Atlas guide/handoff. Update roadmap status on accepted closeout.
  - Evidence: Host tests on production and real data; locked restore/build; atlas.json in Debug output and Release latest.zip; in-game load/unload/reload, open/close/search/refocus, direction, forward/backward boundaries, state recovery/persistence, sources, minimum/large windows at 100%/150% scale, offline/no-key operation, and malformed/missing-data isolation with dictionary/chat links/Explain intact. Report all lanes and explicit acceptance separately; missing in-game evidence remains pending. Content fixes repeat affected-record validation/review.
  - Dependencies: Accepted `NDL-002`, `NDL-003`, and `NDL-005` (the window implements the accepted `NDL-005` design); branch `codex/ndl-004-atlas-window`, PR base `main` after all three merges. Lead coordinates integration; no overlapping Plugin.cs edits.

- [x] `NDL-005` **Design the Atlas user experience and prototype it in the local viewer**
  - Owner: `ui`
  - Outcome: The user accepts a concrete Atlas interaction and visual design, proven in the local viewer, before any ImGui window is built.
  - Acceptance: `docs/atlas/ux-design.md` specifies the layout and minimum window size; the primary flows (first open at the earliest checkpoint, search → focus → refocus, raising the ceiling with confirmation, lowering and clamping, switching the content view, the overflow neighbor list, opening a source behind the spoiler warning); the visual language (category glyph plus color, never color alone; edge direction and labels; symmetric edges; hover, selected and focus states); empty, no-result and load-failure states; accessibility at 100%/150% font scale and contrast; and an ImGui feasibility note for every element. The local viewer is updated to the accepted design over synthetic sample data. Any new behavior or player-facing text goes into the shared core (`AtlasSession`, `AtlasText`, `AtlasGraphLayout`) with tests, so `NDL-004` renders the same thing. Frozen schema and spoiler invariants are unchanged; a needed change is flagged, not made. No plugin wiring, packaging, or real lore.
  - Evidence: Design doc with annotated viewer screenshots at the minimum and a large size; a walkthrough of each flow; host tests for core changes; locked restore and plugin/viewer builds; ImGui feasibility review. In-game: not applicable. User design acceptance recorded separately.
  - Dependencies: Accepted `NDL-002`; branch `codex/ndl-005-atlas-ux-design`, PR base `main` after NDL-002 merge. May run in parallel with `NDL-003`: this story owns the viewer front end, `docs/atlas/ux-design.md`, and presentation-level core files, while `NDL-003` owns content; serialize any overlapping core edits.

- [x] `NDL-003` **Research and curate the reviewed Scions Atlas dataset**
  - Owner: `content`
  - Outcome: The pilot's two historical snapshots contain researched, original, human-reviewed descriptions and relationships.
  - Acceptance: 8–12 entities, exactly the two approved checkpoints, at least one description and one relationship change, safe names/aliases/citations, complete evidence matrix and readable review sheet, plus actual `NpcDialogueLinks/atlas.json` passing production validation/snapshot tests. Human acceptance precedes the mechanical reviewed-marker commit and strict shippable recheck. Omit/narrow unsupported claims; any necessary pilot-preserving contract correction is one bounded versioned model-plus-tests amendment, explicitly flagged in this PR. No packaging or runtime integration.
  - Evidence: Web research with claim/source passage/player-knowledge boundary traceability; real-data structural and expected-snapshot tests, human content review, then strict shippable validation before merge. In-game: not applicable to unintegrated content. AI review is not human canon acceptance.
  - Dependencies: Accepted `NDL-002`; branch `codex/ndl-003-atlas-scions-content`, PR base `main` after NDL-002 merge. Research may overlap after its contract freezes; finalization may not bypass foundation acceptance.

- [x] `NDL-002` **Research Atlas requirements and build the tested foundation**
  - Owner: `lead`
  - Outcome: Source-backed discovery informs a minimal, independently testable Atlas model before real lore is encoded.
  - Acceptance: Provisional evidence matrix and worked examples under `docs/` establish an 8–12-entity Scions pilot at ARR 2.0/2.55 completion, anchored to terminal quests. Pure production loader/validator/projection and two-control state policy implement the Atlas contract, including draft/strict review modes and conservative recovery. A sibling host-runnable test project uses actual production files and its own lock file. A local browser viewer (user request, 2026-11-14) renders the same core over synthetic sample data, so the Atlas can be viewed without FFXIV. No runtime wiring, packaging, or shipped lore data.
  - Evidence: Discovery source/claim/checkpoint matrix and traceable synthetic examples; local host tests for spoiler fields/counts, temporal validity/direction, bounds/references, review modes, malformed/missing data, and saved-state recovery; locked restore and plugin build with actual SDK recorded. In-game: not applicable to disconnected pure code. User acceptance recorded separately.
  - Dependencies: Planning publication on `origin/main`; branch `codex/ndl-002-atlas-foundation`, PR base `main` from refreshed `origin/main`.

- [x] `NDL-001` **Adopt acceptance-gated GitHub delivery**
  - Owner: `lead`
  - Outcome: Repository agents use an isolated story branch, draft substantive pull request, explicit acceptance gate, merge, synchronization, and cleanup lifecycle.
  - Acceptance: The project-local delivery skill and canonical workflow are discoverable from `AGENTS.md`, preserve unrelated dirty work, and distinguish agent validation from user acceptance.
  - Evidence: Skill structure validation and scoped Git diff checks pass; publication is recorded by the merged baseline pull request.
  - Dependencies: `None`

## Legacy Candidate Inventory

### Lore Explain

- Prototype direct in-game dialogue explanation with a file-export fallback.
- Keep the internal codename "girl wtf are they talking about" in docs as the design north star.
- Validate `/npclinks config` with a user-provided OpenAI API key.
- Verify OpenAI web search citations render usefully in the Lore Explain window.
- Validate clickable source links in the Lore Explain window.
- Validate hidden-by-default Context, Recent Context, and Sources sections in game.
- Validate rolling dialogue history quality across normal NPC conversations.
- Refine Ask Follow-Up transcript styling after in-game testing.
- Validate zone and best-effort target/speaker metadata in game.
- Investigate reliable `Talk` addon speaker-name capture.
- Investigate quest metadata capture for quest-bound dialogue.
- Validate Lore Explain dictionary proposal review and save flow in game.
- Keep generated dictionary proposals out of bundled `terms.json` until human review.

### Runtime

- Verify `Talk` capture against multiple NPC dialogue situations.
- Confirm the best text node selection for standard conversations.
- Validate the debug-only quest metadata probe before exposing quest context to Lore Explain.

### Dictionary

- Add more core place names to `terms.json`.
- Expand alias coverage for terms that commonly appear under alternate names.
- Validate user dictionary create/update/delete behavior across plugin reloads and updates.
- Plan dictionary metadata for story/patch freshness so definitions can be marked with source patch, spoiler range, last verified date, and review status.
- Design fallback behavior for outdated or progression-sensitive definitions, such as preferring Lore Explain/web research over stale local text when a term's status is uncertain.
- Consider multiple definitions per proper noun keyed by story progression, expansion, quest, or patch when the same noun changes meaning over time.

### UI

- Evaluate whether chat output remains sufficient for definitions.
- Refine the in-game dictionary editor layout after live testing.

### Content

- Seed starter entries for city-states, regions, and guild names.

## Parking Lot

- Support richer term categories.
- Add data import tooling for larger dictionaries.
- Add dictionary review tooling to flag stale entries after new FFXIV patches or expansions.
- Explore direct dialogue-box presentation instead of chat links.
- Consider `/ndl` as a shorter alias once command naming settles.

### Deferred: Follow (`NDL-007`)

The user deferred Follow on 2026-11-14, before the in-game probe run, so Atlas v2 ships without it (the plan's [failure path](atlas/v2-plan.md#follow-completed-story-progress)). The investigation is kept for a later pickup:

- **Kept:** draft PR [#16](https://github.com/Jonathon-Sherrouse/dalamud-lore/pull/16) on branch `codex/ndl-007-follow-progress`, with the read-only progress adapter, its host tests, the Debug-only `/npclinks followprobe` command, and the write-up `docs/atlas/follow-progress-investigation.md`.
- **Kept in the core:** `AtlasFollow` and `AtlasSpoilerPolicy.SetCeilingToFollowed` from `NDL-006` stay, unused by any front end.
- **To resume:** merge `main` into the branch (`SetCeilingToFollowed` now takes the progress function), then run the probe's do/expect table on at least two characters. Open question: did any test character finish A Realm Reborn before Aug 2020 or Apr 2022, when old quest rows were replaced?

The card, unchanged apart from moving here:

- [ ] `NDL-007` **Investigate completed-progress detection for Follow**
  - Owner: `runtime`
  - Outcome: Runtime evidence settles whether client completed-quest flags can drive Follow safely.
  - Acceptance: Every exit criterion in the plan is met or documented as failing:
    1. the flag flips before/after for known pairs on at least two characters;
    2. Lumina → client ID conversion is verified, with a title cross-check;
    3. reads are framework-thread and logged-in only, with unknown never treated as incomplete;
    4. a character switch triggers a re-read;
    5. story-skip behavior is documented.

    A minimal adapter sits outside the pure core and never touches `QuestMetadataProbe`. If it fails, the result is reported and Follow's reduced scope goes to the user.
  - Evidence: An in-game probe run by the user through a short do/expect table, with logs; the adapter's host tests where possible; locked build. Missing in-game evidence stays pending.
  - Dependencies: Atlas v2 planning publication; branch `codex/ndl-007-follow-progress`. Must conclude before `NDL-008` is accepted.

### Deferred during the Atlas work (collected by the user's request, 2026-11-14)

Everything consciously put off during the Atlas pilot and the v2 planning, in one place. None of it is approved; each item needs its own groomed story. `Pre-Ship` and `Next Polish Pass` stay tracked in [enhancement-roadmap.md](enhancement-roadmap.md), so they aren't repeated here.

**Atlas content and coverage**
- **The arc "The rescue at Castrum Centri"** (MSQ #142–155, 14 quests). Deferred by the `NDL-006` arc-map decision ([v2-discovery.md](atlas/v2-discovery.md)). Building it would prove arc overlap in real content and would need higher step and checkpoint caps, plus an ordering rule for the parallel quest paths at #150–151.
- **The long 2.0 threads:** "After the raid" (#106–155, the captives) and "Coerthas and the *Enterprise*" (#110–141). Candidates for breadth coverage.
- **Breadth coverage across the main scenario.** Choose the route after the first arc shows whether a confused player can explain the story. Don't use patch-sized outer arcs, which break the selection rule and the cast cap; milestone-only recaps cover endpoints only ([v2-plan.md](atlas/v2-plan.md)).
- **More checkpoints, groups and languages,** for example Heavensward and characters beyond the Scions (from the pilot's future-candidate list).
- **A larger cast or more relationship types** if real arcs need them, for example an "opposes" type for the Alliance and the Empire. The v2 caps are 10 cast members and 3 new types.

**Atlas views and behaviour**
- **"During a quest" positions,** so facts that start and end inside one quest can be relationships. That needs a flagged amendment, because v2 keeps them as summary text.
- **Richer Changes lens:** pairing a type change into one "~ changed" row, and distinguishing "revealed" from "began".
- **Follow itself** is parked above, as `NDL-007`. Beyond it: **continuous Follow** (live updates, instead of on open or Refresh), and Follow for optional-quest progress.
- **Optional quests on the timeline,** in some order. v2's timeline is main scenario only.
- **Scene- or objective-level positions** inside a quest.
- **Navigation history:** a back button. It was excluded from the pilot.
- **Portraits** instead of category shapes, and **map or situation views** over the same data.
- **Import and editing tools** for Atlas data that keep the source and review history.

**Atlas and the rest of the plugin**
- **"View in Atlas" from dictionary terms and Lore Explain,** with the term or quest passed through. v2 adds only a plain "Open Atlas" button.
- **Lore Explain grounded in the Atlas's reviewed recaps,** and aware of the spoiler limit. Its own spoiler caution is only a prompt, not a reviewed guarantee.
- **Reusing reviewed dictionary text** in Atlas descriptions.
- **Document `/npclinks atlas` in the README** once the unrelated local README edits are settled. It was deferred in `NDL-004`, and the [Atlas guide](atlas/README.md) documents it in the meantime.

**Data model**
- **Optional-presentation persistence** ([schema.md](atlas/schema.md), "v2 candidate"). An optional presentation can never stop, even after the main story catches up, which forces some duplication. Spoiler-safe as-is; only a maintenance cost.
- **Showing the "Leveilleur" surname** from patch 2.4 onward, and a general surname policy beyond first names.
- **Atlas data for a "home" entry,** moving the pilot's hard-coded `AtlasDefaults.HomeEntityId` into `atlas.json`.

**Verification and tooling**
- **In-game checks never run for `NDL-004`** (recorded in PR #13): plugin reload, lowering the limit, the 150% font scale, no API key, a missing or broken `atlas.json`, and an invalid saved setting.
- **Spot-checking the wiki transcriptions in game.** Every Atlas source is a fan transcription of in-game text.
- **Agent-driven in-game testing.** Blocked because T3 Code lacks macOS Accessibility and Screen Recording access, and the game must be logged in (an automated run was tried during `NDL-004`).
- **Visual review of the local viewer by an agent.** So far it has been checked through its API, a static snapshot, and the user's own eyes.

### Quest-scoped Atlas views (parked by the user, 2026-11-14)

> **Now planned (2026-11-14):** A–E are delivered by [Atlas v2](atlas/v2-plan.md) (`NDL-006` to `NDL-010`); E as completed progress, and C and D through arcs. The entries below are kept for history.

These are not approved and are not part of the Atlas pilot. Each needs its own groomed story after the pilot. Today, every story point is a cumulative snapshot of what the player knows as of that point; these ideas would add quest-level views. See the [Atlas contract](lore-relationship-atlas.md#future-candidates--not-approved).

- **A. Quest-level story points.** Allow any quest as a story point, not only patch endings. Same cumulative model at finer steps. Needs a higher checkpoint limit (the schema caps it at 16) and exact per-quest timing research for every claim, so cost grows with the size of the MSQ.
- **B. "What this quest changed."** Pick a quest and see only the relationships and descriptions it introduced or ended. Records already cite their quest as display text; this needs a structured quest reference on each record (a schema change) and a "changes" mode. Cheapest of the five.
- **C. Quest and story-event entries.** Quests or events, such as *The Parting Glass*, as their own nodes, linked to who was involved and what changed. Already a deferred contract candidate ("curated story-event entities"). Needs a new category and new relationship types.
- **D. Short-lived, in-quest relationships.** Facts true only during a quest, such as a temporary alliance. The current rules forbid a relationship that starts and ends between two story points (it becomes description text instead); quest-scoped intervals would lift that rule. Pairs naturally with C.
- **E. Follow the player's current quest.** Open the Atlas at the quest the player is on in game. Deferred: automatic progression or quest inference needs verified runtime evidence first. Start from [quest-metadata-investigation.md](quest-metadata-investigation.md).

Initial take when grooming: B is the cheapest; C with D is the full quest-scoped Atlas; A gets expensive across the whole MSQ.
