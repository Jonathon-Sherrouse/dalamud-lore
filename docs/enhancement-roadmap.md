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

- Added a merged dictionary model with bundled seed terms plus user `user-terms.json`.
- Added in-game create, update, delete/hide, reload, and editor UI support.
- Added command-line dictionary set/delete/reload/path commands.
- Added reviewed Lore Explain dictionary proposal saving.
- Added first-pass visual polish for the dictionary window and Lore Explain window.
- Added opt-in `/npclinks questprobe` JSONL export for quest metadata investigation.
- Made dialogue term detection case-aware so all-caps acronyms like `FATE` do not match lowercase words like `fate`, while lowercase terms can still match sentence-start capitalization.
