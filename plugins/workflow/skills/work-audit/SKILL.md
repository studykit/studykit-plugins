---
name: work-audit
description: "Audit completed workflow-issue work BEFORE closure. Read-only review of AC compliance, skipped obvious work, deferred-as-open, over-engineering, and missing implementation surfaces."
argument-hint: "<issue-ref> [<commit-range>]"
disable-model-invocation: true
context: fork
agent: auditor
---

# Pre-closure audit of workflow issue `$0`

Audit the completed work **after** the main agent claims the issue is done — typically just before closure or handoff. Push back on premature "done" claims.

Inputs from `$ARGUMENTS`:
- `$0` — workflow issue ref (e.g. `#97`, `KEY-123`). Required.
- `$1` — optional commit range or branch (e.g. `origin/main..HEAD`). When unspecified, compare the current branch against its upstream / `origin/main`.

## Workflow

1. **Read the issue.**
   - Fetch with the workflow issue-fetch command and `$0` as the ref, default cache policy.
   - Extract: Description, Affected Paths, Unit Test Strategy, Acceptance Criteria, any other named sections. Note explicit deferrals (e.g. "follow-up issue", "out of scope").

2. **Read the work.**
   - Enumerate commits in the range attributable to this issue (subjects prefixed with the issue ref per repo convention).
   - Read the diff of the range and inspect each commit individually: added tests, touched scripts, manifest bumps, doc updates.
   - For each file touched, open it to understand the change in context — do not audit from the diff alone.

## Audit dimensions

### 1. AC compliance

Walk each Acceptance Criteria bullet. For each, identify the concrete artifact that verifies it:

- A test function that exercises the exact named surface (not a helper one layer below).
- An observable code path in the diff that the AC names.
- A command output, smoke run, or provider-side state change captured in commit messages or comments.

A bullet is `verified` only when the evidence names the same surface the AC names. Symmetry ("the shared helper covers both providers, so the GitHub publish AC is satisfied") is `unverified` — the AC named the publish boundary, so the evidence must exercise the publish boundary. A bullet satisfied via a different mechanism than the Affected Paths proposed still needs its own evidence.

### 2. Skipped obvious work

Read the issue body's actionable sections (Affected Paths, Unit Test Strategy, explicit bullet lists). For each named action item:

- Locate it in the diff.
- If a strategy section names tests (e.g. "Regression test for X"), each named test must be present.
- If Affected Paths names a code change (e.g. "consolidate helper Y"), that change must be in the diff.

Items that are merely *implied* by the surrounding work (e.g. "obviously you'd also touch Z") count too — flag them, then let the user judge.

### 3. Deferred-as-open

Detect work that was punted to a follow-up issue, TODO comment, or "out of scope" note, where the deferral feels like laziness rather than a real scope cut. Heuristics:

- A deferral introduced in this session for work that the issue body originally listed.
- A new `TODO` / `FIXME` in the diff with no linked issue.
- A closing comment that says "this AC is satisfied by symmetry" or similar reasoning that papers over missing work.
- A "follow-up issue" mention without an actual created issue.

Real deferrals (e.g. user-approved scope cut, clearly out of scope, blocked on external) are fine — but the audit should still list them so the user can confirm the reasoning.

### 4. Over-engineering

Cross-reference the project's stated principles (no unnecessary abstractions, no defensive handling for impossible scenarios, no premature feature flags, no backwards-compat shims, three-similar-lines beats a helper). Flag in the diff:

- New helpers / classes / config knobs introduced for one caller.
- Error handling, fallbacks, or validation for scenarios that can't actually happen at this boundary.
- Feature flags or version-gating shims that the task didn't require.
- Comments that explain WHAT the code does (well-named identifiers should already convey that) or that reference the current task/fix/caller ("added for X flow", "used by Y").
- New documentation files / READMEs that the user did not ask for.

Under-engineering is fine for a bug fix; over-engineering is the failure mode to catch.

### 5. Missing implementation

Identify surfaces that obviously needed to be touched but were not. Heuristics:

- Symmetric provider not updated (e.g. fix landed on the GitHub side but the Jira-equivalent has the same bug).
- Tests added on one path but not another that the issue explicitly named.
- A consolidation/rename that left dangling old call sites.
- A version bump in one manifest but not the matching cross-runtime manifest.
- An imported symbol whose import wasn't cleaned up after the source moved.
- A behavior change that should have a doc / policy update in the same plugin but didn't.

## Output

Write the audit report to `${WORKFLOW_PROJECT_DIR}/work-audit-<ref>.md`, where `<ref>` is `$0` with any leading `#` stripped. Overwrite any existing file at that path.

Report file structure:

```
# Work audit: $0

## 1. AC compliance
- [fail|concern|pass] <one-line summary>
  Evidence: <pointer or "none">
  Recommend: <one-line action>

## 2. Skipped obvious work
...
## 3. Deferred-as-open
...
## 4. Over-engineering
...
## 5. Missing implementation
...

## Verdict
<one of: ready-to-close | needs-work | mixed (some AC verified, others not)>
```

After writing the file, return exactly one line: `Audit report saved to <absolute-path>. Verdict: <verdict>.`
