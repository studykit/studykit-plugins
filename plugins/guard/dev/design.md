# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py`) is the truth for control flow — this file records *why* the
design is shaped this way and the runtime facts verified against the real CLI, not a
line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Archive the user turn to the session log. Ignores `/guard:settings` / `/guard:audit-{claims,deferrals,korean}`. |
| `UserPromptExpansion` (matcher `^(guard:)?audit-<axis>$`, one per axis) | `verify <axis>` | On demand, dispatch **that axis's** auditor for the last completed turn (`pending_verify_prompt_id`). The axis rides in argv, not in a dispatch input the auditor has to be trusted to honor. |
| `PostToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `refs-index` | Block when a file saved in the refs dir is not listed in that dir's `AGENTS.md`. |
| (called via Bash, not a hook) | `settings` | `guard:settings` skill (forked) shows/sets guard.local.json settings; `audit_gate`/`audit_claims`/`audit_deferrals`/`audit_korean` also apply to the live session's `state/<sid>.json` (session id from `--session`/`CLAUDE_CODE_SESSION_ID`). Every other key preserved; never the list key (`exempt_skills`). |
| (called via Bash, not a hook) | `exempt` | `guard:settings` skill records the user's confirmed `exempt_skills` selection (that key only). |
| `Stop` | `stop` | manual: record pending target, no audit. headless: one in-hook judge **per enabled axis**, spawned in parallel; blocks on any axis's violation. |
| `SessionStart` | `session-start` | Age-sweep state/sessions/verified/turns; inject the per-project refs directory the style cannot hardcode. |
| (called via Bash, not a hook) | `refs-dir` | Print the resolved refs directory (auditor fallback; applies `refs_dir` validation). |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no turn buffer of its own; at
Stop it reconstructs the turn from Claude Code's transcript, sliced by `prompt_id`.

- `state/<sid>.json` — the session's live judge settings (`audit_gate` and the three axis
  switches), plus the per-turn markers keyed on `prompt_id` that keep each once-only
  action once-only (`last_audited_prompt_id`, `pending_verify_prompt_id`).
  `_read_state` honors only known keys, so a hand-edited or stale file degrades to
  defaults instead of injecting state.
- `sessions/<sid>.jsonl` — full session archive, one line per user/assistant/judge
  record. A judge record carries `axes` (what ran) and `missing` (what failed) alongside
  the per-axis findings, so a partial audit is legible after the fact and not mistaken
  for an axis that found nothing.
- `turns/<sid>/<prompt_id>.json` — **manual mode only**: the turn slice guard cut from
  the transcript (`{user, tools[], assistant}`) and hands to whichever axis auditor is
  dispatched, so the auditor reads one turn, not the whole transcript. Manual-mode Stop
  writes it and records `pending_verify_prompt_id`; the per-axis `/guard:audit-*`
  commands read it back. Headless mode judges in-process and writes no turn file.
- `verified/<sid>.jsonl` — supported claims from FULLY-AUDITED PASSED turns only (`{ts,
  turn, claim, evidence}`, `turn` = prompt_id), replayed to later Stops as a
  VERIFIED_FACTS block so an established fact isn't re-derived. Only passed turns
  contribute, so a blocked/unsupported claim never becomes "verified" — and a turn with
  a *missing* axis (a judge that failed) contributes nothing either, even when every
  axis that did report was clean: a partially-audited turn is not evidence that the
  claim survived the audit.
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

- **`prompt_id` is common to every hook** (PostToolUse and Stop included) and equals
  the transcript record's `promptId` — this is what lets a per-turn marker written by one
  event match the same turn at another. Observed on real payloads (seen on Claude Code 2.1.197;
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
  "task-notification"`, `promptSource: "system"`, NOT `isMeta`; verified 2.1.197). An
  auditor dispatch is itself a background task, so auditing its completion would
  re-dispatch it — the loop no auto-dispatch mode exists to hit any more, but the skip
  still guards the on-demand path and the Codex adapter. `cmd_stop` skips these
  (`skip_task_notification`) from BOTH archive and judge. Ordering that must not
  regress: the skip precedes `_append_log`, and `_append_log` stays ahead of the
  `stop_hook_active` check (so a corrected response after a headless block is still
  archived).
