# Atlas UX design (NDL-005)

> **Status: in progress.** This is the design that `NDL-004` will build in game. It is prototyped in the [local viewer](local-viewer.md). The full design covers layout, flows, visual language, empty and error states, accessibility, and an ImGui feasibility note for each element ([backlog card](../backlog.md)). Each section is added as it is designed with the user. Nothing here is accepted until the user accepts the whole story.

## Decisions so far

### D1. Sources are collapsed by default (user decision, 2026-11-14)

The details pane shows the summary and connections first. Sources sit in one small collapsible section below the summary, labelled with their count, such as "Sources (3)".

- **Default.** Every session starts collapsed. Opening the section keeps it open for the rest of the session, across refocusing, connection selection and checkpoint or content-view changes. It is never persisted.
- **One setting.** The same open or closed state applies to the selected entity's sources and the selected connection's sources.
- **Spoiler warning.** The external-page warning (`AtlasText.ExternalLinkWarning`) sits inside the section, so it is always visible before any link can be clicked.
- **Shared core.** The state is `AtlasSession.SourcesExpanded` and `SetSourcesExpanded`, and the label is `AtlasText.SourcesToggle(count)`. Both front ends render them; neither keeps its own copy.
- **ImGui feasibility.** `ImGui.CollapsingHeader` (or a `TreeNode`) labelled with `SourcesToggle`, with its open state driven by `SourcesExpanded` through `ImGui.SetNextItemOpen` on every frame, and toggles written back through `SetSourcesExpanded`. Links are buttons that show the warning tooltip and open only on an explicit click.
