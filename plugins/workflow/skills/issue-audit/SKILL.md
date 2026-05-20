---
name: issue-audit
description: "Audit a workflow-issue spec BEFORE implementation. Read-only review of AC quality, Affected Paths grounding, root-cause coherence, workaround detection, cross-issue context, and scope sizing."
argument-hint: "<issue-ref>"
disable-model-invocation: true
context: fork
agent: auditor
---

# Pre-implementation audit of workflow issue `$ARGUMENTS`

Audit the spec **before** it is implemented. Push back on the issue itself: an unclear AC, a stale Affected Paths, a plan that quietly works around the real problem, a scope that bundles unrelated concerns.

## Workflow

1. **Read the target issue.**
   - Fetch with the workflow issue-fetch command and `$ARGUMENTS` as the ref, default cache policy.
   - Extract Description, Root Cause (if present), Affected Paths, Unit Test Strategy, Acceptance Criteria, any other named sections.
   - Read the frontmatter `relationships` block: capture parent, children, blocked-by, blocking, related refs.

2. **Walk the related issue graph (one hop).**
   - For each related ref, fetch with the same command and read the resulting cache projection.
   - Note state (open/closed), purpose, and any constraint each related issue places on this work (parent direction, blocked-by deliverable, sibling overlap, prior decision in `related`).

3. **Ground the plan in current code.**
   - For every file path, symbol, or line number cited in Description / Root Cause / Affected Paths, verify it exists in the current working tree; line numbers should reasonably match the named symbol (allow small drift).
   - For every behavioral claim ("the helper truncates microseconds", "Y calls Z"), open the cited code and verify the claim is true today.

## Audit dimensions

### 1. AC quality

For each Acceptance Criteria bullet:

- Is it concrete? Does it name an observable surface (a test that would pass, a code path that would exist, a behavior that would be triggered)?
- Could a later auditor verify it without inferring? Vague items ("improve performance", "make it robust", "ensure correctness") are `concern` or `fail`.
- Is each bullet independently verifiable? An AC bullet that bundles multiple checks should be split.

### 2. Plan-skipped obvious work

Read Description and Root Cause. List the implementation surfaces the stated problem demands. Then walk the Affected Paths and mark which are present.

Flag anything that the goal obviously requires but the plan omits — e.g. "fix X for both providers" with a Affected Paths that touches only one provider; a consolidation that leaves dangling callers; a behavior change with no doc/policy update where one is expected.

### 3. Plan over-scoped

Walk each Affected Paths item. For each, ask: does the stated problem require this?

Flag work that exceeds the problem: new abstractions, helpers, error-handling layers, feature flags, version-gating, parallel writes, "while we're at it" cleanups, refactors that don't fall out of the fix. Plan-stage over-engineering is cheaper to cut than post-implementation.

### 4. Plan grounding

For each cited file path / symbol / line:

- File path exists in the working tree.
- Symbol still exists at the cited location (allow small line drift).
- Behavioral claim is true in the current code.

Stale references = `fail`. The implementer cannot follow a plan whose anchors have moved.

### 5. Root-cause coherence

For bug issues:

- Is the root cause named as a concrete mechanism, not a symptom? "Half of publish --epic calls fail" is symptom; "`fetched_at` is truncated to whole seconds while `source_updated_at` keeps milliseconds" is mechanism.
- Does the cause fully explain the reported symptom? If the cause only explains some failure modes, the analysis is incomplete.

For feature/refactor issues:

- Is there a single coherent reason for the change? Or is the motivation a list of weakly related justifications?

### 6. Workaround detection

Treat the plan with suspicion when any of these appear:

- The plan **disables, skips, suppresses, or silences** the failing behavior rather than fixing it.
- The plan introduces a **flag, config, or env var to opt out** of the broken behavior.
- Language like **"temporary"**, **"interim"**, **"until X is fixed"**, **"as a stopgap"**, **"defer the real fix"**.
- The plan touches the **symptom location** while the Root Cause names a **different** location.
- The plan **reverts or rolls back** instead of fixing forward.
- The plan **wraps** the buggy code path in a guard that hides it without addressing it.

A real deferral can be legitimate, but it must be named as such with rationale. Quiet workarounds = `fail`.

### 7. Cross-issue context

Using the related issues fetched in step 2:

- **Parent**: does the plan respect the parent epic's stated direction? Does the parent contain decisions (in body or comments) that this plan ignores?
- **Blocked-by**: are the prerequisite issues actually closed / their deliverables present? Does the plan assume something a blocked-by issue still owes?
- **Blocking**: does this plan deliver what the issues it blocks expect?
- **Child**: are children covered by this plan, or does the plan leave them orphaned?
- **Related**: does prior decision in a related issue contradict this plan?

### 8. Issue scope sizing

Assess whether the issue is one coherent unit:

- **AC independence** — count AC bullets that target distinct surfaces.
- **Title / Description bundling** — phrases like "X and Y", "do A, B, and C", multiple unrelated concerns under one Description.
- **Phased Approach** — explicit phases / stages where each could stand alone as a follow-up issue.
- **Subsystem spread** — the work touches multiple subsystems that do not share a single root cause.
- **PR sizing** — would a single PR closing this issue be reviewable, or would it need to be split?

A well-scoped issue should map cleanly to one PR with one coherent rationale.

## Output

Write the audit report to `${WORKFLOW_PROJECT_DIR}/issue-audit-<ref>.md`, where `<ref>` is `$ARGUMENTS` with any leading `#` stripped. Overwrite any existing file at that path.

Report file structure:

```
# Issue audit: $ARGUMENTS

Related issues read: <list of refs, or "none">

## 1. AC quality
- [fail|concern|pass] <one-line summary>
  Evidence: <AC bullet verbatim, or file:line>
  Recommend: <one-line action>

## 2. Plan-skipped obvious work
...
## 3. Plan over-scoped
...
## 4. Plan grounding
...
## 5. Root-cause coherence
...
## 6. Workaround detection
...
## 7. Cross-issue context
...
## 8. Issue scope sizing
...

## Verdict
<one of: ready-to-implement | needs-revision | mixed (some dimensions clean, others need work)>
```

After writing the file, return exactly one line: `Audit report saved to <absolute-path>. Verdict: <verdict>.`
