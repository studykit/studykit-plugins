---
name: handoff
description: "Wrap a workflow session: refresh in-flight issue Resume sections and capture residual session findings, gaps, or questions as review issues."
argument-hint: "[additional requirements]"
disable-model-invocation: true
allowed-tools:
  - 'Bash("$WORKFLOW":*)'
  - 'Bash(date:*)'
  - 'Bash(git status:*)'
  - 'Bash(git log:*)'
  - 'Bash(git diff:*)'
---

# Workflow Session Handoff

Leave durable continuation context for a fresh session that cannot see this conversation. Every handoff artifact lives at the issue provider — there is no separate handoff file. The session is wrapped by refreshing each in-flight issue's body and, only if residual session-level meta remains, publishing one or more `review`-type issues that capture it as atomic findings, gaps, or questions.

## Core rules

- Refresh in-issue resume context first: for every touched mid-flight issue, rewrite the `Resume` section in the issue body so the issue alone shows current approach, who/what it is waiting for, open questions, and the next step. Append a comment only for narrative-worthy events: decision pivots, blocker resolutions, or approach changes. Follow `${CLAUDE_PLUGIN_ROOT}/authoring/common/issue-body.md` for `Resume` slot meaning and reference form.
- The cached `issue.md` and `comment-*.md` projections are read-only. Resume rewrites and comments must go through the configured provider write scripts via `$WORKFLOW` per `${CLAUDE_PLUGIN_ROOT}/main-context/policy/provider-writes/`. Mutations require a temp body file, user approval, and the freshness-check flow.
- Session-level residual that does not fit any in-flight issue's body lands in `review`-type issues. Each review item holds one concern only (`finding` / `gap` / `question`) per `${CLAUDE_PLUGIN_ROOT}/authoring/common/review-authoring.md`. Do not pack multiple concerns into one review; do not create a review item when an existing in-flight issue's `Resume` or a comment can hold it.

## Handoff gate

Decide in two stages; the gate exists to avoid ceremonial review issues.

### Stage 1 — fold first

Try each candidate's natural anchor before treating it as session-level residual:

| Candidate | Fold target first | Residual that justifies a review issue |
|-----------|-------------------|----------------------------------------|
| **In-flight issue state** — approach, blocker, open questions, next step on a single issue (including failing validation, which lands in the `Waiting for` slot) | That issue's `Resume` section via the configured provider's `*_issue_writeback.py update --body-file` flow | None when the section captures it cleanly |
| **Narrative-worthy event** — decision pivot, blocker resolution, approach change on one issue | A comment on that issue via `*_issue_comments.py append --body-file`. Per project memory, do not list commit SHAs in the comment by default — the timeline already links commits whose subjects carry the `<ref>` prefix | None; sequencing across multiple issues is recoverable from the timeline |
| **Cross-cutting decision across siblings** — same parent, multiple in-flight issues | A comment on the common parent (epic, where applicable), with each affected child's `Resume` Open-questions slot updated to cite the parent's decision. Create an `epic` only when sibling issues need a shared narrative home | An unresolved finding / gap / question exposed by the decision → one review item per concern |
| **Anchorless work** — production source, build, tooling, config with no clean single-issue anchor | Parent issue's `Resume` / a comment when cleanly anchored; otherwise the commit message, prefixed with the issue ref per `${CLAUDE_PLUGIN_ROOT}/main-context/commit-prefix.md` | Unanchored change whose rationale still matters beyond the commit body → one review item describing the gap or question |
| **Branch / commit state** | Nothing when obvious from `git status` and `git log --oneline origin/main..HEAD` | Non-obvious state (mid-merge, mid-rebase, divergence, opaque commits, commits whose `<ref>` prefix does not match the in-flight issue set) → one review item describing the gap |

Long-lived user or project preferences belong in durable project guidance (`CLAUDE.md`, or project memory only when explicitly requested), not a review issue.

### Stage 2 — residual check

Ask: can the next session reach every mid-flight issue's next step by running `"$WORKFLOW" <provider>_issue_fetch.py <ref>` for each touched ref, reading the resulting `issue.md` (Resume section plus the recent `comment-*.md` tail), plus `git log --oneline origin/main..HEAD` and commit messages?

- If yes, stop. Report pre-handoff commit(s) or `skipped`, the issue refs whose `Resume` and / or comments were updated, and `no session-level residual — no review issues published`.
- If no, identify each residual concern as a single `finding`, `gap`, or `question`, and publish one review issue per concern.

Non-triggers on their own (do not publish a review for these):

