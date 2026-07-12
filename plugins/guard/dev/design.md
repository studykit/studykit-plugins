# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py`) is the truth for control flow — this file records *why* the
design is shaped this way and the runtime facts verified against the real CLI, not a
line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Update approval state. Ignores `/guard:settings` / `/guard:judge`. |
| `UserPromptExpansion` (matcher `^(guard:)?judge$`) | `verify` | On demand, dispatch the guardian for the last completed turn (`pending_verify_prompt_id`). |
| `PreToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `gate` | Stop unapproved file edits — `ask` (default) escalates to the permission prompt, `deny` blocks the call (`edit_gate`). |
| `PostToolUse` (matcher `ExitPlanMode`) | `plan-approved` | On plan approval, arm the gate when the plan defers no in-scope work. |
| `PostToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `gate-approved` | `edit_gate` ask only: after the user approves an edit's permission prompt, arm the session for the rest of the task. |
| (called via Bash, not a hook) | `record-verified` | Guardian appends a passed turn's claims to the verified store. |
| (called via Bash, not a hook) | `settings` | `guard:settings` skill (forked) shows/sets guard.local.json settings; `edit_gate`/`judge_gate` also apply to the live session's `state/<sid>.json` (session id from `--session`/`CLAUDE_CODE_SESSION_ID`). Every other key preserved; never `exempt_skills`. |
| (called via Bash, not a hook) | `exempt` | `guard:settings` skill records the user's confirmed `exempt_skills` selection (that key only). |
| `Stop` | `stop` | manual: record pending target, no audit. subagent: dispatch guardian. headless: in-hook judge that blocks. |
| `SessionStart` | `session-start` | Age-sweep state/sessions/verified/turns; export `GUARD_REFS_DIR` (resolved refs dir) via `$CLAUDE_ENV_FILE`. |
| (called via Bash, not a hook) | `refs-dir` | Print the resolved refs directory (guardian fallback; applies `refs_dir` validation). |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no turn buffer of its own; at
Stop it reconstructs the turn from Claude Code's transcript, sliced by `prompt_id`.

- `state/<sid>.json` — `{edit_gate, approved, judge_gate, last_audited_prompt_id, gated_prompt_id, asked_prompt_id, pending_verify_prompt_id, updated_at}`.
- `sessions/<sid>.jsonl` — full session archive, one line per user/assistant/gate/judge record.
- `turns/<sid>/<prompt_id>.json` — **subagent and manual modes**: the turn slice guard
  cut from the transcript (`{user, tools[], assistant}`) and hands to the `guardian`
  subagent, so guardian reads one turn, not the whole transcript. Subagent mode dispatches
  immediately; manual mode leaves it for `/guard:judge` (targeting
  `pending_verify_prompt_id`). Headless mode judges in-process and writes no turn file.
- `verified/<sid>.jsonl` — supported claims from PASSED turns only (`{ts, turn, claim,
  evidence}`, `turn` = prompt_id), replayed to later Stops as a VERIFIED_FACTS block
  so an established fact isn't re-derived. Only passed turns contribute, so a
  blocked/unsupported claim never becomes "verified".
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

State survives session end (a resumed `claude --resume` must keep its flags);
age-based `SessionStart` sweep is the only reaper. There is no SessionEnd hook.

## Verified runtime facts (confirmed against the CLI / real payloads; do not regress)

Re-verify before changing anything that depends on these — they came from real
payloads, not memory.

