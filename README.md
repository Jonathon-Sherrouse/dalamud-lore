# NPC Dialogue Links

Small proof-of-concept Dalamud plugin for FFXIV.

## Workflow

- Agent workflow guidance lives in [AGENTS.md](C:\Users\18633\Documents\dalamud-dev\AGENTS.md).
- Plugin-specific ownership rules live in [NpcDialogueLinks/AGENTS.md](C:\Users\18633\Documents\dalamud-dev\NpcDialogueLinks\AGENTS.md).
- Planning templates and backlog live under [docs](C:\Users\18633\Documents\dalamud-dev\docs\agent-workflow.md).

## Current POC

- Watches the native `Talk` addon for active NPC dialogue.
- Pulls the current dialogue text from likely `AtkTextNode` fields on `AddonTalk`.
- Sanitizes captured dialogue formatting artifacts before matching or explaining.
- Extracts candidate phrases only from case-aware exact matches in a local term dictionary.
- Prints clickable Dalamud chat links when a new dialogue line appears.
- Clicking a known dictionary term shows its definition in chat.
- `/npclinks dict` opens an in-game dictionary window with search, an alphabetical term list, and user dictionary editing.
- Alias terms can appear as their own dictionary rows while still resolving to the same shared definition.
- `/npclinks explain` can call OpenAI directly when live explain is enabled.
- Lore Explain can surface editable dictionary proposals that must be reviewed before saving.
- Lore Explain requests include scene context for current-dialogue explanations: recent dialogue history, zone, and best-effort possible speaker.
- Explicit pasted text is treated as standalone and does not attach stale scene metadata/history.

## Dictionary

- Bundled seed terms live in [NpcDialogueLinks/terms.json](C:\Users\18633\Documents\dalamud-dev\NpcDialogueLinks\terms.json).
- User-created edits are saved to `user-terms.json` under the Dalamud plugin config directory.
- Create, update, and delete terms from `/npclinks dict` without reloading the plugin.
- Command-line edits are also available through `/npclinks dict set`, `/npclinks dict delete`, and `/npclinks dict reload`.
- Simple entries can stay in the short form: `"Gridania": "definition..."`.
- Entries with alternate names can use the object form with `definition` and optional `aliases`.
- Deleting a user term removes it from `user-terms.json`; deleting a bundled term hides it through user dictionary metadata instead of changing the bundled file.
- User entries override bundled entries with the same canonical term name.
- The first seeded entry is `Gridania`.
- Dictionary terms are matched with exact casing by default and also used when handling clicks.
- Lowercase terms and aliases also match a sentence-start capitalized form, such as `electrope` matching `Electrope`.
- Alias matches resolve to the same shared definition as their canonical entry.
- Terms that are not present in the dictionary are ignored, even if they are capitalized.
- Manual external edits to `user-terms.json` can be picked up with `/npclinks dict reload`.
- Manual edits to bundled `terms.json` still require rebuilding or recopying the plugin output in a dev workflow.

Example:

```json
{
  "Black Shroud": {
    "definition": "A vast forest region surrounding Gridania...",
    "aliases": ["Twelveswood"]
  },
  "Gridania": "One of Eorzea's three starting city-states..."
}
```

Command examples:

```text
/npclinks dict set Meracydia | Southern continent tied to dragons, Allag, and ancient history.
/npclinks dict set Order of the Twin Adder | Gridania's Grand Company. | Twin Adder, The Order of the Twin Adder
/npclinks dict delete Meracydia
/npclinks dict reload
/npclinks dict path
```

## Commands

- `/npclinks`
- `/npclinks dict`
- `/npclinks dict set <term> | <definition> | <optional aliases>`
- `/npclinks dict delete <term>`
- `/npclinks dict reload`
- `/npclinks dict path`
- `/npclinks questprobe on|off|status|path`
- `/npclinks questprobe capture <verified quest name>`
- `/npclinks config`
- `/npclinks lore`
- `/npclinks show`
- `/npclinks list`
- `/npclinks explain <dialogue> | <question>`

