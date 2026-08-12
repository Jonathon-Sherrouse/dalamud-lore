# Lore Explain

Internal codename: "girl wtf are they talking about"

## Purpose

`Lore Explain` is an in-game contextual explanation workflow for FFXIV dialogue. Instead of trying to pre-build dictionary entries for every proper noun, the user can explain the current captured dialogue or paste standalone text and ask a short contextual question.

The core question is:

> What are they talking about, and what context do I need to understand this?

## Proposed Command

Primary command:

```text
/npclinks explain <dialogue paragraph>
```

Optional focused-question form:

```text
/npclinks explain <dialogue paragraph> | <specific question>
```

If the dialogue side is empty, the plugin can use the last captured Talk dialogue:

```text
/npclinks explain | Why is this NPC warning me about the elementals?
```

Possible future alias:

```text
/ndl explain <dialogue paragraph>
```

User-facing label candidates:

- Lore Explain
- Explain This Dialogue
- Pray Explain
- Context Echo

## Expected Behavior

Given a pasted dialogue paragraph, the workflow should:

- explain the passage in concise plain language
- answer the user's specific question when one is provided after `|`
- identify only the lore terms, factions, places, people, and events needed for that passage
- explain relationships and narrative meaning, not just define capitalized words
- use web research when needed rather than relying only on model memory
- cite sources for researched claims
- optionally propose reusable dictionary entries for human review
- avoid writing generated lore directly into bundled `terms.json`

## Current Architecture

Keep the Dalamud plugin focused on capture, context, settings, and presentation. Live LLM work is optional and user-configured; a file-export helper remains available as a fallback.

The plugin currently:

- explains current dialogue through `/npclinks explain`
- accepts pasted standalone text through `/npclinks explain <text>`
- accept an optional focused question after `|`
- call OpenAI directly when live explain is enabled in `/npclinks config`
- show the response in a Lore Explain window with a conversation transcript and follow-up input
- show editable dictionary proposals when the response includes reviewable entries
- include recent dialogue history, zone, and best-effort possible speaker for current-dialogue requests
- treat pasted text as standalone so stale scene context is not attached
- prefer `ffxiv.consolegameswiki.com` when web search is enabled
- clean inline markdown citations from the displayed answer while preserving clickable sources
- write a small request file for companion tooling when live explain is disabled or no API key is configured

The external helper:

- receive the paragraph and optional surrounding metadata
- create a Markdown draft for human/LLM research
- include local dictionary context when known terms are detected
- keep generated dictionary proposals reviewable instead of writing to bundled `terms.json`

## Suggested Request Shape

```json
{
  "source": "manual-command",
  "dialogue": "The pasted dialogue paragraph.",
  "question": "Optional focused user question.",
  "knownTerms": ["Gridania", "Black Shroud"],
  "metadata": {
    "zoneName": "Labyrinthos",
    "territoryType": 956,
    "mapId": 0,
    "targetName": "Una'to Akhabila",
    "speakerName": "Una'to Akhabila",
    "speakerConfidence": "target-name-best-effort",
    "questName": "",
    "questId": null,
    "questConfidence": "not-implemented"
  },
  "dialogueHistory": [
    "Previous captured dialogue line."
  ],
  "output": {
    "explanation": true,
    "citations": true,
    "dictionaryProposals": true
  }
}
```

## Live Plugin Settings

`/npclinks config` controls direct in-game explanation:

- `Enable live Lore Explain`: turns direct OpenAI calls on or off
- `OpenAI API key`: user-provided key stored in local Dalamud plugin config
- `Model`: dropdown with curated model IDs and price hints
- `Allow OpenAI web search for citations`: enables the Responses API web search tool
- `Max output tokens`: caps response length for in-game readability

If live explain is off, the command falls back to the file-export helper workflow.

## Scene Context Rules

- `/npclinks explain` uses the last captured dialogue and attaches current scene context.
- `/npclinks explain | <question>` asks about the last captured dialogue and attaches current scene context.
- `/npclinks explain <text>` treats `<text>` as standalone and does not attach current scene context/history.
- `/npclinks explain <text> | <question>` treats `<text>` as standalone and answers the focused question.

Current scene context includes:

- recent unique Talk dialogue lines
- current zone/territory metadata when available
- current target as best-effort possible speaker metadata
- local dictionary matches

## Suggested Response Shape

```json
{
  "summary": "Short explanation of what the passage means.",
  "questionAnswer": "Direct answer to the user's focused question, when provided.",
  "relevantContext": [
    {
      "term": "Gridania",
      "whyItMatters": "Why this term matters for this exact passage.",
      "sources": ["https://..."]
    }
  ],
  "dictionaryProposals": [
    {
      "canonicalName": "Gridania",
      "definition": "Concise proposed dictionary definition.",
      "aliases": [],
      "sources": ["https://..."],
      "status": "proposed"
    }
  ]
}
```

## Dictionary Proposal Saving

Live Lore Explain may append machine-readable dictionary proposals to the model response. The plugin strips that proposal block from the player-facing answer, then shows editable proposal drafts in the Lore Explain window.

Saving a proposal:

- writes to `user-terms.json` in the Dalamud plugin config directory
- updates the in-memory dictionary immediately
- does not modify bundled `NpcDialogueLinks/terms.json`
- still requires human review through the visible Save action

## Guardrails

- Do not treat generated explanations as canon without citations and review.
- Do not silently mutate any dictionary file from generated output.
- Do not write generated entries to bundled `terms.json`; approved saves belong in the user dictionary.
- Prefer short answers over lore essays unless the user asks for depth.
- Keep source citations attached to researched claims.
- When source quality is weak or conflicting, say so in the helper output.
- Treat best-effort speaker metadata as a hint, not guaranteed truth.
- Do not invent quest metadata when no verified quest context is available.

## Implemented Milestone

Direct plugin prototype with file-export fallback:

1. `tools/explain_dialogue.py` accepts plugin-exported request JSON and creates a Markdown draft.
2. `/npclinks explain` supports current dialogue, pasted text, and optional focused questions.
3. `/npclinks config` supports API key, model selection with price hints, web search toggle, live explain toggle, and output token cap.
4. Live requests call OpenAI through the Responses API.
5. The Lore Explain window displays loading, errors, transcript turns, follow-up input, scene context, recent context, and clickable sources.
6. Recent dialogue history and zone/best-effort speaker metadata are attached only for scene-aware requests.
7. Reviewable dictionary proposal drafts can be edited and saved to the user dictionary.

## Open Questions

- Should helper output be Markdown, JSON, or both?
- Where should queued explain requests live?
- Should the short alias be `/ndl`, or should command naming stay under `/npclinks` for now?
- Which Talk addon field reliably contains the speaker name?
- Can quest id/name be captured reliably during quest-bound dialogue?
- How much dialogue history should be sent before answers become noisy?

## Follow-Up Planning

See `docs/lore-explain-next-steps.md` for planned Dialogue History, Ask Follow-Up, Speaker/Zone Context, and Quest Metadata work.
