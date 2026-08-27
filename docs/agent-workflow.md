# Agent Workflow

This document defines how to run `NpcDialogueLinks` as a lead-agent project with specialist side agents.

## Goals

- Keep architecture decisions centralized.
- Reduce context crowding by splitting technical, UI, and content work.
- Make parallel work safe by assigning clear file ownership.

## Roles

### Lead agent

- Owns milestone planning
- Decides architecture and tradeoffs
- Integrates side-agent work
- Reviews cross-cutting changes

### Runtime agent

- Owns Dalamud integration details
- Investigates addon capture issues
- Owns quest metadata probe work until a verified source is found
- Verifies reload and lifecycle safety
- Documents in-game reproduction steps

### Dictionary agent

- Owns term matching behavior
- Evolves dictionary schema when needed
- Maintains lookup and normalization logic
- Keeps matching predictable

### UI agent

- Owns clickable term presentation
- Designs chat output and future overlay behavior
- Keeps user feedback readable and minimal

### Content agent

- Seeds and maintains term definitions
- Researches definitions on the web before adding or revising entries
- Keeps content internally consistent
- Proposes new entries grouped by category

## Standard Workflow

1. Lead agent confirms an approved `NDL-###` story, its success criteria, and its dependencies.
2. Lead agent invokes `$deliver-github-story` and follows [github-workflow.md](github-workflow.md) for branch, pull-request, acceptance, merge, and cleanup mechanics.
3. Lead agent checks [enhancement-roadmap.md](enhancement-roadmap.md) when the work involves feature polish, dictionary UX, Lore Explain, dialogue matching, or schema planning. Roadmap items remain candidates until promoted through the approval rules in the GitHub workflow.
4. Lead agent splits bounded tasks using the task brief template.
5. Side agents work only within their assigned ownership unless escalation is required.
6. Lead agent integrates changes and resolves cross-cutting conflicts.
7. Lead agent runs final verification, opens the draft substantive pull request, and publishes **In Review** through the status-only synchronization process.
8. After explicit user acceptance, the lead agent refreshes, revalidates, merges, synchronizes `main`, and cleans up the story branches and worktree.

## Content Research Policy

- Content tasks should use web research by default when writing or revising definitions.
- If a source policy is known for the task, the lead agent should include it in the task brief.
- If research is not possible, the task handoff should say so explicitly instead of silently falling back to memory.

## Spawn Patterns

### Full-context helper

Use this when the sub-agent should inherit the full conversation and current repo state.

- Set `fork_context: true`
- Do not explicitly set `agent_type`
- Do not explicitly set `model`
- Do not explicitly set `reasoning_effort`
- Prefer this for short, bounded parallel tasks

### Narrow specialist

Use this when the sub-agent should receive only a limited task brief or intentionally constrained context.

- Provide a focused task description and file ownership
- Explicit specialization is acceptable only when not using the inherited full-context pattern
- Prefer this for reusable specialist work where too much shared context would be noise

## Current Milestone Tracks

### Milestone 1: Stable dictionary-backed dialogue links

- Runtime: verify `Talk` capture across several NPC dialogue scenarios
- Dictionary: keep extraction exact and reliable
- Content: seed core location definitions
- Lead: integrate and confirm the end-to-end click flow

### Milestone 2: Better authoring model

- Dictionary: maintain bundled seed terms plus user dictionary overrides
- Dictionary: refine alias support and consider richer term records if needed
- Content: expand the term set for city-states, regions, and guilds
- Lead: decide whether schema changes justify a migration step

### Milestone 3: Better in-game presentation

- UI: iterate on the dictionary window layout, search, and browsing experience
- Runtime: verify reload stability after UI additions
- Lead: choose the long-term surface

### Milestone 4: Lore Explain direct workflow

- Lead: keep direct LLM behavior optional, user-configured, and bounded by clear scene-context rules
- Runtime: validate Talk capture, recent dialogue history, zone metadata, and best-effort speaker metadata across dialogue scenarios
- Runtime: investigate quest metadata only through verified active-dialogue sources; see [quest-metadata-investigation.md](quest-metadata-investigation.md)
- Dictionary: review proposed dictionary entries before they are saved to the user dictionary
- Content: prefer `ffxiv.consolegameswiki.com` for researched citations and flag uncertain or conflicting sources
- UI: keep the Lore Explain window readable with hidden context/source sections, transcript turns, follow-up input, and clickable sources

## Escalation Rules

- Escalate to the lead agent when more than one owned file area must change together.
- Escalate to the lead agent when the task affects user-facing behavior beyond the assigned scope.
- Escalate to the runtime agent when there is uncertainty about addon structure or game-state timing.

## Definition of Done

- The assigned files are updated cleanly.
- The expected player-visible behavior is stated.
- Any required rebuild/reload steps are called out.
- Follow-up risks or unknowns are written down briefly.
- Automated checks, plugin build, in-game verification, and explicit user acceptance are reported separately.
- For substantive story work, "implemented" or "ready for review" is not reported as merged or user accepted.
