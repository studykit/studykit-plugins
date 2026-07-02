# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py`) is the truth for control flow — this file records *why* the
design is shaped this way and the runtime facts verified against the real CLI, not a
line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Update approval state. Ignores `/guard:turn` / `/guard:mode` / `/guard:exempt`. |
| `UserPromptExpansion` (matcher `(guard:)?turn`) | `toggle` | Flip session `enabled` (judge + gate). |
| `UserPromptExpansion` (matcher `(guard:)?mode`) | `set-mode` | Set session `mode` (`manual`\|`subagent`\|`headless`). |
| `UserPromptExpansion` (matcher `(guard:)?verify`) | `verify` | On demand, dispatch the guardian for the last completed turn (`pending_verify_prompt_id`). |
| `PreToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `gate` | Deny file edits until approved. |
| (called via Bash, not a hook) | `record-verified` | Guardian appends a passed turn's claims to the verified store. |
| (called via Bash, not a hook) | `exempt` | `guard:exempt` skill records the user's confirmed `exempt_skills` selection (that key only). |
| `Stop` | `stop` | manual: record pending target, no audit. subagent: dispatch guardian. headless: in-hook judge that blocks. |
| `SessionStart` | `session-start` | Age-sweep state/sessions/verified/turns. |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no turn buffer of its own; at
Stop it reconstructs the turn from Claude Code's transcript, sliced by `prompt_id`.

- `state/<sid>.json` — `{enabled, approved, mode, last_audited_prompt_id, gated_prompt_id, pending_verify_prompt_id, updated_at}`.
- `sessions/<sid>.jsonl` — full session archive, one line per user/assistant/gate/judge record.
- `turns/<sid>/<prompt_id>.json` — **subagent and manual modes**: the turn slice guard
  cut from the transcript (`{user, tools[], assistant}`) and hands to the `guardian`
  subagent, so guardian reads one turn, not the whole transcript. Subagent mode dispatches
  immediately; manual mode leaves it for `/guard:verify` (targeting
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
- **`/guard:turn` and `/guard:mode` take a `--project` / `--global` scope flag.** No
  flag sets the live session (`toggle` / `set-mode` write `state/`); `--project` writes
  only the session-start default (`enabled` / `mode`) to `guard.local.json`, live
  session untouched; `--global` is reserved (reported unsupported). Safe despite writing
  config: these fire ONLY on a user-typed slash command via UserPromptExpansion, which
  the model cannot invoke. `_scope_of` parses the flag; `_write_config` edits only the
  one key.

## Design invariants (why, not how)

- **Always exit 0; fail open.** Blocking is a decision payload on stdout, never a
  non-zero exit. Any judge failure (missing binary, timeout, unparseable output)
  leaves state untouched and does not block — guard must never harass the user
  because its own machinery broke.
- **Approval is armed only by a user message**, only on an explicit-implementation
  verdict from the classifier. The `turn` skill and the model cannot arm it. It is
  **revoked only when the user clearly starts an unrelated new task**
  (`starts_unrelated_task`) — NOT on questions, refinements, corrections, or
  continuations of the current work, so a mid-implementation question doesn't re-lock
  the gate. The two axes are mutually exclusive; the dispatcher resolves defensively
  (`if explicit: approved=True elif starts_unrelated_task: approved=False`).
- **One master switch.** Session `enabled` gates BOTH the judge and the approval gate;
  when off, gate/stop/classifier all early-return. `turn` flips it (default from the
  config `enabled` key).
- **Control turns and exempt commands are never judged.** `/guard:turn` and
  `/guard:mode` are skipped on BOTH sides: the approval classifier skips them at
  UserPromptSubmit (`_CONTROL_CMD_RE` on the raw prompt), and `cmd_stop` skips them via
  `command_name` (extracted from the transcript's expanded
  `<command-name>/guard:turn</command-name>`). This second skip is load-bearing — a
  control turn's response is a one-line relay ("guard on") with no evidence, and
  without it the Stop judge falsely blocked it (session b30dbaec). The same
  `command_name` path skips any skill / slash command the user lists in
  `exempt_skills` — named with its plugin namespace (`plugin:skill`), since a
  user-invoked skill reaches the transcript as a namespaced `<command-name>` just like
  a command (skill output is not a body of technical claims to ground). Both modes
  honor it (checked before the `mode` branch).
- **Three modes, one criteria.** `mode` selects only *how/when* the Stop audit runs —
  `manual` (default; no auto-audit, `/guard:verify` dispatches on demand), `subagent`
  (dispatch guardian each turn), or `headless` (in-hook judge that blocks). The two-axis
  criteria are identical across all three, and `guardian.md` mirrors them in prose. Bad
  `mode` → the default (`manual`, via `_mode`). `set-mode` flips it, mirroring `toggle`.
  The approval gate is independent of `mode` (governed by `enabled`), so `manual` narrows
  auto-verification without weakening the gate.
- **Manual mode + on-demand verify.** manual-mode Stop archives the turn, writes its
  slice (shared `_write_turn_slice`), and records `pending_verify_prompt_id` — then emits
  nothing. `/guard:verify` (`cmd_verify`, UserPromptExpansion) reads that pending target's
  slice off disk and emits the same guardian-dispatch context as subagent Stop
  (`_guardian_dispatch_context`), so it needs no transcript access. `/guard:verify` is a
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
  1. **refs/** — the target resolves inside `.claude/guard/refs/` (the Grounded
     output style tells the assistant to save cited docs there — guard must not forbid its own
     required behavior). Both paths `resolve()`d so `..` can't escape.
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
  to disable the judge / change `mode`. refs/ is the one deliberate hole and is checked
  first. Failing to resolve a path ⇒ treated as guard-owned (no exemption). (`exempt_skills`
  is edited only via the `exempt` CLI — that one key, never `enabled`/`mode`/state — so
  it can narrow the judge's coverage but not disable the gate.)
- **Gated turns aren't audited.** A gate denial records `gated_prompt_id`; Stop skips
  that turn (its response is a plan/approval request, not claims to ground). A new
  turn has a new prompt_id, so the flag self-expires.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. Keys: `model` (default `"haiku"`),
`effort` (low/medium/high/xhigh/max, default `"medium"`), `enabled` (bool, default
`true`), `mode` (`"manual"`|`"subagent"`|`"headless"`, default `"manual"`), `exempt_skills`
(list of strings, default `[]`) — skills / slash commands whose turn the Stop judge
skips, named with their plugin namespace (`plugin:skill`, e.g. `guard:turn`) or bare
for un-namespaced skills, matched leading-`/`-stripped and case-insensitively (guard's
own `turn`/`mode`/`verify`/`exempt` control commands are always exempt regardless). Manage
`exempt_skills` interactively with the `guard:exempt` skill (lists session skills →
AskUserQuestion → records via the `exempt` CLI); no need to hand-edit. Only keys whose value matches the
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

# headless judge on the turn (real claude; unsupported claim -> block)
echo '{"session_id":"s1","prompt":"/guard:turn on"}' | "$H" toggle
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p1\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"Redis is always faster than Postgres.\",\"stop_hook_active\":false}" | "$H" stop

# gate records gated_prompt_id; a same-prompt_id Stop is then skipped
echo '{"session_id":"s1","prompt_id":"pG","tool_name":"Write","tool_input":{"file_path":"x"}}' | "$H" gate

# subagent mode: Stop slices the turn to a file + injects a dispatch (no `decision`)
echo '{"session_id":"s1","prompt":"/guard:mode subagent"}' | "$H" set-mode
echo '{"session_id":"s1","prompt_id":"p1","claims":[{"claim":"x","evidence":"y"}]}' | "$H" record-verified
```

`gate`, `toggle`, `set-mode`, subagent `stop`, `record-verified`, and session
subcommands are deterministic (no CLI/auth). Headless `stop` and `user-prompt` spawn a
real `claude`. Unit-test the slice directly:
`_read_turn_from_transcript(path, prompt_id)` on a fixture JSONL.
