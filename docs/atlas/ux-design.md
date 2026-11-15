# Atlas UX design (NDL-005)

> **Status: proposal, awaiting the user's reaction.** This is the design that `NDL-004` will build in game, prototyped in the [local viewer](local-viewer.md). Sections marked **Proposed** are not decided. Sections marked **Decided** record a user decision. Nothing is accepted until the user accepts the whole story ([backlog card](../backlog.md)).

## Constraints the design keeps

These come from the accepted contract and the frozen schema. The design may not weaken them; a needed change gets flagged, not made.

- **Two spoiler controls stay separate.**
  - Raising the spoiler limit always needs a neutral confirmation and never moves the view.
  - Lowering the limit clamps the view.
- **Only visible records ever reach the screen.** That covers search, counts, lists, labels and tooltips. Nothing hints at hidden entries.
- **The graph shows one hop:** the focus plus at most 8 neighbors on the canvas, with every neighbor always in the list. There is no force-directed layout and no navigation history.
- **Every string and every behavior lives in the shared core** (`AtlasText`, `AtlasSession`, `AtlasGraphLayout`), so the ImGui window and the viewer render the same thing.

## Layout (Proposed)

A static mockup in real 2.0 data is in [ux-mockup.html](ux-mockup.html). Open it in a browser.

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

## Flows (Proposed)

| # | Flow | Behavior |
|---|---|---|
| F1 | **First open** | View and limit are at the earliest checkpoint and nothing is focused. The browse pane lists every visible entry, and the canvas shows "Search or pick an entry to see its connections." |
| F2 | **Search → focus** | Typing filters names and aliases live, as a case-insensitive substring. Clicking an entry, or pressing Enter for the top result, focuses it. |
| F3 | **Refocus** | Click a neighbor on the canvas or a name in the Connections list. The graph re-centers on it and the details update. There is no back button: history is out of scope. |
| F4 | **Inspect a connection** | Click an edge label or a Connections row's label. A card shows "Minfilia **leads** The Scions…" with its own sources. **Close** dismisses it. |
| F5 | **Change "Viewing as of"** | Only checkpoints at or below the limit are selectable. Later ones show greyed with a lock, and their labels stay neutral. Changing the view clears the focus, search and selection, and shows a hint: "Selection cleared because the story point changed." |
| F6 | **Raise the limit** | **Raise…** opens a menu of later checkpoints. Picking one opens a modal: *Allow story knowledge through "…"? The current view will not change.* **Show** raises the limit only, and the view stays put. **Cancel** changes nothing. |
| F7 | **Lower the limit** | Choosing an earlier limit from the same menu needs no confirmation. If the view was above the new limit, it clamps down, with the same cleared-selection hint as F5. |
| F8 | **Content view** | The segmented toggle switches between Main story + optional (the default) and Main story only. Switching clears transient state, like F5. |
| F9 | **More than 8 neighbors** | The canvas keeps the first 8 in category/ID order. The Connections list always shows every neighbor and marks the extras "(list only)". |
| F10 | **Open a source** | Expand Sources (n). The warning, *External pages may contain later spoilers…*, sits at the top of the section. Clicking a title opens it in the browser. Nothing opens without an explicit click. |
| F11 | **Data fails to load** | The window shows only the generic message, *The Lore Atlas could not load its data. Other features are unaffected.*, and the details go to the log. Reopening the window retries. |

## Visual language (Proposed)

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
- **Text:** summaries wrap. Canvas names truncate with an ellipsis and show the full name in a tooltip.

## States (Proposed)

| State | What shows |
|---|---|
| Nothing focused | Canvas hint (F1). Details show the same hint. |
| No search results | "No matching entries at this point in the story." It never says "hidden". |
| Focus has no connections | "None at this point." in Connections, with a lone node on the canvas. |
| Selection cleared by a story-point or content change | One-line hint above the browse list until the next action. |
| Load failure | F11. Nothing else renders. |
| Viewer only: draft data | "Draft data — not shippable" badge in the footer. |

## Accessibility (Proposed)

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
| Graph | `ImDrawList` circles, squares (`AddRectFilled`) and diamonds (`AddQuadFilled`); `AddLine` plus a triangle for arrowheads; `InvisibleButton` hit areas for nodes and labels |
| Tooltips | `IsItemHovered` + `SetTooltip` for truncated names and links |
| Sources | `CollapsingHeader`, with its state driven by `SourcesExpanded` ([D1](#d1-sources-are-collapsed-by-default-user-decision-2026-11-14)) |
| Links | Text buttons that call Dalamud's `Util.OpenLink` on click only |

## Questions for the user

1. **Control names.** Rename "Knowledge approved through" to **"Spoiler limit"**, and keep "Viewing as of"? It's shorter, and it says what the control does.
2. **Mark optional content?** In the main + optional view, should edges from optional quests be **dashed**, with descriptions tagged "includes optional quests"? It helps you see what the toggle changes. It needs a small core change to expose each record's scope to the UI; that isn't a spoiler, and the schema doesn't change.
3. **Group the browse list by category** (Characters / Organizations / Locations), or keep one flat list?
4. **Starting focus.** Open with nothing focused (current), or focus a starting entry such as the Scions?

## Decisions so far

### D1. Sources are collapsed by default (user decision, 2026-11-14)

The details pane shows the summary and connections first. Sources sit in one small collapsible section below the summary, labelled with their count, such as "Sources (3)".

- **Default.** Every session starts collapsed. Opening the section keeps it open for the rest of the session, across refocusing, connection selection and checkpoint or content-view changes. It is never persisted.
- **One setting.** The same open or closed state applies to the selected entity's sources and the selected connection's sources.
- **Spoiler warning.** The external-page warning (`AtlasText.ExternalLinkWarning`) sits inside the section, so it is always visible before any link can be clicked.
- **Shared core.** The state is `AtlasSession.SourcesExpanded` and `SetSourcesExpanded`, and the label is `AtlasText.SourcesToggle(count)`. Both front ends render them; neither keeps its own copy.
- **ImGui feasibility.** `ImGui.CollapsingHeader` (or a `TreeNode`) labelled with `SourcesToggle`, with its open state driven by `SourcesExpanded` through `ImGui.SetNextItemOpen` on every frame, and toggles written back through `SetSourcesExpanded`. Links are buttons that show the warning tooltip and open only on an explicit click.
