# NPC Dialogue Links

Small proof-of-concept Dalamud plugin for FFXIV.

## Workflow

- Agent workflow guidance lives in [AGENTS.md](C:\Users\18633\Documents\dalamud-dev\AGENTS.md).
- Plugin-specific ownership rules live in [NpcDialogueLinks/AGENTS.md](C:\Users\18633\Documents\dalamud-dev\NpcDialogueLinks\AGENTS.md).
- Planning templates and backlog live under [docs](C:\Users\18633\Documents\dalamud-dev\docs\agent-workflow.md).

## Current POC

- Watches the native `Talk` addon for active NPC dialogue.
- Pulls the current dialogue text from likely `AtkTextNode` fields on `AddonTalk`.
- Extracts candidate phrases only from exact matches in a local term dictionary.
- Prints clickable Dalamud chat links when a new dialogue line appears.
- Clicking a known dictionary term shows its definition in chat.

## Dictionary

- Terms live in [NpcDialogueLinks/terms.json](C:\Users\18633\Documents\dalamud-dev\NpcDialogueLinks\terms.json).
- Add new entries by editing `terms.json` with a new term key and its definition text.
- The first seeded entry is `Gridania`.
- Dictionary terms are matched directly against captured dialogue and also used when handling clicks.
- Terms that are not present in the dictionary are ignored, even if they are capitalized.
- Rebuild the plugin and reload it in Dalamud after changing `terms.json` so new entries are picked up.

## Commands

- `/npclinks`
- `/npclinks show`
- `/npclinks list`

## Why this shape for v0

This keeps the first milestone low-risk:

- real game integration through the `Talk` addon
- real click handling through Dalamud chat links
- no native node mutation yet

That gives us a stable loop to improve before we attempt:

- injecting clickable text into the actual dialogue box
- richer phrase extraction backed by game data
- context actions like map links, quest lookups, or wiki/search routing

## Build note

The project targets `Dalamud.NET.Sdk/14.0.2` and `net10.0-windows`, which matches current Dalamud API 14 guidance.
