# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. The always-loaded summary and the non-negotiable runtime facts live
in `../AGENTS.md`. The source (`scripts/guard_hook.py`) is the truth for control flow
— this file records *why* the design is shaped this way, not a line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Update approval state. Ignores `/guard:turn` / `/guard:mode`. |
| `UserPromptExpansion` (matcher `(guard:)?turn`) | `toggle` | Flip session `enabled` (judge + gate). |
| `UserPromptExpansion` (matcher `(guard:)?mode`) | `set-mode` | Set session `mode` (`headless`\|`subagent`). |
| `PreToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `gate` | Deny file edits until approved. |
| (called via Bash, not a hook) | `record-verified` | Guardian appends a passed turn's claims to the verified store. |
| `Stop` | `stop` | Audit the turn (headless judge / subagent dispatch). |
| `SessionStart` | `session-start` | Age-sweep state/sessions/verified/turns. |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no turn buffer of its own; at
Stop it reconstructs the turn from Claude Code's transcript, sliced by `prompt_id`.

- `state/<sid>.json` — `{enabled, approved, mode, last_audited_prompt_id, gated_prompt_id, updated_at}`.
- `sessions/<sid>.jsonl` — full session archive, one line per user/assistant/gate/judge record.
- `turns/<sid>/<prompt_id>.json` — **subagent mode only**: the turn slice guard cut
  from the transcript (`{user, tools[], assistant}`) and hands to the `guardian`
  subagent, so guardian reads one turn, not the whole transcript. Headless mode judges
  in-process and writes no turn file.
- `verified/<sid>.jsonl` — supported claims from PASSED turns only (`{ts, turn, claim,
  evidence}`, `turn` = prompt_id), replayed to later Stops as a VERIFIED_FACTS block
  so an established fact isn't re-derived. Only passed turns contribute, so a
  blocked/unsupported claim never becomes "verified".
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

State survives session end (a resumed `claude --resume` must keep its flags);
age-based `SessionStart` sweep is the only reaper. There is no SessionEnd hook.

## Design invariants (why, not how)

- **Always exit 0; fail open.** Blocking is a decision payload on stdout, never a
  non-zero exit. Any judge failure (missing binary, timeout, unparseable output)
  leaves state untouched and does not block — guard must never harass the user
  because its own machinery broke.
- **Approval is armed only by a user message**, only on an explicit-implementation
  verdict from the classifier. The `turn` skill and the model cannot arm it.
  Approval/discussion are mutually exclusive; the dispatcher still resolves
  defensively (`if explicit: approved=True elif opens_new: approved=False`).
- **One master switch.** Session `enabled` gates BOTH the judge and the approval gate;
  when off, gate/stop/classifier all early-return. `turn` flips it (default from the
  config `enabled` key). `/guard:turn` and `/guard:mode` are skipped as turns (never
  opened, never judged).
- **Two modes, one criteria.** `mode` selects only *how* the Stop audit runs (in-hook
  judge that blocks vs. dispatch guardian); the two-axis criteria are identical, and
  `guardian.md` mirrors them in prose. Bad `mode` → `headless`. `set-mode` flips it,
  mirroring `toggle`.
- **Judge once per turn.** headless relies on the payload's `stop_hook_active`;
  subagent (which never blocks, so that flag won't be set on the next Stop) instead
  guards on `last_audited_prompt_id == prompt_id`.
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
- **The gate is state-only** (no judge call, so PreToolUse stays fast). It gates only
  `MUTATING_TOOLS`; Bash and reads/searches always pass.
- **Refs exemption.** The gate lets an unapproved write through only when the target
  resolves inside `.claude/guard/refs/` (the evidence-first style tells the assistant
  to save cited docs there — guard must not forbid its own required behavior). Scoped
  to `refs/` ONLY, never the wider `.claude/guard/` tree, so the model can't write
  `state/` to arm its own approval; both target and refs dir are `resolve()`d so `..`
  can't escape into `state/`.
- **Gated turns aren't audited.** A gate denial records `gated_prompt_id`; Stop skips
  that turn (its response is a plan/approval request, not claims to ground). A new
  turn has a new prompt_id, so the flag self-expires.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. Keys: `model` (default `"haiku"`),
`effort` (low/medium/high/xhigh/max, default `"medium"`), `enabled` (bool, default
`true`), `mode` (`"headless"`|`"subagent"`, default `"headless"`). Only keys whose
value matches the default's type are honored (a malformed value can't flip a flag);
unknown keys ignored; missing/malformed file → all defaults. `guard.local.json.example`
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
