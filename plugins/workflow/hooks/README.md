# plugins/workflow/hooks/

Workflow hooks dispatch through runtime-specific entry scripts. Both scripts
dispatch from the payload `hook_event_name` and own their runtime-specific
payload/env extraction. They call common plain functions from
`../scripts/workflow_hook.py` for shared workflow behavior such as policy
injection, provider cache projection protection, and issue-cache context.

The Codex manifest registers only `SessionStart` and `UserPromptSubmit`. Claude
also registers `PreToolUse` for provider cache projection protection and
repeated authoring-read notices, `PostToolUse` for main-session authoring read
tracking, and `SubagentStart` for spawned subagent identity tracking.

When either runtime script writes hook output to stdout, it writes JSON only.
Empty stdout is used for no-op hook runs.

## PreToolUse Write/Edit (Claude only)

`PreToolUse` on file writes protects provider cache issue body projections.

Behavior:

- Allows normal workflow artifact writes without hidden authoring read checks.
- Blocks provider cache issue body writes when the projection is missing.
- Blocks provider cache issue body writes that alter projection-owned YAML frontmatter.
- Emits nothing for non-workflow projects or safe body-only writes.

## PreToolUse Read (Claude only)

`PreToolUse` on `Read` notifies the main assistant when an authoring file was already read in the same session.

Behavior:

- Checks only main-assistant `Read` calls whose resolved file path is under `../authoring/`.
- Reads the unified session state file under `.workflow-cache/hook-state/`.
- Emits `additionalContext` when the same authoring file is already recorded in `authoring.read_files`.
- Does not block or modify the read.
- Emits nothing for the first read, subagents, non-workflow projects, non-authoring files, or clean no-op cases.

## PostToolUse Read (Claude only)

`PostToolUse` on `Read` records main-assistant authoring file reads.

Behavior:

- Records only successful main-assistant `Read` calls whose resolved file path is under `../authoring/`.
- Uses `../scripts/authoring_resolver.py` to classify authoring paths.
- Writes deduplicated `authoring.read_files` entries in the unified session state file under `.workflow-cache/hook-state/`.
- Stores each read entry as `path` plus `relative_path`; the hook matcher already identifies the tool.
- Emits nothing for subagents, non-workflow projects, non-authoring files, or clean no-op cases.

## SubagentStart (Claude only)

`SubagentStart` records spawned subagent identities in the main session state and injects a narrow workflow context block for the subagent.

Behavior:

- Records `agent_id` and `agent_type` for each spawned Claude subagent under `subagents.started` in the unified session state file.
- Deduplicates repeated records by `agent_id`.
- For workflow-configured projects, emits `additionalContext` built from `../main-context/subagent-policy.md`. The block tells the subagent that the main-session workflow shell environment is inherited and inlines the runtime launcher snippet from `../main-context/snippets/launcher/claude.md` plus the provider-specific issue-fetch snippet so the subagent knows which `*_issue_fetch.py` script to call.
- Does not inject the full main-session policy. Provider writes, knowledge-provider rules, and the on-demand `policy/` detail files stay main-session-only.
- Emits nothing for non-workflow projects.

## SessionStart

`SessionStart` injects workflow policy for configured projects.

Behavior:

