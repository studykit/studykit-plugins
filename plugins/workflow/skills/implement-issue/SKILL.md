---
name: implement-issue
description: "Implement a workflow `task`, `bug`, or `spike` issue: read the issue body, enter plan mode to converge on the implementation plan, apply the change, verify Acceptance Criteria, commit with the issue ref prefix, and close the issue with a refreshed Resume."
argument-hint: "<issue-ref> [additional requirements]"
disable-model-invocation: true
allowed-tools:
  - 'Bash("$WORKFLOW":*)'
  - 'Bash(git status:*)'
  - 'Bash(git diff:*)'
  - 'Bash(git add:*)'
  - 'Bash(git commit:*)'
  - EnterPlanMode
  - ExitPlanMode
  - Read
  - Edit
  - Write
  - Grep
  - Glob
---

# Plan-Mode Implement

The issue body is the spec. Read it, enter plan mode to converge on the
implementation plan, apply the change after approval, verify, commit, close.
Provider command shapes (fetch, writeback, close, freshness handling) come
from the session's workflow policy context — this skill does not restate
them.

## Scope

In scope: `task`, `bug`, `spike`. The type lives in the cached `issue.md`
frontmatter. For any other type (`epic`, `review`, `research`, `usecase`,
knowledge types), stop and redirect — these coordinate other work or live
on a different surface, and forcing plan-mode implementation onto them
distorts the type's role.

## Flow

1. **Read the issue.** Fetch the ref from the first `$ARGUMENTS` token (ask
   when missing or ambiguous), then read the cached `issue.md`. Follow the
   links the body cites: parent, blocked-by, knowledge pages, and paths
   named in `Affected Paths`. The body is the contract; its links complete
   it. Never edit the cached `issue.md` or `comment-*.md` projections in
   place.

2. **Enter plan mode and converge on the plan.** Call `EnterPlanMode`
   before drafting so the harness blocks edits during planning. Map the
   issue's `Description`, `Approach`, `Affected Paths`, `Unit Test
   Strategy`, and `Acceptance Criteria` (plus `Reproduction` for `bug`,
   `Hypothesis` / `Validation Method` for `spike`) onto a concrete plan:
   files to touch by absolute path, the verification step for each
   Acceptance Criterion, and the intended commit split. Present the
   converged plan via `ExitPlanMode`; no edits before the user accepts the
   plan and exits plan mode. If the plan keeps diverging from the body,
   the body itself is usually the problem — propose updating the body via
   the provider's writeback flow before iterating further on the plan.

3. **Implement.** Apply the approved plan exactly. Keep the change to the
   smallest shape that satisfies Acceptance Criteria; surface unrelated
   cleanups as follow-ups instead of folding them in. For `bug`, add the
   regression test first and confirm it fails on the unfixed code, then
   apply the fix and confirm it passes — both outputs become AC evidence.
   For `spike`, run the validation method and capture evidence; PoC code
   stays throwaway and production work belongs in a follow-up `task`.

4. **Verify Acceptance Criteria.** Pair every AC bullet with concrete
   evidence — test command and outcome, manual observation, artifact
   produced. Symmetry from a primary fix is not evidence for related ACs;
   each bullet needs its own check. If any AC fails, stop and ask the
   user before committing.

5. **Commit.** Stage only the changes the plan covered and split into
   meaningful commits (implementation, tests, scaffolding, tooling). Every
   subject carries the issue ref prefix per the session's commit-prefix
   policy. Do not list commit SHAs in the issue body or comments — the
   timeline already links commits by ref prefix.

6. **Refresh `Resume` and close.** Rewrite the `Resume` section to a
   closed-state snapshot (Approach summarised, `Waiting for` empty,
   `Open questions` resolved or moved to follow-ups, `Next` empty or
   naming the follow-up) and close in the same writeback call. Present
   the draft body to the user before invoking. For `spike`, the body
   update also carries the captured evidence (typically `Artifact Links`
   plus a short summary); close as `not_planned` only when the user
   agrees the question is no longer load-bearing. On freshness drift,
   reread the cache paths the script reports and retry — never bypass the
   check.

## Additional Requirements

Treat `$ARGUMENTS` past the issue ref as extra emphasis from the user.
Incorporate it into the relevant step rather than tacking it on at the end.

$ARGUMENTS

## Output

Report only:

1. Issue ref and final state — `closed: completed`, `closed: not_planned`,
   or `still open: <reason>`.
2. Commit SHA(s), or `skipped`.
3. One line per Acceptance Criterion paired with its evidence.
