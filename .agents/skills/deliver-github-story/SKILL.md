---
name: deliver-github-story
description: Deliver one approved Dalamud Lore story through an isolated branch, draft pull request, agent validation, explicit user acceptance, merge, and cleanup. Use when implementing, resuming, reviewing, accepting, or closing repository work that belongs in the project's GitHub story lifecycle; do not use for read-only investigation, brainstorming, or unapproved roadmap candidates.
---

# Deliver a GitHub story

1. Read the root `AGENTS.md`, `docs/github-workflow.md`, the exact approved story in `docs/backlog.md`, and any scoped `AGENTS.md` or planning reference named by the task.
2. Confirm the story's stable `NDL-###` ID, outcome, acceptance criteria, evidence needs, and dependencies. Treat `docs/enhancement-roadmap.md`, the legacy candidate inventory, and ordinary discussion as non-executable. When the user unmistakably requests immediate implementation, formalize the story and continue without forcing a second approval round.
3. Inspect Git status, remotes, current pull requests, and GitHub authentication. Fetch `origin` before choosing a base. If the active checkout is dirty, preserve it and use a dedicated sibling worktree from the latest `origin/main`.
4. Work on `codex/<story-id>-<slug>`. Keep one substantive story per branch and pull request. Give side agents bounded, non-overlapping ownership; the lead retains integration ownership, especially for `Plugin.cs` or cross-cutting changes.
5. Implement only the approved story. Stage explicit paths, commit, push, and open a draft substantive pull request. Validate in proportion to risk and report automated checks, plugin build, in-game verification, and user acceptance as distinct evidence.
6. After agent validation passes, publish the story's **In Review** move on authoritative `main` using the status-only pull-request procedure in `docs/github-workflow.md`, then merge the refreshed `origin/main` into the substantive branch and rerun affected checks.
7. Keep the substantive pull request open until the user explicitly accepts the story. A build, clean merge, general praise, or in-game evidence does not by itself authorize acceptance.
8. Explicit acceptance authorizes the routine closeout: refresh from `origin/main`, revalidate affected behavior, move the story to **User Accepted**, remove temporary PR metadata, mark the substantive pull request ready, merge it when checks pass, delete its branches, synchronize `main`, and safely remove the worktree.

If GitHub authentication, network access, required checks, or a genuine decision gate blocks a remote step, finish all safe local work and report the exact remaining action. Never claim a branch, pull request, merge, cleanup, or verification that was not observed.
