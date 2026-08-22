# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py`) is the truth for control flow — this file records *why* the
design is shaped this way and the runtime facts verified against the real CLI, not a
line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Name the answer file for this turn — Stop is too late for it, since by then the answer is already printed and a printed answer cannot be corrected. Silent (trace only) when every agent is `off`, when `audit_paused` is set, on a control command, and with no `prompt_id`. Also saves the prompt verbatim to `<prompt_id>.request.md` for the router, which is the only copy guard keeps and the only reader it has. The hook stays registered even when silent so a "guard said nothing" report can be told apart from a hook that never ran. |
| `UserPromptExpansion` (one matcher per agent: `claims-auditor`, `deferrals-auditor`, `clarity-auditor`, `korean-corrector`) | `verify <agent>` | On demand, dispatch **that agent** for the last completed turn. The agent name rides in argv, not in a dispatch input the model has to be trusted to honor. |
| `PostToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `post-edit` | Record a source file this turn wrote (the candidate list for a `comment-corrector` recommendation), then block when a file saved in the refs dir is not listed in that dir's `AGENTS.md`. |
| (called via Bash, not a hook) | `settings` | `guard:settings` (a `context: fork` skill, so it runs in a forked `general-purpose` agent rather than in the main session) shows/sets/unsets guard.local.json settings; the agent modes also apply to the live session's `state/<sid>.json` (session id from `--session`/`CLAUDE_CODE_SESSION_ID`). A mode change away from `reuse` also prints a stand-down note, the only channel guard has to a running instance. `set` preserves every other key; `unset <key>` is the only way to delete one. |
| `Stop` | `stop` | Write the response section of the turn record and mark the turn as the on-demand target — always. Then, when any agent is not `off`, emit `additionalContext` asking the main agent to dispatch `guard:router` over the record, carrying the eligible agents with their modes and this turn's paths. The router names sections of `hooks/context/dispatch-playbook.md`; the main agent follows those, completing the record's second section only if a named section asks for it. `comment-corrector` never goes to the router: it is dispatched directly in the same emission, to be sent in the same message — see the invariant below. |
| `SessionStart` | `session-start` | Sweep state and turn records past retention, export `GUARD_REFS_DIR`, state the refs rule as session context, name the dispatch playbook once when any *turn-end* agent is on, state the standing `refs-finder` policy once when that agent is on (Claude only), and — when any agent is in `reuse` — state the standing reuse policy once. |
| (called via Bash, not a hook) | `transcript` | `index` / `turn` / `find` over the session transcript, for the audit agents. Writes an extract file and prints only its path plus a one-line summary; `--since` / `--until` / `--last` bound which turns are scanned. |
| `UserPromptExpansion` (`^(guard:)?toggle$`) | `toggle` | Mute/unmute the automatic audit for THIS session (`audit_paused`, session state only — never guard.local.json). `command_args` carries `on`/`off`; empty flips. The hook does the work and prints the result. |
| (called via Bash, not a hook) | `status` | Status-line segment: `guard <n>` / `guard off` / `guard ·`, or nothing on any failure. Reads one state file; runs on every assistant message. |
| (called via Bash, not a hook) | `refs-dir` | Print the resolved refs directory (auditor fallback; applies `refs_dir` validation). |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no copy of a turn's content: it
reads the transcript only for the turn's *kind* (`_turn_identity`), and the turn itself is
written by the main agent.

- `state/<sid>.json` — the session's live agent modes (one key per agent, named after it,
  valued `off`/`fresh`/`reuse`), the per-turn markers keyed on `prompt_id` that keep each once-only action once-only
  (`last_audited_prompt_id`, `pending_verify_prompt_id`), and the turn's edited source
  files (`edited_prompt_id` + `edited_files`). The edited list is stored WITH the prompt_id
  it belongs to, not as a bare list: PostToolUse appends and Stop reads back, and without
  the id a previous turn's files would ride into this turn's recommendation.
  `_read_state` honors only known keys, so a hand-edited or stale file degrades to
  defaults instead of injecting state. `audit_paused` is here rather than in the config on
  purpose — see the session-mute invariant below.
- `turns/<sid>/<prompt_id>.md` — the answer to the user's question, one file per typed
  prompt. The session writes it during the turn (the path comes from `UserPromptSubmit`);
  guard fills it in at Stop from `last_assistant_message` only when the turn left it empty,
  which is the fallback, not the path. The correctors edit it in place, so it is also the
  file the user is shown at the end.
- `turns/<sid>/<prompt_id>.request.md` — the user's request for that turn, verbatim, written
  by guard at `UserPromptSubmit`. Handed to the ROUTER and to nothing else; never audited,
  corrected, or included in an audit agent's dispatch. Swept with the answer beside it, since
  it lands in the same per-session directory.
- `extracts/<dir>/…` — whatever an agent pulled out of the transcript: `index.md`,
  `turn-<id>.md`, `find.md`, or a `--out` path it chose. Written by the `transcript`
  subcommand on request, never on a schedule, and swept with the rest of the session's
  state. `<dir>` is *not* a session id by contract: `transcript` takes the name from
  `--session` when given and from the transcript filename's stem otherwise, and no caller
  passes `--session` — the auditors are handed a transcript path and a turn id, nothing
  more. Claude Code happens to name that file after the session, so the directory reads
  like a session id; do not build on it. Nothing needs to, because nothing looks these up
  by name — the subcommand prints the path it wrote, and the SessionStart sweep decides by
  the directory's mtime.
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

Not state, but part of the same picture: `hooks/context/dispatch-playbook.md` in the plugin
holds one section per agent — how to dispatch it, what its report means, what to do about
it — plus a `router` section. guard's hook output and the router both refer to it by section
name; nothing copies its text. `_playbook_path()` resolves it from the script's own location
rather than `CLAUDE_PLUGIN_ROOT`, because the same script is also the Codex adapter's
library and a plain CLI the settings skill runs over Bash, and only the hook case has that
variable set. That is not in tension with `commands/settings.md` writing
`${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py`: there it is a text substitution Claude Code
performs while building the command, so the path arrives already resolved and the launched
process still sees no such variable in its environment.

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

- **A `SessionStart` entry with no matcher fires on every source**, and the sources are
  `startup`, `resume`, `clear`, `compact` and `fork`. `compact` is the load-bearing one:
  guard's SessionStart hook registers no matcher, so a context compaction that drops its
  injected lines immediately gets them restated. That is the whole reason the `refs-finder`
  standing policy can be stated once per session instead of on every `UserPromptSubmit`. The
  same section confirms that plain stdout becomes model-visible context for exactly three
  events — `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart` — which is how those
  lines reach the model at all. Source: official hooks docs
  (https://code.claude.com/docs/en/hooks), excerpt saved at
  `wiki/ref/claude-code-hooks-session-env.md`, fetched 2026-08-22 — docs-verified, not
  observed on a live compaction. If the policy line stops surviving a compact, re-check this
  first and fall back to a per-turn line rather than letting the agent go silent.
- **`prompt_id` is common to every hook** (PostToolUse and Stop included) and equals
  the transcript record's `promptId` — this is what lets a per-turn marker written by one
  event match the same turn at another. Observed on real payloads (seen on Claude Code 2.1.197;
  needs ≥ 2.1.196); the hook input schema is in the official hooks docs
  (https://code.claude.com/docs/en/hooks). Re-verify against those docs and a live Stop
  payload before relying on this.
- **Turn anchor.** The anchor record is the one whose top-level `promptId == prompt_id`
  (a typed prompt: `origin={"kind":"human"}` + str content). Records derived from the turn
  carry `promptId=None`. guard reads the anchor and stops — `_turn_identity` needs the
  turn's kind, not its content — so the slice-boundary rules that used to matter here (the
  next different non-empty promptId ends the slice; `isMeta:true` records are guard's own
  feedback and are skipped) no longer bear on anything. They are recorded in case a future
  change needs to walk the turn again; do not re-add the walk without a reason.
- **Machinery reporting in opens its own transcript turn**, with a fresh promptId and
  `promptSource: "system"`. Two kinds observed: `origin.kind == "task-notification"` for a
  background agent's completion (NOT `isMeta`; verified 2.1.197) and `origin.kind ==
  "peer"` for an inbound `SendMessage` from a subagent or another session (`isMeta: true`;
  verified 2.1.239). This is load-bearing: the recommendation asks the main agent to
  dispatch agents, and those agents both complete and message back, so an audit *of such a
  turn* dispatches again without end. `cmd_stop` audits only `origin.kind == "human"` and
  skips every other named kind (`skip_nonhuman_turn`), which is what keeps a kind added
  later from reopening the loop; an *absent* kind still audits, so guard cannot go silently
  dormant if `origin` stops being emitted.

  Shipping only the `task-notification` skip left `peer` open and the loop was observed in
  a real session (2.1.239): the `claims-auditor` asked the session a question via
  `SendMessage`, the reply opened a `peer` turn, guard handed that turn an answer file of
  its own and recommended a full audit of guard's own audit report — two extra rounds, and
  the main agent ended up opening the audit memo instead of the answer. Hence the second
  half of the rule: one user question, one answer file. `UserPromptSubmit` (which fires only
  for a typed prompt) and the Stop dispatch name the same path, the correctors edit that
  file, and the playbook's `Presenting the result` opens that file and forbids starting
  another for the audit report.
- **The answer file is an input, so it is gated on the agents that read it** (`_reads_turn`,
  over `AUDIT_AGENTS[...].reads == "turn"`) — not on any switch being on. `comment-corrector`
  reads the source files the turn wrote and never opens the answer file, so a project with
  only that one on must get neither the `UserPromptSubmit` instruction to write into it nor
  the `answer file:` line in the dispatch. Both once ignored this and cost the same thing the
  all-off case is careful to avoid: a per-turn instruction to write a document nothing would
  read. Keep the two sides gated by the same predicate — they name one path, so they must
  agree on whether it is wanted, and `- files for` / `- history` are already conditional on
  the eligible set the same way. On-demand audits are unaffected: Stop writes the response
  section on every turn, and the record carries a note saying it was filled in from the
  response because the turn was never told to write it.
- **`hookSpecificOutput.additionalContext` on Stop continues the conversation.** Claude
  acts on the text in the same turn, exactly as with `decision: "block"`, and under the
  same loop protections — `stop_hook_active` plus an 8-consecutive-continuation cap. The
  only difference is presentation: block surfaces as a hook error, `additionalContext` as
  `Stop hook feedback`. Source: official hooks docs
  (https://code.claude.com/docs/en/hooks, "Stop decision control"), excerpt saved at
  `wiki/ref/claude-code-stop-hook-decision-control.md`, fetched 2026-08-21. This is why
  guard's recommendation is `additionalContext` and its refs-index gap is still a block:
  one is guidance from a working hook, the other is unfinished work.
- **`memory: <scope>` gives a subagent a persistent store, and silently gives it Write and
  Edit.** Scopes and directories: `user` → `~/.claude/agent-memory/<agent>/`, `project` →
  `.claude/agent-memory/<agent>/`, `local` → `.claude/agent-memory-local/<agent>/`; the
  first 200 lines or 25KB of that directory's `MEMORY.md` is injected into the agent's
  system prompt, and Read/Write/Edit are enabled so it can curate. It is part of *auto
  memory*, so `autoMemoryEnabled: false` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY` turns it off
  entirely with no signal to the agent. Docs: https://code.claude.com/docs/en/sub-agents
  ("Persistent Memory for Subagents"), excerpt at
  `wiki/ref/claude-code-subagent-memory.md`, fetched 2026-08-22. Unverified: whether
  `<agent>` is the bare or the namespaced name for a plugin subagent — guard is written not
  to care, since it never touches those directories.
- **The settings skill needs the live session id, and gets it by substitution.**
  `${CLAUDE_SESSION_ID}` is a skill-content substitution expanded before the skill runs (per
  the skills docs, https://code.claude.com/docs/en/skills, "string substitution"), so the
  real id is baked into the text; `CLAUDE_SESSION_ID` is only that token and is NOT a
  process env var (`printenv CLAUDE_SESSION_ID` is empty), so the CLI reads
  `CLAUDE_CODE_SESSION_ID` when no `--session` is passed. The skill used to run
  `context: fork` and both facts had to survive the fork boundary; it no longer does — a
  handful of Bash calls and a short summary do not earn a separate context, and the fork
  had to be handed the session id and the CLI path only to relay its result back.
- **Always exit 0; fail open.** Blocking is a decision payload on stdout, never a
  non-zero exit. Any internal failure — an unreadable transcript, a state file that will
  not write — leaves state untouched and says nothing: guard must never harass the user
  because its own machinery broke.
- **guard routes; the agents audit; guard runs no model.** No judgment about the *content*
  of a turn happens in the hook. Stop asks the main agent to dispatch one subagent — the
  router — which reads the turn and names which eligible agents would find something in it;
  the main agent dispatches those. Three shapes were tried before this one. Auditing inside
  the hook (the old `headless`) meant every criterion existed twice, once as a judge prompt
  and once as an agent definition, and they drifted. Picking agents by lexical pattern meant
  guard could detect `TBD` but not "asserted without evidence", which is the axis that
  matters most — so it named the claims auditor every turn, which is the same as naming
  none. Spawning the router as a `claude -p` child worked, but see the next invariant.
- **The router is a subagent, not a child process.** Every problem it used to have came
  from being a process guard spawned: the Stop hook blocked for the router's whole runtime
  at the end of every turn the user was waiting on; the child needed `--safe-mode` or
  guard's own Stop hook fired inside it and recursed; it needed an explicit
  `--disallowedTools` list because omitting `--allowedTools` leaves a child fully tooled
  (probed on 2.1.238 — the intuition is wrong, and `wiki/ref/claude-code-headless-child-flags.md`
  has the table); `--bare` was lighter but took auth down to `ANTHROPIC_API_KEY` only, so
  it would silently never run for an OAuth user; and spawn failure, timeout, non-zero exit
  and unparseable output were four failure paths guard had to tell apart from a clean
  verdict, in code and in the trace. As a subagent, the host runs it, its model lives in
  its definition, and the hook returns immediately. Do not reintroduce the child.
- **The router triages; it does not adjudicate.** Per agent it answers one question — is
  there material here — with a materiality bar (a five-word acknowledgement is Korean and
  is technically a statement; naming agents for it is the noise that makes the whole
  recommendation ignorable). Whether a claim is adequately backed, a deferral legitimate,
  or some Korean any good is the agent's call, and the agent reads the turn itself. This
  line is stated in `agents/router.md` per candidate, and it is the thing most easily lost
  in an edit: a router that starts judging quality stops naming the agent that would have
  judged it properly.
- **The router routes on the answer AND the request; materiality needs both.** Triage used
  to see the answer only, stated as a prohibition — "never because of what the user asked"
  — and that was wrong, because the one judgment left to the router is materiality and
  materiality is relative to the request. The same explanatory paragraph is the substance
  the user came for when they asked how something works, and padding when they asked for a
  one-line setting change; from the answer alone the two are the same text. What that cost
  was measured on: a plain-language "refs-finder는 켜줘" (so `_CONTROL_CMD_RE` did not skip
  it — see the control-turn bullet), whose answer file carried the CLI's own output plus a
  volunteered section explaining the switch. The router named `claims-auditor` and
  `clarity-auditor`, correctly by its own cues, and both returned pass.

  So `cmd_user_prompt` saves the prompt verbatim to `turns/<sid>/<pid>.request.md` and
  `_router_context` hands the path to the router. Four constraints, each load-bearing:

  - *a sibling file, not a section of the answer* — inside the answer file the user's own
    sentences become text `korean-corrector` rewrites, in a file the user is then shown, and
    text the auditors weigh as part of the answer;
  - *the router only* — no audit agent is given it. An auditor that knew what was asked
    would start excusing an unsupported claim because nobody asked for it;
  - *it can only subtract* — the request may make the router name FEWER agents than the
    answer alone would, never more, and "the user did not ask for this" discounts a passage
    as padding without ever excusing a skip. This is what keeps the old prohibition's
    guarantee: the expensive failure is still omission, and doubt still resolves to naming;
  - *guard keeps no other copy* — this restores a prompt store removed in v0.42.0, but for
    one reader and one question. Do not let it grow back into a general turn record.

  Best-effort and silent on failure: the field is conditional on the file existing, and a
  turn whose prompt guard never saw (a resumed session, a `!` command) routes on the answer
  as before. The hook is what decides that, never the router — absence learned from a failed
  `Read` cannot be told apart from a path built wrong, and that failure is silent.

  The two paths share a long prefix, so `_router_context` spells it once as `turn dir:` and
  names each file as `{turn dir}/<name>` (851 → 730 characters on a routed turn). The
  substitution is shown in the value rather than explained, and the same shape is emitted
  whether or not the request file exists: one input shape for the router beats saving four
  characters on the turns that have no request. What was rejected is the version that goes
  further — passing only the `prompt_id` and having the router derive both paths. The
  mechanism does not exist (env vars reach Bash only, `wiki/ref/claude-code-hooks-session-env.md`;
  `${CLAUDE_SESSION_ID}` is documented for skill and command content, not for `agents/*.md`,
  `wiki/ref/claude-code-skill-substitutions.md`), it would need `Bash` on a `Read`-only
  agent, and it would put guard's storage layout in router prose as a second copy — which,
  once drifted, reads nothing and clears every turn.
- **Nobody gathers the session's history; agents extract it.** guard's turn store holds the
  response, plus one sibling file holding the request for the router alone (next bullet).
  Everything else around it — this turn's tool activity, what an earlier turn established —
  is already in the transcript, and the agents that may
  need it (`AuditAgent.needs_history`: the two auditors) are handed a transcript path, the
  turn id, and the `transcript` subcommand. Three shapes were tried and each failed
  differently, so do not go back to them:

  - *the main agent copies it into a record* — puts the largest cost of an audit in the one
    context the user is talking to, before anything is known to need it, and makes the turn's
    own author the source for the record of the turn;
  - *guard accumulates every turn into a file* — writes a full record on every turn to serve
    the few that are ever audited, and goes stale the moment the session continues;
  - *the extract prints to stdout* — lands in the caller's context, which is the cost the
    whole design exists to avoid.

  Hence: extraction writes a FILE and prints only its path plus a one-line summary. The path
  is also how two agents look at the same evidence without either re-deriving it. Scans are
  bounded by `--since` / `--until` / `--last`, because a session runs to hundreds of turns
  and an auditor asking "what came before this turn" must not be handed turn 3 with equal
  prominence.
- **When extraction fails, asking the main session is a fallback with a mark on it.** No
  transcript path, a missing file, a turn id compacted away — the agent may `SendMessage`
  the main session for the specific text. The answer comes from the author of the text being
  audited, so it is testimony: the agent is required to use the raw text rather than the
  main session's account of it, and to say in its report that the finding rests on that
  rather than on the transcript. An agent that cannot get either reports what it could not
  check; it never treats unverifiable as verified.
- **Text is stored where it is read, not where it is emitted.** Three homes, split by how
  often each is paid for. `additionalContext` is paid in the main agent's context on *every*
  routed turn, so it is one imperative plus a list of fields — the paths, which agents are
  on, each one's mode — and nothing that reads the same twice. `agents/router.md` is paid
  once per routed turn, in the router's own context, so it holds the triage method, the cue
  per candidate, and the shape of the report. `hooks/context/dispatch-playbook.md` is paid
  only by whoever is sent to a section, so it holds how to dispatch an agent and what to do
  with its report — needed only for the agents actually picked.

  The test for any line in the hook output is: could the playbook or the router's own
  definition have said this instead? If yes it belongs there. That test removed the whole
  procedure from the hook, and it is why there is **no `router` section in the playbook** —
  the router's report names the playbook and the sections to follow, so the main agent never
  reads a section about routing.

  Three temptations to refuse. Printing each candidate's dispatch block in the hook pays for
  four blocks every turn to use at most four and usually none, the common case being the
  router clearing the turn. Having the *router* write those blocks instead makes an LLM
  re-type instructions it was handed, which is where wording drifts from the file that owns
  it — it names sections, it does not reproduce them. And restating the procedure "so the
  main agent does not have to look it up" is paying every turn to save one Read on the turns
  that route.
- **What bounds the dispatch is the playbook, not the roster.** A key the router invents
  has no section, so a switched-off agent stays unreachable even when it is named anyway.
  The roster is what stops it being reached for in the first place; the missing section is
  what stops it working.
- **The router's reason is part of the output, not decoration.** Each pick carries one
  sentence naming what in the response triggered it, quoted where possible, and the main
  agent is told to relay it. A recommendation nobody can second-guess is one that gets
  waved through, which is the failure this whole shape is built to avoid.
- **Control turns never get a recommendation.** `/guard:settings` and all of
  `/guard:{claims,deferrals,clarity}-auditor` / `/guard:korean-corrector` are skipped on
  BOTH sides: `_CONTROL_CMD_RE` matches the raw prompt at UserPromptSubmit, and `cmd_stop`
  skips them via `command_name` (extracted from the transcript's expanded
  `<command-name>/guard:settings</command-name>`). This second skip is load-bearing — a
  control turn's response is a one-line relay ("guard on") with no evidence, and without
  it Stop falsely blocked such a turn (session b30dbaec). It also has to land BEFORE the
  record write, so a control turn never becomes `pending_verify_prompt_id`: were it to,
  the next on-demand `/guard:<agent>` would audit the previous audit's relay instead of
  the answer the user wants checked. `comment-corrector` is deliberately NOT in
  `_CONTROL_CMD_RE` — that skill relays findings about real files and reports edits made to
  them, so its turn stays auditable — and the regex's `(?=\s|$)` is what keeps
  `claims-auditor` from matching a bare `/claims`.
  **A user-configurable version of this skip is gone.** `exempt_skills` (a list of
  skill/command names whose turns Stop dropped, default `[]`) was removed in v0.45.0. It
  was consulted in `cmd_stop` only, so once the answer file arrived in v0.44.0 a listed
  skill's turn was still handed a draft path by `cmd_user_prompt` and then silently
  dropped — the user asked to write into a file nothing would read. Sharing this branch it
  also inherited the skip of the record write, which is right for a control turn and wrong
  for a user's skill: `pending_verify_prompt_id` kept pointing at an older turn, so the
  next on-demand audit quietly audited the wrong answer. Against that, all it bought was
  one router call on a turn the router would have cleared anyway. If per-skill silence is
  wanted again, it belongs on the recommendation, not on the record — or in
  `/guard:toggle`, which already stops the recommendation while keeping the turn
  auditable.
- **A CLI verb finds the project root by walking to the git root; a hook never guesses.**
  `CLAUDE_PROJECT_DIR` is given to hook processes and substituted into skill/command content.
  It is **not** in the Bash tool's environment — reaching that takes an explicit
  `CLAUDE_ENV_FILE` export and nothing here does one
  (`wiki/ref/claude-code-hooks-session-env.md`, `wiki/ref/claude-code-skill-substitutions.md`).
  So the three Bash-invoked verbs — `transcript` (an audit agent), `settings` (the settings
  skill), `refs-dir` (the auditor fallback and the output style) — never see it, and what
  stands in for it decides whether they are correct at all.

  It was `Path.cwd()`, and that failed silently in both directions. An agent that had
  `cd`-ed into a subdirectory to read code wrote its extract to
  `<subdir>/.claude/guard/extracts/`, and `settings show` from the same place reported a
  project with every switch off — a second, empty state tree beside the real one. Observed as
  `plugins/guard/.claude/guard/extracts/…` in this repository. Worse, the root `.gitignore`
  did not cover it: a pattern containing a slash is anchored to the file's own directory, so
  `.claude/guard/` matched the root and nothing else, and `git add -A` would have committed a
  session extract into the plugin directory — the exact outcome `memory: local` is chosen to
  avoid. Both halves are fixed: `_cli_project_dir` walks up to the git root, and the ignore
  patterns are `**/`-prefixed so a stray tree anywhere is still ignored.

  `refs-dir` was on `_project_dir` and therefore printed NOTHING to every caller it has ever
  had. That is not a fail-open — the verb *is* the answer it was asked for.

  The primary fix is that guard now **tells** the Bash environment the root instead of
  letting it be inferred: SessionStart appends `export GUARD_PROJECT_DIR=…` to
  `$CLAUDE_ENV_FILE`, the one channel whose variables reach every later Bash command. So on
  Claude Code the CLI verbs read the root the host decided on, and they resolve correctly
  even from outside the checkout. The git-root walk stays as the fallback and still has to be
  right: the export is best-effort, `CLAUDE_ENV_FILE` is Claude Code only, and it is not
  documented to reach a SUBAGENT's Bash — which is exactly where `transcript` runs from.

  Both exports go through `_export_to_bash_env`, which appends a line only when it is not
  already there. SessionStart registers no matcher, so it fires on `startup`, `resume`,
  `clear`, `compact` and `fork` alike; before this was shared, `GUARD_REFS_DIR` was appended
  again on every compaction for the life of the session. Only `GUARD_`-prefixed names are
  ever exported — the host owns `CLAUDE_PROJECT_DIR`, and other tooling reads its presence as
  "running inside a hook".

  Keep the two resolvers apart. A hook is given the root, so an absent value means a broken
  installation and `_project_dir` returns None rather than writing state under whatever
  directory the host launched in. A CLI verb must answer, so `_cli_project_dir` never returns
  None. `.git` is tested with `exists()`, not `is_dir()`, because a worktree or submodule has
  it as a file — and stopping at a worktree's own root is right, since a worktree is its own
  checkout with its own state. A project that is not a git repository still falls back to the
  cwd; there is nothing better to offer, and `status` is unaffected either way because its
  root arrives in the status-line payload.
- **A saved reference must be indexed.** The `post-edit` hook (PostToolUse) blocks when a
  file written inside the refs dir is not named in that directory's `AGENTS.md`. A
  reference nothing points at is one the next reader never finds, so the index is part of
  the save, not a courtesy. It runs *after* the write, not as a PreToolUse gate: the
  natural order is save-then-index, and blocking the save would demand an index row for a
  file that does not exist yet. Matching is a substring search for the file name anywhere
  in the index — the index is prose a human maintains, so pinning the check to a table
  layout would fail the first time someone reformats it. `AGENTS.md` and its `CLAUDE.md`
  shim are skipped (`_REFS_INDEX_SKIP`) or writing the index would trip its own hook.
  The check itself is `refs_index_gap`, shared by both hosts: Claude reaches it through
  `post-edit`, Codex from its single PostToolUse adapter. This one stays a
  `decision: "block"` rather than `additionalContext`: it is unfinished work, not
  guidance.
- **The Simple output style is opt-in, and nothing may depend on it.**
  `output-styles/simple.md` omits `force-for-plugin` (which defaults to false), so enabling guard does not
  switch a user's output style — they select **Simple** in `/config` (or set
  `outputStyle`) themselves. Deliberate: the style rewrites how every answer in the
  session is written, which is too large a change to impose on someone who installed
  guard for its gates. The consequence is a rule for authors — no guard behavior may be
  implemented in the style file, because it is inactive for most users. Anything that
  must always hold goes in the SessionStart context (`guard_hook.py`)
  or an agent definition. Note the style also does not reach subagents at all: per the
  official docs a subagent runs its own system prompt, which is why
  `agents/simple-explainer.md` carries its own copy of the explain-clearly rules rather
  than inheriting them.
- **Eligibility is mechanical; selection is the router's.** The four agent modes and one
  prerequisite (a `reads="files"` agent needs a source file the turn actually wrote, since
  that list is its whole input and the router cannot invent one) decide what the router may
  choose from. Nothing else. In particular there is no Hangul-ratio test for
  `korean-corrector`: deciding whether a response is Korean enough to audit is a reading
  task, and a ratio has to guess how many English identifiers a Korean answer may carry
  before it stops counting as Korean.
- **`reads="prompt"` is outside the turn-end machinery entirely.** `refs-finder` works on
  the question before an answer exists, so `_eligible_agents` drops it and the router never
  sees it. The exclusion is there and nowhere further downstream on purpose: `cmd_stop`
  filters `routed`/`direct` on the other two values and would drop it anyway, but `eligible`
  is also what decides whether Stop emits at all — leaving it in makes a turn look routable
  on the strength of an agent that already ran, and the Codex adapter, which shares that
  function, would fold it into its own recommendation. Two more places test `reads` for the
  same reason: `_reads_turn` (so `refs-finder` alone never asks the session to write an
  answer file nothing reads) and the SessionStart "audits are on" line (so a project running
  only `refs-finder` is not told it has an audit).
- **`comment-corrector` is never routed.** The Stop hook splits the eligible set by `reads`:
  the `reads="turn"` agents go to the router, and `comment-corrector` is dispatched directly
  in the same emission, to be sent in the same message so the two run concurrently. Two
  reasons, and the second is why this is a split rather than the narrower "skip the router
  when it is alone".

  Triage asks whether there is material for an agent, and for this one that is a diff-level
  question — logic changed, or only a rename or a formatting pass. The router cannot answer
  it from what it is given: the file list is the corrector's input, not a diff, and reading
  those files would show their current state, never what this turn changed in them. So the
  hop can only restate what `_eligible_agents` already decided, and bill a subagent for it.

  Nor does it need to wait. The ordering rule in the playbook's `Dispatching` — auditors
  before correctors — exists so a corrector does not rewrite a sentence an auditor was about
  to flag, and it is entirely about the **answer file**. `comment-corrector` never opens that
  file; it edits comments in source. It shares no input with the routed agents, so there is
  nothing for it to be ordered against and no round trip to pay.

  Consequences worth keeping straight: `agents/router.md` has no `comment-corrector` section
  and candidate lines carry no paths, which restores its "record missing → pick nothing" rule
  to always-correct (the router is now dispatched only when an answer file exists). And a
  dispatch of `comment-corrector` alone names no answer file at all, which the playbook's
  `Presenting the result` has to branch on — there is nothing to correct and nothing to open.
- **The session mute is not `audit_gate` coming back.** `/guard:toggle` adds one boolean in
  front of the switches, which is the shape removed below, so the difference has to be
  stated or it reads as a regression. Three things differ and all three are load-bearing.
  It is **session-only** — `audit_paused` lives in `state/<sid>.json` and the code has no
  path from it to guard.local.json — so it cannot answer the question "what does this
  project do by default" differently from the switches. It is **two-valued**, so there is no
  `ask` to reason about. And it is **visible**: the `status` subcommand puts it in the user's
  status line, which is what the old gate never had. That last one is the real fix. The old
  gate's cost was not the extra layer; it was that you could not tell which state you were
  in without going and reading a file. A mute you can see costs nothing to hold in your
  head. If the indicator ever becomes impossible to ship, delete the mute rather than let it
  go invisible.

  What it does NOT suppress is deliberate: `pending_verify_prompt_id` and the answer file are
  still written while muted, so `/guard:claims-auditor` works on the turn the user just
  muted. Muting is "stop recommending", not "refuse to audit".

- **The per-agent settings are the only control, and each is named after its agent.**
  There is no gate in front of them. `audit_gate` (`off`/`ask`/`auto`) used to be one, and
  removing it removed a whole class of question — "the switch is on but is the gate open,
  and does `ask` mean the user is asked before or after routing" — that the user had to
  hold in their head to predict what guard would do. Now: an agent not `off` means it can
  be recommended; every switch `off` means guard emits nothing and makes no model call, which
  is what `audit_gate off` used to mean. Every switch ships `off`, so installing guard does not
  start auditing; and the key is the agent's own bare name, so `settings set
  korean-corrector reuse`, `/guard:korean-corrector`, and
  `subagent_type: "guard:korean-corrector"` are one string. Renaming an agent means
  renaming its directory under `agents/`, its skill directory and `name:`, its
  `AUDIT_AGENTS` key, its `hooks.json` matcher, and `_CONTROL_CMD_RE` — together, or the
  vocabulary splits again.
- **The value is a mode, not a boolean, so reuse cannot disagree with the switch.**
  `AgentMode` is `off` / `fresh` / `reuse`, and how an agent runs is therefore the same
  setting as whether it runs. The alternative — a boolean per agent plus a `reuse_agents`
  list — allows a state that means nothing (an agent named in the reuse list while it is
  switched off) and forces every reader to consult two keys to answer one question. The
  boolean CLI words survive as aliases (`on` → `fresh`, `off` → `off`) because that is
  what a setting here has always been set with, and `on` has to keep meaning something:
  it means the mode every agent definition was written for.
- **Reuse trades independence for continuity, which is why it is a setting and not a
  default.** A reused instance already knows the repository and the session's conventions,
  stops re-deriving the same thing every turn, and can be asked follow-ups ("you cleared
  this claim two turns ago — does the change I just made break it?"). A fresh instance
  cannot inherit its own mistake: a verdict a reused instance got wrong sits in its history
  as settled, and every later turn is built on it. Continuity is worth most where the
  judgment is about text and conventions (the correctors); independence is worth most where
  it is about whether something is true (the auditors). guard states the trade-off and lets
  the user choose it per agent; it does not pick sides by defaulting one of them on.
  Two consequences in the agent definitions: each of the four carries an "If you are
  resumed" section telling it to judge the record it was just handed rather than remember a
  verdict, and the "fresh context" wording had to become "by a reader rather than its
  author" — that is the guarantee reuse preserves, where an empty context is not.
- **Reuse is per session, and guard cannot see the instances.** Subagent transcripts live
  under the session id (`wiki/ref/claude-code-subagent-resume.md`), so a new session starts
  every agent fresh whatever the config says, and guard has no handle on a running
  instance: no registry, no way to stop one. Two things follow. The instance name is
  *derived* (`_instance_name` → `guard-<agent>`), so both sides can name it without either
  tracking it. And a mode change away from `reuse` has to be *reported* — `cmd_settings`
  prints a stand-down note and the settings skill relays it — because the session holding
  that instance is the only party that can retire it. The standing policy is stated
  once at SessionStart instead, so the per-turn text carries only the mechanic.
- **Memory is what the agent knows about the project; reuse is what the instance saw this
  session.** Both exist, they are different axes, and neither substitutes for the other.
  The audit agents carry `memory: local` — conventions, where the answers live, a
  correction the user rejected. The docs recommend `project`, and for an agent a team wrote
  for itself that is right; guard is installed from a marketplace and runs in repositories
  it does not own, where `project` would create files that land in someone else's commits
  and pull requests without their asking. `local` is the reversible default: a team that
  wants the knowledge shared changes one word in the agent. Note that neither scope is
  gitignored for free — in this very repo `.claude/agent-memory-local/` is not matched by
  any ignore rule, so "not meant for version control" is an intent the project still has to
  enforce. Three rules hold this together and each one is a failure mode if dropped: the Write/Edit that `memory` enables is bounded IN PROSE to the memory directory,
  because the frontmatter cannot express it and the two auditors are otherwise read-only; a
  remembered claim is re-checked before it is relied on, since memory records where to look
  and never what is true; and nothing in guard reads or writes those directories, so a user
  with auto memory disabled loses accumulated knowledge and nothing else.
- **The router has no memory, for the same reason it is never reused.** A remembered habit
  ("this project rarely writes Korean") is indistinguishable from a judgment about this
  turn, and routing is the step nothing else checks.
- **The router is never reused.** Its question is about one turn; an instance carrying the
  last five can answer it from the wrong one, silently, at the step nothing else checks.
- **The router is not the place to save on model.** `agents/router.md` defaults to `opus`.
  Every other agent in the set is paid for by a decision this one makes, so a cheap router
  that misreads a turn saves nothing: it either omits the agent that would have caught the
  defect, or spends a whole subagent for each agent it named on material that was not
  there. The second compounds — it is what teaches the user to wave the recommendation
  through unread, after which the omissions stop being caught either. The triage itself is
  a short read of two files, so the model is the cheap part of it. `router_model` still
  overrides per project, in the direction a project chooses.
- **Reuse needs `SendMessage` in the agent's `tools:`, and the router must not have it.**
  `tools` is an allowlist when present (`wiki/ref/claude-code-subagent-frontmatter.md`), so
  the audit agents list `SendMessage` and the router does not. This also fixes an older
  inconsistency: the auditor definitions have always said "ask the main session where to
  look", with no tool to ask with. The discipline they already carry is what keeps that
  safe — ask for a pointer, then look yourself, because an answer from the turn's author is
  a claim, not evidence. The router is excluded on purpose: it triages what it was handed
  and has nothing to negotiate.
- **The agent settings govern what guard says unasked, never what the user may ask for.** Each
  per-agent command has its own `UserPromptExpansion` matcher and passes its agent name to
  `cmd_verify` in argv; `_dispatch_context` dispatches exactly that one agent. It does not
  consult the mode's on/off-ness at all — refusing `/guard:korean-corrector` because it is `off`
  would take away the only way to check the very thing a project keeps off by default,
  which is the main reason to keep it off. `pending_verify_prompt_id` is only a "has a turn
  finished yet" check there; the agent gets the turn from the main agent like any other.
  `AUDIT_AGENTS[...].verify_command` is what keeps `comment-corrector` out of that path: it
  has a skill but no turn-record command, since its input is files rather than the turn.
- **Earlier evidence is in scope, and it is asked for as inclusion, not selection.** A
  claim made in this turn is often grounded by a command run three turns ago, and an
  auditor that never sees it reports a backed claim as unbacked — the false positive that
  teaches the user to stop reading guard. So the record's evidence section explicitly
  reaches past the turn. But "include what is relevant", asked of the claim's own author,
  invites picking exactly the evidence that supports it. Hence the three-part shape of
  `TURN_CONTEXT_INSTRUCTION`: err toward including, keep your argument for why the claim
  holds out of the file, and — on the reading side — `claims-auditor` treats that section
  as evidence *offered* and checks the repository itself before calling anything
  unsupported. Do not soften this into "summarize the relevant context": a summary of
  evidence is an argument about evidence.
- **The dispatch passes only what the agent cannot obtain itself.** That is the answer
  file's path — nothing more. Not the refs directory: the
  agent resolves it with the `refs-dir` subcommand. Not the repository: it is the working
  tree the agent already runs in. Not a transcript path: a pointer an agent cannot use is
  one it may chase anyway. Not a summary of the turn either, from guard or from the main
  agent — priming an audit with the author's own account of the work is how an unexamined
  claim becomes an established one, and it is why the record's own instruction forbids
  summarizing rather than merely asking for the text. `comment-corrector` is the one agent
  handed something other than the turn record, for the same reason: it audits files, and
  the list of files this turn edited is exactly what it cannot work out for itself (its own
  skill refuses to guess). `session_id` / `prompt_id` stay parameters of the dispatch
  builders because they build those paths; they are never handed to an agent. When an agent
  needs something else, it asks the main session where to look and then looks itself — an
  answer from the turn's own author is a claim, not evidence.
- **The turn record is split by who can be trusted with which half.** It travels as a file
  because a routed turn has up to five readers (the router, then the agents it names) that
  must all see the *same* text, and pasting it into each dispatch means the main agent
  writing its own turn out several times — which is where a turn quietly becomes a
  paraphrase of the turn. Ownership follows from what each party can actually vouch for:
  - guard writes the **response** section, at every Stop, from `last_assistant_message` in
    the payload. It is the text being audited, so it is the one part that must not pass
    through the author's hands — and guard is handed it for free. It stopped cutting the
    turn out of the transcript, but it never had to give up this piece.
  - the main session appends **request, tool activity, and prior evidence**, because guard
    cannot see any of it: it has no slice any more and no window past this turn.
  The `_write_turn_response` failure path is silent and the instruction says "create the
  file if it is missing", so a scratch-file error costs at most the verbatim guarantee, not
  the recommendation.
- **File or prose is a per-case choice.** A file earns its place when the text has several
  readers who must all see the same thing (the turn record) or is long enough to crowd out
  the message carrying it (the Korean rewrite, `comment-corrector`'s report — which is why
  that agent holds `Write` despite editing in place). Everything short and single-hop stays
  prose: the roster, the edited-file list, the router's picks and reasons. Routing a
  two-line verdict through a file only adds a read. The two auditors hold no `Write` at
  all: their output is a short fixed-shape `<report>`, and granting a write path to an
  agent whose whole contract is "changes nothing" would cost more than the context it saves.
- **Two agents report; two correct.** `claims-auditor` and `deferrals-auditor` are
  read-only by design — their findings need a human decision about the *work*, and an
  agent that rewrote a claim to match the evidence would be laundering the failure it was
  dispatched to surface. Korean and comments are different: the finding *is* the fix (this
  phrase reads wrong → this is what it should say), so `korean-corrector` and
  `comment-corrector` carry the repair. The `-auditor` / `-corrector` suffix is the
  contract, so keep it honest — an agent granted `Edit`/`Write` on what it audits must not
  be called an auditor. The consequence: `comment-corrector on` means unattended edits to
  the files the turn just wrote, which is why its dispatch text tells the main agent to
  relay what was left unfixed.
- **`clarity-auditor` audits against a reader, and says so when it has none.** Its three
  axes are not symmetric in what they need. "Is there a concrete example" is answerable from
  the answer alone. "Is this term unexplained" needs the session — a term defined two turns
  ago is defined, and the windowed `transcript find --until <this turn>` is the only way to
  know, because an explanation *later* in the session could not have helped a reader reading
  this turn. "Is this pitched right" needs the reader profile and nothing else can substitute.
  So with no profile it runs axes 1 (narrowed to terms the answer itself leaves undefined)
  and 2, reports `profile: MISSING`, and skips axis 3 by name. The alternative — picking a
  level — fails in both directions at once: assume a beginner and every technical term is a
  finding, assume an expert and nothing ever is. A named gap is the only honest state, and it
  is also the one the user can fix (`/guard:reader-profile`).

  Two consequences. The profile is `memory: user`, the only non-`local` memory in guard,
  because it describes a person rather than a checkout. And it is only ever written from what
  the user said — never inferred from the repository, since the code someone works in is not
  evidence of their vocabulary, and a guess written to memory becomes a calibration fact for
  months.

- **Both correctors edit in place; only their targets differ.** `comment-corrector` edits
  the source files the turn wrote, `korean-corrector` edits the answer file. That the second
  one is possible at all is the point of the answer file: when the corrector's input was a
  transcript of prose the assistant had already said, a correction could only be a new
  artifact the user then had to be talked into reading, and the rewrite (`.ko-fix.md`) plus
  the relay of its path existed for that reason alone. An answer the user has not read yet
  can simply be fixed, one `Edit` per finding, which also makes the diff the findings. Do
  not reintroduce a rewrite file.
- **Recommend once per turn, and spend the marker before emitting.** Two independent
  guards: `stop_hook_active` covers the ordinary continuation, and
  `last_audited_prompt_id` covers what it cannot — the recommendation asks the main agent
  to dispatch background agents, each of whose completions opens a transcript turn of its
  own, and the marker does not depend on the payload flag surviving that. It is written
  *before* the emit, so a turn whose first recommendation is still being acted on cannot
  collect a second. Codex spends its marker only after filtering to agents it actually has,
  since marking a turn audited for a message never sent burns the turn's one chance.
- **Codex shares eligibility, not the router.** `core._eligible_agents` is common, so both
  hosts agree on what an agent is *available* for. The router is not shared, and the reason
  is no longer a missing binary: Codex ships **one** named agent (`guard_claims_auditor`,
  installed by `$guard:setup`), and a router that can only forward to that same agent
  decides nothing. So Codex recommends the whole eligible set, unrouted and correspondingly
  noisier, rendering the choice as a scope sentence via `_SCOPE` in the adapter. A key
  absent from `_SCOPE` is dropped, which is how `comment-corrector` stays Claude-only while
  the eligibility code stays host-agnostic. Codex also keeps its own turn record
  (`_save_turn`), unlike Claude, because its transcript is not a stable hook interface —
  the caps for that record (`TOOL_CONTEXT_MAX_CHARS`, `TOOL_RESULT_MAX_CHARS`) live in the
  adapter for the same reason. Reuse is Claude-only too, and for a plainer reason: the
  mode's whole mechanism is a named instance addressed with `SendMessage`, and the Codex
  adapter has neither. `core._eligible_agents` only asks whether a mode is `off`, so a
  `reuse` value costs Codex nothing and means nothing there. Closing either gap means
  giving Codex the agent set first, not adding a router; keep `_SCOPE` as the seam and do
  not push host detail into `_eligible_agents`.
- **Assistant tool output is first-class evidence, and the auditor fetches it itself.** A
  claim that restates or follows from a command this turn ran is supported without a
  re-cite — but the answer file holds only the answer, so the auditor gets that output from
  a `transcript turn` extract rather than from the record. Two rules that used to live here
  are gone and should not come back by habit. The record no longer carries a tool-activity
  section, so nothing asks the turn's own author to assemble the evidence it will be judged
  on. And a user-run `!` command no longer disqualifies its turn *on evidence grounds*:
  that skip existed because guard cut the slice itself and the `!` output landed *after* the
  response an audit would judge, so evidence arrived later than the claims. guard cuts no
  slice at Stop, so that ordering problem is gone.
- **A `!`-opened turn is skipped anyway, for a different reason: it has no answer file.**
  `UserPromptSubmit` does not fire for a `!` command — it is not a prompt — so no draft path
  is ever named, and audit-then-*correct* needs the answer to exist somewhere editable while
  the turn is still running. What Stop would hand an auditor is the fallback copy it just
  made of an answer already printed to the user, which no correction can reach. Such a turn
  also carries no `origin` field at all, so the `origin_kind` skip lets it through and
  `_turn_identity` reports it separately (`bash_input`, matched on the `<bash-input>` anchor).
  Verified in 2.1.239, session 6bc60bbf: every turn in that transcript was handed a draft
  path except the `!` one, and the router was dispatched at a file the user never saw. Like
  the control-command skip, it lands BEFORE the record write so a `!` turn cannot displace
  the user's real question as `pending_verify_prompt_id`. Re-establish this reason, not the
  old one, before removing it again: if `UserPromptSubmit` starts firing for `!` commands,
  the skip has no basis left.
- **`_safe_project_subdir` is guard's self-neutering defense** for the one config key that
  names a directory guard treats specially (`refs_dir`): strictly inside the project (the
  root itself fails, because a path is never in its own `.parents` — this is what rejects
  `"."`), and never guard's state root, a path under it, or the config file. Without it a
  `refs_dir` of `.claude/guard` would make guard's own state a directory it invites the
  model to write into, and `.claude/guard.local.json` would put the agent settings there.
  Keep it one implementation; two copies means one of them gets fixed.
  **What it deliberately does not catch: an ANCESTOR of guard's state.** `.claude` is
  neither the state root nor under it, so it is a legal value — the rule is containment,
  not reachability, and anything else that starts trusting a configured directory has to
  bring its own check on the actual target rather than assume this one covered it.
- **The config-mutating CLI can weaken guard, and Bash is ungated.** `settings set
  claims-auditor off` reaches guard's own configuration, and the model can invoke this
  script through Bash — nothing stops it. `_cli_write_allowed` requires a marker
  (`GUARD_SETTINGS_SKILL`) that only the user-invoked `guard:settings` sets, on every
  mutating verb. Since that skill became a `context: fork` one the marker is set by the
  forked agent rather than by the main one, which changes nothing here — it was always a
  model setting it, and the guarantee was always "the chain began at the user's entry
  point", never "no agent did this". A custom `tools: Bash` agent would have made
  hand-editing the config impossible rather than forbidden; it was built, then dropped as
  one more definition to keep in step with a file that already says all of this. The skill
  sets `disallowed-tools: Write Edit NotebookEdit` in its place, but whether that reaches
  inside a fork is undocumented, so the standing prohibition in the skill body remains the
  thing actually holding. (`allowed-tools` is not an option: per the docs it pre-approves
  and "does not restrict which tools are available".)
  **This is a speed bump, not a boundary**: the variable name is in the source the model
  reads. It buys that the unreflective path ("this audit is in my way, let me turn it
  off") fails closed, that the refusal names the user as the only legitimate widener, and
  that attempts land in the trace as `refused_no_skill_marker`. A model that deliberately
  sets the marker is outside guard's threat model — and the Bash call is visible to the
  user either way. Read verbs (`list`, `show`) need no marker.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. Only keys whose value matches the
default's type are honored; unknown
keys are ignored and a missing or malformed file falls back to every default.
`guard.local.json.example` ships at the plugin root.

Keys: one `AgentMode` per agent, named after that agent — `claims-auditor`,
`deferrals-auditor`, `clarity-auditor`, `korean-corrector`, `comment-corrector`,
`refs-finder`, **all default `off`** — which together are the only control over whether
guard says anything unasked. `refs-finder` is the only one of them that governs something
said *before* an answer rather than after; the key behaves identically, which is the point
of putting it in the same registry. See the
invariants above for why the value is a mode rather than a boolean, why reuse is the user's
call, and why they all ship off. A value that is not a mode word reads as `off` — the safe
direction, since the alternative is guard acting on a setting the user did not write.

One subtlety `_load_config` must keep: an `AgentMode` default round-trips through JSON as a
plain `str`, and `isinstance("reuse", AgentMode)` is False, so the accepted type is widened
to `str` for those keys. Without that widening every mode in the file is dropped and only
the session state is ever honored — which is exactly the bug this shape introduced once.

`router_model` (string, default `""`) — a model override for the router agent alone. Empty
means guard prints no model line at all and `agents/router.md` decides, which is where a
subagent's model normally comes from; the key exists for a project that wants the router
cheaper or sharper than the plugin ships it. When set, the line is worded as an instruction
to pass `model:` on the router dispatch rather than as a bare value, because it is the one
field the main agent acts on before the playbook is opened — nothing downstream could
explain it (see `_router_context`). It is never validated against a list of names
(an alias, a full id, and a provider's own name are all legitimate, and the set moves).
Every agent the router names brings its own model and effort from its own frontmatter in
`agents/`, which is also where its criteria live — a second copy in guard's config would
let the two disagree about the same agent.

Getting the router's model wrong costs in both directions, which is why the default is left
to the agent rather than pinned to the cheapest thing that runs. A router that misses means
the audit silently never happens — the exact failure guard exists to prevent. A router that
cannot tell a backed claim from one that merely sounds backed names every agent every turn,
which is the same as naming none, because the user stops reading the recommendation.

`refs_dir` (string, default `""`) — project-relative directory for guard's cited-doc
copies; empty = the git-tracked default `wiki/ref/` (references committed with the repo), a
different tracked path (e.g. `"docs/refs"`) overrides it; commits stay in the user's normal
workflow (guard never commits). `_refs_dir` validates the value (see `_safe_project_subdir`
above) and everything that names the location follows it: the `post-edit` index check, the
claims auditor's own resolution (via the `refs-dir` CLI subcommand), and the SessionStart
context line, which states the refs rule to the agent and names the resolved path (also
exported as `GUARD_REFS_DIR` via `$CLAUDE_ENV_FILE`, per the official hooks docs, so a Bash
caller resolves it with one `echo`). The output style carries no refs instruction: it is
user-selected (no `force-for-plugin`), so nothing load-bearing may depend on it being
active. guard fixes no reference-mark syntax — `claims-auditor` is told to check that a
mark *resolves*, never to grade its form.

`settings unset <key>` is the only way a key leaves the file, and it exists because `set`'s
preserve-everything rule has no other exit. A key guard stopped honoring — `exempt_skills`,
`audit_gate` — is invisible to `show`, ignored by `_load_config`, and carried forward by
every `set` indefinitely; since the file may only be written through this CLI, without this
verb the only way to clear one is the hand-edit the settings skill forbids. Two things about
its shape are deliberate. It deletes **any** key, live or dead, rather than pruning what it
judges stale: guard cannot know which keys a newer version owns, so a downgraded user's
config would be silently destroyed. And deleting an agent switch goes through the same two
steps a `set` does — the session's cached mode is reset to the default and a `reuse`
transition is reported — because reverting a switch is a change to what guard does, not just
to the file, and the instance left running still has to be told to stand down.

## Manual testing

**Everything the hook does is deterministic and runs without the CLI or auth.** That is new:
the router used to be a real `claude` child, so testing meant tolerating a model's
nondeterminism and a 5-11s wait per turn. It is a subagent now, so the hook's whole job is
eligibility plus text generation, and every case below is an exact assertion.

What this recipe can no longer check is the routing itself — whether the router picks the
right agents. That lives in `agents/router.md` and is exercised by using guard, not by this
script. What it does check is that the router is *asked* correctly: the right candidates,
the same turn-record path for every agent, and nothing offered that is set to `off`.

```bash
export CLAUDE_PROJECT_DIR=/tmp/guard-test/proj
export CLAUDE_PLUGIN_ROOT=/path/to/plugins/guard
export GUARD_TRACE=1
H="$CLAUDE_PLUGIN_ROOT/scripts/guard_hook.py"
# From scratch every time: the recipe leans on the once-per-turn guard, so a leftover
# state file from a previous run turns the recommendation checks silently into no-ops.
rm -rf "$CLAUDE_PROJECT_DIR"; mkdir -p "$CLAUDE_PROJECT_DIR/src"
T=/tmp/guard-test/tx.jsonl; : > "$T"

# The transcript is still needed, but only for the turn's ANCHOR: `stop` reads how the turn
# was opened (origin kind, command name) and nothing else.
anchor(){ printf '{"promptId":"%s","origin":{"kind":"%s"},"message":{"role":"user","content":"%s"}}\n' \
  "$1" "${2:-human}" "${3:-q}" >> "$T"; }
run(){ anchor "$1"; echo "{\"session_id\":\"s1\",\"prompt_id\":\"$1\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"$2\",\"stop_hook_active\":false}" \
  | "$H" stop | python3 -c 'import json,sys;d=sys.stdin.read();print(json.loads(d)["hookSpecificOutput"]["additionalContext"] if d.strip() else "(EMPTY)")'; }

"$H" settings show --session s1        # read verbs need no marker
export GUARD_SETTINGS_SKILL=1         # mutating verbs do — see _cli_write_allowed

# All switches off (the shipped default): NOTHING is emitted, but the pending target must
# still be recorded or every /guard:* audit command breaks in the state guard installs in.
run p0 "Redis is always faster."        # -> (EMPTY); trace: none_eligible
python3 -c "import json;print(json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'))['pending_verify_prompt_id'])"

# guard writes the response section itself, on EVERY Stop, whatever the modes say. This is the
# verbatim guarantee — check it survived, including multi-line and non-ASCII text.
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/p0.md"
#   -> "## Assistant response (written by guard, verbatim)" holding the exact response,
#      then the empty "## Request, tool activity, and prior evidence" section.

# One agent not-off is guard on. Check the shape, not just non-emptiness:
"$H" settings set claims-auditor fresh --session s1     # "on" is an accepted alias
"$H" settings set korean-corrector fresh --session s1
run p1 "Redis는 Postgres보다 항상 빠릅니다."
#   -> one imperative plus fields: the playbook path, the answer file, exactly two
#      candidates with their modes, and the transcript + turn id. Nothing here describes
#      what an agent does, how to dispatch it, or what to do with its report — those are
#      the playbook's, and the router's answer is what names the sections.
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/p1.md"
#   -> the second section reads "Not collected" and carries the ask for earlier evidence
#      plus the ban on the main agent's own case for the claim. Nothing collected it.

# The roster must never offer a switched-off agent. The playbook is the second bound: a key
# the router invents has no section to follow.
"$H" settings set korean-corrector off --session s1
run p2 "Redis는 Postgres보다 항상 빠릅니다."   # -> claims-auditor is the only candidate

# The CLI verbs must not depend on the cwd. `CLAUDE_PROJECT_DIR` is absent in Bash, so this
# is the normal case, not an edge one: all three must agree from anywhere in the checkout.
for d in . plugins/guard wiki/ref; do (cd "$CLAUDE_PROJECT_DIR/$d" 2>/dev/null && \
  "$H" settings show --session s1 | head -2 && "$H" refs-dir); done
#   -> identical settings and the same absolute refs dir from every cwd. Before the fix the
#      subdirectory runs reported an all-off project and refs-dir printed nothing at all.

# The export, and its append-once rule. Run session-start three times (startup + two
# compactions) against one env file: TWO lines, not six.
EF=$(mktemp); CLAUDE_ENV_FILE="$EF"
for i in 1 2 3; do echo '{"session_id":"s1"}' | CLAUDE_ENV_FILE="$EF" "$H" session-start >/dev/null; done
cat "$EF"    # -> export GUARD_PROJECT_DIR=... and export GUARD_REFS_DIR=..., once each
( . "$EF"; cd / && "$H" refs-dir )   # -> the project's refs dir, from outside the checkout
find "$CLAUDE_PROJECT_DIR" -type d -name guard -path '*/.claude/*' -not -path "$CLAUDE_PROJECT_DIR/.claude/*"
#   -> empty. Anything here is a state tree written outside the project root.

# The request file: written verbatim by `user-prompt`, and the ONLY thing the dispatch adds
# for it is a `request file:` line — for the router, never for an audit agent's dispatch.
# Without a `user-prompt` for the turn there is no such file and no such line, which is the
# resumed-session / `!`-command case.
echo '{"session_id":"s1","prompt_id":"pq","prompt":"refs-finder는 켜줘"}' | "$H" user-prompt
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/pq.request.md"   # -> header, then the prompt verbatim
run pq "Turned it on."      # -> `turn dir:` once, then `{turn dir}/pq.md` and `{turn dir}/pq.request.md`
run pnone "Turned it on."   # -> same shape MINUS `request file:` (no user-prompt ran)
echo '{"session_id":"s1"}' | "$H" verify claims-auditor
#   -> no `request file:` line, ever, and a PLAIN absolute answer path: an audit agent gets
#      one file, so there is no shared prefix to factor out and no placeholder to resolve.

# The answer file is gated on the agents that READ it. With only `comment-corrector` on,
# `user-prompt` says nothing and the dispatch carries no `answer file:` line — that agent
# reads source files. On-demand audits still work: the record holds guard's verbatim
# response section plus a note saying the turn was never told to write into it.
"$H" settings set claims-auditor off --session s1
"$H" settings set comment-corrector on --session s1
echo '{"session_id":"s1","prompt_id":"pc","prompt":"rename a variable"}' | "$H" user-prompt   # -> nothing
echo "{\"session_id\":\"s1\",\"prompt_id\":\"pc\",\"tool_input\":{\"file_path\":\"$CLAUDE_PROJECT_DIR/src/cache.py\"}}" | "$H" post-edit
run pc "Renamed it."   # -> playbook, candidates, `files for` — and NO `answer file:` line
"$H" settings set claims-auditor fresh --session s1     # both on -> the line is back

# comment-corrector needs a source file the turn actually WROTE, and the file must exist.
echo 'x = 1' > "$CLAUDE_PROJECT_DIR/src/cache.py"
"$H" settings set comment-corrector on --session s1
for f in src/cache.py notes.md; do
  echo "{\"session_id\":\"s1\",\"prompt_id\":\"p3\",\"tool_input\":{\"file_path\":\"$CLAUDE_PROJECT_DIR/$f\"}}" | "$H" post-edit
done
python3 -c "import json;print(json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'))['edited_files'])"  # cache.py only
run p3 "Refactored the cache."          # -> comment-corrector offered, "this turn wrote: cache.py"
run p4 "Refactored the cache."          # -> claims-auditor only: p4 wrote nothing

# Recommend-once: a second Stop on the same prompt_id is silent even with
# stop_hook_active false.
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p4\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"x\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: skip_already_recommended

# Only a turn a person typed is audited. A background agent's completion and a subagent's
# SendMessage both open turns of their own, and both are turns guard's own dispatch caused —
# auditing either recommends an audit of guard auditing, without end. A kind guard has never
# seen must skip too; an absent kind must still audit, or guard goes silently dormant.
anchor p5 task-notification '<task-notification>done</task-notification>'
anchor p5b peer 'Another Claude session sent a message: <agent-message from="guard:claims-auditor">where is X?</agent-message>'
anchor p5c cron 'scheduled'
for p in p5 p5b p5c; do
  echo "{\"session_id\":\"s1\",\"prompt_id\":\"$p\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"the agent reported\",\"stop_hook_active\":false}" | "$H" stop
done
#   -> all three empty; trace: skip_nonhuman_turn with origin_kind naming which
#   -> and no turn record written for any of them: `ls .claude/guard/turns/s1/` has no p5*

# No `origin` at all is the fail-open direction and must still audit (`anchor` always writes
# one, so this anchor is hand-rolled).
printf '{"promptId":"p5d","message":{"role":"user","content":"q"}}\n' >> "$T"
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p5d\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"Redis는 항상 빠릅니다.\",\"stop_hook_active\":false}" | "$H" stop
#   -> a recommendation, NOT empty

# guard's own control turns are skipped by command name, and leave no record behind —
# `pending_verify_prompt_id` must still name the turn BEFORE this one.
anchor p6 human '/guard:settings show'
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p6\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"guard on\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: skip_control_cmd; no .claude/guard/turns/s1/p6.md

# A user `!` command opens a turn with no `origin` and no draft path, so it is skipped on the
# `<bash-input>` anchor — and leaves no record, for the same reason p6 leaves none.
printf '{"promptId":"p6b","message":{"role":"user","content":"<bash-input>env | grep CLAUDE</bash-input>"}}\n' >> "$T"
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p6b\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"환경변수 확인만 하신 것으로 보입니다.\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: skip_bash_input; no .claude/guard/turns/s1/p6b.md

# Reuse mode changes the dispatch line, not the inputs, and the CLI must report the
# transition in both directions — that print is guard's only channel to a live instance.
"$H" settings set korean-corrector reuse --session s1
#   -> settings, then a note naming `guard-korean-corrector` and how to address it
run p9 "Redis는 Postgres보다 항상 빠릅니다."
#   -> korean-corrector's block says: SendMessage `guard-korean-corrector` if it exists,
#      else dispatch with name: "guard-korean-corrector". RESUME BEFORE DISPATCH — the
#      other order spawns a second instance under a taken name.
echo '{"session_id":"s1"}' | "$H" session-start
#   -> the standing reuse policy, stated once, naming that instance
"$H" settings set korean-corrector fresh --session s1
#   -> a stand-down note: stop sending to it, spawn new ones from the next turn
"$H" settings set korean-corrector fresh --session s1
#   -> no note: nothing changed, so there is nothing to retire

# `refs-finder` is announced at SessionStart and never routed. Its three failure modes are
# all "leaked into the turn-end path", so check each end explicitly.
for k in claims-auditor deferrals-auditor clarity-auditor korean-corrector comment-corrector; do
  "$H" settings set $k off --session s1
done
"$H" settings set refs-finder fresh --session s1
echo '{"session_id":"s1"}' | "$H" session-start
#   -> the refs rule, then the refs-finder policy line naming the playbook.
#      NOT the "audits are on" line: nothing here audits anything.
GUARD_HOST=codex "$H" session-start < /dev/null
#   -> the refs rule only. Codex has no refs-finder agent to dispatch.
echo "{\"session_id\":\"s1\",\"prompt_id\":\"pr1\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"done.\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: none_eligible. A prompt-time agent must never make a turn look routable.
echo '{"session_id":"s1","prompt_id":"pr1"}' | "$H" user-prompt
#   -> empty: no agent READS the answer file, so none is named (`_reads_turn`)
echo '{"session_id":"s1"}' | "$H" verify refs-finder   # no output: verify_command=False

# On-demand dispatch must work with every agent OFF — the invariant most easily broken by
# a change to the recommendation path. No router is involved: the user already chose.
for k in claims-auditor deferrals-auditor korean-corrector; do
  "$H" settings set $k off --session s1
  echo '{"session_id":"s1"}' | "$H" verify $k; echo
done
echo '{"session_id":"s1"}' | "$H" verify comment-corrector  # no output: no turn-record command
"$H" verify bogus < /dev/null                               # unknown name -> no output at all

# Unknown keys and unknown values are both rejected outright rather than silently accepted.
"$H" settings set audit_gate off --session s1   # -> error listing the settable keys;
#   `audit_gate` was the old off/ask/auto gate in front of the switches and must stay rejected
"$H" settings set claims-auditor maybe --session s1  # -> error naming off/fresh/reuse

# `unset` is the only way a key leaves the file. It must handle the key that is not there,
# the key guard does not honor, and the live switch whose instance has to stand down.
"$H" settings set korean-corrector reuse --session s1
"$H" settings unset nope --session s1            # -> "nothing to remove", lists keys present
python3 -c "import json,pathlib;p=pathlib.Path('$CLAUDE_PROJECT_DIR/.claude/guard.local.json');d=json.loads(p.read_text());d['exempt_skills']=[];p.write_text(json.dumps(d))"
"$H" settings unset exempt_skills --session s1   # -> "guard does not honor that key"
"$H" settings unset korean-corrector --session s1
#   -> "back to the default ('off')", then the settings, then the stand-down note for
#      `guard-korean-corrector`. Reverting a switch is a change to what guard does, so it
#      owes the same note a `settings set ... off` does.

# The mutating CLI verbs refuse without the marker; reads still work.
(unset GUARD_SETTINGS_SKILL; "$H" settings set claims-auditor off; "$H" settings unset refs_dir; "$H" settings show)
```

Directly unit-testable without any subprocess: `_write_turn_response` (both headings
present, response exact, parent dir created, and a read-only dir returning None rather
than raising), `_turn_identity(path, prompt_id)` on a
fixture JSONL (a typed prompt, a `task-notification`, a slash command, a prompt_id absent
from the file), `_safe_project_subdir(project_dir, value)` on its rejection cases (`"."`,
`".."`, `".claude/guard"`, `"../elsewhere"`, `"/etc"` — all None; a plain subdirectory
resolves), `_eligible_agents(state, edited)` on the `reads="files"` prerequisite, `_parse_mode` /
`_agent_mode` on the aliases and on a junk value (which must read as `off`), `_load_config`
on a mode written into the file (it must survive the type gate — see the Config section),
and `_router_context` / `_agent_pointer`, which must never name an agent outside the
eligible list and must name the playbook path exactly once each.
