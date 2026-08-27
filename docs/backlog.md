# Backlog

This is the executable acceptance queue used by the [GitHub workflow](github-workflow.md). For feature and polish candidates, see [enhancement-roadmap.md](enhancement-roadmap.md).

Only stable `NDL-###` story cards in the three workflow states below are executable. The legacy inventory is retained for grooming context and is not blanket implementation approval.

## To Do

No approved stories.

## In Review

No stories awaiting acceptance.

## User Accepted

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
