# plugins/workflow/hooks/

Workflow hooks dispatch through runtime-specific entry scripts. Both scripts
dispatch from the payload `hook_event_name` and own their runtime-specific
payload/env extraction. They call common plain functions from
`../scripts/workflow_hook.py` for shared workflow behavior such as policy
injection, provider cache projection protection, and issue-cache context.

The Codex manifest registers only `SessionStart`, `UserPromptSubmit`, and
`Stop`. Claude also registers `PreToolUse` for provider cache projection
protection. Authoring read tracking is not hook-enforced in either runtime.

When either runtime script writes hook output to stdout, it writes JSON only.
Empty stdout is used for no-op hook runs.

## PreToolUse Write/Edit (Claude only)

`PreToolUse` on file writes protects provider cache issue body projections.

Behavior:

- Allows normal workflow artifact writes without hidden authoring read checks.
- Blocks provider cache issue body writes when the projection is missing.
- Blocks provider cache issue body writes that alter projection-owned YAML frontmatter.
- Emits nothing for non-workflow projects or safe body-only writes.

## SessionStart

`SessionStart` injects workflow policy for configured projects.

Behavior:

- If the active project has no `.workflow/config.yml`, the hook emits nothing.
- Main-assistant SessionStart wording lives under `../agents/workflow-main-context/`: base policy in `../agents/workflow-main-context/session-policy.md`, GitHub knowledge guidance in `../agents/workflow-main-context/knowledge/github.md`, and Codex reuse guidance in `../agents/workflow-main-context/codex-operator-reuse.md`.
- The hook prepares a normalized shell environment contract for workflow shell commands: `WORKFLOW`, `WORKFLOW_PLUGIN_ROOT`, `WORKFLOW_PROJECT_DIR`, and `WORKFLOW_SESSION_ID`.
- Claude writes that contract to `CLAUDE_ENV_FILE` when Claude provides it for `SessionStart`. Claude operator subagent shell commands can use the same persisted `WORKFLOW_*` contract.
- The Claude `workflow-operator` agent frontmatter registers a `SubagentStart` hook. When the spawned agent matches `workflow-operator`, `hook_claude.py` loads configured fragments from `../agents/workflow-operator-context/` and injects a bootstrap context containing the absolute `../scripts/workflow` launcher path, the configured issue command aliases, and configured knowledge-provider guidance.
- Codex cannot persist environment variables from `SessionStart`; `hook_codex.py` records a unified session state file under `.workflow-cache/hook-state/`, keyed by the Codex hook `session_id`. The `../scripts/workflow` wrapper later reads that state and evaluates the generated exports from the shell-visible `CODEX_THREAD_ID`.
- If the active project has a valid `.workflow/config.yml`, the hook injects a concise routing policy as `additionalContext`. The policy is intentionally narrow: it tells the main assistant to delegate workflow operations to `../agents/workflow-operator.md` and keep provider CLI use behind the operator.
- Codex main-session policy additionally tells the main assistant to reuse an already open `workflow-operator` thread for later workflow operations. Claude main-session policy does not include this Codex-specific thread-reuse instruction.
- In Codex subagent shells, `CODEX_THREAD_ID` is the subagent's own thread id and no parent-thread environment variable is available. For Codex subagent `SessionStart` payloads, `hook_codex.py` checks `transcript_path` for `session_meta` records that identify the spawned agent. When the spawned agent matches `workflow-operator`, the hook extracts the parent thread id from transcript metadata, records a state file keyed by the subagent session id, and stores `parent_session_id` plus `WORKFLOW_SESSION_ID` set to the parent thread id. The hook also loads configured fragments from `../agents/workflow-operator-context/` and injects a bootstrap context containing the absolute `../scripts/workflow` launcher path, the configured issue command aliases, and configured knowledge-provider guidance. The operator uses that path as `$WORKFLOW`; `../scripts/workflow` owns session translation.
- For all other subagent SessionStart payloads (non-operator agents, or operator subagents without an extractable parent id), the hook emits nothing.
- Claude operator subagents use the persisted contract from the Claude session environment plus the `SubagentStart` bootstrap context. If Claude sends an agent-tagged `SessionStart` payload, the hook does not inject the main-session policy into that subagent.
- For GitHub issue providers, the policy adds that the main assistant does not run raw `gh` for workflow operations; the operator runs workflow scripts and may fall back to raw `gh` internally. New issue flows stop at pending draft creation until the user explicitly approves provider issue creation. Cached issue body edits use cached `issue.md` projections before delegating write-back.
- For filesystem issue providers, the policy adds that workflow issues are local Markdown artifacts edited directly at the paths the operator returns; provider cache, write-back, and comment-append delegation does not apply.
- For other providers, the policy tells the main assistant to report any limitation when the operator cannot complete a provider operation, rather than reaching for provider-specific tools directly.
- Detailed authoring resolver and `NONE` convention behavior are not injected into main-session context. Provider-specific operator command aliases are injected only into `workflow-operator` subagent context.
- The hook always exits `0`.

## UserPromptSubmit

`UserPromptSubmit` caches issue references and injects terse commit guidance.

Behavior:

- Scans the submitted prompt for same-repository issue references such as `#45`, `owner/repo#45`, and matching GitHub issue URLs.
- Reads each detected issue through the workflow provider read path with the default cache policy.
- Uses existing cache projections on cache hits; fetches provider data and writes the cache on misses.
- Emits concise `additionalContext` only for issue numbers not already announced in the current session.
- When the prompt asks for a commit, injects the main-assistant commit guidance from `../agents/workflow-main-context/commit-prefix.md` at most once per session.
- For Codex subagent sessions, emits nothing. The main session owns workflow prompt context.
- Reports project-relative issue cache paths, for example `.workflow-cache/issues/45/`.
- For issue-cache context, emits nothing for missing issue references or provider read failures.
- Emits nothing for non-workflow projects or unsupported issue providers.

## Stop

`Stop` is intentionally silent.

Behavior:

- Does not read providers or write issue cache projections.
- Emits no JSON output; `Stop` output is reserved for host-supported block decisions.
- Skips when `stop_hook_active` is true to avoid hook loops.
- Emits nothing for clean no-op cases and never blocks the stop flow.

## Manifests

- `hooks.json` is the Claude hook manifest; all event commands invoke `../scripts/hook_claude.py` through `uv run --script`.
- `hooks.codex.json` is referenced by `../.codex-plugin/plugin.json`; all event commands invoke `../scripts/hook_codex.py` through `uv run --script`.
- Hook entrypoints use inline script dependencies so hook-imported workflow modules can use `python-frontmatter` for Markdown frontmatter and `PyYAML` for `.workflow/config.yml` without relying on a host-global Python environment.