- **A Stop hook may inject `additionalContext` without `decision`** and the
  conversation continues — the auditor-dispatch mechanism, still used by the Codex
  adapter and by `UserPromptExpansion` on the Claude side. `stop_hook_active: true`
  ⇒ guard already blocked this turn, so Stop returns at once.
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
  only) plus, for `audit_gate` and the axis switches, the session state; it runs only from
  the user-invoked (`disable-model-invocation`) skill, which the model cannot trigger.

## Design invariants (why, not how)

- **Always exit 0; fail open.** Blocking is a decision payload on stdout, never a
  non-zero exit. Any judge failure (missing binary, timeout, unparseable output)
  leaves state untouched and does not block — guard must never harass the user
  because its own machinery broke.
- **The evidence judge has no setting of its own** beyond `audit_gate`, and `manual` (the
  default) is its practical off: Stop archives the turn and records the pending target,
  but spawns no judge. `/guard:settings` sets it (writing the config key and, with a
  session id, the live session state).
- **Control turns and exempt commands are never judged.** `/guard:settings` and all three
  `/guard:audit-{claims,deferrals,korean}` commands are skipped on BOTH sides: the
  UserPromptSubmit archive skips them (`_CONTROL_CMD_RE` on the raw prompt, so they never
  become a turn in the log), and `cmd_stop` skips them via
  `command_name` (extracted from the transcript's expanded
  `<command-name>/guard:settings</command-name>`). This second skip is load-bearing — a
  control turn's response is a one-line relay ("guard on") with no evidence, and
  without it the Stop judge falsely blocked it (session b30dbaec). The same
  `command_name` path skips any skill / slash command the user lists in
  `exempt_skills` — named with its plugin namespace (`plugin:skill`), since a
  user-invoked skill reaches the transcript as a namespaced `<command-name>` just like
  a command (skill output is not a body of technical claims to ground). Both modes
  honor it (checked before the `audit_gate` branch). `audit-comment` is deliberately NOT
  in `_CONTROL_CMD_RE` — that skill relays findings about real files, so its turn stays
  auditable — and the regex's `(?=\s|$)` is what keeps `audit-claims` from matching a
  bare `/audit`.
- **Mark resolution is the judge's call, not a mechanical gate.** guard once ran a
  deterministic Stop-time check on reference marks (dangling mark, unused entry, mixed
  syntax, non-numeric footnote id) and blocked on it in every `audit_gate` mode. It was
  removed with the `refs_format` setting: guard no longer fixes a mark syntax, so there is
  no format to enforce, and whether a mark resolves to adequate evidence is a judgment
  about the claim — which is the evidence judge's job and follows the `audit_gate`
  modes like every other criterion. Nothing at Stop blocks on marks now.
- **A saved reference must be indexed.** `refs-index` (PostToolUse) blocks when a file
  written inside the refs dir is not named in that directory's `AGENTS.md`. A reference
  nothing points at is one the next reader never finds, so the index is part of the
  save, not a courtesy. It runs *after* the write, not as a PreToolUse gate: the natural
  order is save-then-index, and blocking the save would demand an index row for a file
  that does not exist yet. Matching is a substring search for the file name anywhere in
  the index — the index is prose a human maintains, so pinning the check to a table
  layout would fail the first time someone reformats it. `AGENTS.md` and its `CLAUDE.md`
  shim are skipped (`_REFS_INDEX_SKIP`) or writing the index would trip its own hook.
  The check itself is `refs_index_gap`, shared by both hosts: Claude registers a
  `refs-index` subcommand, Codex calls it from its single PostToolUse adapter.
- **The Simple output style is opt-in, and nothing may depend on it.**
  `output-styles/simple.md` omits `force-for-plugin` (which defaults to false), so enabling guard does not
  switch a user's output style — they select **Simple** in `/config` (or set
  `outputStyle`) themselves. Deliberate: the style rewrites how every answer in the
  session is written, which is too large a change to impose on someone who installed
  guard for its gates. The consequence is a rule for authors — no guard behavior may be
  implemented in the style file, because it is inactive for most users. Anything that
  must always hold goes in the SessionStart context (`guard_hook.py`), a judge prompt,
  or an agent definition. Note the style also does not reach subagents at all: per the
  official docs a subagent runs its own system prompt, which is why
  `agents/simple-explainer.md` carries its own copy of the explain-clearly rules rather
  than inheriting them.
