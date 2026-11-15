# Backlog

This is the executable acceptance queue used by the [GitHub workflow](github-workflow.md). For feature and polish candidates, see [enhancement-roadmap.md](enhancement-roadmap.md).

Only stable `NDL-###` story cards in the three workflow states below are executable. The legacy inventory is retained for grooming context and is not blanket implementation approval.

## To Do

The user approved publication of the bounded Atlas pilot plan and priority exception on 2026-11-14. Part 1 publishes these cards; it does not start research or implementation. On 2026-11-14 the user also approved a dedicated UX design story, `NDL-005`, which the window story implements. Execute in the order below (`NDL-005` may run alongside `NDL-003`); the complete contract is in [lore-relationship-atlas.md](lore-relationship-atlas.md).

- [ ] `NDL-004` **Deliver the standalone Atlas window and validate it in game**
  - Owner: `ui`
  - Outcome: `/npclinks atlas` opens a readable offline relationship browser over the accepted pilot data.
  - Acceptance: Visible-only search, focus/refocus, directed incoming/outgoing one-hop graph with at most eight canvas neighbors and a complete neighbor list, original details/safe sources, two persisted manual controls, declared minimum window size, and Atlas-only failure recovery. The local viewer stays at parity with the window, both rendering the shared `AtlasSession` (see the Atlas local-viewer guide). Lead owns Plugin.cs command/help/window lifecycle, configuration, and project packaging. No new Talk hooks, quest/progression inference, bridge, or API dependency. README changes deliberately deferred while unrelated local edits remain; document the command in the Atlas guide/handoff. Update roadmap status on accepted closeout.
  - Evidence: Host tests on production and real data; locked restore/build; atlas.json in Debug output and Release latest.zip; in-game load/unload/reload, open/close/search/refocus, direction, forward/backward boundaries, state recovery/persistence, sources, minimum/large windows at 100%/150% scale, offline/no-key operation, and malformed/missing-data isolation with dictionary/chat links/Explain intact. Report all lanes and explicit acceptance separately; missing in-game evidence remains pending. Content fixes repeat affected-record validation/review.
  - Dependencies: Accepted `NDL-002`, `NDL-003`, and `NDL-005` (the window implements the accepted `NDL-005` design); branch `codex/ndl-004-atlas-window`, PR base `main` after all three merges. Lead coordinates integration; no overlapping Plugin.cs edits.

## In Review

- [ ] `NDL-005` **Design the Atlas user experience and prototype it in the local viewer**
  - Owner: `ui`
  - Outcome: The user accepts a concrete Atlas interaction and visual design, proven in the local viewer, before any ImGui window is built.
  - Acceptance: `docs/atlas/ux-design.md` specifies the layout and minimum window size; the primary flows (first open at the earliest checkpoint, search → focus → refocus, raising the ceiling with confirmation, lowering and clamping, switching the content view, the overflow neighbor list, opening a source behind the spoiler warning); the visual language (category glyph plus color, never color alone; edge direction and labels; symmetric edges; hover, selected and focus states); empty, no-result and load-failure states; accessibility at 100%/150% font scale and contrast; and an ImGui feasibility note for every element. The local viewer is updated to the accepted design over synthetic sample data. Any new behavior or player-facing text goes into the shared core (`AtlasSession`, `AtlasText`, `AtlasGraphLayout`) with tests, so `NDL-004` renders the same thing. Frozen schema and spoiler invariants are unchanged; a needed change is flagged, not made. No plugin wiring, packaging, or real lore.
  - Evidence: Design doc with annotated viewer screenshots at the minimum and a large size; a walkthrough of each flow; host tests for core changes; locked restore and plugin/viewer builds; ImGui feasibility review. In-game: not applicable. User design acceptance recorded separately.
  - Dependencies: Accepted `NDL-002`; branch `codex/ndl-005-atlas-ux-design`, PR base `main` after NDL-002 merge. May run in parallel with `NDL-003`: this story owns the viewer front end, `docs/atlas/ux-design.md`, and presentation-level core files, while `NDL-003` owns content; serialize any overlapping core edits.
  - Substantive PR: [#10](https://github.com/Jonathon-Sherrouse/dalamud-lore/pull/10)

## User Accepted

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
