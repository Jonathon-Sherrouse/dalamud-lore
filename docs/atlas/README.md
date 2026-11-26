# Lore Atlas guide

> **Atlas v2** ([plan](v2-plan.md), `NDL-006` to `NDL-010`) adds quest-level story steps, the first story arc (*The Black Wolf's Challenge*, MSQ #155–161) and three lenses. **Follow** (`NDL-017`, awaiting acceptance) moves the view to your completed main-scenario progress when you turn it on. It is off by default, and while it's off the Atlas never reads your quest progress.

> **Coverage (2026-11-19):** one story point per main-scenario quest from MSQ #1 (all three starting cities) through 7.56 (*The World Locked in Ice*), the latest patch, plus the 2.0, 2.55, 3.0, 3.56, 4.0, 4.56, 5.0, 5.55, 6.0, 6.55, 7.0 and 7.56 milestones: 1,045 points and 169 arcs. See [through-heavensward.md](through-heavensward.md), [through-stormblood.md](through-stormblood.md), [through-shadowbringers.md](through-shadowbringers.md), [through-endwalker.md](through-endwalker.md), [through-dawntrail.md](through-dawntrail.md) and [arr-1-to-101.md](arr-1-to-101.md).

> **Earlier coverage (`NDL-012`, accepted 2026-11-17):** one story point per main-scenario quest from MSQ #102 to the 2.0 finale, with six arcs, from *The Road to Titan* to *The Black Wolf's Challenge*. See [ndl-012-discovery.md](ndl-012-discovery.md).

The Lore Atlas is a spoiler-safe relationship browser for the Scions of the Seventh Dawn pilot. You pick a story point, and it shows only what a player knows by then. The contract is [lore-relationship-atlas.md](../lore-relationship-atlas.md).

## In game

```text
/npclinks atlas
```

This toggles the Atlas window. It works offline and needs no OpenAI key.

- **Viewing as of** picks the story point. Points beyond your spoiler limit are greyed out and marked "(locked)".
- **Spoiler limit → Raise…** moves the limit. Raising it always asks first and never changes your view. Lowering it clamps the view.
- **Content** switches between main story + optional (the default) and main story only. In the full view, optional-quest connections are dashed and tagged "optional".
- The window opens on the Scions. Click a node or a name to refocus, and click an edge label or a connection's label to inspect that connection.
- **Sources (n)** starts collapsed. Links open in your browser only when clicked, behind the spoiler warning.
- **Lens** (the second row) switches between three views of the same story point ([design](ux-design.md#v2-lenses-ndl-008)). Next to it, "Viewing: after ‹quest›" names the point you chose, and quest steps add a note that they cover only the characters involved.
  - **Arc** shows the arc around the point: its whole cast on one chart, with the arc at the centre and faint lines to each member. The right pane has the arc's "Story so far" recap, what is new at this point, and what has ended so far. Click a member to see their own connections, inside the cast, and **< Whole cast** to go back. The **Story arc** picker reopens an arc that has already started.
  - **Story point** is the v1 browser described above.
  - **Changes** lists what this point added, ended or redescribed compared with the one before. Only an ended row shows **Sources for the ending**.
  - Until you pick a lens or an arc, the window chooses for you each time the view changes: Arc inside an arc, Story point elsewhere. A pick lasts until the window closes and is never saved.
- **Portraits.** Most entries show a picture from the game's own data (Triple Triad cards, quest and duty art) in a ring of their category colour, with their shape as a small badge. The Waking Sands has none, so it keeps its shape. Game icons load from your installation. Bundled face crops fill out the character roster, including some revealed identities and later forms. See [NPC portrait coverage](npc-portrait-coverage.md).
- **Follow my progress** (on the Lens row, off by default) moves the view to the latest main-scenario quest you've completed, never past your spoiler limit.
  - It reads your completed quests only, never your active quests or journal.
  - It re-reads when the window opens, when you click **Refresh**, and when you finish a quest.
  - Picking a point yourself turns it off.
  - Logged out or loading, it says "Progress unavailable" and leaves the view alone.
  - If your progress is past the limit, it stops at the limit and offers **Raise to my progress…** once, without naming a quest.
  - The toggle is saved; your progress isn't.
- **Open Atlas** in the Lore Explain window opens this window. It passes nothing across; the Atlas keeps its own spoiler limit and view.

**Dictionary previews** in the footer starts off. The first time you enable it, confirm the warning about later-story spoilers. Matching words and phrases in entry summaries and arc recaps get a dotted underline. Hover over a match for its definition, or click it to open that entry in the Dictionary. Turn previews off in the same spot. Your acknowledgement is remembered if you turn them back on.

The two spoiler controls and dictionary preview preference are saved in the plugin configuration. The checkpoint selections are revalidated every time the window opens. The window reads the bundled `atlas.json` in Strict mode on every open. If the file is missing or invalid, only the Atlas shows a generic message; the structured errors go to the Dalamud log (`/xllog`), and every other plugin feature keeps working.

### In-game check for dictionary previews

1. Reload the plugin and open `/npclinks atlas`. On a fresh preference, hover a known term and verify the prose is plain. Toggle **Dictionary previews**, cancel the warning, and check again.
2. Toggle again and select **Enable previews**. Hover a dotted term in a summary or recap, including a term that wraps across lines. Click it and verify the Dictionary opens on the definition shown in the tooltip. Return to the same Atlas entry.
3. Turn previews off, reload the plugin, and verify the choice persisted. Turn them back on and verify they activate without another warning.

## Files

| Path | What it is |
|---|---|
| `NpcDialogueLinks/Atlas/` | Pure shared core: model, loader, validator, projector, spoiler policy, session, layout and text |
| `NpcDialogueLinks/AtlasWindow.cs` | The ImGui window, a thin renderer over `AtlasSession` |
| `NpcDialogueLinks/atlas.json` | The accepted pilot data, generated by `tools/atlas/build_pilot_content.py` and packaged with the plugin |
| `tools/atlas/PortraitCache/` | Copies the portraits from your game install into the viewer's local cache, outside the repository ([local-viewer.md](local-viewer.md#portraits-ndl-011)) |
| `NpcDialogueLinks.AtlasViewer/` | The local browser viewer, kept at parity with the window ([local-viewer.md](local-viewer.md)) |
| `NpcDialogueLinks.Tests/` | Host tests over the production core, the sample and the real data |
| [schema.md](schema.md), [ux-design.md](ux-design.md), [content-evidence.md](content-evidence.md) | The data format, the accepted design, and the content's evidence |

## Loading a development build

1. Build the plugin: `cd NpcDialogueLinks && dotnet build -c Debug`. The output, `bin/x64/Debug/`, contains `NpcDialogueLinks.dll`, `terms.json` and `atlas.json`.
2. In game, open `/xlsettings` → **Experimental**. Add the full path to `NpcDialogueLinks.dll` under **Dev Plugin Locations**, then save.
   - On XIV on Mac, the Mac file system appears as the `Z:` drive, for example `Z:\Users\<you>\…\NpcDialogueLinks\bin\x64\Debug\NpcDialogueLinks.dll`.
3. Open `/xlplugins` → **Dev Tools** → **Installed Dev Plugins**, then enable **NPC Dialogue Links**. Rebuild and use **Reload** after changes.

## In-game acceptance checklist (NDL-004)

Record each result as pass or fail. A check that wasn't run stays pending; it never counts as passed.

| # | Check | Expected |
|---|---|---|
| 1 | Load the plugin and run `/npclinks atlas`. Close the window with ✕ and with the command. | The window opens and closes. It starts at 2.0, focused on the Scions, with the browse list grouped 8 / 1 / 1. |
| 2 | Disable and re-enable the plugin, or use **Reload**, then reopen the Atlas. | No errors in `/xllog`. The window works and your spoiler controls are kept. |
| 3 | At 2.0, search "Braves", then search "Wak" and press Enter. | "Braves" finds nothing. Enter focuses The Waking Sands. |
| 4 | Refocus by clicking a node, then by clicking a name in Connections. | The graph re-centers on the clicked entry. |
| 5 | Focus the Scions and read Minfilia's edge. Focus Alphinaud. | The arrow points into the Scions ("leads"), and the list shows "led by Minfilia" with a left arrow. Alphinaud's "twin of" edge has no arrowhead. |
| 6 | **Raise…** → 2.55. Answer **Cancel** once, then **Show**. | The prompt names only the checkpoint. After **Show**, the limit is 2.55 and the view is still 2.0. |
| 7 | Set **Viewing as of** to 2.55, then back to 2.0. | At 2.55, the Crystal Braves and the Rising Stones appear and the Waking Sands headquarters edge is gone. At 2.0 they are hidden again. |
| 8 | Set the view to 2.55, then lower the limit to 2.0. | The view clamps to 2.0 with no prompt. |
| 9 | Switch **Content** to **Main story only**, then back. | Alisaie's dashed "member of" edge disappears, and Louisoix's text changes. The reset notice shows if you had picked something. |
| 10 | Open **Sources (n)** and click a link. | The section starts collapsed and shows the spoiler warning. The link opens the quest's wiki page in your browser. |
| 11 | Resize to the minimum and to something large. Repeat at 150% global font scale (`/xlsettings` → **Look & Feel**). | No overlapping or clipped controls at the minimum size, and the labels are readable at both scales. |
| 12 | Turn off **Enable live Lore Explain** and leave the API key empty. | The Atlas works the same; it makes no network calls of its own. |
| 13 | Rename `atlas.json` in the output folder and reopen the Atlas. Then restore it, add a stray character to the file, and reopen. | Both times the Atlas shows only "The Lore Atlas could not load its data. Other features are unaffected.", and `/xllog` has the details. Restoring the file and reopening fixes it. |
| 14 | With the Atlas broken (13), talk to an NPC, click a chat link, and open `/npclinks dict` and `/npclinks lore`. | Dialogue links, the dictionary and Lore Explain all still work. |
| 15 | Disable the plugin. In `pluginConfigs/NpcDialogueLinks.json` (XIV on Mac: `~/Library/Application Support/XIV on Mac/pluginConfigs/`), set `AtlasViewId` to `nope`. Re-enable the plugin and open the Atlas. | The Atlas falls back to 2.0 with no error, and the config is repaired. |

## In-game test (NDL-010)

> **Status:** the user accepted `NDL-010` on 2026-11-15 without running this table, so every row is still untested in game.

Build the main checkout (see [Loading a development build](#loading-a-development-build)), then **Reload** the plugin.

| # | Do | Expect |
|---|---|---|
| 1 | `/npclinks atlas` | A second row under the top bar: **Lens** [Arc · Story point · Changes] and "Viewing: after …". |
| 2 | **Viewing as of** → "After Every Little Thing She Does Is Magitek". If later points are locked: **Raise…** → "A Realm Reborn — Patch 2.0 complete" → **Show**. | Story point is highlighted, and a grey note says the point covers only the characters involved. |
| 3 | View → "After Escape from Castrum Centri". | The lens switches to **Arc** by itself. Left: the **Story arc** picker ("The arc at this point") and CAST (9). Centre: a violet hexagon with 9 members around it, faint violet lines to each, and 4 labelled edges. Right: The Black Wolf's Challenge, "STORY SO FAR, THROUGH ESCAPE FROM CASTRUM CENTRI", the recap, New: "Thancred possessed by Lahabrea", Ended: "Minfilia prisoner of Livia (ended in Escape from Castrum Centri)", with no sources on either row. |
| 4 | Click the "possessed by" label on the chart, then **Close**. Try clicking a faint line. | A Selected connection card with Sources (n) appears above the recap, and Close removes it. The faint lines do nothing. |
| 5 | Click "Thancred" in the New row, then **< Whole cast**. Then click the centre hexagon, and **< Whole cast** again. | Thancred's one-hop graph shows, with only cast members in Connections. The button brings the chart back. The hexagon opens the arc's own connections. |
| 6 | View → "After Rock the Castrum". | Still Arc, now CAST (10). Ended adds "Livia serves Gaius (ended in Rock the Castrum)". |
| 7 | **Lens → Changes**, then click "- Livia serves Gaius". | The list fills the left and centre: "What this quest changed", ENDED, and DESCRIPTION UPDATED (Cid, Livia, The Black Wolf's Challenge, Operation Archon). The right pane shows the row, Sources (n) and **Sources for the ending (1)**. |
| 8 | View → "A Realm Reborn — Patch 2.0 complete". | Still Changes: "Changes compare one quest step with the one before it … There is no comparison for this point." |
| 9 | **Lens → Story point**. Search and refocus as usual. | The v1 browser, unchanged. |
| 10 | Resize to the minimum size and repeat 3 and 7 at 150% font scale. | Nothing overlaps or clips; long rows wrap. |
| 11 | `/npclinks lore`. Close the Atlas, then click **Open Atlas** (right end of the Status line). Click it again with the Atlas behind another window. | The Atlas opens at the view you left. The second click brings it to the front. Lore Explain is unchanged. |


## In-game look (NDL-011)

> **Status:** the user accepted `NDL-011` on 2026-11-16; this table was not reported, so it is still untested in game.

Build the main checkout, **Reload** the plugin, and open `/npclinks atlas`.

| # | Do | Expect |
|---|---|---|
| 1 | View → "After Escape from Castrum Centri" (Arc lens). | Every node on the chart is a round portrait in a coloured ring with a small shape badge, and the centre is the arc's picture. The browse list shows small round portraits. |
| 2 | Click Thancred. | A large portrait beside his name in the details pane. |
| 3 | **Story point**, view → "A Realm Reborn — Patch 2.55 complete", search "Waking". | The Waking Sands is still a green diamond: it has no portrait. |
| 4 | Resize to the minimum and to something large. | Portraits stay round and sharp, and names stay readable below them. |

## In-game check (NDL-012)

> **Status:** the user accepted `NDL-012` on 2026-11-17 without reporting this table, so every row is still untested in game.

Build the main checkout, **Reload** the plugin, and open `/npclinks atlas`. If later points are locked, use **Raise…** → "A Realm Reborn — Patch 2.0 complete" → **Show**.

| # | Do | Expect |
|---|---|---|
| 1 | Open **Viewing as of**. | The list starts at "After It Was a Very Good Year" and runs one quest at a time to "After Rock the Castrum", then the two milestones. |
| 2 | View → "After Lord of Crags". | Arc lens: *The Road to Titan*, CAST (6), and a "New" row "Lahabrea allied with The Garlean Empire". No "Nero" anywhere. |
| 3 | View → "After Bury Me Not on the Lone Prairie". Search "Cid". | *The Fall of the Waking Sands*. Marques is in the cast, shown as a shape (no portrait), and the search finds nothing. |
| 4 | View → "After Eyes on Me". Open the **Story arc** picker. | The default is still *The Fall of the Waking Sands*, with "Marques revealed as Cid" under New. The picker also offers *The Search for the Enterprise*. |
| 5 | View → "After The Heretic among Us", then **Lens → Changes**. | Ended: "The false Guillaime opposes Alphinaud", with **Sources for the ending (1)**. |
| 6 | View → "After Lady of the Vortex". | *Garuda's Barrier*, CAST (8). Garuda's aliases now include "the Lady of the Vortex". |
| 7 | View → "After Acting the Part", then **Lens → Changes**. | The label reads "Changes since …", not "What this quest changed". |
| 8 | View → "After Escape from Castrum Centri". | Still *The Black Wolf's Challenge*, exactly as before. |
| 9 | Scroll the **Viewing as of** list at the minimum window size and at 150% font scale. | It scrolls, and nothing overlaps or clips. |

## In-game check (through Heavensward)

> **Status:** not run in game.

Build the main checkout, **Reload** the plugin, and open `/npclinks atlas`. If later points are locked, use **Raise…** → "Heavensward — Patch 3.56 complete" → **Show**.

| # | Do | Expect |
|---|---|---|
| 1 | Open **Viewing as of**. | A tall list that opens scrolled to the current point, and runs through "After Fly Free, My Pretty" and the four milestones. |
| 2 | Open **Raise…**. | At most 16 rows, scrolled to the current limit. |
| 3 | View → "After Build on the Stone". | Arc lens: *Myths Made Manifest*. The Rising Stones is visible, and the Scions are headquartered there. |
| 4 | View → "A Realm Reborn — Patch 2.55 complete". | Arc lens: *The Royal Banquet*. The accepted 2.55 text for Minfilia and the Scions is unchanged. |
| 5 | View → "After Coming to Ishgard". | *Wards of House Fortemps*. Alphinaud and Tataru are wards of House Fortemps. |
| 6 | View → "After Where the Chocobos Roam", search "Ysayle". | Ysayle (also searchable as Iceheart), with a "revealed as" edge from Iceheart. |
| 7 | View → "Heavensward — Patch 3.0 complete". | *The Floating Isle*. Estinien is possessed. |
| 8 | View → "After An Uncertain Future", then **Lens → Changes**. | "There is no comparison for this point" (the step after a milestone). |
| 9 | View → "Heavensward — Patch 3.56 complete", search "Lyse". | Lyse, also searchable as Yda. |
| 10 | View → "After Rock the Castrum", search "Raubahn". | Raubahn is there (from #159), with no 2.1+ details. |
| 11 | View → "After Coming to Ishgard" (Arc lens). | Nearly every node is a round portrait: the arc's picture is Ishgard, and Artoirel, Emmanellain and Edmont show their cards. |
| 12 | View → "After All Good Things", search "Marques". | Marques is still a shape with no portrait, so Cid's face never shows before #110. |

## In-game check (through Stormblood)

> **Status:** not run in game.

| # | Do | Expect |
|---|---|---|
| 1 | **Raise…** → "Stormblood — Patch 4.56 complete" → **Show**. Open **Viewing as of**. | The list runs on past 3.56 to "After A Brief Reprieve" and the 4.0 and 4.56 milestones. |
| 2 | View → "After Beyond the Great Wall". | Arc lens: *Envoys to the Resistance*, with Conrad's portrait in the cast. |
| 3 | View → "After A Familiar Face Forgotten". | Arc lens: *Return to Ala Gannha* (the second Gyr Abania chain). |
| 4 | View → "After Once More, to the Ruby Sea", search "Hien". | Hien, with his card portrait. |
| 5 | View → "Stormblood — Patch 4.0 complete". | *The March on Ala Mhigo*. Zenos's entry says he took his own life. |
| 6 | View → "After Gosetsu and Tsuyu", search "Tsuyu". | Yotsuyu, also searchable as Tsuyu. |
| 7 | View → "Stormblood — Patch 4.56 complete". | *War on the Border*. No "Exarch" anywhere; the hooded figure is "the enigmatic figure", with no portrait. |

## In-game check (through Shadowbringers)

> **Status:** not run in game.

| # | Do | Expect |
|---|---|---|
| 1 | **Raise…** → "Shadowbringers — Patch 5.55 complete" → **Show**. View → "After The Syrcus Trench". | *Answering the Summons*. The Crystal Exarch has no portrait; searching "enigmatic" finds him. |
| 2 | View → "After In Search of Alisaie". | *The Inn at Journey's Head* (the Amh Araeng chain). |
| 3 | View → "After The Oracle of Light", search "Minfilia". | The girl's own entry ("Minfilia of the First"), separate from the Scions' Minfilia. |
| 4 | View → "After A Party Soon Divided", search "Solus". | Emet-Selch, with a "revealed as" edge from Solus. |
| 5 | View → "After The Unbroken Thread", search "Exarch". | G'raha Tia, with a portrait, revealed from the Crystal Exarch. |
| 6 | View → "Shadowbringers — Patch 5.0 complete", search "Emet". | Hades, also searchable as Emet-Selch and Solus. |
| 7 | View → "Shadowbringers — Patch 5.55 complete". | *One Banner for Eorzea*. No "Endwalker" anywhere. |

## In-game check (through Dawntrail)

> **Status:** not run in game.

| # | Do | Expect |
|---|---|---|
| 1 | **Raise…** → "Dawntrail — Patch 7.56 complete" → **Show**. View → "After A New World to Explore". | *Landfall in Tuliyollal*. |
| 2 | Open **Viewing as of**. | After "The Rite of Succession", the Kozama'uka chain, then the Urqopacha chain (#859b on), then "After The Success of Others". |
| 3 | View → "After Braced for Trouble", search "Vulture". | The Vulture, with no portrait. One step later ("After Blowing Smoke"), he is revealed as Wihuwte. |
| 4 | View → "After History's Keepers", search "Valigarmanda". | Valigarmanda, with its card portrait, in *The Vidraal Unbound*. |
| 5 | View → "After A Glimmer of the Past", search "Sphene". | Two entries: Endless Sphene and Sphene, the living queen. |
| 6 | View → "After Crossroads" (#960). | *Children Left Behind*. The 5.0 arc is now listed as *The Oracle's Fork in the Road*. |
| 7 | View → "Dawntrail — Patch 7.56 complete". | *The Ice-Locked Sky*. |

## In-game check (through Endwalker)

> **Status:** not run in game.

| # | Do | Expect |
|---|---|---|
| 1 | **Raise…** → "Endwalker — Patch 6.55 complete" → **Show**. View → "After The Next Ship to Sail". | *A Nation of Secrets*. No "Endwalker" anywhere. |
| 2 | View → "After The Satrap of Radz-at-Han", search "Varshahn". | Vrtra, with his card portrait, revealed from Varshahn. |
| 3 | View → "After The Martyr", **Lens → Changes**. | Fandaniel's lead of the Telophoroi and Hydaelyn's opposition to Zodiark are listed as ended. |
| 4 | View → "After Hope Upon a Flower", search "Fandaniel". | Hermes, with his card portrait, revealed from Fandaniel. |
| 5 | View → "After Her Children, One and All", search "Venat". | Hydaelyn, also searchable as Venat. |
| 6 | View → "Endwalker — Patch 6.0 complete". | *The Last Song*. Meteion is also searchable as "The Endsinger" and keeps her winged-girl portrait. |
| 7 | View → "After Where Everything Begins", search "knight". | Golbez, revealed from the knight in black. Zero has no portrait. |
| 8 | View → "Endwalker — Patch 6.55 complete". | *A Letter from Tural*, with Wuk Lamat's card portrait. |

## In-game check: Follow (NDL-017)

> **Status:** not run in game.

Build and **Reload** as in [Loading a development build](#loading-a-development-build). The two characters should be at different points in the story; a third on a different starting city helps. Rows 2–5 and 7–8 also settle `NDL-007`'s pending criteria.

| # | Do | Expect |
|---|---|---|
| 1 | `/npclinks atlas`. Note **Viewing as of** and **Spoiler limit**. | A **Follow my progress** button on the Lens row, off. "Viewing: after …" as before. |
| 2 | Raise the limit to a milestone past your progress, then click **Follow my progress**. | A brief "Reading your progress…", then the view jumps to your last completed main-scenario quest and the line reads "Your progress: through ‹that quest›". The lens follows the default rule (Arc inside an arc). |
| 3 | Lower the limit below your progress. | The view stops at the limit. The line reads "Your progress is past your spoiler limit. Viewing: after ‹limit quest›", and no later quest is named anywhere. |
| 4 | Close and reopen the window. Click **Raise to my progress…**, read the prompt, then **Cancel**. Click **Refresh**. | The button shows once. The prompt names no quest. After Cancel and Refresh it doesn't come back. |
| 5 | Pick a different point in **Viewing as of**. | Follow turns off and the line goes back to "Viewing: after …". Turn it on again: the view returns to your progress. |
| 6 | With Follow on, complete a main-scenario quest (or hand one in). | Shortly after the completion, the view moves one step on, with no click. If it doesn't, **Refresh** does it (record which). |
| 7 | With Follow on and the window open, log out to the title screen. | "Progress unavailable. Log in to a character to read your progress." The view doesn't move. |
| 8 | Log in to the other character. | Once the character has loaded, the view moves to *their* progress. No raise or result from the first character carries over. |
| 9 | Teleport or enter a duty with Follow on. | During the loading screen, at most "Waiting for the game to finish loading."; afterwards it settles back on your progress. |
| 10 | `/xllog`, filter "Follow". | No "failed the cross-check" warnings. A warning names a row to fix in `atlas.json` (run `tools/atlas/QuestRowCheck`). |
| 11 | If your client isn't in English, repeat 2. | The same result: the cross-check reads English titles. |

## In-game check (ARR #1–#101)

> **Status:** not run in game.

| # | Do | Expect |
|---|---|---|
| 1 | Open **Viewing as of**. | The list now starts at "After Close to Home (Gridania)", then the Limsa Lominsa and Ul'dah chains, then "After It's Probably Pirates". |
| 2 | View → your own city's "After Close to Home (…)", **Lens → Story point**. | "Search or pick an entry to see its connections": no Scions yet. |
| 3 | View → "After A Wild Rose by Any Other Name". | Arc lens: *The Drybone Vanishings*. The Story point lens opens on the Scions. |
| 4 | View → "After Lord of the Inferno", search "Ifrit". | Ifrit, with his card portrait. |
| 5 | View → "After The Company You Keep (Maelstrom)". | *Choosing a Grand Company*, with the Maelstrom's own recap. |
| 6 | View → "After Battle Scars", then "After It Was a Very Good Year". | *A Feast at Costa del Sol* leads straight into the accepted #102 point. |

