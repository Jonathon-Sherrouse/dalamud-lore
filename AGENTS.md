# Repo Workflow

This repository uses a lead-agent workflow with specialist side agents.

## Core Rule

- Keep one lead agent responsible for milestone planning, integration, and final review.
- Delegate only bounded tasks with clear ownership and a short definition of done.
- Avoid overlapping edits whenever possible.
- Prefer side agents for parallel work, not for the immediate blocking task.

## Project Shape

- `NpcDialogueLinks/` contains the Dalamud plugin source.
- `README.md` at the repo root explains the current product state.
- `docs/` contains workflow, task, and planning artifacts for agent collaboration.
- `docs/enhancement-roadmap.md` contains the running feature and polish plan. Check it before proposing or implementing enhancement work.
- `docs/github-workflow.md` defines the acceptance-gated branch, pull-request, merge, and cleanup policy.
- `.agents/skills/deliver-github-story/` contains the project-local skill for executing that policy.

## GitHub Delivery

- Use `$deliver-github-story` for approved implementation, resumed story work, review handoff, explicit acceptance, and closeout.
- Start substantive work from the latest `origin/main` on `codex/<story-id>-<slug>` and use an isolated worktree when the active checkout is dirty.
- Keep substantive pull requests draft and unmerged until explicit user acceptance. Agent validation publishes **In Review** through a metadata-only status pull request.
- The user does not need to direct routine Git or GitHub mechanics after approving the story; follow [docs/github-workflow.md](docs/github-workflow.md).
- Treat `docs/enhancement-roadmap.md`, legacy backlog candidates, screenshots, and design discussion as non-executable until the user approves a story or unmistakably requests immediate implementation.

## Agent Roles

- `lead`: architecture, prioritization, integration, release readiness
- `runtime`: Dalamud hooks, addon lifecycle, pointer safety, reload behavior
- `dictionary`: term matching, dictionary schema, lookup logic
- `ui`: clickable presentation, chat output, debug surfaces, future overlay work
- `content`: lore entries, web-researched definitions, data quality, seed content

## Delegation Rules

- Every delegated task should name the files or module it owns.
- If a task touches `Plugin.cs`, the lead agent should usually keep integration ownership.
- If the root cause is unknown, let the lead or runtime agent investigate first.
- If a task can be described in one to three sentences, it is a good candidate for delegation.

## Sub-Agent Spawn Rules

- When spawning a sub-agent with full inherited context, use `fork_context: true`.
- When `fork_context: true` is used, do not explicitly set `agent_type`, `model`, or `reasoning_effort`.
- Use full-context forks for short parallel helper tasks that benefit from shared project state.
- Use narrower manual-context spawns when a task needs a specialized role or intentionally limited context.
- If a spawn attempt fails because of inherited-context constraints, retry with the inherited-context form before changing the task itself.

## Validation

- Prefer validating only the files and behavior touched by the current task.
- For runtime-sensitive changes, include explicit reload and in-game test notes in the handoff.
- Do not silently change dictionary content format without updating workflow docs in `docs/`.
- Content definitions should be researched on the web by default rather than drafted from memory alone.
- Report automated checks, plugin build, in-game verification, and explicit user acceptance as separate evidence lanes.

## Planning References

- For feature polish, dictionary UX, Lore Explain improvements, dialogue matching ideas, and future schema work, start with `docs/enhancement-roadmap.md`.
- For quest metadata work, read `docs/quest-metadata-investigation.md` before changing runtime capture or Lore Explain context.
- When completing an enhancement from the roadmap, update its status or move it to the Completed section.
- If the user asks "what next?" or asks for enhancement options, summarize from the roadmap before adding new ideas.
