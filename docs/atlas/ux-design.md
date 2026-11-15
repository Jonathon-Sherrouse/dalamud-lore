# Atlas UX design (NDL-005)

> **v2 note.** [Atlas v2](v2-plan.md) adds three lenses, designed in [v2 lenses](#v2-lenses-ndl-008) below (`NDL-008`, accepted 2026-11-14; `NDL-010` builds it in game). Everything above that section is the accepted v1 design, and it stays the **Story point** lens unchanged, except that flows F5 and F6 follow v2 spoiler rule 1: above the spoiler limit, pickers and the raise menu show only neutral milestone labels plus an unnamed "next story step", never quest titles.
>
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

## v2 lenses (NDL-008)

> **Status: accepted.** The user accepted this design, decisions D6–D12 included, on 2026-11-14. It is prototyped in the local viewer over the synthetic arc sample (`--arc-sample`). `NDL-010` renders it in the in-game window. **Follow is deferred** (user decision, 2026-11-14), so there is no Follow toggle, status line or "your progress" wording.

### What changes on screen

A **lens bar** sits under the top bar: the lens switch, then the position line, then the coverage note on slice steps.

```text
┌ Lore Atlas ─────────────────────────────────────────────────────────────────────── ✕ ┐
│ Viewing as of [After The Captain's Bargain ▾]  Spoiler limit: … [Raise…]  Content [ … ] │
│ Lens [ Arc | Story point | Changes ]  Viewing: after The Captain's Bargain               │
│                                       This point covers only the characters involved…   │
├────────────────┬─────────────────────────────────────────┬────────────────────────────┤
│ Story arc      │              ● Mira                     │ ⬡ The Siege of Saltmere     │
│ [The arc at ▾] │      ◆ Harbor    ·    ● Tobin           │ Event                       │
│ [Search…]      │            ⬡ THE SIEGE                  │ STORY SO FAR, THROUGH THE   │
│ CAST (6)       │      ● Vessa     ·    ■ The Watch       │ CAPTAIN'S BARGAIN           │
│ CHARACTERS     │              ■ The Drowned Court        │ Tobin is still a prisoner…  │
│ ● Captain Mira │                                         │ ▸ Sources (1)               │
│ …              │  (faint spokes to the centre, labelled  │ NEW AT THIS POINT           │
│ LOCATIONS      │   edges between cast members)           │ Mira allied with Vessa      │
│ ◆ Saltmere …   │                                         │ ENDED SO FAR IN THIS ARC    │
│                │                                         │ Mira member of … (ended in …)│
└────────────────┴─────────────────────────────────────────┴────────────────────────────┘
```

| Lens | Browse pane | Centre | Details pane |
|---|---|---|---|
| **Arc** | The **Story arc** picker, then search, then the cast members under "Cast (n)", grouped by category. The arc entry is the panel's subject, so it is not listed while the search is empty; searching finds it, and its centre node can always be clicked. | The **whole-cast chart**: the arc entry in the centre, every cast member on a ring, every cast-to-cast relationship drawn | The **arc panel**: name, "Story so far, through ‹quest›", the recap, Sources (n), **New at this point**, **Ended so far in this arc** |
| **Story point** | Unchanged (v1) | Unchanged one-hop graph | Unchanged |
| **Changes** | Replaced by the change list | Replaced by the change list | The selected change |

### Flows

| # | Flow | Behavior |
|---|---|---|
| L1 | **Open** | The default lens rule: **Arc** when an arc contains the view, **Story point** otherwise. Until the player picks a lens or an arc, the rule is re-applied whenever the view changes ([D11](#decisions-accepted-by-the-user-2026-11-14)). An explicit pick lasts for the session and is never saved. Saved state still opens at the earliest checkpoint when absent or invalid, which is the pre-arc baseline, so a first open is always Story point. |
| L2 | **Switch lens** | The lens switch changes what is shown. Like a checkpoint change it clears search, focus and selection, but it never shows the "Selection reset" hint, because the player did it on purpose. |
| L3 | **Arc lens at rest** | Nothing is focused: the whole-cast chart and the arc panel show. The recap is the arc entry's reviewed summary at the effective step. Clicking a labelled edge on the chart opens its **Selected connection** card, with its sources and Close, at the top of the arc panel; the recap stays below it. |
| L4 | **Refocus in the arc** | Clicking a cast member (canvas, cast list, or a name in the panel's rows) shows the v1 one-hop graph and details, **inside the cast**. Search, counts and connections never leave the cast. A **← Whole cast** button returns to rest. |
| L5 | **Pick an arc** | The **Story arc** picker lists "The arc at this point" (the automatic choice), then every arc already started by the view, by start and then authored order, each named as of its effective step. No spans, step counts or end markers. |
| L6 | **Pick lifetime** | Picking an arc also chooses the Arc lens ([D12](#decisions-accepted-by-the-user-2026-11-14)). A pick holds while the view moves, and ends when the view drops below the arc's first step (also when lowering the limit clamps the view there); it does not come back when the view rises again. "The arc at this point" clears it; the Arc lens stays chosen either way. A picked arc that has already ended shows "As of ‹last quest›" beside the recap, and its "New" heading becomes "New in ‹last quest›". |
| L7 | **No arc here** | In the Arc lens with no arc covering the view: "No story arc covers this point." The picker still lists started arcs, so an ended one can be reopened. |
| L8 | **Changes lens** | A heading, "What this quest changed" or "Changes since ‹previous point›", then rows under **Added** (+), **Ended** (−) and **Description updated** (~). Picking a row shows it on the right: the relationship and its sources, plus **Sources for the ending (n)** on an ended row, the only place end evidence ever appears. |
| L9 | **Changes not offered** | At the first step or across a slice ↔ milestone boundary: "Changes compare one quest step with the one before it, or one milestone with the previous milestone. There is no comparison for this point." |
| L10 | **Position and coverage** | The lens bar always says "Viewing: after ‹quest›", the chosen point, never "you are here". On slice steps the shared coverage note follows it. |

### Visual language additions

- **Events and arc entries:** a flat-topped **hexagon** in violet (`#c39bd3`), the fourth category glyph, ordered last in lists ("Events").
- **Participation spokes:** in the whole-cast chart, each member's `participant-in` edge to the entry is a faint violet line with no label, arrow or click target (`AtlasGraphEdge.IsParticipation`; the session refuses to select one there). Membership is already shown by the member being on the chart, and ten labelled spokes would bury the real relationships. For the same reason, **New at this point** leaves out participation edges. In a refocused one-hop graph the same edge is drawn and selectable like any other.
- **Recap label:** small caps in the accent colour, above the recap text, which is slightly larger than a summary.
- **Change marks:** `+`, `−` and `~` repeat the group heading, so meaning never rests on colour.
- **Ended rows in the Arc lens** carry "(ended in ‹quest›)" and **no sources** of any kind.

### States

| State | What shows |
|---|---|
| Arc lens, no arc | Centre and details: "No story arc covers this point." The browse list is empty apart from the picker. |
| Arc lens, nothing new or ended | "Nothing new." / "Nothing has ended yet." |
| Changes, nothing changed | "Nothing changed at this point." |
| Changes, no row picked | "Pick a change to see its details." |

### Shared core

Every rule and string lives in the shared core, as in v1: `AtlasSession` (`Lens`, `SetLens`, `LensOptions`, `PositionLabel`, `CoverageNote`; `Arc`, `ArcPickerOptions`, `PickArc`, `CastHeading`, `ArcNewHeading`, `ShowsWholeCast`, `ShowWholeCast`, `ArcNewRows`, `ArcEndedRows`; `ChangesOffered`, `ChangesLabel`, `ChangeGroups`, `SelectChange`, `SelectedChange`) and `AtlasText`. In the Arc lens the session's `Snapshot` is the arc's cast-filtered snapshot at its effective step, so every v1 browsing method is cast-filtered for free.

**Per-frame cost.** The derived lens state (change groups, picker options, arc rows, the whole-cast layout) is built once and cached until the next change of limit, view, content view, lens or pick, so an ImGui window can read it every frame.

**Leak sweep.** `V2LeakSweepTests` covers every limit, view, content view, lens and arc pick. It runs in three ways: in fresh sessions, along a walk down and back up the timeline, and along a walk that turns at the picked arc's first step, so the pick is held both ways. At each stop it selects every chart edge and every change, and refocuses every entry. It checks four things:
- Every entity, relationship and source shown exists, exactly as shown, at some step at or before the view. Each end citation on a Changes row must be that relationship's own end evidence.
- No text names a later quest, entity or source.
- Pickers and prompts name nothing past the limit.
- End evidence appears only on Changes "ended" rows, proved by a source cited nowhere else.

### ImGui feasibility (for `NDL-010`)

| Element | ImGui approach |
|---|---|
| Lens switch | Three `Selectable`s in a row (or `RadioButton`s), the same pattern as the content toggle |
| Position and coverage | `TextUnformatted` and `TextDisabled` on the lens bar line; the coverage note wraps with `TextWrapped` on narrow windows |
| Story arc picker | `BeginCombo` over `ArcPickerOptions`; the automatic option first |
| Whole-cast chart | The existing `ImDrawList` renderer over `AtlasGraphLayout.ComputeWholeCast`: up to 11 nodes on one ring, so no new layout code. Spokes are a single `AddLine` with a low-alpha `EventColor` and no `InvisibleButton`. The hexagon is `AddNgonFilled` / `AddNgon` with 6 sides, already drawn by the window. |
| Arc panel | `BeginChild` details pane: a `PushStyleColor` accent `TextUnformatted` for the recap label, `TextWrapped` for the recap, the existing Sources `CollapsingHeader`, then the window's existing heading pattern (`TextColored(MutedColor, LABEL)` + `Separator`) and its `ClickableText` helper for inline names in rows. The selected-connection card is the window's existing card, drawn above the recap. |
| ← Whole cast | `SmallButton` at the top of the details pane |
| Changes list | One `BeginChild` spanning the browse and canvas width (the window already sizes panes from a table), group headings in the same heading pattern, full-width `Selectable` rows; the mark glyph as a fixed-width `TextDisabled` |
| End evidence | A second `CollapsingHeader` labelled `EndSourcesToggle(n)`, driven by the same `SourcesExpanded` setting |
| Known layout limit | With an even ring (for example ten members), an edge between two opposite members runs through the centre hexagon and its label. The viewer accepts it. The in-game window (`NDL-010`) moves such a label off the centre node. |

### Decisions (accepted by the user, 2026-11-14)

1. **D6. The lens bar** is a second row under the top bar, not a tab strip above the panes.
2. **D7. The Changes lens takes the browse pane and the canvas** for its list, with no chart. A diff is a list; a chart of a diff would need its own layout rules.
3. **D8. Participation spokes are faint and unlabelled** on the whole-cast chart, and can't be clicked there. "New at this point" leaves out these spokes too, so a member joining shows by appearing on the chart, not as a row. After refocusing, the same edge is an ordinary labelled connection.
4. **D9. The automatic arc option reads "The arc at this point".** It avoids "current" and "you are here", which would imply progress.
5. **D10. Switching lens clears focus and search silently**, without the reset hint.
6. **D11. The default lens rule re-applies on every view change** until the player picks a lens or an arc. The plan names only "on open" and "when Follow moves the view". With Follow deferred, this is how a player moving through the story lands in the Arc lens on their own.
7. **D12. Picking an arc counts as picking the Arc lens,** so a picked arc stays on screen when the view moves past its end. The cost: the Arc lens then stays chosen for the session, even after the pick ends or is cleared with "The arc at this point". Moving before every arc shows "No story arc covers this point." rather than returning to Story point.