- Routine green validation.
- Authoring contract reads that the resolver will surface again next session.
- Provider cache refreshes that next session will redo on demand.
- General-guideline `CLAUDE.md` edits that are auto-loaded next session.
- Background context rederivable from issue content and git history.

## Context

- Timestamp: !`date +"%Y-%m-%d_%H%M"`
- Timezone: !`date +"%Z %z"`
- Git status preview: !`git status --short | head -10`

## Task

1. **Refresh touched mid-flight issues before anything else.**
   - Scope: every issue touched, opened, advanced, blocked, or relied on this session, excluding ones already closed / discarded / superseded at the provider.
   - For each, draft the new `Resume` section as a current snapshot per `${CLAUDE_PLUGIN_ROOT}/authoring/common/issue-body.md`: Approach / Waiting for / Open questions / Next. Remove stale items; the `Resume` section is rewritten in place and does not preserve history.
   - Resolve authoring paths first: `"$WORKFLOW" authoring_resolver.py --type <type>` and read the returned files. The provider-write contract (publish / append / update body-file flow, freshness handling) lives at `${CLAUDE_PLUGIN_ROOT}/main-context/policy/provider-writes/<provider>.md` — open it before drafting.
   - Apply the rewrite via `*_issue_writeback.py update --issue <ref> --body-file <path>`. Present the draft body to the user for approval before invoking the script. On `status=blocked` (freshness drift), reread the listed cache paths and retry; never bypass the freshness check.
   - For narrative-worthy events (decision pivot, blocker resolution, approach change), add a comment via `*_issue_comments.py append --issue <ref> --body-file <path>`. Do not log routine status changes. Do not list commit SHAs in the comment body by default; the timeline already links commits whose subjects carry the issue ref prefix.
   - For cross-cutting decisions across siblings sharing a parent, leave the parent's comment as the durable record and update each affected child's `Resume` Open-questions slot to cite the parent.

2. **Commit relevant non-handoff changes, split by meaningful unit.**
   - Inspect `git status --short` and `git diff --stat` before deciding.
   - Stage only changes that clearly belong to this session; leave unrelated user changes untouched and mention them in the report. Ask only if ownership is unclear.
   - Split commits by coherent meaning: implementation source, tests, scaffolding, tooling, build, config, or unrelated cleanup.
   - Prefix each commit subject with the related issue ref per `${CLAUDE_PLUGIN_ROOT}/main-context/commit-prefix.md`. Ask the user if the prefix is unclear.
   - Skip this step if there are no relevant non-handoff changes.

3. **Run the Stage 2 residual check.**
   - If no residual remains, stop here and report the no-op outcome.
   - Otherwise, list each residual concern atomically. One concern per review item. The concern type is one of `finding`, `gap`, or `question` per `${CLAUDE_PLUGIN_ROOT}/authoring/common/review-authoring.md`.

4. **Publish one `review` issue per residual concern.**
   - Resolve authoring paths: `"$WORKFLOW" authoring_resolver.py --type review` and read the returned files.
   - Draft each review body per `${CLAUDE_PLUGIN_ROOT}/authoring/common/review-authoring.md`: a `Description` that states the single concern, why it matters, and what would resolve it; optional `Suggested Fix`, `Evidence`, `Resume`. Identify the target issue or content per the review-target rules; if truly cross-cutting, say so explicitly in `Description`.
   - Reference related in-flight issues by provider-native ref (`#NNN` for GitHub Issues, `KEY-NNN` for Jira). Do not use cache projection paths as identity. Do not paste issue body or comment content; link instead.
   - Publish via `*_issue_drafts.py publish --type review --title <title> --body-file <path>` after presenting the draft and obtaining user approval. Link siblings or the parent using relationship flags when appropriate.

5. **Record verification.**
   - Capture exact commands and outcomes already run this session (workflow plugin commands, project tests, linters, type-checks, smoke checks, or explicit user-provided output). Failing validation should be reflected in the relevant in-flight issue's `Resume` Waiting-for slot or a comment; a review item is appropriate only when the failure represents a finding, gap, or question that needs independent tracking.

## Additional Requirements

Treat `$ARGUMENTS` as extra emphasis or constraints from the user. Incorporate them into the relevant steps instead of appending them at the end.

$ARGUMENTS

## Output

After the run, report only:

1. Pre-handoff commit SHA(s), or `skipped`.
2. Issue refs whose `Resume` and / or comments were updated this session, or `none`.
3. Published review issue refs with one-line concern summaries, or `no session-level residual — no review issues published`.
4. One-line validation summary, or `none recorded`.

Do not restate review issue bodies or refreshed issue content in the output.