## Lore Explain

`/npclinks explain <dialogue> | <question>` explains a pasted paragraph of dialogue. The optional `| <question>` portion lets the player ask what they specifically want explained.

Examples:

```text
/npclinks explain Pray return to the Waking Sands.
/npclinks explain The Black Wolf moves again. | Who is the Black Wolf and why does this matter?
/npclinks explain | Why is this NPC warning me about the elementals?
```

If no paragraph is provided, it uses the last captured Talk dialogue. This means `/npclinks explain | <question>` asks a question about the last captured line.

Scene context behavior:

- `/npclinks explain` and `/npclinks explain | <question>` include current zone, possible speaker, and recent dialogue history.
- `/npclinks explain <text>` treats the pasted text as standalone and does not attach current scene metadata/history.
- `/npclinks explain <text> | <question>` also treats the pasted text as standalone.

Live explain is controlled by `/npclinks config`.

- Enable live Lore Explain to call OpenAI directly from the plugin.
- Paste your own OpenAI API key into settings.
- Choose a model from the dropdown, which includes price hints.
- Toggle OpenAI web search for source-backed answers.
- Web search instructions prefer `ffxiv.consolegameswiki.com` before falling back to other sources.
- Results appear in the Lore Explain window.
- Reopen the latest result with `/npclinks lore`.
- Ask follow-up questions from the Lore Explain window.
- Review and edit dictionary proposals in the Lore Explain window before saving them to the user dictionary.

If live explain is off, or if no API key is configured, the command writes a JSON request under the plugin config directory so external tooling can research and explain the passage with citations.

## Quest Metadata Probe

Quest metadata is not sent to Lore Explain yet. The probe is an opt-in investigation tool for collecting evidence about which quest, if any, owns a captured `Talk` dialogue line.

Workflow:

```text
/npclinks questprobe on
```

Talk to a quest NPC. The plugin will auto-export each newly captured Talk line while the probe is enabled. If you can verify the quest name from the journal or your in-game context, add a manual marked capture:

```text
/npclinks questprobe capture The Verified Quest Name
```

Probe output is written as JSONL under the plugin config directory:

```text
quest-metadata-probes/quest-probe-YYYYMMDD.jsonl
```

Each record includes the dialogue line, your optional verified quest name, zone/target context, target object identifiers, known local dictionary terms, and recent `Talk` addon setup/refresh `AtkValue` snapshots. Treat all captured quest-related fields as investigative data until runtime validation identifies a direct source of truth.

Starter helper:

```powershell
python tools\explain_dialogue.py <path-to-exported-request.json>
```

The helper creates a Markdown draft next to the request file. It includes the pasted dialogue, optional user question, locally known dictionary terms, and TODO sections for researched explanation, citations, and optional dictionary proposals.

Term lookup helper:

```powershell
$env:OPENAI_API_KEY = "sk-..."
python tools\lookup_terms.py "Gridania" "Black Shroud" --out term-lookup-results.json
python tools\lookup_terms.py --terms-file terms-to-research.txt --out term-lookup-results.json
```

The lookup helper performs one OpenAI web-search request per term and writes reviewable dictionary proposals with sources. It does not modify bundled `terms.json` or the user dictionary automatically.

## Current UI

- Dialogue term clicks remain chat-based for now.
- The in-game dictionary window is separate from dialogue clicks.
- The Lore Explain window shows live explanation status, a conversation transcript, follow-up input, and sources returned by OpenAI.
- Context, Recent Context, and Sources sections are hidden behind headers by default.
- Source titles are blue, underlined, and clickable; clicking opens the source URL in the default browser.
- Inline markdown citations are stripped from the main answer text so answers read cleanly in game.
- The dictionary window supports manual close via the title bar close button.
- The dictionary list is alphabetical and searchable.
- The dictionary window supports New, Edit, Save, Delete, and Reload actions for the user dictionary.

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

The project targets `Dalamud.NET.Sdk/15.0.0` and `net10.0-windows`, which matches current Dalamud API 15 guidance.