- **Renamed keys and dropped modes get no fallback.** `evidence_gate` → `audit_gate` is
  ignored outright (a config still carrying the old key silently gets the `audit_gate`
  default), and the dropped `subagent` mode behaves the same way: `"audit_gate":
  "subagent"` passes `_load_config`'s type check as a string but fails `_audit_gate`'s
  enum coercion, so it lands on `manual`. Deliberate — guard is pre-1.0 and read-compat
  for renamed keys and retired enum members is not worth a permanent branch in
  `_load_config`. The cost is real and accepted: a project that had set `subagent` loses
  its Stop-time auditing entirely on upgrade, with no warning, so this belongs in the
  release notes rather than in migration code.
- **Mode and criteria are separate settings.** `audit_gate` picks *how/when* the audit
  runs; `audit_claims` / `audit_deferrals` / `audit_korean` pick *which axes* run. Split
  because the axes fail differently — a project that wants its claims grounded
  may still want to defer work openly, and forcing one setting to carry both meant turning
  off the whole judge to escape either. `audit_korean` (axis 3, natural Korean vs 번역체)
  defaults **off**, unlike the other two: it reports nothing on an English response, so an
  English-only project should not pay a judge spawn for it. It is governed by `audit_gate`
  with the others — it audits the finished turn, so *how/when* is the same one question.
  Since headless spawns one judge per axis, a disabled axis is simply never spawned;
  there is no prompt-level "this axis is off" note any more, and nothing for an
  over-reporting judge to resurrect (an axis absent from `_enabled_axes` has no verdict
  to read). The axis filter still lands at the single place blocking is decided (the
  per-axis `violates` predicates in `cmd_stop`). **All axes off skips the audit
  outright** in every mode — no judge spawn, no dispatch, and manual mode records no
  pending target — since a run that can report nothing is pure cost. An axis switched off
  is nonetheless auditable *on demand*: the switch governs the automatic Stop-time audit, and refusing the command
  would leave no way to check the very axis a project keeps off by default.
- **Two modes, one set of criteria.** `manual` (default; no auto-audit — the per-axis
  `/guard:audit-*` commands dispatch on demand) or `headless` (in-hook judges that block).
  The criteria are identical across both, and each auditor agent definition mirrors its
  axis's judge prompt in prose — when one changes, the other has to. Bad `audit_gate` →
  the default (`manual`, via `_audit_gate`). `refs-index` is independent of `audit_gate`,
  so `manual` narrows auto-verification without dropping the index rule.
- **Headless fans out: one judge per enabled axis, spawned in parallel.**
  `run_judges_parallel` `Popen`s every enabled axis at once and collects them. The win is
  measured, not assumed, and comes from the **per-axis tool budget** rather than from the
  concurrency alone: claims gets `Read,Grep,Glob,Bash`, deferrals `Read,Grep,Glob`, and
  korean **no `--allowedTools` flag at all** — an axis that judges prose cannot use the
  repository, and withholding it takes that judge from ~30s (any repo-reading judge) to
  ~5-13s. A full three-axis fan-out measured 21.7s wall clock against 29-41s for the old
  single combined judge. The timeout is a **group** deadline, not per child: they run
  concurrently, so the wall clock is the slowest one, and giving each its own full
  `JUDGE_TIMEOUT_SECONDS` would let a slow set outlive the Stop hook's own timeout and be
  killed mid-write. The **axis text is copied verbatim into each judge and must not be
  trimmed for the split** — a shortened Korean prompt was measured demanding that
  `prompt_id`, 커밋, 리팩토링 and `git rebase` be translated, so the loanword and
  identifier carve-outs are load-bearing, not padding. The user prompt is split the same
  way: the Korean judge gets the response text alone, with neither TOOL_ACTIVITY nor
  VERIFIED_FACTS, since it cannot use evidence it is not judging against — which is most
  of the token saving. `AXIS_JUDGES` is the one table holding each axis's
  field/system/schema/tools/predicate/label, so adding an axis does not mean touching the
  fan-out.
