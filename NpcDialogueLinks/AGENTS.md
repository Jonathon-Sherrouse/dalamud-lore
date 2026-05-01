# Plugin Workflow

These instructions apply to everything under `NpcDialogueLinks/`.

## Ownership Map

- `Plugin.cs`: lead-owned integration point
- `DialogueCapture.cs`: runtime-owned
- `LinkCandidateExtractor.cs`: dictionary-owned
- `TermDictionary.cs`: dictionary-owned
- `terms.json`: content-owned
- `NpcDialogueLinks.csproj`: lead-owned unless a task is purely packaging-related

## Editing Rules

- Keep changes small and local to the owned area when possible.
- Do not widen the command surface in `Plugin.cs` unless the task specifically calls for it.
- For dictionary behavior changes, prefer exact and predictable matching over clever heuristics.
- For content changes in `terms.json`, keep definitions concise, neutral, and in-universe where practical.
- For content changes in `terms.json`, research definitions on the web before writing or revising entries.

## Handoff Expectations

- Runtime work should note how to reproduce the in-game scenario.
- Dictionary work should list which terms or matching behaviors changed.
- UI work should describe what the player should expect to see in chat or in a window.
