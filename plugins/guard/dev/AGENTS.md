# guard — contributor notes

Design and runtime internals for the `guard` plugin. End-user docs live in
`../README.md`; keep user-facing surface there and implementation detail here.

## Purpose

Two independent capabilities, both expressed through hooks over a single stdlib
dispatcher (`scripts/guard_hook.py`):

1. **Evidence judge** (Stop) — a single repo-reading judge that blocks a turn on
   any of three grounds: (a) a load-bearing technical claim stated as fact without
   adequate evidence; (b) a claim backed only by a *surface signal* — reasoning
   from a function/variable/type name, comment, filename, or docstring without
   reading the body, or built on an earlier unverified assumption; (c) an
   *unjustified deferral* — punting as "open question / TBD / deferred / needs
   investigation / 결정 안 됨" on something the repository could answer. Genuine
   human product/policy decisions are left alone. All three are one `run_judge`
   call (EVIDENCE_SYSTEM / EVIDENCE_SCHEMA: `claims[]` + `deferrals[]`).
2. **Approval gate** — block file mutation until the user explicitly approves
   implementation.

Claude Code only. The judge relies on the `claude` CLI and Claude-specific hook
payload fields; there is no Codex path.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Open a new turn record; update approval state. Ignores `/guard:turn`. |
| `UserPromptExpansion` (matcher `(guard:)?turn`) | `toggle` | Flip the session `enabled` flag (judge + gate). |
| `PreToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `gate` | Deny file-editing tools until approved. |
| `PostToolUse` (all tools) | `post-tool` | Record the tool's command + output into the current turn (evidence). |
| `Stop` | `stop` | Close the turn record; run the evidence judge over the whole turn when armed; write a verdict line. |
| `SessionStart` | `session-start` | Sweep state/sessions/turns/verdicts past retention. |

## Storage layout

Project-local under `${CLAUDE_PROJECT_DIR}/.claude/guard/`:

- `state/<sid>.json` — `{enabled, approved, turn_seq, updated_at}` (atomic write).
- `sessions/<sid>.jsonl` — full session archive: one line per user/assistant/gate/judge record.
- `turns/<sid>/<seq>.json` — one file per turn: `{seq, user, tools[], assistant}`,
  built across UserPromptSubmit → PostToolUse(s) → Stop. This is what the Stop
  judge reads, so a claim grounded in a command's output is evidence, not a
  transcript re-parse.
- `verdicts/<sid>.jsonl` — verification record: one line per judged turn
  (`turn`, `blocked`, `summary`, `unsupported_claims`, `resolvable_deferrals`).
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

`turn_seq` increments on each real user turn; `/guard:turn` control commands do
not bump it or create a turn record.

## Verified runtime facts (do not regress)

These were confirmed against the installed CLI / real payloads, not memory. If you
change behavior that depends on them, re-verify against the current runtime.

- **Stop payload** carries `last_assistant_message` (final response text) and
  `stop_hook_active` (bool). Confirmed in the CLI changelog and against
  `spectrack/hooks/scripts/hook_claude.py`. The Stop subcommand reads the response
  from `last_assistant_message`; it does **not** parse the transcript.
- **`stop_hook_active: true`** means guard already blocked once this turn — the
  Stop subcommand returns immediately to avoid a block loop.
- **UserPromptSubmit** carries the user's text in `prompt`.
- **UserPromptExpansion** fires on a skill/command invocation with `command_name`,
  `command_source`, and the raw `prompt`. The matcher runs against `command_name`.
  For a plugin skill the name is **namespaced**: invoking `/guard:turn` sends
  `command_name = "guard:turn"` (verified empirically with `--plugin-dir`), NOT the
  bare `turn`. A project-level skill would send the bare name. So the matcher is
  `(guard:)?turn` to catch both. Detecting the toggle here (not in UserPromptSubmit)
  is required — UserPromptSubmit is not a reliable place to hook skill invocations.
- **UserPromptExpansion `additionalContext`** is delivered to the model (verified:
  a `hookSpecificOutput.additionalContext` string surfaces as a
  `<system-reminder>` in the model's context). That is how the `turn` toggle's
  armed/disarmed confirmation reaches the user-facing turn.
- **Judge isolation**: the judge runs `claude -p --safe-mode`. `--safe-mode`
  disables hooks/plugins/MCP/skills/output-styles in the child while keeping auth,
  model, and built-in tools working — this is what prevents the child from
  re-triggering guard's own Stop hook (infinite recursion). `--bare` was rejected
  because it forces `ANTHROPIC_API_KEY`/`apiKeyHelper` auth and would break OAuth
  users.
- **Structured output**: with `--json-schema`, the JSON envelope
  (`--output-format json`) exposes the parsed object in `structured_output`;
  `_parse_judge_output` prefers it and falls back to parsing the `result` string
  (stripping code fences).

## Output style

`output-styles/evidence-first.md` sets `force-for-plugin: true` (verified against
the official output-styles docs). This auto-applies the style whenever guard is
enabled and **overrides the user's `outputStyle` setting** — no manual `/config`
selection needed. If several enabled plugins force a style, Claude Code uses the
first loaded. No `plugin.json` field is required; the `output-styles/` directory
location is sufficient for discovery.

## Dispatcher invariants (`scripts/guard_hook.py`)

- stdlib only; executed via shebang (no `uv run`). Keep it dependency-free.
- **Always exit 0.** Blocking is expressed via decision payloads on stdout, never
  via non-zero exit.
- **Fail open.** Any judge failure (missing binary, timeout, non-zero exit,
  unparseable output) returns `None` and the caller leaves state untouched / does
  not block. guard must never harass the user because its own machinery broke.
- **Approval can only be armed by a user message.** `cmd_user_prompt` is the only
  writer that sets `approved = True`, and only on an explicit-implementation
  verdict. The `turn` skill and the model cannot arm approval.
- Approval/discussion are mutually exclusive in the classifier prompt; the
  dispatcher still resolves defensively (`if explicit: approved=True elif
  opens_new: approved=False`).
- One master switch: the session `enabled` flag gates BOTH the evidence judge
  (Stop) and the approval gate (UserPromptSubmit + PreToolUse). `turn` flips it;
  its session-start default is the config `enabled` key. When off, `cmd_gate`,
  `cmd_stop`, and the approval-classifier in `cmd_user_prompt` all early-return.
- `turn` only flips `enabled` (a persistent session toggle) — it does not touch
  the judge's per-turn logic. `/guard:turn` is also skipped by `cmd_user_prompt`
  (via `_TURN_CMD_RE`) so it neither opens a turn nor is judged.
- Command output is evidence: the turn record (`turns/<sid>/<seq>.json`) is
  assembled across UserPromptSubmit (user) → PostToolUse (each command + output) →
  Stop (assistant). At Stop the judge is handed the whole turn via
  `_render_turn_for_judge` (USER_REQUEST + TOOL_ACTIVITY + ASSISTANT_RESPONSE), and
  EVIDENCE_SYSTEM treats TOOL_ACTIVITY as first-class evidence. This is why a claim
  grounded in a command the assistant ran (e.g. `source-analyzer repos`) is not
  judged unsupported — `last_assistant_message` alone would omit that output.
- The gate reads state only (no judge call) so PreToolUse stays fast and
  deterministic. It gates only the file-editing tools in `MUTATING_TOOLS`
  (Write/Edit/MultiEdit/NotebookEdit). Bash is intentionally NOT gated — shell
  commands, reads, and searches always pass.
- Retention: `SessionStart` sweeps `state/`, `sessions/`, `verdicts/` (files) and
  `turns/` (whole per-session dirs) older than `ORPHAN_MAX_AGE_SECONDS` (7 days).
  Nothing is cleared at SessionEnd — a resumed session (`claude --resume`) must
  keep its `enabled`/`approved`/`turn_seq` state, so age-based expiry is the only
  reaper. There is no SessionEnd hook.

## Config (`.claude/guard.local.json`)

JSON object parsed by `_load_config`. Keys: `model` (str, default `"haiku"`),
`effort` (str, one of low/medium/high/xhigh/max, default `"medium"` — validated by
`_effort`, bad values fall back to medium), and `enabled` (bool, default `true` —
session-start default of the master switch for the evidence judge + approval gate). Only keys in `DEFAULT_CONFIG` whose value
matches the default's type are honored (so a malformed value can't flip a flag);
unknown keys ignored; missing/malformed file → all defaults. A
`guard.local.json.example` template ships at the plugin root.

The judge always reads the repo: `run_judge` passes `--allowedTools
Read,Grep,Glob,Bash` and no `--disallowedTools` (leaving room to extend the judge,
e.g. writing a verification artifact). Isolation comes from `--safe-mode` +
`--no-session-persistence`, not from withholding tools.

## Manual testing

Drive subcommands directly with synthetic payloads and `GUARD_TRACE=1`:

```bash
export CLAUDE_PROJECT_DIR=/tmp/guard-test/proj
export CLAUDE_PLUGIN_ROOT=/path/to/plugins/guard
export GUARD_TRACE=1
H="$CLAUDE_PLUGIN_ROOT/scripts/guard_hook.py"

# gate denies a mutating tool before approval
echo '{"session_id":"s1","tool_name":"Write","tool_input":{"file_path":"x"}}' | "$H" gate

# arm the judge, then block an unsupported claim
echo '{"session_id":"s1","prompt":"/guard:turn on"}' | "$H" toggle
echo '{"session_id":"s1","last_assistant_message":"Redis is always faster than Postgres.","stop_hook_active":false}' | "$H" stop
```

The `user-prompt` and `stop` subcommands spawn a real `claude` judge, so they need
a working CLI and network/auth. The `gate`, `toggle`, and session subcommands are
deterministic and need neither.
