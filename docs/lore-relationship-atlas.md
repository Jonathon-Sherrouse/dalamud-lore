# Lore Relationship Atlas

## Status and priority exception

**Atlas dictionary previews approved (NDL-013).** The Atlas annotates visible summaries and recaps with links to the live dictionary only after the player opts in and acknowledges a one-time spoiler warning. Definitions can reveal events beyond the selected checkpoint. With previews off, the Atlas shows its reviewed prose and checkpoint-filtered facts.

**Atlas v2 approved (2026-11-14).** The user approved [Atlas v2: arc context](atlas/v2-plan.md) after an eight-round council review, and made it the priority ahead of `Pre-Ship`. v2 amends this contract as follows. The pilot text below stays the record of v1.
- **Exclusions.** v2 lifts two items from the excluded list in [Fixed pilot scope](#fixed-pilot-scope): **story-event entities** (now the `event` category, with arc entries) and **automatic progression filtering**. Follow uses client completed-quest flags for authored `gameQuestIds` as the **only** allowed progress source, and moves only the view within the spoiler limit. The rest of the list stays excluded, including dictionary/Lore Explain bridges. v2's Lore Explain "Open Atlas" button only opens the window; no data passes between the two.
- **Checkpoints.** v2 replaces "exactly two ordered checkpoints" with a main-scenario timeline of one "after this quest" step per covered quest. `cp-arr-2-0` and `cp-arr-2-55` stay as milestone steps.
- **Defaults.** v2 replaces "Both default to `cp-arr-2-0`": absent or invalid saved state resets both controls to the earliest checkpoint. The limit-raise and clamping rules stay, with v2's no-titles rule for raising.
- **Guardrail.** The guardrail "never infer relationships from … the active quest list" stands unchanged. Completion flags place the view, and never create, infer or alter relationships.
- **Bounds.** Unchanged for v2; later content stories may raise them with a justification.

**Pilot complete (2026-11-14).** `NDL-002`, `NDL-003`, `NDL-005` and `NDL-004` are all User Accepted, and `/npclinks atlas` ships the pilot. See the [Atlas guide](atlas/README.md). The text below records how the pilot was authorized.

The user authorized Part 1 (planning publication) on 2026-11-14 after council agreement on the pilot and research-to-implementation order. This planning bootstrap publishes the pilot contract and the three approved **To Do** cards in [backlog.md](backlog.md). No research, plugin implementation, content acceptance, or in-game validation has been completed by this change.

The bounded pilot `NDL-002` → `NDL-003` and `NDL-005` → `NDL-004` is explicitly allowed ahead of the existing `Pre-Ship` and `Next Polish Pass` work in [enhancement-roadmap.md](enhancement-roadmap.md). Those earlier items remain open. This exception does not approve the broader Atlas roadmap, remove any story acceptance gate, or make future candidates executable. Part 1 ends at planning publication; beginning discovery/foundation work is the next execution step. The user added the UX design story `NDL-005` to the pilot on 2026-11-14, so the window is designed and accepted before it is built.

The original deferred brief is superseded by this contract for the pilot. Its broader ideas are retained below as non-executable future candidates. Existing unrelated changes to `README.md` and `global.json` are outside this publication.

## Product goal and surface boundaries

Help the player identify a story entity, see its connections, and understand those connections at a selected point in the story. The inspiration is FFXVI's State of the Realm and Grand Cast: readable local relationships and changing story context, rather than a whole-world graph.

- **Dictionary:** detected term clicks continue to show their existing definitions.
- **Lore Explain:** continues to explain dialogue and its scene context.
- **Atlas:** opens independently through `/npclinks atlas` and browses separately curated, reviewed entities and relationships.

Dictionary membership never grants Atlas eligibility. The pilot uses original, reviewed, checkpoint-specific summaries with citations, not live dictionary definitions: generic definitions and user edits have no verified spoiler boundary. There is no dictionary schema change or **View in Atlas** bridge in this pilot.

## Fixed pilot scope

- English-only Core Scions sample with **8–12 entities**: characters, the Scions organization, and supporting locations. Exact membership is researched, not assumed here.
- Exactly two ordered checkpoints: `cp-arr-2-0` (**ARR 2.0 complete**) and `cp-arr-2-55` (**ARR 2.55 complete**). Discovery must anchor each to its terminal MSQ quest in the research evidence; player-facing selectors retain neutral patch labels.
- At least one description **and** one relationship change between the snapshots.
- A standalone window with visible-entity search, selected-entity details, reviewed citations, and a labeled, directed one-hop graph covering incoming and outgoing connections.
- Deterministic layout ordered by category then stable ID, with at most eight neighbors on the canvas and an always-complete visible-neighbor list for overflow and refocusing. A real readable graph is required at the supported window size; no force-directed physics.
- Authored category glyphs/shapes, with no portrait or external-art dependency.
- Versioned bundled `atlas.json`, separate from `terms.json` and `user-terms.json`.
- Offline operation without an OpenAI key or network access.

Excluded: story-event entities, maps, portraits, lore editors, automatic dialogue launch, dictionary/Lore Explain bridges, navigation history, AI-created canonical relationships, automatic progression filtering, and new native `Talk` hooks. The Atlas must not read `QuestMetadataProbe` or depend on its paused investigation.

## Research and content rules

Research story facts on the web; prefer `ffxiv.consolegameswiki.com`, with official material and game text where useful. Inspect actual supporting passages. A citation to a general character page alone is not evidence of when the player learned a fact.

For every factual claim, record the entity or relationship, the source title/URL and passage locator, the checkpoint where the player knows it, and any uncertainty. Separate **when an event occurred** from **when the player learns it**. Write original concise summaries rather than copying wiki prose.

**Available-content rule** (user decision, 2026-11-14). Player knowledge at a checkpoint includes required main-scenario content through its terminal quest. It also includes optional story content that is both doable at that story point and released in or before that checkpoint's patch. "Doable" means the whole unlock chain is satisfiable by main-scenario progress through the checkpoint plus other eligible optional content. Content released later never counts early, even when today's game lets the player reach it sooner. Record each optional source's verified unlock chain in the evidence matrix. The Atlas shows only authored facts; it never derives a relationship from others. Because snapshots include optional content, the checkpoint selector's help text should say so. Sources and model-generated drafts are inputs to review, not human acceptance or canonical data.

Initial discovery produces a provisional evidence matrix and two or three worked examples under `docs/`; label them unreviewed and never package them. Link the worked examples to the synthetic test cases that exercise their requirements. Do not import historical research or counts as accepted canon.

If a claim is unsupported or does not fit, omit or narrow it by default. If that would defeat the fixed pilot, report the decision rather than inventing facts or expanding scope. During the full content story, a necessary contract correction may be one bounded, versioned model-plus-tests amendment in `NDL-003`'s PR, explicitly flagged for user review; do not reopen the accepted foundation story.

## Temporal and validation contract

Use stable IDs, typed directed relationships, and checkpoint-specific entity presentations including names, aliases, descriptions, and displayed citation metadata. Use inclusive-start/exclusive-end intervals `[validFrom, validUntil)`; an absent end means ongoing.

Require exactly one reviewed presentation for each visible entity at each selected checkpoint **in each content view** (main-story only, or main plus optional; see [schema v1](atlas/schema.md)). Reject same-scope overlapping presentations, gaps inside each view's visibility, duplicate IDs, unknown references, invalid intervals, unsupported schema versions, and edges whose endpoints are not visible throughout their interval. Enforce bounds of 64 entities, 256 edges, 16 checkpoints, and 1 MiB of JSON; these are loader limits, not permission to enlarge the pilot. (`NDL-012` raised the checkpoint bound to 128 for one step per quest across ARR 2.0; see [its discovery doc](atlas/ndl-012-discovery.md).) (On 2026-11-19 the timeline was extended to one step per quest through 3.56, and the bounds rose to 256 entities, 1,024 edges, 512 checkpoints, 64 arcs, 64 relationship types, 64 presentations per entity and 4 MiB; see [era-modules.md](atlas/era-modules.md). Extending through Stormblood raised them again: 512 entities, 2,048 edges, 1,024 checkpoints, 128 arcs, 128 presentations per entity and 8 MiB; Shadowbringers raised presentations per entity to 512.)

Validation has two explicit modes:

- **Draft structural validation:** pending-review records are allowed so the actual dataset can be checked before human acceptance.
- **Strict shippable validation:** every runtime record must be reviewed. The runtime loader uses this mode and returns structured failure with no usable graph on invalid data.

After the user accepts the exact content, a mechanical commit may change only its accepted review markers. Rerun strict validation and real-data snapshot tests before merging. Any factual change needs review of the affected records, including content corrections discovered during UI testing.

Missing, malformed, unsupported, or invalid Atlas data must never escape through `Plugin` construction. Load lazily or guard the boundary and show an Atlas-only error. Dictionary links and Lore Explain must remain operational.

## Manual spoiler controls

Keep two persisted checkpoint IDs with conservative defaults:

1. **Knowledge approved through:** the spoiler ceiling. Raising it requires an explicit, neutral confirmation and never advances the displayed view.
2. **Viewing as of:** the historical snapshot at or below that ceiling. It alone determines every displayed fact. It cannot raise the ceiling, and later knowledge never backfills earlier views.

Both default to `cp-arr-2-0`. Lowering the ceiling clamps the view. Changing either control clears transient search, focus, selection, and details before rebuilding; no navigation back-stack is in scope. Unknown, missing, or invalid saved checkpoint IDs reset both controls to the earliest checkpoint. Revalidate persisted state after content/schema updates.

Keep the projection pure: `Project(dataset, viewCheckpoint, contentView)`. The content view (user request, 2026-11-14) selects main-story-only or main-plus-optional records; it is a data axis, not a spoiler control. Ceiling rules are separate state logic, not a second axis of lore data. Apply filtering before search, sorting, counts, graph layout, neighbor lists, details, and citation titles/URLs/tooltips. Never disclose hidden-entity counts or future names as hints. Checkpoint labels themselves must be spoiler-neutral.

Displayed citation metadata must be safe for its snapshot. If a URL itself reveals later facts, omit that outbound link and retain safe reviewed citation text. Open only explicit `http`/`https` clicks; do not fetch automatically or reuse the current Lore Explain source renderer unchanged. Explain briefly that external pages may contain later spoilers: the Atlas UI's filtering guarantee does not extend to destination pages.

## Execution order and ownership

All stories use isolated worktrees and [the delivery workflow](github-workflow.md); the lead owns integration and `Plugin.cs`. Record the actual SDK used rather than silently importing the primary checkout's untracked `global.json`. Preserve unrelated dirty work even when it prevents synchronizing primary `main`.

**Local viewer parity** (user decision, 2026-11-14). A browser-based local viewer (`NpcDialogueLinks.AtlasViewer/`, never packaged) is maintained alongside the in-game window for the whole pilot, so the Atlas can be viewed without launching FFXIV. Both front ends render the shared pure `AtlasSession`, and all browsing rules and player-facing text stay in `NpcDialogueLinks/Atlas/`. Every Atlas UI change updates both in the same pull request, and handoffs report viewer parity as its own evidence lane. See [local-viewer.md](atlas/local-viewer.md).

### Part 1: Publish this plan

Publish the reconciled Atlas brief, Atlas-specific roadmap entry, and three **To Do** cards. Record the priority exception at every former gate and distinguish the pilot from future candidates. No lore research or runtime code belongs in this planning bootstrap.

### NDL-002: Discovery, contract, and tested foundation

Owner: `lead`, with bounded content research and model/test ownership.

1. Research the candidate roster, player-knowledge boundaries, citations, and representative temporal changes first. Exit discovery only when the fixed pilot is sourceable and worked examples demonstrate both required changes.
2. Freeze the minimal schema from that evidence, then implement production model/loader/validator/projection and spoiler-state policy in `NpcDialogueLinks/Atlas/`, free of Dalamud, ImGui, and `Plugin.*` dependencies.
3. Add sibling `NpcDialogueLinks.Tests/`, plain `net10.0`, compile-linking the actual pure production files. Keep it outside plugin globs, with its own dependency lock file and documented direct restore/test commands. Preserve the plugin's `net10.0-windows`/x64 target.
4. Test synthetic fixtures for both snapshots, temporal edges, direction, every display/search leak surface, hidden counts, invalid references and bounds, draft/strict review modes, malformed/missing data, reverse viewing, stale saved state, clamping, and no view-driven ceiling raise. Run locked restore, local tests, and the plugin build.

No `Plugin.cs` wiring, packaging changes, or shipped `atlas.json` in this story. In-game testing is not applicable while this remains disconnected pure code; runtime wiring would change that evidence requirement. Obtain story acceptance before dependent finalization.

### NDL-003: Complete research and reviewed Scions content

Owner: `content`; depends on accepted `NDL-002`.

Complete the evidence matrix for every entity, name, alias, description, relationship, and citation at both checkpoints. Author `NpcDialogueLinks/atlas.json` against the production validator, with original summaries, category glyph mapping, expected snapshots, and a readable source review sheet. Validate the actual file, not only synthetic fixtures.

Present the concrete content for human review; correct it and rerun structural validation/snapshot tests. After acceptance, mechanically update review markers and pass strict shippable validation before merge. This story adds no packaging or runtime integration, except the explicitly reviewed bounded contract-amendment escape hatch above.

Full research may overlap foundation implementation after the contract is frozen, but final content acceptance depends on the production validator and accepted foundation. There is no separate pre-research approval request or extra content story.

### NDL-005: UX design and local-viewer prototype

Owner: `ui`; depends on accepted `NDL-002`. Added by the user on 2026-11-14, because the window story only fixed what the Atlas must do, not how it should look or feel.

Write `docs/atlas/ux-design.md`: layout and minimum window size, the primary flows, visual language (category glyph plus color, direction, edge labels, symmetric edges, interaction states), empty/no-result/failure states, and accessibility at 100%/150% font scale. Every element gets an ImGui feasibility note, so the design is buildable in Dalamud rather than browser-only.

Prototype the design in the local viewer over synthetic data and iterate with the user there. Shared behavior and text belong in the core with tests; the viewer stays a thin renderer. The design may not weaken any spoiler-safety invariant or change the frozen schema; flag such a need instead. It can run alongside `NDL-003` because it needs no real lore. User acceptance of the design is required before `NDL-004` starts.

### NDL-004: Window, integration, and in-game acceptance

Owner: `ui`; lead retains `Plugin.cs`, configuration, and project packaging ownership. Depends on accepted `NDL-002`, `NDL-003`, and `NDL-005`.

Build the window to the accepted `NDL-005` design. Implement `/npclinks atlas` and help strings, register the window with the existing `WindowSystem`, clean it up on disposal, persist both controls, and contain load errors. Build search/focus/refocus, the directed neighborhood, complete visible-neighbor list, detail panel, and safe source actions. Declare minimum size and verify readable labels at small/large sizes and 100%/150% font scales.

Add the `atlas.json` content-copy entry in the project file in this story only. Inspect the Debug output and the actual Release `latest.zip`. Verify offline operation, plugin load/unload/reload, open/close, search/refocus, arrow meaning, checkpoint changes including reverse viewing, conservative recovery, persistence, source handling, and malformed/missing-data isolation. Smoke dictionary/chat links and Explain for regressions. Existing README edits stay out of scope; document the command in the Atlas guide/handoff instead.

If integration reveals a content defect, repeat the content validation and review for the affected records rather than silently editing accepted lore. Keep automated checks, build/package checks, in-game observations, and explicit user acceptance as separate lanes. Missing game access means in-game evidence is pending, never passed.

Present the real usable pilot for final acceptance, then refresh/revalidate/merge, update the roadmap status, and clean only owned branches/worktrees. Do not claim product completion from the planning publication, a passing test, or a draft PR.

## Council agreement

All four delegates ran at high reasoning effort. The implementation-plan review took two full rounds: all requested changes in round 1, then all agreed in round 2. The subsequent sequencing review took one full round plus a targeted Fable wording recheck. Opus, Sol, and Astra agreed with the order; Fable agreed after the three adopted amendments (reconcile the entire brief, bounded contract corrections, draft versus shippable validation). No numerical scores were requested or supplied.

Amended by the user on 2026-11-14: a UX design step (`NDL-005`) now precedes the UI step and may run alongside the data step. The original agreed sequence is: **planning authorization/publication → discovery research → minimal contract and tested foundation → complete researched and reviewed data → UI → integration and in-game validation → explicit acceptance and closeout**.

## Future candidates — not approved

After the pilot, separately groom any dictionary/Lore Explain eligibility bridge, reviewed dictionary-text reuse, additional checkpoints/groups/locales, curated story-event entities, portraits, situation/map views, or import/editing workflows. Ordinary concepts, mechanics, duties, items, currencies, and servers remain dictionary-only. Automatic progression filtering requires verified runtime evidence; AI output never silently creates canon.

Quest-scoped views (quest-level story points, per-quest change views, quest and event entries, in-quest relationships, and following the player's current quest) are parked in the [backlog's Parking Lot](backlog.md#quest-scoped-atlas-views-parked-by-the-user-2026-11-14) (user, 2026-11-14).

Guardrails carried over from the original deferred brief, which this contract supersedes. They apply to every future Atlas story:

- Never infer relationships from conversational proximity, nearby NPCs, the active quest list, or unverified event identifiers.
- Represent motives or feelings only when reviewed sources support them; no AI-interpreted "inner voice" layer.
- Any import, export, sharing, or editing workflow preserves source and review metadata and distinguishes bundled, user-authored, and reviewed AI-assisted provenance.
- Prefer a readable local neighborhood over a whole-world graph; a situation or map view, if ever approved, reuses the same entities, relationships, and checkpoints instead of a parallel lore database.

The original FFXVI design references remain background reading, not evidence for FFXIV story claims:

- [PlayStation Blog: FFXVI lore systems](https://blog.playstation.com/2023/04/13/state-of-play-debuts-25-minutes-of-all-new-final-fantasy-xvi-gameplay/)
- [Square Enix: FFXVI updates](https://www.square-enix-games.com/en_US/documents/update-final-fantasy-xvi?preview=true)
- [GDC Vault: Designing Active Time Lore](https://www.gdcvault.com/play/1034418/Designing-Active-Time-Lore-for)
- [Square Enix: localization and spoiler timing](https://na.finalfantasy.com/topics/566)
