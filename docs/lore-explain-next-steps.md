# Lore Explain Next Steps

This document tracks the next context features for Lore Explain. The goal is to make answers feel aware of the current scene without trying to ingest all of Final Fantasy XIV at once.

## 1. Dialogue History

Goal: send recent scene context, not just one line.

Planned behavior:

- Keep a rolling buffer of the last 5-10 captured `Talk` dialogue lines. Done.
- Deduplicate repeated addon updates so the buffer only stores meaningful new lines. Done.
- Include recent lines in the Lore Explain request as `dialogueHistory`. Done.
- Keep the current line separate as `dialogue`. Done.
- Show recent context in the Lore Explain window hidden behind a header by default. Done.

Suggested request shape:

```json
{
  "dialogue": "Current dialogue line.",
  "dialogueHistory": [
    "Previous line one.",
    "Previous line two."
  ],
  "question": "Optional user question."
}
```

Definition of done:

- `/npclinks explain` includes recent dialogue context. Done.
- `/npclinks explain | <question>` answers against the latest line plus history. Done.
- `/npclinks explain <text>` treats pasted text as standalone and does not attach stale scene history. Done.
- The prompt tells the LLM to use history only when relevant. Done.

## 2. Ask Follow-Up

Goal: let the user ask a second question without re-running the whole command.

Planned behavior:

- Add a text input at the bottom of the Lore Explain window. Done.
- Add an `Ask` button. Done.
- Send the previous dialogue, previous answer, conversation transcript, and new follow-up question. Done.
- Replace or append the answer in the Lore Explain window. Done: the window now keeps a conversation transcript.
- Keep follow-ups short and scoped to the current dialogue scene.

Suggested request shape:

```json
{
  "dialogue": "Current dialogue line.",
  "dialogueHistory": [],
  "previousAnswer": "Last explanation text.",
  "followUpQuestion": "User follow-up."
}
```

Definition of done:

- User can ask a follow-up from the Lore Explain window. Done.
- The result window clearly distinguishes original question from follow-up. Done: each turn is shown as `You` and `Lore Explain`.
- Follow-up requests reuse the same settings, model, and web search toggle. Done.

## 3. Speaker And Zone Context

Goal: include cheap, reliable game-state metadata when available.

Planned behavior:

- Capture speaker name from the `Talk` addon if a stable text node or addon value can be identified.
- Include current territory/zone from Dalamud client state if available. Done.
- Include player target/interact target name only if it is reliable for the current dialogue. Current behavior: current target is included as best-effort possible speaker metadata and labeled with confidence.
- Show captured metadata in the Lore Explain window hidden behind a header by default. Done.

Suggested request shape:

```json
{
  "dialogue": "Current dialogue line.",
  "speaker": "Una'to Akhabila",
  "zone": "Labyrinthos",
  "targetName": "Una'to Akhabila"
}
```

Definition of done:

- Zone metadata is included without breaking when unavailable. Done.
- Speaker metadata is included only after verifying the correct Talk addon source. Pending; current target is marked `target-name-best-effort`.
- The LLM prompt treats metadata as context, not as guaranteed canon if uncertain.

## 4. Quest Metadata

Goal: include quest context when dialogue is part of a quest, if it can be obtained reliably.

Investigation tasks:

- Determine whether the active quest id/name is accessible through Dalamud services, agent data, or addon setup/refresh values.
- Check whether `Talk` addon values expose a quest row, event id, or related content id.
- Compare captured metadata across normal NPC talk, MSQ dialogue, sidequest dialogue, and cutscene-adjacent dialogue.
- Avoid brittle pointer assumptions unless runtime testing confirms stability.

Possible request shape:

```json
{
  "quest": {
    "id": 12345,
    "name": "Quest Name",
    "confidence": "verified"
  }
}
```

Definition of done:

- Quest metadata is included only when confidence is high. Guard implemented; capture source still pending.
- If quest metadata is unavailable, the request omits it instead of guessing. Done.
- Runtime notes document which dialogue scenarios were tested. Pending; see `docs/quest-metadata-investigation.md`.

## Suggested Order

1. Quest Metadata investigation
2. Reliable Talk-addon speaker field investigation
3. Spoiler mode
4. Dictionary proposal review flow

Dialogue History, Ask Follow-Up, and zone/best-effort speaker context are implemented and should continue to be validated in game.

## UI Polish Notes

- Inline markdown citations are stripped from the main answer text so the response reads cleanly in game.
- Returned sources are kept in the Sources section.
- Source titles are clickable and open their `http`/`https` URL through the OS shell.
- Context, Recent Context, and Sources are hidden behind headers by default.
- Source titles render blue and underlined.