- **A judge that did not report is UNCHECKED, never a pass.** With N children some can
  fail while others answer, so silence needs its own meaning: **all** failed → fail open
  (return 0, exactly as the single judge did on a `None` verdict); **some** failed → block
  on whatever the reporting axes found *and* name the failed axes in the reason as
  "UNCHECKED rather than clean". Verified facts are recorded only on a pass that was
  **fully** audited (no violations *and* no missing axes) — folding a partial audit into
  the verified store would launder an unexamined claim into an established fact.
- **Manual mode + on-demand verify, per axis.** manual-mode Stop archives the turn, writes
  its slice (shared `_write_turn_slice`), and records `pending_verify_prompt_id` — then
  emits nothing. Each `/guard:audit-<axis>` command has its own `UserPromptExpansion`
  matcher and passes its axis to `cmd_verify` in argv; `_auditor_dispatch_context` takes
  that one `axis` and dispatches exactly one agent from `AXIS_AUDITORS`. One axis per
  dispatch is the point: the auditor learns what to audit from *which agent was
  dispatched*, not from an `axes` argument it has to be trusted to honor. It reads the
  pending slice off disk, so it needs no transcript access. `verified_file` / `dispatcher`
  / `refs_dir` go to the **claims** auditor only — it is the sole writer of verified
  facts, and the other two axes produce nothing reusable. All three commands are in
  `_CONTROL_CMD_RE`, so their own turns are skipped and never become the pending target.
- **The auditor agents cannot express "no tools"; the headless judges can.** The Korean
  axis needs zero repository access, and headless says so by omitting `--allowedTools`
  entirely. `agents/korean-auditor.md` cannot: per the official agent docs, omitting
  `tools` inherits *every* tool, and an empty/unresolvable list makes Claude Code refuse
  to launch the subagent — so it is declared `tools: Read`, the smallest set that still
  lets it read its `turn_file`. The asymmetry is a platform limit, not an oversight; do
  not "fix" it by emptying the frontmatter.
- **Judge once per turn.** headless relies on the payload's `stop_hook_active`. manual
  writes no dispatch, so it needs no once-guard; `last_audited_prompt_id` survives in the
  state schema for the Codex adapter, whose non-blocking dispatch cannot rely on that
  flag.
- **Verified facts belong to the headless path alone.** `cmd_stop` is both the only
  writer (`_append_verified`) and the only reader (`_read_verified_facts`), so the store
  needs no cross-process writer and the auditors are strictly read-only. The
  `record-verified` subcommand that let an auditor subagent write was deleted with
  `subagent` mode: the cache exists to spare an EVERY-TURN judge from re-deriving a
  claim, and the only every-turn path now maintains it inline. An on-demand audit has
  nothing to add — under `manual` nothing reads the store, and under `headless` the
  judge already wrote it. Only passed, evidence-backed claims cross a turn boundary,
  never raw prior-turn text.
- **The Codex side was deliberately left on the old shape.** `hooks/hooks.codex.json`,
  `hooks/scripts/hook_codex.py`, and `skills/setup/` still block-and-dispatch a SINGLE
  `guard_claims_auditor` covering every enabled axis, with the axis list carried as
  dispatch text and the once-guard on `last_audited_prompt_id`. That is intentional, not
  drift: the fan-out is built on `claude -p` subprocesses and per-agent tool grants that
  have no Codex equivalent yet, and Codex will get its own migration. The adapter survived
  the refactor because the only judge-side names it reaches into are `AuditGate.MANUAL`
  and `core._AXIS_FIELDS` (plus the axis accessors and the shared state/config helpers) —
  none of the fan-out. Keep those stable, and do not "unify" the Codex path by accident.
- **Assistant tool output is first-class evidence** (rendered as TOOL_ACTIVITY) — a
  claim that restates or follows from a command's output there is supported without a
  re-cite. **User-run `!` commands are NOT evidence and their turn is not judged.** A
  `!` command inherits the preceding typed prompt's promptId, so its output records
  land in the slice *after* the response guard already judged — the evidence would
  arrive later than the claims it supports, and cannot be judged coherently in that
  turn. `_read_turn_from_transcript` flags the turn (`has_user_command`) and `cmd_stop`
  skips it (`skip_user_command`); the `!` records are never collected or rendered.
