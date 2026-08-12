# Tools Agent Guidance

This folder contains helper scripts that produce reviewable artifacts for the plugin. Tool output is not canon by default.

## Term Lookup Validation

`lookup_terms.py` creates candidate dictionary entries from one web-search LLM call per term. Treat every result as a proposal until reviewed.

Before moving a lookup result into a dictionary file, validate:

- The definition is supported by the returned sources.
- At least one source is appropriate for FFXIV lore or game data; prefer `ffxiv.consolegameswiki.com` when available.
- The term is the intended proper noun, not a same-name NPC, quest, location, item, or title from a different context.
- Aliases are source-supported and likely to appear in dialogue.
- The definition is concise enough for an in-game dictionary click.
- Spoiler-sensitive language is minimized unless the term inherently requires it.
- Story-progress-sensitive claims are either avoided or captured in review notes for future richer schema work.
- `readyForDictionaryReview` is true only when source quality and ambiguity are acceptable.

## Promotion Rules

- Do not automatically write lookup output into bundled `NpcDialogueLinks/terms.json`.
- Prefer adding only entries marked ready after human or lead-agent review.
- Keep definitions neutral, concise, and useful in the current dialogue context.
- Preserve the current `terms.json` format unless the dictionary schema and docs are intentionally updated together.
- Prefer approved runtime/user edits in the plugin config `user-terms.json` so local additions survive plugin updates.
- If a proposed entry introduces aliases, use the object form with `definition` and `aliases`.
- If a proposed entry is uncertain, leave it in the lookup result file or a review note rather than adding it.

## Validation Handoff

When handing off reviewed terms, list:

- Terms accepted.
- Terms rejected or deferred.
- Sources used for accepted terms.
- Any spoiler or patch-freshness concerns.
- Whether a dictionary file was changed.
