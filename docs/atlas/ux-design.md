# Atlas UX design (NDL-005)

> **Status: accepted.** The user accepted this design on 2026-11-14. `NDL-004` builds it in game, and the [local viewer](local-viewer.md) is its reference implementation. Sections marked **Prototyped** are built in the viewer and accepted as part of the whole design. Later changes go through `NDL-004` or a new story, and update both front ends together.

## Constraints the design keeps

These come from the accepted contract and the frozen schema. The design may not weaken them; a needed change gets flagged, not made.

- **Two spoiler controls stay separate.**
  - Raising the spoiler limit always needs a neutral confirmation and never moves the view.
  - Lowering the limit clamps the view.
- **Only visible records ever reach the screen.** That covers search, counts, lists, labels and tooltips. Nothing hints at hidden entries.
- **The graph shows one hop:** the focus plus at most 8 neighbors on the canvas, with every neighbor always in the list. There is no force-directed layout and no navigation history.
- **Every string and every behavior lives in the shared core** (`AtlasText`, `AtlasSession`, `AtlasGraphLayout`), so the ImGui window and the viewer render the same thing.

## Layout (Prototyped)

The live prototype is the local viewer. The original static mockup is in [ux-mockup.html](ux-mockup.html).

The window has one top bar, three panes, and a one-line footer.

- **Default size** is about 960 × 600. **Minimum size** is 760 × 480 at 100% font scale; every dimension scales with the global font scale.

```text
┌ Lore Atlas ───────────────────────────────────────────────────────────────── ✕ ┐
│ Viewing as of [A Realm Reborn — Patch 2.0 complete ▾]   Spoiler limit: 2.0 [Raise…] │
│ Content  [ Main story + optional | Main story only ]                               │
├────────────────┬──────────────────────────────────────────┬─────────────────────┤
│ [Search names…]│                 ● Alisaie                │ ■ The Scions of the  │
│ CHARACTERS     │      ◆ Waking Sands      ● Alphinaud     │   Seventh Dawn       │
│ ● Alisaie      │                                          │ Organization         │
│ ● Alphinaud    │   ● Y'shtola    ■ SCIONS    ● Minfilia   │ An order that…       │
│ ● Louisoix     │                                          │ ▸ Sources (5)        │
│ …              │      ● Urianger          ● Tataru        │ CONNECTIONS (8)      │
│ ORGANIZATIONS  │                 ● Thancred               │ ← led by  Minfilia   │
│ ■ The Scions…  │                                          │ ← has member  Alisaie│
│ LOCATIONS      │                                          │ → headquartered at … │
│ ◆ The Waking…  │                                          │                      │
├────────────────┴──────────────────────────────────────────┴─────────────────────┤
│ Includes optional story content available by the selected patch.                 │
└──────────────────────────────────────────────────────────────────────────────────┘
```

| Region | Width | Contents |
|---|---|---|
| **Top bar** | full | "Viewing as of" picker, the spoiler limit with a **Raise…** button, and the content-view toggle |
| **Browse pane** | 200 px | Search box, then visible entries grouped under Characters / Organizations / Locations, each with its glyph |
| **Graph** | flexible, ≥ 300 px | The focus in the center, up to 8 neighbors on a ring, labelled directed edges |
| **Details pane** | 280 px | Name, glyph and category; aliases; summary; collapsed **Sources (n)**; **Connections (n)**, grouped by direction; the selected connection's card |
| **Footer** | full | Help text for the content view. The viewer also shows its draft badge and Reload here. |

The browse pane and the details pane scroll independently. The graph never scrolls; it scales to fit.

## Flows (Prototyped)