- **`_safe_project_subdir` is guard's self-neutering defense** for the one config key that
  names a directory guard treats specially (`refs_dir`): strictly inside the project (the
  root itself fails, because a path is never in its own `.parents` — this is what rejects
  `"."`), and never guard's state root, a path under it, or the config file. Without it a
  `refs_dir` of `.claude/guard` would make guard's own state a directory it invites the
  model to write into, and `.claude/guard.local.json` would put the judge switch there.
  Keep it one implementation; two copies means one of them gets fixed.
  **What it deliberately does not catch: an ANCESTOR of guard's state.** `.claude` is
  neither the state root nor under it, so it is a legal value — the rule is containment,
  not reachability, and anything else that starts trusting a configured directory has to
  bring its own check on the actual target rather than assume this one covered it.
- **The config-mutating CLIs can weaken guard, and Bash is ungated.** `settings set
  audit_gate manual` and `exempt add <skill>` both reach guard's own configuration, and
  the model can invoke this script through Bash — nothing stops it. `_cli_write_allowed`
  requires a marker (`GUARD_SETTINGS_SKILL`) that only the user-invoked `guard:settings`
  skill sets, on the mutating verbs of both — covering only `exempt` would be theater,
  since `audit_gate manual` is the easier move.
  **This is a speed bump, not a boundary**: the variable name is in the source the model
  reads. It buys that the unreflective path ("this audit is in my way, let me turn it
  off") fails closed, that the refusal names the user as the only legitimate widener, and
  that attempts land in the trace as `refused_no_skill_marker`. A model that deliberately
  sets the marker is outside guard's threat model — and the Bash call is visible to the
  user either way. Read verbs (`list`, `show`) need no marker.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. `audit_gate` is an `enum.StrEnum`
member (`AuditGate`) — the reason guard requires Python 3.11+ (`StrEnum`
"Added in version 3.11": https://docs.python.org/3/library/enum.html, excerpt saved at
`wiki/ref/python-strenum.md`). Keys: `model`
(default `"haiku"`), `effort` (low/medium/high/xhigh/max, default `"medium"` — the
reasoning effort of the HEADLESS judges only; an auditor subagent's model/effort come from
its own agent frontmatter), `audit_gate`
(`"manual"`|`"headless"`, default
`"manual"` — the evidence judge's control; `manual` is its practical off, and a stale
`"subagent"` falls through the enum coercion to it), `audit_claims` / `audit_deferrals`
(booleans, default `true`) and `audit_korean` (boolean, default **`false`** — see the
axis invariant for why this one is opt-in), the three axis switches; all axes off skips
the audit outright. Non-bool values fall back to the default rather than to Python
truthiness, so a stringy `"false"` cannot silently disable an axis. `exempt_skills`
(list of strings, default `[]`) — skills / slash commands whose turn the Stop judge
skips, named with their plugin namespace (`plugin:skill`, e.g. `guard:settings`) or bare
for un-namespaced skills, matched leading-`/`-stripped and case-insensitively (guard's
own `settings`/`judge` control commands are always exempt regardless). Manage
`exempt_skills` interactively with the `guard:settings` skill (which records the user's
chosen names via the `exempt` CLI); no need to hand-edit. `refs_dir`
(string, default `""`) — project-relative directory for guard's cited-doc
copies; empty = the git-tracked default `wiki/ref/` (references committed with the
repo), a different tracked path (e.g. `"docs/refs"`) overrides it; commits stay in the
user's normal workflow (guard never commits). `_refs_dir` validates the value (see
`_safe_project_subdir` above) and everything that names the location follows it: the
`refs-index` check, the headless claims judge's prompt (`__REFS_DIR__` substitution — the
substitution is applied to every axis's system prompt, but only the claims axis carries
the token), the claims auditor's
dispatch inputs (`refs_dir`, with the `refs-dir` CLI subcommand as its fallback), and
the SessionStart context line, which states the refs rule to the agent and names the
resolved path (also exported as `GUARD_REFS_DIR` via `$CLAUDE_ENV_FILE`, per the official
hooks docs, so a Bash caller resolves it with one `echo`). The output style carries no
refs instruction: it is user-selected (no `force-for-plugin`), so nothing load-bearing
may depend on it being active. guard fixes no
reference-mark syntax: both judge paths are told to check that a mark *resolves* and never
to grade its form. Only keys whose value matches the
default's type are honored (a malformed value can't flip a flag); unknown keys ignored;
missing/malformed file → all defaults. `guard.local.json.example`
ships at the plugin root. Judge tools are per axis, not global (`AXIS_JUDGES`; no
`--disallowedTools` — room to extend, e.g. a verification artifact), and the Korean axis
gets none; **isolation is `--safe-mode` + `--no-session-persistence`, never the tool
list** — withholding tools from the Korean axis is a speed decision, and must not be
mistaken for the sandbox.

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
# and, for audit_gate and the axis switches, state/<sid>.json.
"$H" settings show --session s1
"$H" settings set effort high --session s1