- If the active project has no `.workflow/config.yml`, the hook emits nothing.
- Main-assistant SessionStart wording lives under `../main-context/`: the always-loaded entry point in `session-policy.md`, GitHub knowledge guidance in `knowledge/github.md`, and on-demand detail files under `policy/` (launcher, authoring, provider writes).
- The hook prepares a normalized shell environment contract for workflow shell commands: `WORKFLOW`, `WORKFLOW_PLUGIN_ROOT`, `WORKFLOW_PROJECT_DIR`, and `WORKFLOW_SESSION_ID`.
- Claude writes that contract to `CLAUDE_ENV_FILE` when Claude provides it for `SessionStart`, so the main session shell exports `$WORKFLOW` directly.
- Codex cannot persist environment variables from `SessionStart`; `hook_codex.py` records a unified session state file under `.workflow-cache/hook-state/`, keyed by the Codex hook `session_id`. The `../scripts/workflow` wrapper later reads that state and evaluates the generated exports from the shell-visible `CODEX_THREAD_ID`.
- If the active project has a valid `.workflow/config.yml`, the hook injects the main-session policy as `additionalContext`. The policy tells the main assistant to run workflow operations through the bundled launcher (Claude uses the persisted `$WORKFLOW` env contract; Codex uses the absolute launcher path inlined at SessionStart) and points at the on-demand `policy/` detail files. Template placeholders use `{{NAME}}` so they stay visually distinct from real shell variables. The hook resolves `{{WORKFLOW_POLICY_DIR}}` to the absolute path of `../main-context/policy/`, inlines the runtime-specific launcher snippet from `../main-context/snippets/launcher/<runtime>.md` as `{{WORKFLOW_LAUNCHER_BLOCK}}` (resolving `{{WORKFLOW_PLUGIN_ROOT}}` to the absolute plugin root in the Codex snippet), and inlines the provider-specific issue-fetch snippet as `{{WORKFLOW_ISSUE_FETCH_BLOCK}}`.
- In Codex subagent shells, `CODEX_THREAD_ID` is the subagent's own thread id and no parent-thread environment variable is available. For Codex subagent `SessionStart` payloads, `hook_codex.py` checks `transcript_path` for `session_meta` records that identify the spawned agent. When the hook can extract a parent thread id, it records the spawned subagent under the parent session state's `subagents.started` list and emits no `additionalContext`. If transcript metadata does not provide a distinct agent id, the subagent session id is used as `agent_id`.
- For Codex subagent SessionStart payloads without an extractable parent id, the hook emits nothing.
- Claude subagents do not receive the main-session policy; if Claude sends an agent-tagged `SessionStart` payload, the hook records environment and exits without injecting policy.
- For GitHub issue providers, the policy stays narrow: it tells the main assistant to run workflow scripts (`$WORKFLOW github_issue_*.py`) rather than raw `gh` for workflow operations, and to follow the publish/append/update body-file contract in `policy/provider-writes.md`.
- For filesystem issue providers, the policy stays narrow: workflow issues are local Markdown artifacts edited directly at the paths the resolver returns; the body-file contract still applies for any provider-backed writes.
- The hook always exits `0`.

## UserPromptSubmit

`UserPromptSubmit` caches issue references and injects terse commit guidance.

Behavior:

- Scans the submitted prompt for same-repository issue references such as `#45`, `owner/repo#45`, and matching GitHub issue URLs.
- Reads each detected issue through the workflow provider read path with the default cache policy.
- Uses existing cache projections on cache hits; fetches provider data and writes the cache on misses.
- Emits concise `additionalContext` only for issue numbers not already announced in the current session.
- When the prompt asks for a commit, injects the main-assistant commit guidance from `../main-context/commit-prefix.md` at most once per session.
- For Codex subagent sessions, emits nothing. The main session owns workflow prompt context.
- Reports project-relative issue cache paths, for example `.workflow-cache/issues/45/`.
- For issue-cache context, emits nothing for missing issue references or provider read failures.
- Emits nothing for non-workflow projects or unsupported issue providers.

## Stop

`Stop` is intentionally silent when invoked directly through a runtime adapter.
Neither plugin manifest registers `Stop` because workflow has no stop-time
behavior.

Behavior:

- Does not read providers or write issue cache projections.
- Emits no JSON output; `Stop` output is reserved for host-supported block decisions.
- Does not continue or block the stop flow.
- Emits nothing for clean no-op cases and never blocks the stop flow.

## Manifests

- `hooks.json` is the Claude hook manifest; all event commands invoke `../scripts/hook_claude.py` through `uv run --script`.
- `hooks.codex.json` is referenced by `../.codex-plugin/plugin.json`; all event commands invoke `../scripts/hook_codex.py` through `uv run --script`.
- Hook entrypoints use inline script dependencies so hook-imported workflow modules can use `python-frontmatter` for Markdown frontmatter and `PyYAML` for `.workflow/config.yml` without relying on a host-global Python environment.
