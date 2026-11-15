# Atlas local viewer and tests

The local viewer lets you browse the Atlas in a browser without launching FFXIV. It is a development tool only; it is never packaged with the plugin.

**Parity rule** (user decision, 2026-11-14): the local viewer and the in-game Atlas window are maintained together for the whole pilot.

The page's current look and layout are a functional placeholder. `NDL-005` owns the real UX design ([ux-design.md](ux-design.md)), and both front ends will follow it.

## Run it

```sh
dotnet run --project NpcDialogueLinks.AtlasViewer
```

Run this from the repository root, then open <http://127.0.0.1:5219/>.

| Flag | Default | Purpose |
|---|---|---|
| `--data <path>` | the synthetic `sample-atlas.json` | Load another Atlas file, such as the real pilot data: `--data "$PWD/NpcDialogueLinks/atlas.json"`. Its records are reviewed, so it loads in Strict mode like the plugin. Use an absolute path, because `dotnet run` starts the viewer in its project folder. |
| `--draft` | off (Strict, same as the runtime) | Allow `pending` records. A banner marks the data as not shippable. Needed for content still under review. |
| `--port <n>` | `5219` | Listen on another port. The viewer only ever binds to `127.0.0.1`. |
| `--state <path>` | `NpcDialogueLinks.AtlasViewer/viewer-state.json` in the OS local app-data folder; the exact path is printed at startup | Where the two spoiler controls persist. It mirrors the plugin's configuration and is kept outside the repository. |

- **Reload data** re-reads the file from disk. Edit `atlas.json`, click it, and the saved controls are revalidated, just as after a plugin content update.
- **On load failure** the page shows the same generic message the plugin will. The structured errors are printed in the terminal.

Avoid `--no-build` while the code is changing: it reuses an old binary.

The sample is invented data with the pilot's shape: 12 entities, 14 relationships, two checkpoints, and the same changes and optional records as the [worked examples](worked-examples.md). Its records are marked `reviewed` only so that Strict validation can exercise it. They are structural test data, not lore.

## How parity is kept

Neither front end has its own browsing logic. Everything lives in the pure core under `NpcDialogueLinks/Atlas/`:

| Core piece | Provides |
|---|---|
| `AtlasSession` | Spoiler controls and the confirmation flow, content view, search and grouped results, focus and refocus, the home entry (`AtlasDefaults`), relationship selection, the collapsed-by-default sources section, transient-state reset and its notice, persistence events |
| `AtlasProjector` | Visible-only snapshots, including each record's optional-content flag |
| `AtlasGraphLayout` | Deterministic node positions (at most 8 neighbors) and edge lanes |
| `AtlasText` | Every player-facing string, the category glyphs, and the neutral confirmation prompt |
| `AtlasLoader` | Loading, Strict validation, and failure isolation |

The plugin, the viewer and the tests all compile these same files. The viewer (`NpcDialogueLinks.AtlasViewer/`) and the future Dalamud window (`NDL-004`) only render a session and forward clicks to its methods.

Maintenance rules for every change, starting with `NDL-004`:

1. **Change behavior in the core first.** Then render it in both the ImGui window and `wwwroot/index.html` in the same pull request.
2. **Add new player-facing text to `AtlasText`,** never inline in one front end.
3. **Keep the viewer's sample valid.** `NpcDialogueLinks.Tests` loads it, so a broken sample fails the build.
4. **Report viewer parity as its own evidence lane** in each Atlas handoff, separate from in-game checks.

### Deliberate differences

| Viewer | In-game window |
|---|---|
| Content selector (main story only / main + optional) is always shown, so both views can be compared. | Uses the default main + optional view until a toggle is approved. |
| `--data` and `--draft` flags, a draft banner, and a Reload button. | Loads only the bundled `atlas.json`, Strict, once per open. |
| Errors go to the terminal. | Errors go to the Dalamud log. |
| Browser rendering (HTML and SVG). | ImGui rendering. Same layout coordinates, glyphs and text. |

## Tests

```sh
dotnet restore NpcDialogueLinks.Tests --locked-mode
dotnet test NpcDialogueLinks.Tests
```

The tests are plain `net10.0` with no Dalamud dependency, so they run on any host. They compile the actual production files and have their own `packages.lock.json`.

Other locked checks:
- **Viewer:** `dotnet restore NpcDialogueLinks.AtlasViewer --locked-mode`
- **Plugin:** `cd NpcDialogueLinks && dotnet build -c Release -p:RestoreLockedMode=true`

SDK used for `NDL-002` validation: .NET SDK 10.0.400 (runtime 10.0.11), macOS. The story worktree has no `global.json`. The primary checkout's untracked `global.json` was not imported.
