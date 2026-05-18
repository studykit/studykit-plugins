---
sequence: 13
timestamp: 2026-05-18_2247
timezone: KST +0900
topic: workflow-authoring-and-session-policy
---

> **DO NOT UPDATE THIS FILE.** This handoff is a point-in-time snapshot of the session at 2026-05-18_2247. To record a later state, create a new handoff file via `/handoff` — never edit this one.

## Goal

Two intertwined refactors in `plugins/workflow/`:

1. Push literal body-markup ownership out of `authoring/common/` and into provider conventions (so Jira issue bodies stop receiving Markdown that renders as plain text in Jira wiki markup).
2. Tighten the SessionStart policy so the pending-draft flow is explicit and keeps issue/comment body content out of `workflow-operator`'s context.

Both threads originated from the user noting that Jira issues were not rendering Markdown and that several `## Heading`/`## Comments`/`## Completion` patterns were duplicated across common files. The session also discovered operator-side coverage gaps in pending-draft preparation, which were filed as a separate follow-up.

## Current State

- Branch: `main` (clean working tree).
- HEAD: `e195293 #78 Split pending-draft flow into skeleton + publish steps in SessionStart policy`.
- Recent session-relevant commits, newest first:
  - `e195293` #78 — Split pending-draft flow into skeleton + publish steps.
  - `d714cb0` #78 — Tighten SessionStart policy: pending-draft flow + provider-aware knowledge fragment + condense.
  - `7e1e4cb` #80 — Refactor workflow authoring: provider-owned body markup; dedupe shared common sections.
  - `e9c75e7` — Pre-session commit by the user ("Clarify workflow draft path ownership"); did not originate in this session, see Known Issues.
- Issue state on GitHub:
  - **#78 closed** in this session after summary comment.
  - **#80 open** — work done in `7e1e4cb` covers the body of the AC list, but README-update AC for that thread is not closed.
  - **#81 open** — created in this session for the operator-side gap.

## Changes Made

### Authoring refactor (commit `7e1e4cb`, issue #80)

33 files changed, +459/-885. Inspect with `git show 7e1e4cb`.

- `authoring/common/` is now semantic-only. Body shapes refer to sections by canonical Title Case names (`Description`, `Acceptance Criteria`, …) rather than literal `## Heading` / ` ```markdown ` fences.
- `common/markdown-authoring.md` deleted; `scripts/authoring_resolver.py` no longer injects it (was unconditionally first in every resolution).
- `common/issue-authoring.md` now hosts shared baselines: `Common mistakes (all issue-backed types)`, `Completion baseline (all issue-backed types)`, canonical relationship intents (`parent`, `blocked_by`, `blocking`, `related`) aligned with `workflow_cache.py` normalization.
- `common/knowledge-body.md` now hosts `Common mistakes (all knowledge types)` (local-projection identity, page-comment substitute for review).
- Each `common/<type>-authoring.md` keeps only type-specific mistakes, completion criteria, and body shape; `## Done rule` / `## Done criteria` were renamed to `## Completion criteria` (spike, ci); shared `## Comments and discussion` sections removed (foundation's `## Comments and history` covers them).
- `providers/github-issue-convention.md` & `providers/github-knowledge-convention.md` got brief Body-markup sections declaring GFM and task-list usage.
- `providers/jira-issue-convention.md` Body-markup section declares wiki markup + `h2.` heading mapping + the no-native-checklist rule. The full markup table was removed; full Markdown-to-wiki mapping lives in `providers/jira-issue-anti-patterns.md` ("Markdown leakage").
- Each `providers/jira-issue-<type>-authoring.md` shows the final body structure in `h2.` form.
- Operator-internal `.workflow/config.yml` resolution notes removed from provider authoring files (this is operator state, not main-agent guidance).
- `target` removed from common relationship vocabulary (review-only; lives in `review-authoring.md`).
- `tests/test_authoring_resolver.py` updated to reflect the dropped `common/markdown-authoring.md`.

### SessionStart policy tightening (commits `d714cb0` and `e195293`, issue #78)

`plugins/workflow/agents/workflow-main-context/session-policy.md` was rewritten to be both more concise and explicit about the new flow.

- Removed `Read and interpret returned local files` (LLM default behavior + already mirrored by operator no-summary rule).
- Removed `Do not infer relationships from prose` (redundant once relationship intent is an explicit parameter).
- Folded `Authoring rules:` numbered list into main responsibilities bullets; collapsed `Workflow operations include …` paragraph to a single line; removed operator's redundant re-listing of workflow operations.
- Pending-draft flow is now described in two distinct steps:
  1. `main → operator`: send metadata (title, labels, issue type, relationship intent). Operator prepares a draft skeleton, records metadata in frontmatter, and returns the path.
  2. `main` edits **only the body** of the skeleton; does not touch frontmatter.
  3. After explicit user approval, `main` hands the path back with publish/update intent. Operator publishes from the path; it does not read the body content otherwise.