| # | Flow | Behavior |
|---|---|---|
| F1 | **First open** | View and limit are at the earliest checkpoint, and the window opens focused on the home entry, the Scions ([D5](#d5-open-on-the-scions-user-decision-2026-11-14)). The browse pane lists every visible entry, grouped by category. |
| F2 | **Search → focus** | Typing filters names and aliases live, as a case-insensitive substring. Clicking an entry, or pressing Enter for the top result, focuses it. |
| F3 | **Refocus** | Click a neighbor on the canvas or a name in the Connections list. The graph re-centers on it and the details update. There is no back button: history is out of scope. |
| F4 | **Inspect a connection** | Click an edge label or a Connections row's label. A card shows "Minfilia **leads** The Scions…" with its own sources. **Close** dismisses it. |
| F5 | **Change "Viewing as of"** | Only checkpoints at or below the limit are selectable. Later ones show greyed with a lock, and their labels stay neutral. Changing the view clears the search and selection and returns the focus to the Scions. If that discarded something you had chosen, a hint shows above the browse list: "Selection reset because the story settings changed." |
| F6 | **Raise the limit** | **Raise…** opens a menu of later checkpoints. Picking one opens a modal: *Allow story knowledge through "…"? The current view will not change.* **Show** raises the limit only, and the view stays put. **Cancel** changes nothing. |
| F7 | **Lower the limit** | Choosing an earlier limit from the same menu needs no confirmation. If the view was above the new limit, it clamps down and resets like F5. |
| F8 | **Content view** | The segmented toggle switches between Main story + optional (the default) and Main story only. Switching resets like F5. In the full view, optional-quest records are marked ([D3](#d3-optional-content-is-marked-user-decision-2026-11-14)). |
| F9 | **More than 8 neighbors** | The canvas keeps the first 8 in category/ID order. The Connections list always shows every neighbor and marks the extras "(list only)". |
| F10 | **Open a source** | Expand Sources (n). The warning, *External pages may contain later spoilers…*, sits at the top of the section. Clicking a title opens it in the browser. Nothing opens without an explicit click. |
| F11 | **Data fails to load** | The window shows only the generic message, *The Lore Atlas could not load its data. Other features are unaffected.*, and the details go to the log. Reopening the window retries. |

## Visual language (Prototyped)

- **Categories use shape plus color, never color alone.** The category name always appears in the details too.

  | Category | Shape | Color |
  |---|---|---|
  | Character | ● circle | blue |
  | Organization | ■ square | gold |
  | Location | ◆ diamond | green |

- **Focus node:** larger, with an accent ring. Neighbors are normal size and brighten on hover.
- **Edges:**
  - Directed edges get an arrowhead at the target.
  - Symmetric edges (twin of) have no arrowhead.
  - Labels sit at the edge midpoint and read from source to target. Parallel edges get separate lanes (`AtlasGraphLayout`).
- **Connections list:**
  - Rows read from the focus's point of view: "← led by Minfilia", "→ headquartered at The Waking Sands", "↔ twin of Alisaie".
  - The arrow glyph repeats the direction, so color is never the only cue.
- **Selection:** the selected edge and its label turn the accent color. The selected row is highlighted in the list.
- **Text:** summaries wrap. Canvas names truncate with an ellipsis, show the full name in a tooltip, and have a dark halo so they stay legible where they cross an edge.
- **Optional content** ([D3](#d3-optional-content-is-marked-user-decision-2026-11-14)): optional edges are dashed, optional connections carry an "optional" tag, and text that includes optional quests carries an "Includes optional quests." tag.

## States (Prototyped)

| State | What shows |
|---|---|
| Nothing focused | Only when the home entry is not visible. Canvas hint: "Search or pick an entry to see its connections." Details show the same hint. |
| No search results | "No matching entries at this point in the story." It never says "hidden". |
| Focus has no connections | "None at this point." in Connections, with a lone node on the canvas. |
| Selection reset by a story-settings change | One-line hint above the browse list until the next browsing action (`AtlasSession.SelectionWasReset`). |
| Load failure | F11. Nothing else renders. |
| Viewer only: draft data | "Draft data — not shippable" badge in the footer. |

## Accessibility (Prototyped)

- Every fixed width, the minimum window size and the graph's node radius multiply by the global font scale. The layout is checked at 100% and 150%.
- Text contrast is at least 4.5:1 against its panel. No meaning is carried by color alone: shapes, arrows and labels carry it.
- Keyboard: Tab moves through the top-bar controls, search and the browse list, and Enter focuses an entry. ImGui's keyboard navigation is limited, so the canvas is mouse-only and the Connections list is the keyboard path.

## ImGui feasibility

| Element | ImGui approach |
|---|---|
| Panes | `BeginChild` for each pane, with widths from the table above × `ImGuiHelpers.GlobalScale` |
| "Viewing as of", Raise… menu | `BeginCombo` with locked items disabled (`BeginDisabled`); `BeginPopup` for the Raise… menu |
| Raise confirmation | `BeginPopupModal` with `AtlasText.ConfirmRaise` and the Show / Cancel buttons |
| Content toggle | Two `Selectable` / `RadioButton` items in a row |
| Search and browse list | `InputTextWithHint`; `Selectable` rows under `SeparatorText` category headers |
| Graph | `ImDrawList` circles, squares (`AddRectFilled`) and diamonds (`AddQuadFilled`); `AddLine` plus a triangle for arrowheads; `InvisibleButton` hit areas for nodes and labels. Dashed optional edges: short `AddLine` segments along the edge, since ImGui has no dash style. Label halo: a dark `AddRectFilled` behind the text. |
| Optional tags | `TextDisabled` (or a small framed `SmallButton`-style label) with the `OptionalTooltip` on hover |
| Tooltips | `IsItemHovered` + `SetTooltip` for truncated names and links |
| Sources | `CollapsingHeader`, with its state driven by `SourcesExpanded` ([D1](#d1-sources-are-collapsed-by-default-user-decision-2026-11-14)) |
| Links | Text buttons that call Dalamud's `Util.OpenLink` on click only |

## Decisions

### D1. Sources are collapsed by default (user decision, 2026-11-14)

The details pane shows the summary and connections first. Sources sit in one small collapsible section below the summary, labelled with their count, such as "Sources (3)".

- **Default.** Every session starts collapsed. Opening the section keeps it open for the rest of the session, across refocusing, connection selection and checkpoint or content-view changes. It is never persisted.
- **One setting.** The same open or closed state applies to the selected entity's sources and the selected connection's sources.
- **Spoiler warning.** The external-page warning (`AtlasText.ExternalLinkWarning`) sits inside the section, so it is always visible before any link can be clicked.
- **Shared core.** The state is `AtlasSession.SourcesExpanded` and `SetSourcesExpanded`, and the label is `AtlasText.SourcesToggle(count)`. Both front ends render them; neither keeps its own copy.
- **ImGui feasibility.** `ImGui.CollapsingHeader` (or a `TreeNode`) labelled with `SourcesToggle`, with its open state driven by `SourcesExpanded` through `ImGui.SetNextItemOpen` on every frame, and toggles written back through `SetSourcesExpanded`. Links are buttons that show the warning tooltip and open only on an explicit click.

### D2. "Spoiler limit" (user decision, 2026-11-14)

The ceiling control is labelled **Spoiler limit** (`AtlasText.CeilingLabel`). "Viewing as of" stays. The confirmation prompt is unchanged.

### D3. Optional content is marked (user decision, 2026-11-14)

In the main + optional view:
- edges known only from optional quests are dashed;
- their Connections rows and the selected-connection card carry an "optional" tag;
- an entity whose shown text is an optional presentation carries "Includes optional quests.";
- every tag explains itself on hover (`AtlasText.OptionalTooltip`).

The main-story view never shows a mark, because it has no optional records.

The marks come from `AtlasRelationshipView.IsOptional` and `AtlasEntityView.IncludesOptional`, set by the projector. This is a display flag only: the schema is unchanged, and it reveals nothing that is not already visible.

### D4. The browse list is grouped by category (user decision, 2026-11-14)

The list is grouped under Characters, Organizations and Locations (`AtlasSession.SearchResultGroups`, with headings from `AtlasText.CategoryGroupLabel`). Search filters within the groups, and empty groups are omitted.

### D5. Open on the Scions (user decision, 2026-11-14)

The window opens focused on the Scions (`AtlasDefaults.HomeEntityId`). It returns there whenever a story-settings change (limit, view or content view) resets the selection, as long as the Scions are visible.

- The reset hint appears only when the reset discarded something the player had chosen.
- The home entry is a pilot constant in the shared core, not data. A later schema version could move it into `atlas.json`.

