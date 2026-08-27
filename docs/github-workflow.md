# Acceptance-gated GitHub workflow

Status: active project policy

The user does not need to direct routine branching, synchronization, commits, pushes, pull requests, merges, or branch cleanup. Agents own those mechanics while preserving the acceptance boundary below.

The repository state already present on `origin/main` when this policy was adopted is the authorized initial baseline. Uncommitted user work is not part of that exception and must remain untouched unless explicitly placed in scope.

## Planning contract

[`backlog.md`](backlog.md) is the executable acceptance queue. Its workflow states are:

- **To Do** — an explicitly approved, groomed story that has not been implemented.
- **In Review** — implementation and agent validation are complete, but the user has not accepted the result.
- **User Accepted** — the user explicitly accepted the story.

Every executable story has a stable ID such as `NDL-001`, a short outcome, acceptance criteria, expected evidence, and declared dependencies. `NDL` means NPC Dialogue Links; the number is identity, not priority. IDs are never reused.

Use this card shape under the appropriate workflow heading:

```markdown
- [ ] `NDL-001` **Short story title**
  - Owner: `runtime` | `dictionary` | `ui` | `content` | `lead`
  - Outcome: One sentence describing the player or maintainer result.
  - Acceptance: Observable conditions the user will review.
  - Evidence: Checks, build, reload, and in-game evidence required for this story.
  - Dependencies: `None` or stable story IDs and pull-request bases.
```

Check the box only in **User Accepted**. While a story is **In Review**, place its indented substantive pull-request link directly below these fields.

[`enhancement-roadmap.md`](enhancement-roadmap.md), the backlog's legacy candidate inventory, and its parking lot are planning sources, not implementation approval. Normally the agent grooms a candidate with the user before promoting it to **To Do**. When the user unmistakably requests immediate implementation, the agent may formalize the story and proceed without a separate approval round. Brainstorming, enthusiasm, screenshots, and read-only requests do not trigger that exception.

## Baseline and branch names

Before story work, fetch `origin` and branch from the latest `origin/main`. Use `codex/<story-id>-<slug>`, for example `codex/ndl-014-speaker-name-capture`.

If the active checkout contains unrelated changes, create a dedicated sibling worktree from `origin/main`. Never hide, overwrite, reset, or opportunistically include the user's dirty work.

## Story lifecycle

1. Formalize or confirm the approved story and move it to **To Do** if it is not already there.
2. Fetch `origin`, create the story branch from the latest `origin/main`, and implement only that story.
3. Run the narrowest relevant checks, broadening in proportion to risk. Stage only explicit story paths, commit, push, and open a draft substantive pull request.
4. After agent validation passes, use the status-only synchronization below to publish **In Review** and the substantive pull-request link on authoritative `main`.
5. Fetch `origin` and merge the updated `origin/main` into the substantive branch. Repeat this refresh before resumed work, final validation, and merge.
6. Resolve conflicts from current approved sources, preserve unrelated cards and changes, and rerun every check affected by either side of the merge.
7. Keep the substantive pull request open until the user explicitly accepts the result. Agent validation, GitHub review state, Simulator or in-game evidence, and a completed turn are not substitutes for acceptance.
8. Explicit user acceptance authorizes the agent to refresh and revalidate the branch, move the story from **In Review** to **User Accepted**, check it off, remove its temporary substantive-PR annotation, make the pull request ready, merge it after required checks pass, delete the merged local and remote branch, synchronize `main`, and safely remove its worktree.

Parallel story branches are allowed. If one depends on another, record the dependency and pull-request base explicitly. Refresh a stack from its owning base in order and revalidate every affected story after upstream changes.

## Status-only synchronization

The backlog on `main` remains the aggregate review queue while substantive pull requests wait for acceptance. Once a substantive pull request is agent-validated:

1. Fetch the latest `origin/main` and create `codex/status-<story-id>-in-review` from that exact commit.
2. Make a metadata-only change in `docs/backlog.md`: move the exact story from **To Do** to **In Review** and add an indented `- Substantive PR: [#<number>](<url>)` line beneath it. Do not include implementation code.
3. Commit and push only the status paths, open a non-draft status pull request, and verify its diff contains workflow metadata only.
4. Status-only pull requests may be merged automatically after their checks pass because they publish agent-validated state rather than unaccepted product behavior.
5. Fetch the resulting `origin/main`, merge it into the still-open substantive branch, and rerun checks affected by the backlog merge.

Serialize status-only updates. Before merging one, fetch `origin/main`; if another status or acceptance update landed, rebase the status branch onto the new tip, preserve every card and pull-request reference, recheck the diff, and push with lease protection. Never merge two status pull requests from the same stale backlog revision. Delete the status branch after merge.

## Safety and evidence

- Never use `git add .`, `git add -A`, or `git add --all`; stage explicit paths only.
- Never force-push a shared or review branch unless the user explicitly authorizes it.
- A clean merge does not replace validation.
- Record automated checks, plugin build, game launch/reload, player-visible behavior, and explicit acceptance separately. Do not report unperformed in-game testing as verified.
- Runtime-sensitive changes include precise reload and smoke-test notes in the handoff.
- Content changes follow the repository's web-research policy and cite the sources used.
- Inspect GitHub authentication before remote mutations. If authentication, network access, or required checks block progress, preserve the local branch and report the exact blocker instead of inventing remote state.