- GitHub-only "edit in working tree" knowledge guidance moved from `session-policy.md` to `agents/workflow-main-context/knowledge/github.md` (per-provider fragment, already auto-injected only for github knowledge).
- `test_workflow_hook.py` policy assertions trimmed to phrases that remain in the policy (`relationship intent`, `Return operational paths, refs, relationship metadata, and verification results`).

## Key Files

- `plugins/workflow/authoring/common/AGENTS.md` — declares the "body markup is provider-defined" boundary.
- `plugins/workflow/authoring/common/issue-authoring.md` — canonical relationship intents, `Common mistakes (all issue-backed types)`, `Completion baseline (all issue-backed types)`.
- `plugins/workflow/authoring/common/knowledge-body.md` — `Common mistakes (all knowledge types)`.
- `plugins/workflow/authoring/providers/jira-issue-convention.md` — short Body markup declaration; main wiki-markup matrix removed.
- `plugins/workflow/authoring/providers/jira-issue-anti-patterns.md` — full Markdown-to-wiki "Markdown leakage" mapping.
- `plugins/workflow/scripts/authoring_resolver.py:209` — `parts: list[str] = []` (no implicit common/markdown-authoring injection).
- `plugins/workflow/agents/workflow-main-context/session-policy.md` — condensed 25-line policy with new 2-step pending-draft flow.
- `plugins/workflow/agents/workflow-main-context/knowledge/github.md` — GitHub-only "edit in working tree" guidance.
- `plugins/workflow/tests/test_authoring_resolver.py`, `plugins/workflow/tests/test_workflow_hook.py` — updated assertions.

## Related Links

- #78 (closed) — Clarify workflow SessionStart operator routing policy. Initial fix landed earlier in `1f4931c`; this session added `d714cb0` and `e195293` and posted a wrap-up comment.
- #80 (open) — Move body markup to provider authoring; dedupe shared common sections. All AC except `README updates` covered by `7e1e4cb`.
- #81 (open) — Implement pending draft preparation entrypoints and operator guidance. Captures the operator-side gap (no script creates a pending comment draft; operator-context docs missing; no filename convention helper).
- Workflow operator transcript log: `~/.claude/projects/-Users-myungo-GitHub-studykit-plugins/f41effd6-…/subagents/agent-aaeeeccf5f61eac55.jsonl` — the 22-tool-call run that motivated #81.

## Decisions and Rationale

- **Common stays semantic-only.** Each provider convention owns literal heading/list/inline/code/table/checklist markup. Less duplication; LLMs already know GFM and Jira wiki markup at coarse level. The Jira-side detail that matters lives in the `jira-issue-anti-patterns` Markdown-leakage table, which is the form LLMs are most likely to misuse.
- **Operator-internal config resolution notes removed from authoring docs.** Main agent only needs to know the *what* (use issue keys) not the *how* (config lookup order).
- **Pending-draft flow uses skeleton + body-only edit.** Body content never enters operator context. Operator owns frontmatter so explicit-parameter handoff is unambiguous (no body-prose inference). Per-session `SessionStart` policy injection cost drops.
- **`Done rule` / `Done criteria` unified to `Completion criteria`.** Same semantic; consistent heading lowers cognitive load for LLMs and humans.
- **`target` relationship is review-only.** Code/cache canonical intents are `parent`/`blocked_by`/`blocking`/`related`. `target` belongs to review semantics; common file no longer hosts it.
- **Knowledge per-provider guidance lives in fragments.** `agents/workflow-main-context/knowledge/<provider>.md` is auto-injected only when knowledge provider matches, so base policy stays markup-agnostic.

## Important Dialog

- User pushed back on overzealous LLM-known content: "LLM이 알고 있는 markdown 문법을 기록할 필요는 없어 보이는데" → led to trimmed GitHub Body markup section.
- User: "Jira wiki markup 규칙까지 기록할 필요가 있는지" → led to trimmed Jira Body markup table; full mapping moved to anti-patterns.
- User on `target` in common: "parent가 epic이 아님. custom field 일 텐데." Clarification that Jira's native parent and Epic Link customfield are separate storage surfaces. Decision deferred to #76 follow-up code path (`epic` intent vs. surface routing).
- User on operator-internal config notes: "이거를 main agent에 알려줄 필요가 없는데." → led to scrubbing `.workflow/config.yml` resolution lines from both jira and github convention files.
- User on policy redundancy: "이 문구는 필요 없어 보이는데" (multiple lines trimmed across iterations).
- User on policy provider neutrality: "knowledge는 provider에 따라 달라야 할텐데." → led to moving GitHub-only knowledge edit guidance to `knowledge/github.md` fragment.
- User on frontmatter: "main agent가 frontmatter를 수정하면 안되는데." → led to body-only edit clause.
- User on policy redundancy v2: "선택 라인은 이제 필요 없는것 같은데." (relationship-infer-from-prose line) → removed.
- User on concise rewrite: "concise하게 다듬으면 좋겠어." → 32 → 25 line condense.
- User on operator opacity: "operator가 전체 이슈를 읽을 일이없을텐데" → motivated the 2-step skeleton-then-publish split.
- User on workflow flow when operator struggles: "이번에는 main agent에서 직접 comment를 달고. 별도 이슈 만들기." → main bypassed operator for the #78 wrap comment via `gh`. Issue creation for #81 still went through operator.