# Config-mutating CLI verbs require the settings-skill marker (see _cli_write_allowed);
# export it once for the recipe. Read verbs (`show`, `list`) need nothing.
export GUARD_SETTINGS_SKILL=1

# headless fan-out (real claude, one child per enabled axis). Two axes by default;
# switch the third on to spawn all three. `time` it — the wall clock should stay near
# the SLOWEST axis, not their sum (that is the whole point of the parallel spawn), and
# the trace shows one judge line per axis.
"$H" settings set audit_gate headless --session s1
"$H" settings set audit_korean on --session s1
S="{\"session_id\":\"s1\",\"prompt_id\":\"p1\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"Redis is always faster than Postgres.\",\"stop_hook_active\":false}"
time (echo "$S" | "$H" stop)          # unsupported claim -> block; korean axis self-skips (English)

# A missing axis must be reported UNCHECKED, not folded into a pass. Every axis failing
# is the fail-open case: shim a `claude` that always exits nonzero, PREPENDED to PATH
# (do not replace PATH — this script's own shebang still needs python3 ≥ 3.11).
D=$(mktemp -d); printf '#!/bin/sh\nexit 1\n' > "$D/claude"; chmod +x "$D/claude"
(PATH="$D:$PATH"; echo "$S" | "$H" stop)   # -> empty; trace: one nonzero_exit per axis + all_judges_failed
# A PARTIAL failure has to be provoked per axis (e.g. shrink JUDGE_TIMEOUT_SECONDS so the
# repo-reading axes time out while korean still answers). The block reason must then name
# the timed-out axes as "UNCHECKED rather than clean", and verified/<sid>.jsonl must gain
# nothing even when every axis that did report was clean.

# Per-axis helper for the cases below.
ax(){ for k in claims deferrals korean; do
        case " $* " in *" $k "*) v=on;; *) v=off;; esac
        "$H" settings set "audit_$k" "$v" --session s1 >/dev/null; done; }

ax korean; time (echo "$S" | "$H" stop)  # korean alone: no --allowedTools, so seconds not ~30s
ax;        echo "$S" | "$H" stop          # every axis off -> empty; trace: skip_axes_off
ax claims deferrals                       # back to the defaults

# manual mode (default): Stop only slices the turn to a file + records the pending
# target; it emits nothing. Then each /guard:audit-<axis> expansion dispatches exactly
# one auditor for it — deterministic (no `claude`), so it is the cheapest way to check
# the per-axis dispatch text and that only `claims` receives verified_file/dispatcher.
"$H" settings set audit_gate manual --session s1
echo "$S" | "$H" stop                  # -> empty; writes turns/s1/p1.json
for ax in claims deferrals korean; do
  echo '{"session_id":"s1"}' | "$H" verify "$ax"
done
"$H" verify bogus < /dev/null           # unknown axis -> no output at all

# The mutating CLI verbs refuse without the marker; reads still work.
(unset GUARD_SETTINGS_SKILL; "$H" exempt add some-skill; "$H" settings set audit_gate headless; "$H" exempt list)
```

`settings`, `exempt`, manual-mode `stop`, `verify`, `refs-index`, and the session
subcommands are deterministic (no CLI/auth). Only headless `stop` spawns a
real `claude` — one child per enabled axis, so budget for that when timing
it. Two pure functions are directly unit-testable:
`_read_turn_from_transcript(path, prompt_id)` on a fixture JSONL, and
`_safe_project_subdir(project_dir, value)` on its rejection cases (`"."`, `".."`,
`".claude/guard"`, `"../elsewhere"`, `"/etc"` — all None; a plain subdirectory resolves).
