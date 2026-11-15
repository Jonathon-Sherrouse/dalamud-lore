# Enhancement Roadmap

This is the working planning list for feature polish and future enhancements. Agents should consult this before proposing new work so recurring ideas stay organized instead of being rediscovered from scratch.

## How Agents Should Use This

- Check this file before planning feature work, UI polish, dictionary schema changes, or content workflow changes.
- Treat `Pre-Ship` items as the highest-priority candidate scope unless the user says otherwise.
- Move completed items into `Completed` with a short note, or update the item in place if the implementation changes the shape of the idea.
- If an enhancement changes dictionary content format, also update [agent-workflow.md](agent-workflow.md), [backlog.md](backlog.md), and any user-facing docs that describe dictionary behavior.
- Content-facing changes should preserve the rule that researched dictionary definitions are reviewed before becoming canonical or user-saved entries.
- For quest metadata work, start with [quest-metadata-investigation.md](quest-metadata-investigation.md). Do not send quest id/name context unless the source is verified for the active `Talk` line.

## Pre-Ship

### Dictionary UX

- Add a way to restore hidden bundled terms.
- Add a reset action for bundled overrides so users can return to the shipped definition without hiding the term.
- Search across canonical terms, aliases, and definitions.
- Add filters for bundled terms, user terms, user overrides, and hidden bundled terms.
- Add clearer duplicate/alias conflict warnings when creating or updating terms.
- Add an "open user dictionary location" action or command for backup/debugging.

### Dictionary Content

- Review generic or meta definitions and rewrite them in a more in-universe style.
- Prefer definitions that explain what the term means to the character/world rather than what it means as FFXIV content.
- Keep definitions concise enough for chat clicks and dictionary browsing.
- Research content changes on the web by default; prefer Final Fantasy XIV community wiki sources when appropriate.
- Flag spoiler-sensitive terms for a future richer metadata pass rather than over-explaining them in the short definition.

### In-Game Validation

- Validate create, update, delete, hide, reload, and override behavior after plugin reload.
- Validate dictionary editor layout at small and large window sizes.
- Validate Lore Explain proposal save flow with at least one response that includes dictionary proposals.
- Confirm user dictionary changes survive plugin rebuild/update scenarios.

### Quest Metadata Readiness

- Paused after first runtime probe analysis. Resume by implementing Probe v2 from [quest-metadata-investigation.md](quest-metadata-investigation.md), then collect a second verified sample pass.
- Validate the debug-only quest metadata probe before enabling player-facing quest context.
- Expand probe coverage if needed to include native event id, tracked quest state, or safely accessible event-handler fields.
- Run the test matrix from [quest-metadata-investigation.md](quest-metadata-investigation.md): non-quest NPC talk, active sidequest dialogue, MSQ dialogue, and repeatable or cutscene-adjacent dialogue.
- Promote quest metadata only if a source gives a direct quest row/id for the active dialogue line.
- Keep current fallback behavior: omit quest metadata rather than infer it from active quests, nearby NPCs, zone, or journal state.

## Next Polish Pass

### Dictionary Window

- Show aliases as secondary rows or compact chips in the detail panel.
- Add a source/status badge for each selected term.
- Add a small activity/status area that does not shift the main layout when messages appear.
- Consider a preview of the exact chat-click output for the selected term.
- Add keyboard-friendly save/cancel behavior if Dalamud/ImGui input handling supports it cleanly.

### Lore Explain

- Add a manual "turn this answer into a dictionary proposal" action.
- Add "Explain selected dictionary term" from the dictionary window.
- Show whether an answer used web search, local dictionary context, or both.
- Keep a small pending proposal queue so proposals can be reviewed later instead of only from the current result.
- When verified quest metadata exists, show the quest name in Context and include it in Lore Explain requests.

### Dialogue Matching

- Prefer longer overlapping matches, such as `Order of the Twin Adder` before `Twin Adder`.
- Add a recent detected terms history.
- Add a setting to suppress repeated detections within the same conversation.
- Add a user ignore list for noisy terms.

## Approved: Atlas v2 (arc context)

- **Priority (user decision, 2026-11-14):** Atlas v2 goes ahead of `Pre-Ship` and `Next Polish Pass`; those items stay open.
- **Plan:** [docs/atlas/v2-plan.md](atlas/v2-plan.md). A confused player opens the Atlas mid-story and sees the researched arc they're in: a reviewed "story so far" recap plus the whole cast's relationships, built quest by quest. It also adds the Story point and Changes lenses and Follow (completed progress). It is proven on one 2.0 arc.
- **Cards:** `NDL-006` to `NDL-010` in [backlog.md](backlog.md).
- **Future candidates (not approved):**
  - **Breadth coverage across the main story.** The route is decided after the slice proves it helps; it must not use patch-sized outer arcs, and milestone-only recaps give endpoint coverage only.
  - **Lore Explain grounded in the reviewed recaps,** and a deep link into the Atlas.