## Validation

- `cd plugins/workflow && uv run --with pytest --with python-frontmatter --with pyyaml pytest tests/ -x -q` → **347 passed**. Run after each significant edit during the session.

## Known Issues and Risks

- **#80 still open.** AC5 (README updates for `plugins/workflow/README.md` and `plugins/workflow/hooks/README.md`) was deferred. Without that, the README still describes the pre-refactor policy.
- **#81 deliverable lag.** `session-policy.md` describes the skeleton + publish pending-draft flow, but no script entrypoint actually prepares a comment skeleton. Operator agents currently improvise (per transcript `agent-aaeeeccf5f61eac55.jsonl`: 22 tool calls / 217 s to mkdir + `Write` an empty file). Until #81 ships, expect operator delegations for comment drafts to remain slow or to fall back to `gh` direct calls.
- **`e9c75e7 Clarify workflow draft path ownership`** appeared in the local log before this session edited the policy. It was authored elsewhere (likely a preceding hand commit by the user or another session); the present session did not write it. Behavior is unchanged but it is worth knowing this commit exists upstream of session work.
- **Cache staleness pattern.** When inspecting `.workflow-cache/issues/<n>/issue.md`, remember the cached `source_updated_at` lags GitHub state. Refresh through `workflow-operator` (`cache-policy refresh`) before drawing conclusions about issue status.
- **`epic` relationship modeling open.** `parent` canonical intent currently covers both native sub-task parent and Epic Link customfield via surface routing. Whether to introduce a dedicated `epic` intent is deferred to the #76 work stream; do not change common/issue-authoring without aligning code.

## Next Steps

1. **#81 implementation** — start here. Add a `--prepare-draft` entrypoint (or new `*_comment_drafts.py`) for github and jira, shared filename helper (`<utc-compact>-pending.md`), `workflow-operator-context/` procedure docs, and tests. Mirror the existing `*_drafts.py` shape for issues.
2. **Decide #80 closeout.** Either (a) implement the README updates and close #80, or (b) split AC5 into its own micro-issue and close #80 with the implementation comment already covered by `7e1e4cb`.
3. **README sync.** `plugins/workflow/README.md` and `plugins/workflow/hooks/README.md` both predate the new policy; bring their SessionStart routing description in line with `session-policy.md`.
4. **Operator-context bootstrap inspection.** Spot-check `agents/workflow-operator-context/*.md` for accuracy against the trimmed convention files. Some of those bootstrap notes referenced the now-removed `.workflow/config.yml` resolution text indirectly.

## Open Questions

- Should `target` be promoted back to a common canonical intent or stay review-only? Decision pending review on whether knowledge "page reviewed by review item" deserves first-class vocabulary.
- For #81, do pending **issue** drafts and pending **comment** drafts share an entrypoint (`*_drafts.py` extended) or split into siblings (`*_drafts.py` + `*_comment_drafts.py`)?
- Filename convention for pending comments: keep `YYYYMMDDTHHMMSSZ-pending.md` (chosen ad-hoc by operator this session) or a more descriptive `pending-<utc>.md`? Decide in #81.
- For Jira `epic` membership writes, intent reaches `parent` via surface routing today; introducing `epic` as a separate canonical intent will require code + config schema changes coordinated with the existing #76 work. Hold until #76 site-profile flow settles.

## Useful Commands and Outputs

```sh
# Workflow tests
cd /Users/myungo/GitHub/studykit-plugins/plugins/workflow \
  && uv run --with pytest --with python-frontmatter --with pyyaml pytest tests/ -x -q

# Inspect a session's commits
git log --oneline -5

# Inspect any of this session's commits
git show 7e1e4cb --stat   # authoring refactor
git show d714cb0          # initial policy tightening
git show e195293          # policy flow split

# Direct gh fallback (used for #78 wrap comment when operator overhead was high)
gh issue comment 78 --repo studykit/studykit-plugins --body "..."
gh issue close 78 --repo studykit/studykit-plugins

# Cache refresh via workflow-operator (do not read cache directly without refresh)
# Delegate through the workflow-operator subagent rather than running scripts here.
```