- **`CLAUDE_ENV_FILE`** — SessionStart hooks receive this env var (a file path);
  `export` lines appended to that file reach all subsequent Bash commands. Source:
  official hooks docs (https://code.claude.com/docs/en/hooks, "CLAUDE_ENV_FILE"),
  fetched 2026-07-09 — docs-verified only, not yet observed on a live session; if
  `GUARD_REFS_DIR` fails to appear, re-check this first.

- **`prompt_id` is common to every hook** (PreToolUse and Stop included) and equals
  the transcript record's `promptId` — this is what lets the gate's `gated_prompt_id`
  match the same turn's Stop. Observed on real payloads (seen on Claude Code 2.1.197;
  needs ≥ 2.1.196); the hook input schema is in the official hooks docs
  (https://code.claude.com/docs/en/hooks). Re-verify against those docs and a live Stop
  payload before relying on this.
- **Transcript slice.** The anchor record has `promptId == prompt_id` (a typed prompt:
  `origin={"kind":"human"}` + str content). Derived records — assistant text,
  tool_use/tool_result — have `promptId=None` and stay in the slice; the slice ends at
  the next different non-empty promptId. `isMeta:true` records (guard's own feedback)
  are skipped. `_read_turn_from_transcript(path, prompt_id)` is unit-testable on a
  fixture JSONL.
- **A background-agent completion opens its own transcript turn** (`origin.kind ==
  "task-notification"`, `promptSource: "system"`, NOT `isMeta`; verified 2.1.197). In
  subagent mode this would loop — the guardian dispatch is itself a background task, so
  its completion re-dispatches the guardian. `cmd_stop` skips these
  (`skip_task_notification`) from BOTH archive and judge. Ordering that must not
  regress: the skip precedes `_append_log`, and `_append_log` stays ahead of the
  `stop_hook_active` check (so a corrected response after a headless block is still
  archived).
- **A Stop hook may inject `additionalContext` without `decision`** and the
  conversation continues — the subagent-dispatch mechanism. `stop_hook_active: true`
  ⇒ guard already blocked this turn, so Stop returns at once.
- **`PostToolUse(ExitPlanMode)` fires only on plan approval.** Verified against live
  payloads (probe on Claude Code 2.1.x): approving a plan fires BOTH `PreToolUse` and
  `PostToolUse`; rejecting it ("Denied by user") fires `PreToolUse` only — consistent
  with the hooks doc rule that a blocked/denied tool produces no PostToolUse
  (https://code.claude.com/docs/en/hooks). The plan text rides in `tool_input.plan`
  on both payloads (and `tool_response.plan` on Post); `prompt_id` is common to both;
  on approval `permission_mode` transitions `plan → acceptEdits`. This is what lets
  `cmd_plan_approved` treat its own invocation as a genuine user approval — the model
  authors the plan but cannot approve its own tool call. Re-verify against a live
  payload before relying on it.
- **A forked skill can reach the pre-fork session id** — the load-bearing fact behind
  `guard:settings` (`context: fork`) writing the live session's `state/<sid>.json`.
  `${CLAUDE_SESSION_ID}` is a skill-content *substitution* expanded in the parent (per the
  skills docs, https://code.claude.com/docs/en/skills, "string substitution"), so the real
  id is baked into the fork's prompt; and `CLAUDE_CODE_SESSION_ID` is an env var inherited
  by subagents (observed 2026-07-10: a spawned subagent reported the same
  `CLAUDE_CODE_SESSION_ID` as its parent, the session UUID). `CLAUDE_SESSION_ID` is only
  the substitution token, NOT a process env var — `printenv CLAUDE_SESSION_ID` is empty in
  both parent and subagent, so the CLI must read `CLAUDE_CODE_SESSION_ID`, and the skill
  passes `--session ${CLAUDE_SESSION_ID}`. For the main session this id equals the hook
  payload's `session_id` that state is keyed on (one id per session; not separately
  probed against a live payload here). `cmd_settings` writes `guard.local.json` (that key
  only) plus, for `edit_gate`/`judge_gate`, the session state; it runs only from the
  user-invoked (`disable-model-invocation`) skill, which the model cannot trigger.

## Design invariants (why, not how)

- **Always exit 0; fail open.** Blocking is a decision payload on stdout, never a
  non-zero exit. Any judge failure (missing binary, timeout, unparseable output)
  leaves state untouched and does not block — guard must never harass the user
  because its own machinery broke.
- **Approval is armed only by a user action**, never by the model. Three paths, all
  requiring the user: (1) a **user message** on an explicit-implementation verdict from
  the classifier; (2) the user **approving a plan** via ExitPlanMode, where
  `cmd_plan_approved` (PostToolUse, which fires only on approval — see Verified facts)
  arms the gate *only if* the approved plan defers no in-scope work (`PLAN_DEFER_SYSTEM`
  judge); (3) in `edit_gate` ask, the user **approving an edit's permission prompt**,
  where `cmd_gate_approved` (PostToolUse, which fires only after the tool executed — i.e.
  the user clicked approve) arms the session for the rest of the task. The model authors
  the plan and issues the edit but can approve neither its own tool call nor its own
  permission prompt, so all three are genuine user actions; a deferring plan does not
  arm, and a judge failure never arms (fail toward the closed gate — the opposite of the
  evidence judge's fail-open).
  The `settings` skill (it sets `edit_gate`/`judge_gate`, never `approved`) and the model
  cannot arm it by either path. The
  classifier sees the tail of the session archive as conversation context
  (`_recent_dialogue`) — used only to resolve what the message refers to, so a bare
  "go ahead" arms only when it answers a proposed plan; context alone can never
  arm or revoke. It is
  **revoked only when the user clearly starts an unrelated new task**
  (`starts_unrelated_task`) — NOT on questions, refinements, corrections, or
  continuations of the current work, so a mid-implementation question doesn't re-lock
  the gate. The two axes are mutually exclusive; the dispatcher resolves defensively
  (`if explicit: approved=True elif starts_unrelated_task: approved=False`).
- **Two independent settings.** Session `edit_gate` governs ONLY the approval gate
  (gate + classifier + plan-approval early-return when `off`); the evidence judge has no
  setting of its own — `judge_gate` is its control, and `manual` is its practical off
  (Stop archives the turn and records the pending target, but spawns no judge).
  `/guard:settings` sets `edit_gate` and `judge_gate` (writing the config key and, with a
  session id, the live session state). Neither setting touches the other's feature.
- **Control turns and exempt commands are never judged.** `/guard:settings` and
  `/guard:judge` are skipped on BOTH sides: the approval classifier skips them at
  UserPromptSubmit (`_CONTROL_CMD_RE` on the raw prompt), and `cmd_stop` skips them via
  `command_name` (extracted from the transcript's expanded
  `<command-name>/guard:settings</command-name>`). This second skip is load-bearing — a
  control turn's response is a one-line relay ("guard on") with no evidence, and
  without it the Stop judge falsely blocked it (session b30dbaec). The same
  `command_name` path skips any skill / slash command the user lists in
  `exempt_skills` — named with its plugin namespace (`plugin:skill`), since a
  user-invoked skill reaches the transcript as a namespaced `<command-name>` just like
  a command (skill output is not a body of technical claims to ground). Both modes
  honor it (checked before the `judge_gate` branch).
- **Three modes, one criteria.** `judge_gate` selects only *how/when* the Stop audit runs —
  `manual` (default; no auto-audit, `/guard:judge` dispatches on demand), `subagent`
  (dispatch guardian each turn), or `headless` (in-hook judge that blocks). The two-axis
  criteria are identical across all three, and `guardian.md` mirrors them in prose. Bad
  `judge_gate` → the default (`manual`, via `_judge_gate`). `cmd_settings` sets it (the config
  key and, with a session id, the live session state).
  The approval gate is independent of `judge_gate` (governed by `edit_gate`), so `manual`
  narrows auto-verification without weakening the gate.
- **Manual mode + on-demand verify.** manual-mode Stop archives the turn, writes its
  slice (shared `_write_turn_slice`), and records `pending_verify_prompt_id` — then emits
  nothing. `/guard:judge` (`cmd_verify`, UserPromptExpansion) reads that pending target's
  slice off disk and emits the same guardian-dispatch context as subagent Stop
  (`_guardian_dispatch_context`), so it needs no transcript access. `/guard:judge` is a
  control command (in `_CONTROL_CMD_RE`), so its own turn is skipped and never becomes the
  pending target.
- **Judge once per turn.** headless relies on the payload's `stop_hook_active`;
  subagent (which never blocks, so that flag won't be set on the next Stop) instead
  guards on `last_audited_prompt_id == prompt_id`. manual writes no dispatch, so it needs
  no once-guard.
- **Verified facts flow forward through a single writer.** Both modes append via the
  dispatcher (`record-verified` for guardian, direct for headless) — never a parallel
  writer. This is the one intentional break from per-turn isolation, and only passed,
  evidence-backed claims cross the boundary, never raw prior-turn text.
- **Assistant tool output is first-class evidence** (rendered as TOOL_ACTIVITY) — a
  claim that restates or follows from a command's output there is supported without a
  re-cite. **User-run `!` commands are NOT evidence and their turn is not judged.** A
  `!` command inherits the preceding typed prompt's promptId, so its output records
  land in the slice *after* the response guard already judged — the evidence would
  arrive later than the claims it supports, and cannot be judged coherently in that
  turn. `_read_turn_from_transcript` flags the turn (`has_user_command`) and `cmd_stop`
  skips it (`skip_user_command`); the `!` records are never collected or rendered.
- **The gate runs no judge** (so PreToolUse stays fast); its only subprocess is at most
  one `git check-ignore` for exemption 3 below (5s timeout, fail-toward-gating). It
  gates only `MUTATING_TOOLS`; Bash and reads/searches always pass.
- **Three exemptions, all narrow.** The gate lets an unapproved write through only when:
  1. **refs dir** — the target resolves inside the refs directory: `.claude/guard/refs/`
     by default, or the `refs_dir` config path (the Grounded output style tells the
     assistant to save cited docs there — guard must not forbid its own required
     behavior). Both paths `resolve()`d so `..` can't escape. `_refs_dir` honors a
     configured value only when it resolves strictly inside the project and outside
     guard's own config/state — this exemption is checked before the guard-owned
     exclusion, so an unvalidated `refs_dir` of `.claude/guard` or `.` would let the
     model self-arm or exempt every project write.
  2. **outside the project dir** (`_is_outside_project`) — not under `CLAUDE_PROJECT_DIR`
     (e.g. the session scratchpad under `/private/tmp`). Not project source, and Bash
     can already write there ungated, so gating the file-edit tools is pure friction.
     `git check-ignore` can't classify an out-of-repo path, so this is a separate check
     (and skips the subprocess).
  3. **git-ignored** inside the repo — `git check-ignore` reports the target ignored:
     scratch/temp, local config (`**/*.local.*`), skill-authored docs (`/handoff` →
     `.handover/`). Honors the global gitignore too.
  **Guard's own config + state are excluded from exemptions 2–3**
  (`_is_guard_owned`): `.claude/guard/` is itself git-ignored, so without this the model
  could `Write` `state/<sid>.json` to arm its own approval or edit `guard.local.json`
  to disable the judge / change `judge_gate`. refs/ is the one deliberate hole and is
  checked first. Failing to resolve a path ⇒ treated as guard-owned (no exemption).
  (`exempt_skills` is edited only via the `exempt` CLI — that one key, never
  `edit_gate`/`judge_gate`/state — so it can narrow the judge's coverage but not disable
  the gate.)
- **Gated turns aren't audited (deny only).** A gate *denial* records `gated_prompt_id`;
  Stop skips that turn (its response is a plan/approval request, not claims to ground). A
  new turn has a new prompt_id, so the flag self-expires. An `ask` escalation records
  `asked_prompt_id` instead and does **not** set `gated_prompt_id`: an approved ask lets
  the edit happen, so the turn carries real work the judge should still audit. `ask`
  arming (`cmd_gate_approved`) keys on that marker — only an edit the gate actually asked
  about arms approval, so an exempt write (refs/gitignored/outside) succeeding while
  unapproved never arms.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. Both gate fields are `enum.StrEnum`
members (`EditGate`, `JudgeGate`) — the reason guard requires Python 3.11+ (`StrEnum`
"Added in version 3.11": https://docs.python.org/3/library/enum.html, excerpt saved at
`docs/refs/python-strenum.md`). Keys: `model`
(default `"haiku"`), `effort` (low/medium/high/xhigh/max, default `"medium"`), `edit_gate`
(`"ask"`|`"deny"`|`"off"`, default `"ask"` — the approval gate: `off` disables it, `ask`
escalates an unapproved edit to the permission prompt and arms the session on approval,
`deny` blocks the call for the plan→approve workflow), `judge_gate`
(`"manual"`|`"subagent"`|`"headless"`, default
`"manual"` — the evidence judge's control; `manual` is its practical off), `exempt_skills`
(list of strings, default `[]`) — skills / slash commands whose turn the Stop judge
skips, named with their plugin namespace (`plugin:skill`, e.g. `guard:settings`) or bare
for un-namespaced skills, matched leading-`/`-stripped and case-insensitively (guard's
own `settings`/`judge` control commands are always exempt regardless). Manage
`exempt_skills` interactively with the `guard:settings` skill (which records the user's
chosen names via the `exempt` CLI); no need to hand-edit. `refs_dir`
(string, default `""`) — project-relative directory for the Grounded style's cited-doc
copies; empty = the git-ignored `.claude/guard/refs/`, a tracked path (e.g.
`"docs/refs"`) keeps the collected references under git; commits stay in the user's
normal workflow (guard never commits). `_refs_dir` validates the value (see the refs
exemption above) and everything that names the location follows it: the gate
exemption, the headless judge prompt (`__REFS_DIR__` substitution), the guardian
dispatch inputs (`refs_dir`, with the `refs-dir` CLI subcommand as its fallback), and
the output style (which reads `GUARD_REFS_DIR` — exported by the SessionStart hook via
`$CLAUDE_ENV_FILE`, per the official hooks docs — before its first save). Only keys whose value matches the
default's type are honored (a malformed value can't flip a flag); unknown keys ignored;
missing/malformed file → all defaults. `guard.local.json.example`
ships at the plugin root. The judge always reads the repo (`--allowedTools
Read,Grep,Glob,Bash`, no `--disallowedTools` — room to extend, e.g. a verification
artifact); isolation comes from `--safe-mode` + `--no-session-persistence`, not from
withholding tools.

## Manual testing

Drive subcommands with synthetic payloads and `GUARD_TRACE=1`. Because `stop` reads
the turn from a transcript, build a small fixture JSONL and pass its path +
`prompt_id`:

```bash
export CLAUDE_PROJECT_DIR=/tmp/guard-test/proj
export CLAUDE_PLUGIN_ROOT=/path/to/plugins/guard
export GUARD_TRACE=1
H="$CLAUDE_PLUGIN_ROOT/scripts/guard_hook.py"

# fixture transcript: typed prompt (anchor p1) + assistant reply
T=/tmp/guard-test/tx.jsonl
printf '%s\n' \
  '{"promptId":"p1","origin":{"kind":"human"},"message":{"role":"user","content":"is redis faster?"}}' \
  '{"promptId":null,"message":{"role":"assistant","content":[{"type":"text","text":"Redis is always faster than Postgres."}]}}' > "$T"

# show/change settings (deterministic CLI; no payload — session id from --session or
# CLAUDE_CODE_SESSION_ID, project dir from CLAUDE_PROJECT_DIR). set writes guard.local.json
# and, for edit_gate/judge_gate, state/<sid>.json.
"$H" settings show --session s1
"$H" settings set edit_gate off --session s1

# headless judge on the turn (real claude; unsupported claim -> block)
"$H" settings set judge_gate headless --session s1
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p1\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"Redis is always faster than Postgres.\",\"stop_hook_active\":false}" | "$H" stop

# gate, default edit_gate "ask": emits permissionDecision "ask" + records asked_prompt_id.
# The matching PostToolUse (user approved the prompt) arms the session's approval.
echo '{"session_id":"s1","prompt_id":"pA","tool_name":"Write","tool_input":{"file_path":"x"}}' | "$H" gate
echo '{"session_id":"s1","prompt_id":"pA","tool_name":"Write","tool_input":{"file_path":"x"}}' | "$H" gate-approved

# edit_gate "deny": emits permissionDecision "deny" + records gated_prompt_id (same-prompt_id Stop is then skipped).
printf '{"edit_gate":"deny"}\n' > "$CLAUDE_PROJECT_DIR/.claude/guard.local.json"
echo '{"session_id":"s2","prompt_id":"pG","tool_name":"Write","tool_input":{"file_path":"x"}}' | "$H" gate

# subagent mode: Stop slices the turn to a file + injects a dispatch (no `decision`)
"$H" settings set judge_gate subagent --session s1
echo '{"session_id":"s1","prompt_id":"p1","claims":[{"claim":"x","evidence":"y"}]}' | "$H" record-verified
```

`gate`, `settings`, subagent `stop`, `record-verified`, and session
subcommands are deterministic (no CLI/auth). Headless `stop` and `user-prompt` spawn a
real `claude`. Unit-test the slice directly:
`_read_turn_from_transcript(path, prompt_id)` on a fixture JSONL.
