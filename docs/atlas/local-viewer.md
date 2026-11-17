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
| `--arc-sample` | off | Load the synthetic arc sample, `sample-arc-atlas.json`, to walk through the v2 lenses ([ux-design.md](ux-design.md#v2-lenses-ndl-008)). |
| `--draft` | off (Strict, same as the runtime) | Allow `pending` records. A banner marks the data as not shippable. Needed for content still under review. |
| `--port <n>` | `5219` | Listen on another port. The viewer only ever binds to `127.0.0.1`. |
| `--portraits <dir>` | `NpcDialogueLinks.AtlasViewer/portraits` in the same local app-data folder; printed at startup | The portrait cache (below). |
| `--state <path>` | `NpcDialogueLinks.AtlasViewer/viewer-state.json` in the OS local app-data folder; the exact path is printed at startup | Where the two spoiler controls persist. It mirrors the plugin's configuration and is kept outside the repository. |

### Portraits (NDL-011)

The window loads portraits from the game. The viewer can't, so it reads the same images from a local cache that you fill once from your own game install:

```sh
dotnet run --project tools/atlas/PortraitCache
```

Run it from the repository root. It finds the game's `sqpack` folder in the XIV on Mac or standard Windows install, or you pass `--game <path>` (or set `FFXIV_SQPACK`). It extracts exactly the icons named in `atlas.json`, as PNGs, into the cache folder, which is outside the repository and never committed or packaged. Run it again after the portraits change.

The viewer draws each portrait with the same crop (`AtlasPortrait.Uv`), the same sizes and ring (`AtlasPortraitStyle`) and the same category badge as the window. It serves only icons named by the loaded data. Without the cache it draws the category shapes, as the window does before an icon loads.

- **Reload data** re-reads the file from disk. Edit `atlas.json`, click it, and the saved controls are revalidated, just as after a plugin content update.
- **On load failure** the page shows the same generic message the plugin will. The structured errors are printed in the terminal.

Avoid `--no-build` while the code is changing: it reuses an old binary.

The sample is invented data with the pilot's shape: 12 entities, 14 relationships, two checkpoints, and the same changes and optional records as the [worked examples](worked-examples.md). Its records are marked `reviewed` only so that Strict validation can exercise it. They are structural test data, not lore.

The **arc sample** (`--arc-sample`) is an invented harbor-siege story built to exercise the v2 lenses: five quest steps and two milestones, two arcs (one nested inside the other), relationships that start, end and restart, end evidence, a character who is in the story but not in the cast (Warden Orrin), and one optional record. It too is structural data, not lore, and `V2LeakSweepTests` sweeps it.

## How parity is kept

Neither front end has its own browsing logic. Everything lives in the pure core under `NpcDialogueLinks/Atlas/`:

| Core piece | Provides |
|---|---|
| `AtlasSession` | Spoiler controls and the confirmation flow, content view, search and grouped results, focus and refocus, the home entry (`AtlasDefaults`), relationship selection, the collapsed-by-default sources section, transient-state reset and its notice, persistence events |
| `AtlasProjector` | Visible-only snapshots, including each record's optional-content flag |
| `AtlasGraphLayout` | Deterministic node positions (at most 8 neighbors) and edge lanes |
| `AtlasText` | Every player-facing string, the category glyphs, and the neutral confirmation prompt |
| `AtlasLoader` | Loading, Strict validation, and failure isolation |

The plugin, the viewer and the tests all compile these same files. The viewer (`NpcDialogueLinks.AtlasViewer/`) and the Dalamud window (`NpcDialogueLinks/AtlasWindow.cs`, `NDL-004`) only render a session and forward clicks to its methods.

Maintenance rules for every change (the in-game window shipped in `NDL-004`):

1. **Change behavior in the core first.** Then render it in both the ImGui window and `wwwroot/index.html` in the same pull request.
2. **Add new player-facing text to `AtlasText`,** never inline in one front end.
3. **Keep the viewer's sample valid.** `NpcDialogueLinks.Tests` loads it, so a broken sample fails the build.
4. **Report viewer parity as its own evidence lane** in each Atlas handoff, separate from in-game checks.

### Deliberate differences

| Viewer | In-game window |
|---|---|
| Content selector, persisted only for the viewer process. | The same selector (accepted design, NDL-005), reset to main + optional on every open. |
| `--data` and `--draft` flags, a draft banner, and a Reload button. | Loads only the bundled `atlas.json`, Strict, once per open. |
| Errors go to the terminal. | Errors go to the Dalamud log. |
| Browser rendering (HTML and SVG). Direction arrows are text glyphs (← → ↔), and optional edges use an SVG dash. | ImGui rendering (`NpcDialogueLinks/AtlasWindow.cs`), with the same layout coordinates, glyphs, colors and text. Arrows are drawn, so they never depend on font coverage, and dashes are short line segments. |
| Portraits from the local cache (`tools/atlas/PortraitCache`); shapes without it. | Portraits from the game's own icons through Dalamud's texture provider; shapes until they load. |
| v2 lenses (`NDL-008`): "← Whole cast" and the change marks `+ − ~`. | The same lenses (`NDL-010`): "< Whole cast" and `+ - ~` in plain ASCII, so they never depend on font coverage. |

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