## Approved Atlas Pilot

### Lore Relationship Atlas

- The user authorized Part 1 planning publication on 2026-11-14. Exception: the bounded `NDL-002` → `NDL-003` and `NDL-005` → `NDL-004` pilot may proceed ahead of `Pre-Ship` and `Next Polish Pass`; those items remain open. This is not blanket approval for broader Atlas features.
- Start with story/source discovery before freezing the contract; build and test the pure foundation, then complete research and human-reviewed data, then implement the window and validate in game. See [backlog.md](backlog.md) for the pilot cards and their acceptance dependencies.
- Pilot: 8–12 English Core Scions entities (characters, organization, supporting locations), two snapshots labeled **ARR 2.0 complete** and **ARR 2.55 complete**, and original sourced checkpoint-specific summaries. Do not reuse live dictionary definitions. Story-event entities are outside this pilot.
- Open independently with `/npclinks atlas`, focused on one selected entity. Use deterministic labeled, directed connections, at most eight neighbors on the canvas, and a complete visible-neighbor list.
- Keep detected dictionary clicks and Lore Explain separate. Dictionary membership does not grant Atlas eligibility; ordinary concepts, mechanics, items, duties, currencies, and servers stay dictionary-only.
- Use **Spoiler limit** (originally "Knowledge approved through", renamed in `NDL-005`) as the confirmed spoiler ceiling and **Viewing as of** as the selected historical snapshot. Checkpoints and filtering belong in the pilot foundation; automatic progression/quest inference remains deferred.
- Sources, names, aliases, descriptions, and relationships require player-knowledge boundaries and human review. No AI-inferred canon or private feelings. Default category glyphs avoid portrait dependencies.
- Future **View in Atlas** bridges, dictionary-text reuse, story-event entities, maps, additional groups/checkpoints, and portraits require separately approved stories. They are not pilot slices or current acceptance prerequisites.
- See [lore-relationship-atlas.md](lore-relationship-atlas.md) for the complete reconciled pilot contract, research order, safety rules, and evidence lanes. This planning publication alone does not start research or implementation or complete the product; update this status only as the actual stories progress.
- **Status (2026-11-14): pilot complete.** `NDL-002` (foundation and local viewer), `NDL-003` (reviewed Scions content), `NDL-005` (UX design) and `NDL-004` (in-game window) are all **User Accepted**. The priority exception has served its purpose: `Pre-Ship` and `Next Polish Pass` were the default priority again until Atlas v2 was approved; see above. Broader Atlas ideas, including the quest-scoped views parked in the backlog, still need their own approved stories. User guide: [docs/atlas/README.md](atlas/README.md).

## Later Enhancements

### Dictionary Schema

- Add optional metadata fields:
  - category
  - sources
  - lastReviewed
  - spoilerLevel
  - patchOrExpansion
  - reviewStatus
- Consider multiple definitions per term keyed by story progress, expansion, quest, or patch.
- Add stale-entry review tooling for new FFXIV patches or expansions.
- Add import/export workflows for larger user dictionaries and shared lore packs.

### Presentation

- Explore direct dialogue-box presentation instead of chat-only links.
- Consider `/ndl` as a shorter command alias once command naming settles.
- Add richer context actions such as map links, wiki/search routing, or quest lookup when reliable metadata exists.
- Add quest-aware actions only after runtime validation proves the active dialogue can be mapped to a specific quest.

## Completed

- Shipped the Lore Relationship Atlas pilot (`NDL-002`–`NDL-005`, 2026-11-14). `/npclinks atlas` opens a spoiler-safe, offline relationship browser over 12 human-reviewed Scions entities at ARR 2.0 and 2.55, with main-story and optional-content views. A local browser viewer renders the same core without FFXIV. Guide: [docs/atlas/README.md](atlas/README.md).
- Added a merged dictionary model with bundled seed terms plus user `user-terms.json`.
- Added in-game create, update, delete/hide, reload, and editor UI support.
- Added command-line dictionary set/delete/reload/path commands.
- Added reviewed Lore Explain dictionary proposal saving.
- Added first-pass visual polish for the dictionary window and Lore Explain window.
- Added opt-in `/npclinks questprobe` JSONL export for quest metadata investigation.
- Made dialogue term detection case-aware so all-caps acronyms like `FATE` do not match lowercase words like `fate`, while lowercase terms can still match sentence-start capitalization.
