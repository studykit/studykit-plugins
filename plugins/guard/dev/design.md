# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py` and the `scripts/guard_core/` package it dispatches into) is the
truth for control flow — this file records *why* the design is shaped this way and the
runtime facts verified against the real CLI, not a line-by-line walkthrough.

## Module layout (`scripts/`)

`guard_hook.py` is the entry point and nothing else: the subcommand table and `main()`. It
keeps that path because the path is a published interface — `hooks/hooks.json`, every
command and agent definition that shells out to the CLI, the turn closeout, and the
Codex adapter all name it. Everything else is `guard_core/`, and each subcommand's own
docstring lives in the module that implements it rather than in a catalogue at the top of
one file, which is where such a catalogue drifts.

Imports run one way only. A cycle is a design error, not a technical one:

```
config -> paths -> turnrec / payload / emit -> transcript
                -> agents -> state -> dispatch -> cmd_* -> guard_hook
```

| Module | Holds |
| --- | --- |
| `config` | the host split, `AgentMode`, the config schema, guard.local.json I/O |
| `paths` | the two project-root resolvers, the state tree's paths, the debug trace |
| `turnrec` | the answer file and the request file beside it |
| `payload` | the hook payload on stdin, and the session id in it |
| `emit` | the three hook-output shapes guard writes to stdout |
| `transcript` | reading the host's transcript, and the `transcript` CLI over it |
| `agents` | the roster, and mechanical eligibility |
| `state` | `state/<sid>.json` |
| `dispatch` | the text handed to the main agent |
| `cmd_turn` | `user-prompt` |
| `cmd_edit` | `post-edit` |
| `cmd_search` | `pre-search` |
| `cmd_stop` | `stop` |
| `cmd_session` | `session-start` |
| `cmd_settings` | `settings`, `refs-dir` |
| `cmd_status` | `toggle`, `toggle-cli`, `status` |

Two rules this layout exists to hold, both of which broke once already:

- **`config` is the only reader of `GUARD_HOST`**, once, at import. The Codex adapter sets
  that variable before importing anything here, so a second reader is a second answer to
  "which host am I". `grep -rn GUARD_HOST scripts/guard_core/` must show one line.
- **Nothing resolves a plugin path by counting `__file__` parents.** `dispatch._plugin_root`
  walks up looking for a directory that *has* the closeout file. A fixed `parent.parent` is a bet
  on a file's depth in the tree, and the split moved this code one level deeper, which
  silently turned every closeout path guard printed into `scripts/hooks/context/…`.

The Codex adapter imports the `guard_core` modules it needs by name rather than through a
single façade, so the layers it leans on are visible in its import block and a name that
moves breaks at import instead of at the call. That is not hypothetical: the façade version
called two turn-record helpers that had been renamed out from under it, and because every
hook there fails open it failed silently for several releases. The adapter also owns the
JSON turn-record format itself — Claude's answer file is markdown the main agent writes, so
there is nothing shared to factor out beyond the state root.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Name the answer file for this turn — Stop is too late for it, since by then the answer is already printed and a printed answer cannot be corrected. Silent (trace only) when every agent is `off`, when `audit_paused` is set, on a control command, and with no `prompt_id`. Also saves the prompt verbatim to `<prompt_id>.request.md` for the router, which is the only copy guard keeps and the only reader it has. The hook stays registered even when silent so a "guard said nothing" report can be told apart from a hook that never ran. |
| `PreToolUse` (`Bash\|Grep\|Glob`) | `pre-search` | Deny a search rooted at the filesystem root: `find /`, `grep -r /`, `rg /` (and `fd`/`ag`/`ack`/`locate`), a `/`-anchored glob like `/*`, or a `Grep`/`Glob` call whose `path` is `/`. Reads the tool ARGUMENT only — never the caller — which is why it survives where the removed `pre-write` hook could not. Ignores the agent switches and the mute. Silent for every other call, and fails open on a command `shlex` cannot parse. |
| `PostToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `post-edit` | Record a source file, an agent instruction file, or a saved reference this turn wrote (the candidate lists for `comment-corrector`, `agents-md-auditor` and `ext-docs-auditor`), then block when a file saved in the refs dir is not listed in that dir's `AGENTS.md`. |
| (called via Bash, not a hook) | `settings` | `guard:settings` (a `context: fork` skill, so it runs in a forked `general-purpose` agent rather than in the main session) shows/sets/unsets guard.local.json settings; the agent modes also apply to the live session's `state/<sid>.json` (session id from `--session`/`CLAUDE_CODE_SESSION_ID`). `set` preserves every other key; `unset <key>` is the only way to delete one. |
| `Stop` | `stop` | Write the response section of the turn record and mark the turn as the on-demand target — always (only Codex reads that marker now; see below). Then, when any agent is not `off`, emit `additionalContext` asking the main agent to dispatch `guard:turn-router` over the record, carrying this turn's paths and the `candidates` command the router runs to get the roster itself. The router names sections of `hooks/context/turn-closeout.md`; the main agent follows those, completing the record's second section only if a named section asks for it. `comment-corrector` never goes to the router: it is dispatched directly in the same emission, to be sent in the same message — see the invariant below. A third block names `ext-docs-auditor` over the refs files the turn wrote; it has no switch, so it can be the only block a turn produces. |
| `SessionEnd` (`clear`) | `session-end` | Hand this session's two switches, and the handover file it recorded, to the session `/clear` is about to open, then let it announce what it adopted. The two halves are independent: writes nothing only when both switches still match this project's `audit-turn` / `audit-plan` AND no handover was recorded. |
| `SessionStart` | `session-start` | Sweep state and turn records past retention, export `GUARD_REFS_DIR` and `GUARD_TOGGLE_CLI`, state the refs rule as session context, say once — when any agent is on — either that the session opened muted (`guard on` arms it) or that audits are on and where the turn closeout is. |
| (called via Bash, not a hook) | `candidates` | The router's own roster: prints the turn-reading agents switched on for this session, one `agent=mode` per line, in `AUDIT_AGENTS` order. `--doc` answers for the document path instead — the same eligibility, mapped through `report_entry`, so an audit with no document-side entry point drops out. Session id from `CLAUDE_CODE_SESSION_ID`, which a subagent's Bash carries as its parent's. Read-only, and the only command the router runs. |
| (called via Bash, not a hook) | `transcript` | `index` / `turn` / `find` over the session transcript, for the audit agents. Writes an extract file and prints only its path plus a one-line summary; `--since` / `--until` / `--last` bound which turns are scanned. |
| (called via Bash, not a hook) | `toggle-cli` | Arm/mute the automatic audit for THIS session (`audit_paused`, session state only — never guard.local.json), from a shell prompt: `on` / `off` / `status` / empty flips. A session opens in whatever `audit-turn` says, armed unless the config says otherwise, so `off` is the direction that usually needs typing. Session id from `CLAUDE_CODE_SESSION_ID`; project from `_cli_project_dir`. The ONE subcommand that does not fail open — see `_MUST_REPORT` in `guard_hook.py`. |
| (called via Bash, not a hook) | `status` | Status-line segment: `guard <will run>/<switched on>` plus the plan gate's flag (`⚑` armed, `⚐` muted), green armed and dim muted on each half; nothing at all on any failure. Reads one state file; runs on every assistant message. |
| (called via Bash, not a hook) | `handover-written` | Record `<path>` as the handover this session wrote, for the `guard:handover` skill to run as its last step. Writes one key into `state/<sid>.json`; the file must exist, so a path that was never written is refused while someone can still act on it. Session id from `CLAUDE_CODE_SESSION_ID`. Fails open — the handover file is the deliverable, and the record only decides whether the next session is offered it. |
| (called via Bash, not a hook) | `refs-dir` | Print the resolved refs directory (auditor fallback; applies `refs_dir` validation). |

## Storage layout (`${CLAUDE_PROJECT_DIR}/.claude/guard/`)

A **turn is the transcript's `promptId`**. guard keeps no copy of a turn's content: it
reads the transcript only for the turn's *kind* (`_turn_identity`), and the turn itself is
written by the main agent.

- `state/<sid>.json` — the session's live agent modes (one key per agent, named after it,
  valued `off`/`fresh`), the per-turn markers keyed on `prompt_id` that keep each once-only action once-only
  (`last_audited_prompt_id`, `pending_verify_prompt_id`), and the turn's edited files
  (`edited_prompt_id` + `edited_files` + `edited_agent_docs` + `edited_refs`). The edited
  lists are stored WITH the prompt_id they belong to, not as bare lists: PostToolUse appends
  and Stop reads back, and without the id a previous turn's files would ride into this turn's
  recommendation. Three lists, one marker — the split is by which agent can judge the file
  (`_edited_bucket`: source code for `comment-corrector`, `AGENTS.md`/`CLAUDE.md` for
  `agents-md-auditor`, anything under the refs directory for `ext-docs-auditor`), while "which
  turn was this" is the same question for all three, and a new turn resets ALL of them or an
  untouched one holds stale files under a fresh id. The refs test is by LOCATION and runs
  first, which is what keeps the buckets disjoint: the refs directory's own `AGENTS.md` index
  and `CLAUDE.md` shim would otherwise be matched by name and sent to `agents-md-auditor`.
  `_read_state` honors only known keys, so a hand-edited or stale file degrades to
  defaults instead of injecting state — which cuts both ways, and a NEW key must be added to
  both the `default` dict and the `keys` tuple. `edited_refs` was added to `default` alone at
  first: every write landed and the next read dropped it, which is indistinguishable from
  PostToolUse never having run. `audit_paused` and `plan_audit_paused` are **seeded from the
  config** on every read — `audit-turn` / `audit-plan`, armed when the file says nothing — and
  are the session's own from then on: the shell toggles write here and never there. See the
  session-mute invariant below. `handover_file` is the odd one out: written by
  `guard-handover` and read by exactly one event, `SessionEnd` on `/clear`. Nothing in the
  turn path touches it, and the session that inherits it never stores it — see the `/clear`
  invariant.
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
- `clear-handoff.json` — what a `/clear`ed session leaves for the session replacing it:
  the two switches, and the handover file it recorded. One file per project, written by
  `SessionEnd` and deleted by the `SessionStart` that reads it. Beside `state/` rather
  than inside it, so the seven-day sweep cannot be confused by a file meant to live for
  milliseconds; its own expiry is `CLEAR_INHERIT_MAX_AGE_SECONDS`.
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

Not state, but part of the same picture: `hooks/context/turn-closeout.md` in the plugin
holds one section per agent — how to dispatch it, what its report means, what to do about
it — and deliberately no `turn-router` section, for the reason under "Text is stored where it is
read". guard's hook output and the router both refer to it by section
name; nothing copies its text. `_closeout_path()` resolves it from the script's own location
rather than `CLAUDE_PLUGIN_ROOT`, because the same script is also the Codex adapter's
library and a plain CLI the settings skill runs over Bash, and only the hook case has that
variable set. That is not in tension with `commands/settings.md` writing
`${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py`: there it is a text substitution Claude Code
performs while building the command, so the path arrives already resolved and the launched
process still sees no such variable in its environment.

State survives session end (a resumed `claude --resume` must keep its flags);
age-based `SessionStart` sweep is the only reaper. The one SessionEnd hook is matched on
`clear` and writes `clear-handoff.json`, which is not session state and not swept with it.

## Verified runtime facts (confirmed against the CLI / real payloads; do not regress)

Re-verify before changing anything that depends on these — they came from real
payloads, not memory.

- **A `PreToolUse` `deny` reason reaches the model verbatim, as the tool's `<error>`
  result** — probed on `claude` 2.1.240, excerpt at
  `wiki/ref/claude-code-pretooluse-deny-reason-visibility.md`. The docs do not state this
  (they only say the reason is shown to the *user* on `"ask"`), which is why it was measured
  rather than assumed. Two consequences: the model **selects and invokes** the tool and only
  then gets blocked, so a deny costs one round-trip rather than zero; and the reason is read as
  tool output, not as an instruction — the probe's child read a "dispatch this agent instead"
  reason, weighed it against its own session instructions, and declined. So a deny can enforce
  a prohibition and can only ever *suggest* a redirect.

  guard had one hook that leaned on this — `pre-fetch`, which denied the main conversation's
  `WebFetch`/`WebSearch` and named the docs agent (then `ext-docs-fetcher`, now
  `docs-finder`) in the reason — and it is gone. The
  measurement above is why the removal costs less than it looks: the half that a deny actually
  enforced was "do not fetch", and the half that mattered, "use the fetcher instead", was never
  more than a suggestion. That half is now carried where a suggestion belongs, in the agent's
  own description. Keep this entry: any future hook that plans to redirect through a deny
  reason is planning on something that was measured not to work.

- **`CLAUDE_ENV_FILE`** — SessionStart hooks receive this env var (a file path);
  `export` lines appended to that file reach all subsequent Bash commands. Source:
  official hooks docs (https://code.claude.com/docs/en/hooks, "CLAUDE_ENV_FILE"),
  fetched 2026-07-09 — docs-verified only, not yet observed on a live session; if
  `GUARD_REFS_DIR` fails to appear, re-check this first.

- **A `SessionStart` entry with no matcher fires on every source**, and the sources are
  `startup`, `resume`, `clear`, `compact` and `fork`. `compact` is the load-bearing one:
  guard's SessionStart hook registers no matcher, so a context compaction that drops its
  injected lines immediately gets them restated. That is the whole reason the refs rule and
  the closeout file pointer can be stated once per session instead of on every `UserPromptSubmit`. The
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
  file, and the closeout file's `Presenting the result` opens that file and forbids starting
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

  **That reading is about Stop, and did not carry to `UserPromptExpansion`.** guard
  registers no expansion hook any more, and this is kept because the two events read
  differently and anyone adding one back will assume they do not. On Stop the two forms are
  presentation — both continue the turn — so the choice is free to express what guard means.
  On the expansion event they are not interchangeable at all: `additionalContext` is added
  "alongside the expanded prompt" for Claude to act on, while `decision: "block"` ends the
  turn and shows `reason` to the user. `/guard:toggle` was a block for a reason that had
  nothing to do with unfinished work — it was the only shape that delivered a finished
  sentence without paying for a model call. Source: official hooks docs
  (https://code.claude.com/docs/en/hooks.md, "UserPromptExpansion decision control"),
  excerpt at `wiki/ref/claude-code-userpromptexpansion-hook.md`, fetched 2026-08-25. Note
  the docs say "the turn ends"; they never describe the model-call lifecycle, so zero
  inference is an inference, not a quoted guarantee.
- **`memory: <scope>` gives a subagent a persistent store, and silently gives it Write and
  Edit.** Scopes and directories: `user` → `~/.claude/agent-memory/<agent>/`, `project` →
  `.claude/agent-memory/<agent>/`, `local` → `.claude/agent-memory-local/<agent>/`; the
  first 200 lines or 25KB of that directory's `MEMORY.md` is injected into the agent's
  system prompt, and Read/Write/Edit are enabled so it can curate. It is part of *auto
  memory*, so `autoMemoryEnabled: false` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY` turns it off
  entirely with no signal to the agent. Docs: https://code.claude.com/docs/en/sub-agents
  ("Persistent Memory for Subagents"), excerpt at
  `wiki/ref/claude-code-subagent-memory.md`, fetched 2026-08-22. Measured 2026-08-23: the
  grant is NOT scoped to the memory directory — an agent declaring only `Read` reported Write
  and Edit present and wrote to an absolute path outside both the project and its memory
  directory. The directory for a plugin subagent is the hyphenated, plugin-prefixed name
  (`.claude/agent-memory/guard-claims-auditor/`), also observed rather than assumed.
  It follows the AGENT, so renaming one strands its accumulated memory in the old directory
  with nothing failing — `git mv` the directory with the agent. That the directory follows the
  agent name is also why two of the three shared audits are one agent behind two skills; see
  "One audit, two paths".
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
  line is stated in `agents/turn-router.md` per candidate, and it is the thing most easily lost
  in an edit: a router that starts judging quality stops naming the agent that would have
  judged it properly.
- **The router routes on the answer AND the request; materiality needs both.** Triage used
  to see the answer only, stated as a prohibition — "never because of what the user asked"
  — and that was wrong, because the one judgment left to the router is materiality and
  materiality is relative to the request. The same explanatory paragraph is the substance
  the user came for when they asked how something works, and padding when they asked for a
  one-line setting change; from the answer alone the two are the same text. What that cost
  was measured on: a plain-language "ext-docs-fetcher는 켜줘" (the agent's name at the time;
  it is `docs-finder` now) (so `_CONTROL_CMD_RE` did not skip
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

- **The mute is a shell command, and the slash command that used to sit beside it was
  removed.** `/guard:toggle` was cheap as hooks go — it blocked the expansion, so no model
  was invoked to relay its sentence — but reaching it still meant typing into the
  conversation, which is a prompt, a turn boundary, and a Stop hook. Someone who just wants
  audits off for the next ten minutes paid all of that. `toggle-cli` is the same three lines
  of state change addressed from a prompt the user already has, and the conversation never
  learns it happened. Keeping both meant keeping a command file and a matcher in step for a
  body that never ran, to offer the more expensive of two identical outcomes, so the second
  one went.

  What makes it possible is `CLAUDE_CODE_SESSION_ID`: Claude Code sets it in every Bash
  subprocess to the value the hook payload carries, so a shell command can address the same
  `state/<sid>.json` the Stop hook will read. `GUARD_TOGGLE_CLI` — exported at SessionStart
  — carries the other half, the script's own path, which the shell cannot otherwise know:
  `CLAUDE_PLUGIN_ROOT` is a hook variable, and the marketplace installs the plugin under a
  versioned cache directory. Because that path is resolved by `_plugin_root()` at session
  start, it names the plugin copy THIS session loaded — a session started with
  `--plugin-dir` gets the working tree, and the command cannot address a different version
  than the hooks do.

  **Nothing is installed.** `CLAUDE_ENV_FILE` is not a list of `export` lines: it is a shell
  script the host SOURCES before each Bash command, so it can prepend a directory as readily
  as set a variable. SessionStart adds `shell/bin` to `PATH`, and `guard` is on it from the
  session's first shell. Verified against a live session — the file is
  `~/.claude/session-env/<sid>/sessionstart-hook-N.sh`, and in that session `command -v
  guard` resolved to the plugin's own `shell/bin/guard`. No startup file is edited, so
  nothing survives the session and there is no uninstall step to forget. An earlier design
  shipped a `/guard:shell` command that appended a `source` line to `~/.zshrc`; it was
  removed once the env file was found to do this itself.

  **A real executable, not a shell function.** Both work in the Bash tool's own shell, and
  the function was built first. The executable wins on inheritance: a function exists only
  in the shell that sourced it, so anything one level down — a subprocess, a Makefile
  recipe, a script the agent writes — would not find `guard`, while an executable is
  inherited like every other command. Confirmed both ways: `sh -c "guard status"` from
  inside a session prints the state, which the function form could not have done. It also
  behaves the way a command is expected to, `command -v` included.

  **The toggle says ON or OFF and nothing about the roster.** It listed the switched-on
  agents at first, then their count; both are gone. Which agents run is the router's answer,
  decided per turn against what the turn contains, so a roster stated at toggle time
  describes a different question than the one the user sees answered — and is a second copy
  of the roster to drift. The one thing kept is "no agent is switched on", which is not a
  roster detail but a different outcome: the turn-reading agents cannot run at all, and
  saying so is what stops `guard on` from promising an audit that will not come. The
  status-line segment still shows a count; it is a different surface, read continuously
  rather than at the moment of a decision.

  Prepending one directory holding one command is not "reordering the user's PATH", which
  is what an earlier draft of this bullet claimed as the reason to avoid it. A user who
  already has a `guard` on their PATH has a genuine collision; `GUARD_TOGGLE_NAME` changes
  the name guard's messages *suggest*, but not the file, so resolving it is theirs.

  Added for every project, with no condition. Gating it on "guard is configured here" gates
  on nothing: a project with no `guard.local.json` loads `DEFAULT_CONFIG` and is an ordinary
  guard project with every switch `off`, so the test would not separate the case it appears
  to — and would remove the command from the project where a user is most likely to reach
  for it first. Verified in a project with no `.claude/` at all: `guard on` armed the
  session and reported that no agent was switched on, which is the honest answer.

  The command lives in `shell/bin/guard` rather than in a Python string, because shell code
  inside a Python literal cannot be syntax-checked and is exactly the text that rots. It is
  POSIX `sh`: the shell that sources the env file is the Bash tool's, not the user's login
  shell. It resolves the CLI from `$GUARD_TOGGLE_CLI` rather than relative to its own
  location, so a `guard` inherited by a subprocess still reaches the session's own plugin
  copy.

- **`guard-candidates` is on that PATH for the router, and it removes the roster line from
  the dispatch entirely.** Moving the roster out of the main agent's context is why the
  `candidates` verb exists at all — the Stop hook printed the command instead of the answer,
  and the router ran it. But printing the command was still the main agent relaying an
  instruction addressed to someone else: it never runs it, so every character was read by
  the wrong party. Shortening the string to a bare name made that cheaper without stopping
  it. The fix is that a FIXED command needs no relay at all — `agents/turn-router.md` names
  `guard-candidates` itself, read once by its only caller — so the hook now sends nothing
  about the roster, and the dispatch carries four fields: closeout, turn dir, answer file,
  history.

  It needs no new plumbing: `_add_shell_command_to_path` already puts the directory on the
  session's PATH, and a subagent's Bash inherits it exactly as a subprocess inherits
  `guard` — the same property that made an executable the right choice over a shell
  function. It reads `$GUARD_TOGGLE_CLI` for the same reason `guard` does, so the router
  cannot address a different plugin copy than the hooks did.

  **There is no fallback for a missing wrapper, and one was removed rather than kept.** It
  tested `is_file()` on each wrapper and added the long `uv run --script <cli> <verb>` form
  when it was absent. Measuring all four present/absent combinations showed it caught
  nothing that happens: a version mismatch is impossible because `agents/turn-router.md` and
  `shell/bin/` install as one tree; a lost exec bit or a PATH the wrappers never reached
  leaves the file in place, so `is_file()` passes and the fallback never fires — and that is
  every realistic failure; Codex never calls `_router_context` at all. The only state it
  caught was one produced by deleting the files by hand.

  It was not free, either. The `candidates` half vanished in the v0.68.0 refactor and
  nothing noticed until these paths were measured directly — a branch that never runs in
  practice is a branch nothing protects. If a wrapper is ever genuinely unreachable, the fix
  belongs in the router's report: "the command failed" and "nothing to audit" produce
  identical output today, and that ambiguity is the real silent failure.

  Measured in a real session with the wrapper present: the Stop hook's dispatch listed
  `closeout`, `turn dir`, `answer file` and `history` and no `candidates` line, and the
  router still returned picks — so it reached the command through its own definition rather
  than through anything the caller passed.

- **`guard-inputs` takes the same argument one step further: the routed dispatch is now the
  turn id and nothing else.** Those four remaining fields were all derivable from that id
  plus the session — the closeout file from the plugin root, the answer and request files from
  `turnrec`'s layout, the transcript from what `cmd_stop` already records in session state —
  and the main agent derived none of them. It relayed them, into a dispatch it composes
  itself, which is the step that can only lose fidelity. `- turn: <id>` replaces the lot.

  Two things this buys beyond the context. The layout goes back to the code that owns it: a
  dispatch spelling out `{turn dir}/<name>` was a second copy of `turnrec`'s layout written
  in prose, and a drifted copy of a path reads nothing and clears every turn silently. And
  the paths are produced by the same functions that create the files, so the agent opening
  one cannot be handed a path assembled by a party that never opens it.

  The transcript is the one field guard cannot derive, because it is the host's path handed
  to the Stop hook in its payload — so the verb reads it back from session state, and says
  on stderr when a session has none. An agent that needs history must be able to tell "no
  transcript" from "I built the path wrong"; those two look identical if the verb is silent.

  This verb had a fallback too — the whole old field list — and it was removed with the
  other one, for the same reason and in the same commit. `_router_context` is now a lead and
  one field, with no branch in it: rendering it with the wrappers deleted produces byte-identical
  output to rendering it with them present, which is the check that the branching is really gone.

  Two things this verb does differently from everything else in guard, both deliberate:

  - **It does not fail open.** Every other subcommand swallows its own exceptions, because
    a broken plugin must not block someone's session. Here a person is standing at a prompt
    reading the output, and printing nothing while exiting 0 is indistinguishable from
    success. That is not hypothetical: during development a missing argument raised
    `TypeError`, `main()` swallowed it, and `guard off` printed nothing and exited 0 —
    which reads exactly like the mute worked. `_MUST_REPORT` in `guard_hook.py` is the
    carve-out.
  - **It verifies the write by reading it back.** `_write_state` swallows `OSError` by
    design, so a full disk or a read-only checkout would otherwise leave the user with a
    sentence announcing a flip that never reached the file. The `flip` case has to resolve
    its target *before* the write; comparing against a state re-read afterwards compares it
    with itself and passes for any outcome at all.

- **Materiality is measured on the turn, not on the answer file — v0.65.2.** The request
  bullet above fixed *what* the router compares against; this fixes *what it is reading*. The
  answer file is where a turn's substance is written down, so it is written even when the
  substance is one sentence, and it arrives with headings and paragraphs because that is the
  format. The router then finds material in text that exists only because the file had to be
  filled. Measured on `gurad 훅 테스트` — five words, a smoke test of the hook wiring, whose
  answer file ran to ~250 words of sections restating what the two hooks had printed. The
  router named `claims-auditor` and `korean-corrector`; both ran, both passed clean, 50s and
  49s of subagent time for a turn whose finding was "the hooks work". Correct by its own
  cues, which is what made it a rule problem rather than a routing mistake — replayed against
  the old definition the same turn also drew `clarity-auditor`, so two agents was the lucky
  end of the range, not the typical one. Three cues were missing, and
  all three had to go together — fixing one alone still leaves the turn drawing an agent:

  - *self-observation is not a claim.* The `claims-auditor` cue excluded a bare report of what
    the assistant just *did* (`수정했습니다`) but not what it just *observed* — which hooks
    fired, what a command printed, what state the session is in. These have nowhere to be
    wrong: evidence and assertion arrived in the same context window, and no file or
    transcript could disagree. Paraphrase is what smuggles them past the old "plainly a
    quotation of tool output" escape, since the paraphrase is formally a statement about the
    output rather than the output. The test now stated is whether the claim has somewhere to
    be wrong: "the Stop hook fired on this turn" narrates the session, "the Stop hook fires on
    every turn" is checkable.
  - *the `korean-corrector` exemption covers the language, not materiality.* Its subject does
    not exist when the router reads, so the request had to be allowed to put it ON the list —
    but that was written as being outside *both* request limits, which read as an exemption
    from the materiality bar too. It is not: the language question is unanswerable from the
    English answer file, the substance question is answerable there like any other agent's. A
    Korean request makes the agent possible, not worth running.
  - *the empty-answer list read as exhaustive.* Four shapes were listed and a hook smoke test
    is none of them literally. Now marked as examples, with the check-that-something-works
    shape named — it is the shape a plugin's own users hit first, since testing the plugin is
    the first thing they do with it.

  The router cannot fix the inflation itself — the answer file must be written, and a
  one-sentence file is indistinguishable from a turn that skipped the convention. So the rule
  is stated at the router instead: judge what the turn established, and treat the file's
  length as format.

- **`none` means nothing runs, the Korean pair included — v0.91.0.** The two bullets above
  gave the router the materiality bar and applied it to `korean-corrector` explicitly. The
  closeout file then overrode the result: `korean-translator`'s section said "if the router did not
  name it, dispatch it anyway", step 2 of `Presenting the result` repeated it, and step 3
  dispatched the corrector behind it. So a turn the router cleared still spent both agents —
  measured on a turn whose entire content was spawning `interviewer` and saying it was running,
  the relay shape the router's own empty-answer list names. It reported `none`, correctly, and
  the caller translated a one-line relay anyway.

  The mistake was reading "no switch" as "unconditional". No switch means the *user* cannot
  turn the pair off, and it exists because `off` on a translator did not mean "no translation"
  — it meant the author translates, which is the defect. It never meant every turn gets one.
  The router is the only step that sees whether this turn is Korean prose being delivered to a
  reader, and `_eligible_agents` puts the pair on its roster precisely so it can answer that.
  A rider that cannot be declined is not a candidate.

  What made the override look reasonable is worth naming, because it is the thing not to
  restore: the caller must never translate the answer file itself, so "the router did not name
  the translator" reads like a gap someone has to fill. It is not a gap. The answer to it is no
  translation — the answer file stays English and is the path the reply names — and the short
  Korean line beside that path is the one piece of the user's language the caller writes. Both
  halves are now stated wherever the old rule was: the preamble, the `korean-translator`
  section, steps 2 and 3, and a `none` paragraph beside the existing no-answer-file one. The
  router's `none` template says "no corrections and no translation" for the same reason — the
  caller reads that line before it reads any section.

- **How to dispatch travels with the dispatch; the closeout file keeps only the closeout — v0.92.0.**
  The bullet above fixed one contradiction between the closeout file and the router. The shape that
  produced it was still there: two files each holding a per-agent list, one of them read by the
  party the other had just instructed. So the closeout file's per-agent sections are gone, and the
  turn router's report template carries the dispatch instruction the way `report-router`'s
  already did — that path has shipped this design all along (`agents/report-router.md`: "Your
  Output section below is the whole of the dispatch instructions for this path, so do not send
  your caller to the closeout file"), which is the counter-evidence to the objection recorded at
  `_agent_pointer` and the reason it is overturned here rather than argued with.

  What made this cheap is the roster the turn router actually sees. `cmd_candidates` filters to
  turn-reading agents, so its whole world is three `audit-turn-*` skills and the Korean pair —
  two shapes, not eight. The template is one sentence for the skills plus one conditional line
  for the pair. The objection stands where it was aimed: an LLM re-typing per-agent blocks it
  was handed is where wording drifts. Reproducing a fixed template verbatim is not that, and
  the alternative was worse than drift — a second authority over a decision already made.

  Three things did not move, and each is a boundary worth stating rather than a leftover:

  - *The closeout.* `Presenting the result` and the answer-file convention are a sequence, not
    a call, and the router would have to reproduce all of it on every routed turn. This is what
    the file is now, and the Korean pair's inputs are stated at steps 2 and 3 where the caller
    already is rather than in sections of their own — which is also where their ordering rule
    lived, so the duplicate that caused v0.91.0 no longer has two homes to disagree between.
  - *The agents the router never sees.* `comment-corrector`, `agents-md-auditor` and
    `ext-docs-auditor` are dispatched by the hook off the file lists, with no report to ride
    on. `_agent_pointer`'s lead now says the shape (`subagent_type: "guard:<name>"`), once, and
    their sections stay — because each is a judgment no report can make for the caller: a
    passage that must be moved rather than deleted, a finding whose fix would mean inventing a
    document.
  - *What the audits report.* The three skills needed nothing added and got nothing: their
    agents' report blocks already carry `verdict`, a `Fix:` per finding, and — for
    `clarity-auditor` — `profile: present | MISSING`. The deleted sections said "invoke with the
    turn id" (now the router's), "it changes nothing you need to review" (now one clause in the
    router's template) and "address what it reports" (the report's own `Fix:` lines). Two of the
    three sections were byte-identical apart from their first line, which is what a section with
    no content of its own looks like.

  The rule that replaces them is negative, and that is the useful half: a closeout sentence that
  decides WHETHER an agent runs, or restates how to call one, is a second authority over a
  decision already made. 376 lines to 267.

- **The file is `hooks/context/turn-closeout.md`, and the router names only
  `korean-translator` — v0.93.0.** Two follow-ons from the bullet above, both of them the
  same move finished properly.

  The rename is not cosmetic bookkeeping. A file called "dispatch playbook" that holds no
  dispatch instruction is an invitation to put one back in it, and the rule it now carries is
  precisely that nothing of that kind belongs there. `CLOSEOUT_REL` / `_closeout_path()`, and
  `guard-inputs` prints `closeout:` rather than `playbook:`. The fixtures under `dev/fixtures/`
  still say `dispatch-playbook.md` on purpose: they are frozen sample answers used as input to
  the design critics, not live pointers.

  Dropping `korean-corrector` from the router's roster (`routed=False`) removes the last place
  two parties decided one thing. The corrector's precondition is that the translation exists,
  and the router reads before it does — so routing it meant inferring from the request what the
  translator would later make true. `korean-translator`'s report already ended in a `next` line
  naming the corrector and the file it wrote, marked **never drop**, which is the hand-off
  happening where the fact is actually known. The router now judges one question about the
  language instead of the same question twice, and `_eligible_agents` still returns the
  corrector so `settings set` keeps refusing it and `status` keeps showing it.

- **The closeout file stops naming agents at all — v0.94.0.** v0.92.0 kept three sections, for
  `comment-corrector`, `ext-docs-auditor` and `agents-md-auditor`, on the argument that their
  findings need a judgment no report can make: a passage that must be moved rather than deleted,
  a fix whose destination does not exist yet. The argument was wrong about *where* — the agent
  is the party that knows which kind a finding is, and it was already writing one line per
  finding. So each of the three now ends a finding in its disposition (`ext-docs-auditor`:
  apply / move to `<where>` / decide; `agents-md-auditor`: a `Fix:` needing a file nobody asked
  for is relayed, not applied; `comment-corrector`: its caller relays and does not re-edit),
  and the sections are gone. The Stop hook's two leads stop naming the closeout file with
  them: a turn dispatched that way wrote no answer file, so it had nothing to close out and
  was being sent to a file it did not need.

  `Common to every dispatch` went the same way and for a plainer reason: every rule in it was
  already in the hook output or the router's template — pass only the named inputs, add no
  instructions of your own, every instance is `fresh`. Its last paragraph was not about
  dispatching at all but about the reply, and moved into step 4 where the reply is written.
  The `/guard:*` warning went with it; the per-agent commands it guarded against no longer
  exist.

  Then the same test was applied to what remained, and most of it failed too. The turn id is in
  the Stop hook's output and in the router's template, so the closeout has no reason to explain
  passing it on. The measurement behind auditing English first is rationale and moved to the
  bullet above. So did the paragraph explaining why guard stores text in a file at all — a
  reader following the closeout does not need guard's cost model. The transcript fallback lost
  its mechanics and kept its two rules: raw text, and say it came from you.

  What is left is a four-line lead, the answer-file convention and `Presenting the result`. The
  rule that keeps it that way is in `AGENTS.md`: a closeout sentence naming a particular agent is
  either a second authority over a decision already made, or a lookup that belongs in that
  agent's report.

- **The translation instruction moves to the router too, and the closeout names nobody — v0.95.0.**
  The last two agent names in the file were `korean-translator` and `korean-corrector`, in steps
  the caller was told to run. That put the decision in the wrong hands twice over: the caller was
  reading a step that told it to translate, when whether this turn is translated at all is the
  router's judgment — the one thing v0.91.0 had just established. So the router's template, when
  it picks the translator, now carries the whole instruction: dispatch it after the findings are
  applied, with the answer file as source and the `.ko.md` path as its target, spelled out in
  full rather than left to the caller's string surgery. The corrector was already reached from
  the translator's `next` line.

  The closeout keeps one sentence in its place — anything the dispatch asked for after step 1
  happens before the reply — which is ordering, not an agent. Its language rule is now the plain
  one: you never write the user's language yourself and you never decide whether it gets
  written. Both are the router's.

  376 lines at v0.91.0, 80 now, and the only proper noun left in it is `/guard:reader-profile`,
  which is the user's command rather than an agent.

- **Concurrent or serial is something the caller has to be told — v0.96.0.** Moving the dispatch
  instruction into the router's template exposed a gap that the playbook had covered by
  accident: it used to say "Send everything you were named in ONE message so they run
  concurrently", and the rewritten template kept only "in ONE message, in this order" — which
  states neither, and reads as a sequence. Nothing in a list of names says whether they wait on
  each other, and this is not derivable: the routed audits are simultaneous, `korean-translator`
  is not, and both facts are properties of what those agents read rather than of the list.

  So both leads say it outright, with the reason attached, because the reason is what makes it
  checkable when the roster changes: the `audit-` picks "edit nothing and share no input", the
  direct-path agents' "file lists are disjoint" (`_edited_bucket` keeps them so). The
  translator's line begins "Once those findings are applied", which is its serial dependency
  stated as the condition it is.

  The roster order stopped meaning anything on the routed path at the same time. It encoded
  auditors-before-correctors, and no corrector is routed now — `cmd_candidates` still prints in
  roster order, but as a stable listing for a reader comparing two turns, not as a constraint.
  Saying so where the order is produced is what stops the next reader reconstructing a
  dependency that is not there.

- **The router stops naming `korean-corrector` in any direction — v0.97.0.** v0.93.0 took it
  off the roster and left a paragraph telling the router not to name it, plus a clause in the
  template telling the caller to follow the translator's `next` line. Both were the router
  speaking about an agent it has no relationship with. The roster rule already forbids naming
  what `candidates` did not print, so the paragraph defended nothing, and the `next` line is
  marked never-drop in the translator's own report — a caller that has just been handed one
  does not need a second party to say it exists. The template now ends "Then do what its report
  tells you", which is true of every agent and names none.

  The translator's position is stated as the fixed thing it is — "Last, once those findings are
  applied" — rather than as a per-turn schedule the router works out. What the router decides
  about the pair is one question, the language; everything after that is sequence the parties
  involved already know.

- **`clarity-auditor` runs after the first wave's findings are applied — v0.98.0.** v0.96.0 said
  the routed audits were simultaneous because they "edit nothing and share no input". True of the
  agents and wrong about the turn: the caller edits between them, and what it edits is the answer
  file all of them read. Applying a claims finding puts evidence into a sentence that did not have
  it; applying a deferrals finding resolves a punt into new text. Those are the passages most
  likely to be hard to follow, and they do not exist while the first wave is running — so a
  `clarity-auditor` beside it judges prose that is about to change and cannot see the prose the
  correction introduces.

  It applies to every pair on the list, not just to clarity, which is why the routed audits are
  **fully serial**: claims, then deferrals, then clarity, then the translator, each dispatched
  only after the one before it has been applied. Claims and deferrals looked independent — one
  judges evidence, the other judges punts — but the repair links them. Fixing an unsupported
  claim you cannot substantiate is *how a deferral gets written*: "I could not establish this"
  is the honest correction, and it is exactly what the next audit exists to catch. Run beside
  each other, the deferrals audit never sees the deferrals the claims fix introduced.

  This makes the roster order load-bearing again — not as auditors-before-correctors, which
  really did stop meaning anything, but as the run order. Said at the roster, at
  `cmd_candidates` and in the router's template, which spells out "ONE AT A TIME ... Do not send
  two of them in one message" because a caller reading three read-only audits will otherwise
  batch them.

  The split of authority is worth stating because it is easy to slide: the ORDER is fixed and
  belongs to the roster, and what the router decides is which of its steps this turn has material
  for. It names a subset, never a sequence of its own — a router free to reorder would be making
  the dependency argument above per turn, from the one position that cannot check it.

  One pass, and the cycle is real but not chased: a deferral resolved in step 2 introduces facts
  that nothing re-audits for evidence. A second round would cost double for something empty on
  almost every turn. The direct path is untouched and still concurrent — its agents read
  disjoint file lists and no caller edit sits between them.

- **Withholding the document is for a skipped audit, not for no audit — v0.111.0.** The open rule
  had four cases and one of them was wrong in the common direction: "no agent read anything this
  turn → open nothing" also caught the turn the router answered `none` on. `none` is the router
  saying no agent had material here, so that turn ended with nothing unfixed and nothing
  unchecked, and the file was withheld anyway — the user got a path and had to open it by hand
  for the reason that the audit correctly declined to run. The gate now asks whether an audit
  ran and skipped this document, which is the only condition under which "unchecked" is a claim
  about the text rather than about the routing. A `none` turn opens its answer file, and the
  closeout's last paragraph covers steps 2 and 3 rather than step 2 alone.

  The translation case collapsed in the same edit. Two branches — checked, unchecked — were a
  restatement of the general gate applied to one file, so the case list now says only that a
  translation is what gets opened when one exists, and the unchecked branch is shared. The one
  thing it still spells out is why an audited English file is not a substitute: it was checked,
  but it is not what this user reads.

  **And the unchecked branch retries before it withholds.** Naming the two survivors made it
  obvious what they have in common: a document reaches step 3 unaudited only because a dispatch
  fell through — `korean-corrector` not reached off the translator's `next` line, or a picked
  audit that errored. Neither is a fact about the text, and withholding answered them as
  though it were: the check that did not happen still does not happen, and the user is handed a
  path to a document nobody will look at again. The turn is still open and the file is still
  there, so the branch now dispatches the missing audit, applies what it finds, and opens.
  Withholding is the residue — refused, or failed twice.

  This does not make the handoff safe, and the closeout is the wrong place to try. The
  translator→corrector step is still held by prose, which v0.110.0 established is the form that
  fails silently; a real session had already been observed ignoring an explicit "ONE AT A TIME",
  and `dev/handoff-audit-workflow.md` listed "a `.ko.md` opened when `korean-corrector` did not
  run" as a failure to watch for. What changed here is only the *response* to that failure, and
  it shares the weakness of every rule in this file: it runs when the main agent notices. A
  mechanism — state that records the translation and a hook that checks the corrector against it
  — is the fix, and is not built.

- **The serial order needed a mechanism, not a rule — v0.110.0.** v0.98.0 argued the turn audits
  fully serial and said so in three places, then left the enforcement to prose while the three
  skills kept `background: true`. Observed in a real session: the caller invoked
  `audit-turn-claims`, `audit-turn-deferrals` and `audit-turn-clarity` in ONE message, all three
  backgrounded, and went back to running integration tests while they ran — the exact batching
  the template's "ONE AT A TIME ... Do not send two of them in one message" was written to
  prevent. Then it applied the clarity findings to a file the claims audit was still reading.

  Instruction-following is the visible failure and the wrong thing to fix. A backgrounded fork
  returns control the instant it is dispatched, so a caller that obeyed the rule perfectly — one
  skill per message — would still have nothing to wait on and nothing to apply: there is no point
  in the turn where the findings exist and the next dispatch has not happened. The rule was
  unenforceable, and asking for it more firmly would only make the next violation quieter.

  So the three turn skills are `background: false`, which is documented to make the invoking turn
  wait for the fork's result (`wiki/ref/claude-code-skill-fork-context.md`). The order is now held
  by the host rather than by the caller's willingness. The reason for keeping `true` was
  consistency with the asynchronous Agent-tool dispatches around it, and that was the wrong thing
  to optimise: one audit waiting by mechanism while the rest wait by rule is *precisely* the
  arrangement worth having, because only one of the two kinds has a caller edit sitting between
  its steps. The tool-set cost of a background fork is still not a factor either direction —
  these agents carry `Read, Grep, Glob, Bash, SendMessage` and the background filter keeps all
  five — it just no longer has to be the deciding argument.

  `audit-report-*` stays `background: true`, and its comments now say why on their own terms
  rather than pointing at the turn path: `report-router` hands all three the same file and
  dispatches them concurrently, with no caller edit in between, so there is no order for blocking
  to hold. The two paths differ here, and the cross-reference that used to make them look
  identical was how the turn path's `false` got argued away in the first place.

  Two stale statements of the old behavior went with it: "and they run in parallel" in both
  plugin manifests' `description`, and "The main agent dispatches those, concurrently" in
  `AGENTS.md`. Both predate v0.98.0. The manifest line is the one users read.

- **Both paths dispatch concurrently and correct once — v0.112.0.** The serial turn order this
  reverses was argued from v0.96.0 through v0.110.0, and what it bought was each audit reading
  the file its predecessor had already corrected. The cost was paid every routed turn: three
  blocking forks in sequence, and a caller that has been observed batching them anyway. The
  ordering is now the same on both paths — the router dispatches every audit in one message, the
  caller applies nothing until the last report is in, then corrects in one pass, and
  `korean-translator` runs on the result.

  What makes the concurrency safe is the barrier, not the dispatch: with no edit landing while a
  fork is reading, every audit judges the same text, so no finding can quote prose that has since
  been rewritten. What is given up is the chain v0.98.0 wanted — a deferral written as the honest
  repair of an unsupported claim is no longer seen by the deferrals audit, and the prose the
  corrections introduce is not read by clarity. That is now a known gap rather than a bug, and it
  is the same gap the report path has always had. The overlap it creates instead is the caller's
  to reconcile: two findings on one sentence become one correction, which `turn-closeout.md` step
  1 now says explicitly.

  `background` goes back to `true` on the three `audit-turn-*` skills, since blocking now holds
  no order — and the three `audit-report-*` comments stop saying "unlike the turn path", because
  the paths no longer differ here. The run-order claims in `agents.py`, `cmd_candidates.py`,
  `AGENTS.md` and both manifest descriptions were rewritten the same way: `AUDIT_AGENTS` order is
  still load-bearing, but as the order findings are APPLIED, not the order anything runs in.

  **The chain is bought back as a second round, not as an order.** What the serial arrangement
  actually protected against is that a correction is prose no audit has read: evidence written
  into a sentence that had none, a punt resolved into new text, and a deferral written as the
  honest repair of an unsupported claim — the exact case v0.98.0 built the ordering around. So
  both templates now end with one further round over the corrected file, dispatched concurrently
  like the first.

  It is limited to the audits whose findings were actually applied. An audit that had nothing to
  fix has already read this file and passed it, and the edits it did not ask for are not its
  subject — the claims audit does not acquire an interest in a sentence because clarity rewrote
  it, so re-running it spends a fork to re-derive a verdict already given. Which audits the round
  contains is therefore the CALLER's to determine and cannot be named by the router, which does
  not know what the caller ended up changing; both templates say so explicitly, because a router
  that guessed would be naming a subset of a subset from the one position that cannot check it.

  And it stops at two. The second round's own corrections are unread prose by the same argument,
  so the rule has no natural end; each round is emptier than the one before, and the caller is
  given the limit rather than left to decide when to stop. This supersedes the "one pass, and the
  cycle is real but not chased" reasoning in the v0.98.0 entry above — the cycle is now chased
  exactly once, and paid for only where something changed.

- **The Korean pair moves to `sonnet` — v0.112.0.** `korean-translator` and `korean-corrector`
  were `model: opus`, argued from the failure mode and never measured. Changed by the
  maintainer's decision, so it is recorded as a decision and not as a result. The asymmetry worth
  knowing: the translator has a reader downstream — the corrector is dispatched by its own report
  — while the corrector is the last judgment made on the Korean the user is about to be shown, so
  prose it cannot hear as unnatural becomes a pass, and a pass looks exactly like a clean file.
  If 직역 or unnatural Korean starts reaching users, this field is the first place to look, and a
  head-to-head under § "Picking a model for an agent" belongs before it changes back.

- **A turn spent addressing an agent directly is empty, and the agent's own answer arrives as a
  file — v0.100.0.** `@some-agent ...` is typed by a person, so `origin.kind` is `human` and the
  Stop hook routes it like any other turn. Measured: the router spent 15s on such a turn and
  returned `none`, correctly — the answer file held "it is running" and a path. Correct but not
  reliable, because nothing in the router's cues named the shape; it got there through "a relay"
  in the empty-answer list, which the turn only resembles.

  So the cue is stated. What makes it worth its own paragraph rather than a fourth word in that
  list is the second half: the agent's real answer is auditable, and a router that treated the
  relay as thin-but-auditable would be auditing the wrong text on the wrong turn.

  **The mechanism for the real answer already exists and needs no new hook.** The agent writes
  its answer to a file and reports the path; the session routes that path with
  `guard:report-router` on the document path. `interviewer` has done exactly this since v0.85.0.
  The alternative considered and rejected was a `SubagentStop` hook: it is the only event that
  hands guard a subagent's text (`last_assistant_message`, and `agent_type` would even settle
  the `@`-versus-file-reference ambiguity that defeats parsing the prompt —
  `wiki/ref/claude-code-hooks-in-subagents.md`). It was rejected because it solves a problem the
  file already solves, and it would make guard slice and store a transcript it has no other
  reason to read.

  What this does not cover, and cannot: an agent that writes no file. guard cannot make a
  third-party agent report a path, so its answer is audited only if the agent chose to leave
  one. That is a property of the agent, not a gap in the routing.

- **The main session asked the interviewer for a report, and got one — v0.114.0.** Reported
  from use, with the transcript. A `@guard:interviewer` dispatch went straight to research
  without a single user message in it, ended a turn with nothing to show, and the main session —
  holding a background agent that had finished empty — messaged it asking for its report. It
  complied: conclusions it had reached alone, a recommendation, and five questions. The main
  session put those five to the user through `AskUserQuestion` and committed. The user never had
  the interview, and the thing the interview exists to prevent — the blank filled in by somebody
  else — happened *through* the interview.

  Every rule that broke was already in the file. What was not in the file is the party that
  broke them: the body said "Nobody relays for you" as a fact about the world, so when a message
  arrived asking for output there was nothing to read it as except the user asking.

  Three things are stated now, and the first is what the other two rest on.

  - *The main session can message it, and it is not the user.* The test is not a heuristic
    about phrasing — it is that **the user never asks for the report**, having read every line
    of it as it was written. A request to produce, send or hand over anything is therefore the
    main session by construction, and gets one line back and nothing else.
  - *Whatever ends a turn reaches the main session too.* The old text implied the transcript
    was private to the two of them, which made a premature summary read as untidiness rather
    than as a report being filed. It is a report being filed.
  - *The handoff is approved, not assumed.* The close signal produces the brief; the user's yes
    produces the path. Splitting them costs one message and buys the only gate that matters,
    because the path is the one thing in this conversation the main session can act on.

  The audit question moved into that same message — still at the close, now after the file
  exists — so the round trip is nobody's extra. Its default is unchanged and is deliberately the
  opposite of the new one beside it: the audit is a yes unless it is a clear no (v0.102.0), the
  handoff is a no unless it is a yes. An audit skipped can be run later; a brief handed over
  early cannot be taken back.

- **The interviewer hands off its own brief — v0.101.0.** The routing instruction lived in the
  agent's `description`, which is standing text the caller reads when it picks an agent, not
  when a brief arrives. Same defect as the two the Korean pair had: a third party stating a
  handoff whose precondition — this file now exists at this path — only one party knows. So the
  interviewer's last message is now the path **and** the dispatch line, marked never-drop, and
  the description says only that the line will come and to do what it says.

  What did not change is the ban it sits inside. "Your last message is that path and nothing
  else" existed so no summary of the brief travels beside the brief, and that still holds: the
  handoff is one imperative line, not a second version of the document. The write-failure branch
  sends no routing line at all — there is no file to route.

  This is deliberately the only agent with it. A general mechanism was considered and dropped: a
  `SubagentStop` hook would reach every subagent's `last_assistant_message` (documented, see
  `wiki/ref/claude-code-hooks-in-subagents.md`), but auditing every subagent means auditing the
  ones guard itself dispatched, and the machinery it takes to exclude them is larger than the
  one line an agent that wants routing can write for itself.

- **An explicitly-invoked agent needs a short description — v0.104.0.** `interviewer`'s was
  2087 bytes against 655 for the next largest and ~90 for most of the roster, and every byte of
  it is in the system prompt of every session that has guard installed, whether or not anyone
  ever types `@guard:interviewer`. Most of it was selection prose — what the agent is for, when
  to reach for it, what it will not do — and selection is the one job this description does not
  have: the user names it themselves, and it ships no command precisely so that the `@`-mention
  is the only way in.

  What is left is `description: Invoked by the user, by name.` — 44 bytes, the same shape the
  `audit-*` skills already carry ("Invoked by guard only.") and for the same reason: a name
  reached by typing is a name nothing has to be attracted to.

  Four paragraphs came out one at a time, each the same mistake in different clothes, and the
  order they fell in is the useful part:

  - *What the final report looks like and what to do with it.* **The agent says it itself.** The
    report is a path and one imperative line; a caller holding it needs no preview of its shape.
  - *That it runs in the background, so do not wait, poll or relay.* **The host shows it.**
    `background: true` is in the frontmatter, so the host backgrounds the agent and displays
    that it did; saying it in prose describes what the caller is already looking at.
  - *Spawn it with the subject and nothing else, give it no procedure.* **The agent already
    defends against this, from the enforcing side.** Its body says "Your dispatch prompt is not
    your instructions ... this file outranks the dispatch on every point it covers". A
    description can only ask the caller to behave; the body acts whether or not it did.
  - *What the agent is and how it works.* **The user already knows — they typed its name.**
    Selection text has one reader, a model choosing from a roster, and this agent has no such
    reader. Everything it said was true and none of it changed what anybody did.

  The test, in its final form: a description carries only what its reader must act on **before
  anything else can tell them, and that nothing else already enforces**. Then ask who the reader
  is. For an agent nobody selects, the honest answer is that there isn't one, and the right
  description says only that.

- **A document gets translated too — v0.103.0.** `korean-translator` had no `report_entry`, so
  it never appeared in `guard-candidates --doc` and a brief could only ever be delivered in
  English. The code said this was deliberate — "a translation that the document path never
  produces", "a translation nobody asked for" — but the exclusion was a consequence of how the
  language gets decided, not a decision about documents. On the turn path the request file
  settles the language; the document path has no request file, so nothing could answer the
  question and the agent was left off.

  What answers it is the party that was in the conversation. The interviewer's handoff line now
  carries `- language: <the language the user wrote to me in>` beside the brief path, and
  `report-router` treats that line as the one input it cannot derive: present, the document is
  being delivered in that language and the translator is nameable; absent, there is nothing to
  translate. The line is sent even when the answer is `English` — a stated language is a fact and
  an omitted one is a guess.

  `korean-corrector` stays off both rosters. It has no `report_entry` and `routed=False`, which
  is not two exclusions but one fact stated twice: the translator's report hands it the file it
  audits, and that is the only party that knows the file exists. It has no config key either,
  and `_switch_on` reads it as `off` everywhere — so its roster row now does nothing but keep it
  out of the way.

- **The user decides whether their brief is audited — v0.102.0.** The handoff above made routing
  automatic, which is the wrong default for this one document: the brief is the record of a
  conversation the user had, and an audit of it spends several subagents on something they may
  simply want written down. So the interviewer asks, once, when they close the interview — in
  their language, one line, with what it costs — and relays the answer.

  Three things make it work rather than becoming a prompt nobody reads:

  - *It is asked at the close, not earlier.* Mid-interview it is a question about machinery
    inside a conversation about their problem, and it invites them to close before they are done.
  - *The second line is never dropped in either shape.* "Declined" is sent explicitly rather than
    by omitting the routing line, because that line was just made never-drop: silence would read
    as the agent forgetting it, not as a decision. Same rule guard applies to `guard-inputs`,
    where an absent field is printed as a stated fact rather than left as silence.
  - *Anything but a clear no is a yes.* A brief that skipped the audit reads exactly like one
    that passed it, and the user is the only party who can tell them apart.

  It is also the only question in the interview whose answer does not go into the brief: it is
  about what happens to the document, not about the request.

- **Nobody gathers the session's history; agents extract it.** guard's turn store holds the
  response, plus one sibling file holding the request for the router alone (see the router
  bullets above).
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
  routed turn, so it is one imperative plus a list of fields — this turn's paths, and the
  command that yields the roster — and nothing that reads the same twice. `agents/turn-router.md` is paid
  once per routed turn, in the router's own context, so it holds the triage method, the cue
  per candidate, and the shape of the report. `hooks/context/turn-closeout.md` is paid
  only by whoever is sent to a section, so it holds how to dispatch an agent and what to do
  with its report — needed only for the agents actually picked.

  The test for any line in the hook output is: could the closeout file or the router's own
  definition have said this instead? If yes it belongs there. That test removed the whole
  procedure from the hook, and it is why there is **no `turn-router` section in the closeout file** —
  the router's report names the closeout file and the sections to follow, so the main agent never
  reads a section about routing.

  Three temptations to refuse. Printing each candidate's dispatch block in the hook pays for
  four blocks every turn to use at most four and usually none, the common case being the
  router clearing the turn. Having the *router* write those blocks instead makes an LLM
  re-type instructions it was handed, which is where wording drifts from the file that owns
  it — it names sections, it does not reproduce them. And restating the procedure "so the
  main agent does not have to look it up" is paying every turn to save one Read on the turns
  that route.
- **What bounds the dispatch is the entry point, not the roster alone.** A key the router
  invents resolves to no skill and no agent, so a switched-off agent stays unreachable even
  when it is named anyway — the invocation finds nothing rather than erroring. The roster is
  what stops it being reached for in the first place; the missing entry point is what stops it
  working. This used to be phrased as "the missing section", back when a name the caller could
  not find a section for was the thing that failed.
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
  the next on-demand audit would audit the previous audit's relay instead of
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
  the session mute, which already stops the recommendation while keeping the turn
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
  official docs a subagent runs its own system prompt, so an agent that needs the style's
  rules carries its own copy rather than inheriting them.
- **Eligibility is mechanical; selection is the router's.** The agent modes and one
  prerequisite (a file-reading agent needs a file of its own kind that the turn actually
  wrote, since that list is its whole input and the router cannot invent one) decide what
  the router may choose from. Nothing else. In particular there is no Hangul-ratio test for
  `korean-corrector`: deciding whether a response is Korean enough to audit is a reading
  task, and a ratio has to guess how many English identifiers a Korean answer may carry
  before it stops counting as Korean.
- **`AUDIT_AGENTS` is the set guard RECOMMENDS, not the set it ships.** Two shipped agents have
  no entry in it, and the absence is the design rather than an oversight. `docs-finder` is
  selected by the main agent from its own description, so there is nothing said unasked for a
  switch to govern and no per-turn eligibility to compute — guard keeps no copy of the prompt
  it would be dispatched on anyway. `ext-docs-auditor` is named by the Stop hook whenever
  `edited_refs` is non-empty, which is a fact about the turn rather than a judgment, so routing
  it could only restate the file list and a switch in front of it would be a way to stop a
  just-saved reference from ever being checked.

  Three things follow, and each of them broke or would have broken by assuming the registry is
  the roster. `edited_refs` is a `_edited_bucket` value with no `AUDIT_AGENTS` entry behind it,
  so nothing computes eligibility for it and `cmd_stop` reads the list directly.
  And `settings set` refuses both names, which is
  correct and has to be *said* — `commands/settings.md` tells the skill to explain the refusal
  rather than let it read as a bug.
- **`docs-finder` and `ext-docs-auditor` are a pair: one writes references, the other checks
  them.** That is the point of shipping both, and each half has a constraint that looks like an
  omission. The names stopped rhyming when the finder's search space outgrew the refs
  directory; the auditor's subject did not move.

  `docs-finder` searches in a fixed order — the refs directory, then the repository's own
  documentation, then any configured knowledge directory — and goes to the network only for an
  external subject that none of them settles. It **reports which of those it was**, and that
  distinction is the whole report. It is what the agent replaced: a read-only lookup that
  answered `none` and left the session to remember, unprompted, to dispatch a fetcher next. If
  the report ever stops making the distinction, restore the distinction — do not split the
  agent back into a looker-up and a fetcher.

  Two rules hold that shape and both were asked for explicitly. **The report carries locations
  and never content** — not a quote, not a gist, on any of the kinds. A sentence about what a
  document says is a second version of it for the caller to disagree with, and the caller is
  about to open the file anyway. And **an internal document does not settle an external
  question**: a repo doc discussing a vendor's API records what somebody here believed, so it
  is reported, labelled internal, and the source is fetched regardless. Drop that second rule
  and the refs requirement in `audit-turn-claims` becomes satisfiable by this project quoting
  itself.

  Why the search space widened at all: the trigger the main agent has to apply is "am I about
  to state something I did not read this session", and the old boundary — external only — made
  it apply a second test it has to already be right about to use. Both misreadings of the old
  name resolved toward not dispatching: `ext-` said "internal is out of scope" and `fetcher`
  said "not applicable when I am not fetching". Under-invocation was the reported failure; the
  name is part of the fix.

  `ext-docs-auditor` has **no network on purpose**. A saved reference exists to be a faithful
  copy of something external, so what the auditor judges is whether the excerpt is honest
  about its own origin — and a page that reads differently today says nothing about whether it
  was honest when it was taken. An auditor that could fetch would drift into doing the
  fetcher's job, leaving nothing that checks the fetcher.

  **MarkItDown stays a Bash one-liner (`uv run --with 'markitdown[all]'`) and must not become
  an MCP server.** The fetcher needs it because `WebFetch` paraphrases a long page and `curl`
  returns tag soup from a source that serves no markdown; the `[all]` extra is for PDFs and
  costs no dependency, since guard already requires `uv`. Two reasons against wiring it as
  MCP, and the first is a trap: `mcpServers` in a plugin-shipped agent's frontmatter is
  **silently ignored**, not rejected (`wiki/ref/claude-code-plugin-mcp-servers.md`), so that
  route looks like it works and does not. The route that does work — a plugin-wide `.mcp.json`
  — is session-wide by design, which would hand `convert_to_markdown` (an arbitrary local-file
  read, by its own README) to the main conversation as well.
- **A finding whose fix is a document that does not exist yet is the user's call, not the
  main agent's.** Two agents produce that kind routinely, and both are barred from writing the
  document they recommend. `agents-md-auditor` says an instruction file carries content that
  belongs in a deeper doc — but creating that doc is a change nobody asked for, so the
  closeout file splits its report into the deletions and pointer fixes that need no new file and
  the findings that need a decision. An auditor that "fixed" a bloated instruction file by
  inventing three new ones would have destroyed content under the name of an audit.
  `ext-docs-auditor` is the same hazard in a different directory: the passage it flags is
  fixed by MOVING it, and the destination is usually a design note nobody has written.
- **A `/clear` carries the session switches over; nothing else does.** `/clear` opens a new
  session id, so `state/<sid>.json` no longer applies and both switches would go back to
  `audit-turn` / `audit-plan` — the user who muted guard a minute ago mutes it again, with
  nothing saying why. It is the one boundary worth crossing because it is the one where a new
  session is not a new intention: the conversation was cleared, the work was not. Every other
  start reads the settings, which is what keeps this from being a second, invisible place the
  project's default lives.

  What it carries is a session that **differs from the settings**, and that comparison
  (`_default_paused`) is the whole test — in either direction. It used to be "is anything
  armed", which was the same question while the switches defaulted to muted and is now the
  wrong one: with them defaulting to on, the intention most likely to be lost across a `/clear`
  is a `guard off`, and a check for "armed" would have written no record for exactly that case.
  The announcement names both switches for the same reason.

  **The predecessor is named, not inferred.** Three payload facts, measured in a live session
  on 2026-08-26 because none of them is documented: `SessionStart` with `source: "clear"`
  carries `cwd`, `hook_event_name`, `session_id`, `source`, `transcript_path` — and nothing
  naming the session it replaced; `SessionEnd` carries `reason: "clear"` and the ENDING
  session's id; and the two fire in that order, 55–68ms apart. So the ending session writes
  the record and names itself. The alternative — picking the most recently touched state file
  — is wrong the moment two sessions run in one project, which is normal here.

  Three properties keep the record honest, and each one is load-bearing. It is **single use**:
  read and deleted, so one clear's choice cannot reach a second clear. It **expires**
  (`CLEAR_INHERIT_MAX_AGE_SECONDS`), which covers the record whose reader never ran — without
  it, a file left behind by a crash arms an unrelated clear hours later. And it is
  **announced** in the session context, because an inheritance nobody is told about is exactly
  the invisible gate, and being told is the whole difference.

  Not carried: `plan_audited_hash`. The plan a cleared session had audited is gone from the
  conversation that approved it, so the gate audits again rather than waving through a plan on
  the strength of a review nobody in this session saw.

  **The record's second half is the handover, and it is independent of the first.** The
  `guard:handover` skill writes a handover file and records its path (`guard-handover` →
  `handover_file`); `SessionEnd` copies the path into the same record, and the replacing
  `SessionStart` tells the model to ask the user whether to read it. Nothing about the two
  halves is shared but the file they travel in: a session that wrote a handover and never
  touched a switch still hands the file over, and a session that muted guard and wrote no
  handover still hands the mute over. Collapsing them into one "is there anything to carry"
  test is the way that breaks, and it breaks silently — the record is written, the half that
  was checked survives, and the other half is simply not there.

  The path is checked for existence twice, at both ends, because a handover written and then
  deleted, moved, or renamed leaves a record that only looks valid. What that buys is a
  failure someone can act on: refused at `guard-handover` time, where the skill is still
  running, rather than discovered by a session with no way to ask what went wrong.

  The inheriting session does **not** store `handover_file`. It is announced once, to the
  session replacing the one that wrote it; a session that carried the key would hand the same
  file on again at its own `/clear`, offering a handover the user has already been shown.

  **Why the skill records it rather than the next session going looking.** The alternative
  considered was scanning the handover directory at session start for the newest untracked
  file, which needs no cooperation from the skill and answers a different question: it finds
  *a* handover, not *this session's*. A file left by a session two days ago, by a colleague, or
  by the same session three clears ago all look identical to that scan, and each one offered is
  a session told to resume work that is already done. What it costs is that a skill step can be
  skipped — a session that crashes between writing the file and recording it hands over
  nothing. That is the right direction to fail: the user still has the file.

  **It is an offer, not a read**, and it ignores the session mute and every agent switch. An
  offer because the first prompt after a `/clear` frequently is not the work the handover
  describes, and reading it unasked spends the context the clear just freed on a document the
  user may have moved on from. Unmutable because it is not an audit and not an opinion about
  the answer — it is the second half of something the user explicitly asked for by running the
  skill, and a `guard off` that also swallowed the handover would make the mute a setting for
  something it does not name. Note the asymmetry with the switch line beside it, which ends
  "do not mention this unless the user asks": a switch the user set is already theirs, while a
  handover is a document they wrote for this session and cannot see from inside it.
- **guard cannot install the status line it wants.** A plugin's `settings.json` honors only
  `agent` and `subagentStatusLine` (`wiki/ref/claude-code-statusline.md`), so the main status
  line stays the user's. `status` prints a segment for them to compose into their own and
  `/guard:statusline` offers to wire it. The segment prints **nothing** on any failure: a
  status line runs on every assistant message and is the one place guard must never report an
  error.

  **Both session switches live in that one field, and they are spelled differently on
  purpose.** The turn audit is a FRACTION — agents that can run on the next finished turn over
  agents switched on — so `3/3` armed, `0/3` muted, and the two commands that move it move
  different halves: `guard on|off` the numerator, `/guard:settings` the denominator. It was
  `guard off` until the readings collided: `off` sounds like a statement about guard, while
  the state next to it — also nothing running, for the entirely different reason that no agent
  is switched on — was spelled `guard ·` and contradicted it. The fraction cannot be read
  that way, and it says what the bare count never did, which is how many switches are set at
  all. A project with nothing switched on is `0/0`, not a dot: one grammar, no special case.

  **GREEN MEANS ARMED, and it is not decoration.** The fraction is green while the session is
  auditing and dim while it is muted; the flag below is green while the plan gate is armed and
  dim while it is not. Two independent switches, one vocabulary, so the field is read by
  counting the green rather than by decoding two conventions. The numbers say it a second time
  — `0/N` against `N/N` — which is what survives a log or a screenshot, and the colour is what
  covers the case the numbers cannot: with nothing switched on, both mute states read `0/0`,
  and green against dim is then the only thing separating them. Tinting that pair identically
  makes `guard on|off` a command with no observable effect, which is the failure that killed
  the persistent gate this mute replaced.

  The plan gate is a MARK — filled `⚑` armed, outline `⚐` muted — and it is never absent. A
  second fraction would imply a second roster and there is none; the gate is one bit. Absence
  was the first spelling and it was wrong for a reason worth keeping: a missing mark cannot be
  told from a guard that does not report plan audits at all, so the reader it failed was
  exactly the one who most needed it — someone who has never run `guard-plan` and would never
  otherwise learn the switch exists. Two glyphs of the same shape and width also mean the
  field neither moves nor grows when it flips.

  Both marks are ordinary Unicode rather than Nerd Font glyphs. A private-use codepoint has no
  fallback, and this segment is composed into status lines whose font guard cannot know;
  U+2690 and U+2691 have identical coverage in the fonts a terminal falls back to.

  This segment is the only place either switch reports itself unasked. `/guard:settings show`
  and the SessionStart line still say nothing about plan audits, which is survivable only
  while this field exists — the same argument as for the mute above.
- **The file-reading agents are never routed.** The Stop hook splits the eligible set by
  `reads`: the `reads="turn"` agents go to the router, and `comment-corrector`
  (`reads="files"`) and `agents-md-auditor` (`reads="agent-docs"`) are dispatched directly in
  the same emission, to be sent in the same message so they run concurrently — as is
  `ext-docs-auditor`, which reaches the same block from `edited_refs` rather than from the
  eligible set. Two
  reasons, and the second is why this is a split rather than the narrower "skip the router
  when it is alone".

  Triage asks whether there is material for an agent, and for these that is a diff-level
  question — logic changed, or only a rename or a formatting pass. The router cannot answer
  it from what it is given: the file list is the agent's input, not a diff, and reading
  those files would show their current state, never what this turn changed in them. So the
  hop can only restate what `_eligible_agents` already decided, and bill a subagent for it.

  They need no ordering among themselves either: `_edited_bucket` keeps the three lists
  disjoint, so the one that edits cannot touch what the ones that only report are reading.

  Nor does it need to wait. The ordering rule the router's report carries — auditors
  before correctors — exists so a corrector does not rewrite a sentence an auditor was about
  to flag, and it is entirely about the **answer file**. `comment-corrector` never opens that
  file; it edits comments in source. It shares no input with the routed agents, so there is
  nothing for it to be ordered against and no round trip to pay.

  Consequences worth keeping straight: `agents/turn-router.md` has no `comment-corrector` section
  and candidate lines carry no paths, which restores its "record missing → pick nothing" rule
  to always-correct (the router is now dispatched only when an answer file exists). And a
  dispatch of `comment-corrector` alone names no answer file at all, and since v0.94.0 it does
  not reach the closeout file either: it is handed its files, it edits comments in source, and
  its report is what the caller acts on. Nothing about it is the router's, in either direction —
  the router cannot select it (`cmd_candidates` filters to turn-reading agents) and it never
  touches the answer file the router is reading.
- **The session mute is not `audit_gate` coming back, and it now has a config key.**
  The mute adds one boolean in front of the switches, which is the shape removed
  below, so the difference has to be stated or it reads as a regression — and `audit-turn` /
  `audit-plan` (`config.DEFAULT_CONFIG`, `on` when absent) make stating it more urgent, because
  persistence used to be half the answer and is not available any more. Two things differ, and
  both are load-bearing. It is **two-valued**, so there is no `ask` to reason about — the
  question the old gate forced on the user ("the switch is on, but is the gate open, and does
  `ask` mean before or after routing") does not exist for a boolean. And it is **visible**: the
  `status` subcommand puts it in the user's status line, SessionStart says which of the two
  states the session opened in, and `settings show` prints both the setting and the live session
  value when they differ. That is the real fix — the old gate's cost was not the extra layer, it
  was that you could not tell which state you were in without going and reading a file. If the
  indicator ever becomes impossible to ship, delete the mute rather than let it go invisible.

  **The split that replaced "session-only".** The setting says what a session *opens* in; the
  shell toggle moves the session and nothing else. There is still no path from the toggle to
  guard.local.json, which is what keeps a mute typed at a prompt from silently becoming this
  project's answer to "audit by default?" — the direction that matters, because that write
  would be invisible in exactly the way the old gate was. The reverse direction is fine and is
  the point: a project states its default once, in a file its users can read.

  Why the default is `on` — and what it costs. It was `off` (a session started muted, armed by
  one command) on the argument that an audit the user did not ask for spends a router call plus
  every agent it names before the user can object. That argument still holds; it lost to a
  plainer one: a user who configured agents and installed the status line has asked, and making
  them ask again every session is a per-session tax on the setup they already did. The cost is
  real and is accepted — a fresh install with an agent switched on now audits without a second
  step, and `audit-plan` defaulting on means an approved plan is held for review in a project
  that never ran `guard-plan`. `audit-turn: off` in the config is the one-line answer for a
  project that does not want it, and unlike the old default it survives the session.

  Codex has the SETTING but not the toggle. The toggle is a shell command against a Claude Code
  session id, which Codex has no equivalent for, so `_session_muted` tests `_HOST_IS_CODEX`
  first — which also keeps it from reading a stdin the Codex adapter has already consumed, and
  means no Codex session announces a mute at start. `audit-turn` is a config key, though, and
  `hook_codex._handle_stop` honors it through the state it seeds: a project that writes
  `audit-turn: off` in `.codex/guard.local.json` and gets audited anyway would have been told
  nothing at all, which is the silent-config failure this repo's cross-runtime rule exists to
  prevent. On that host the state value is therefore always just the config's.

  What it does NOT suppress is deliberate: `pending_verify_prompt_id` and the answer file are
  still written while muted, so an on-demand audit works on the turn the user just
  muted. Muting is "stop recommending", not "refuse to audit".

- **The per-agent settings are the only control, and each is named after its agent.**
  There is no gate in front of them. `audit_gate` (`off`/`ask`/`auto`) used to be one, and
  removing it removed a whole class of question — "the switch is on but is the gate open,
  and does `ask` mean the user is asked before or after routing" — that the user had to
  hold in their head to predict what guard would do. Now: an agent not `off` means it can
  be recommended; every switch `off` means guard emits nothing and makes no model call, which
  is what `audit_gate off` used to mean. Every switch ships `off`, so installing guard does not
  start auditing; and the key is the agent's own bare name, so `settings set
  korean-corrector fresh`, `/guard:korean-corrector`, and
  `subagent_type: "guard:korean-corrector"` are one string. Renaming an agent means
  renaming its directory under `agents/`, its skill directory and `name:`, its
  `AUDIT_AGENTS` key, its `hooks.json` matcher, and `_CONTROL_CMD_RE` — together, or the
  vocabulary splits again.
- **`reuse` was removed, and reviving it costs more than the mode.** `AgentMode` was
  `off` / `fresh` / `reuse`: one named instance per session (`_instance_name` →
  `guard-<agent>`), resumed on later turns with its whole history. It bought continuity —
  the instance already knew the repository and the session's conventions and stopped
  re-deriving them — and cost independence, since a verdict it got wrong sat in its history
  as settled and every later turn was built on it.

  What made that trade survivable was one section per agent definition, "If you are
  resumed", telling the instance that a turn record it has not read is a NEW turn and that a
  remembered verdict is not a checked one. Those sections were removed on request, and a
  hazard whose only mitigation is gone is not a mode worth keeping. **Do not revive `reuse`
  without them.**

  Three things went with it, and each is a reason not to bring it back casually:

  - *`keep` / `resume` are not re-pointed at `fresh`.* They meant `reuse`. A user typing one
    is asking for something that no longer exists, and quietly giving them a different mode
    answers a different question; `_parse_mode` returns `None` and the CLI says so.
  - *The stand-down notices are gone.* guard has no handle on a running instance — no
    registry, no way to stop one — so a mode change away from `reuse` had to be *reported*
    to the session that could retire it (`cmd_settings._mode_transition_note`, relayed by the
    settings skill), and the standing policy was stated once at SessionStart. That asymmetry
    comes back with the mode.
  - *It took a rename trap with it.* `_instance_name` and `_agent_id` derived the instance
    name from the ROSTER KEY, and their only two callers passed the key. A renamed agent
    kept emitting its old instance name with nothing failing — invisible until someone
    addressed a name no agent answered to. Both call sites are deleted now; a revived
    `reuse` must derive from the agent name, not the key.

  The boolean CLI aliases survive (`on` → `fresh`, `off` → `off`) because that is what a
  setting here has always been set with, and `on` has to keep meaning something: the mode
  every agent definition was written for. The value stays a *mode* rather than a boolean so
  that a third state can be added without a second key to disagree with the first.
- **Memory is what the agent knows about the project, and it is now the only thing that
  persists across turns.** With `reuse` gone, an instance sees exactly one turn; memory is
  the deliberate, reviewable exception to that.
  The reporting agents carry `memory: project`, and the scope is chosen for the review, not
  for the sharing — see "A stored verdict is invisible when it is wrong" below. The earlier
  reasoning, kept because it is still the right instinct for a different kind of agent: a
  marketplace plugin runs in repositories it does not own, where `project` creates files
  that land in someone else's commits without their asking. `local` is the reversible
  default for that case: a team that
  wants the knowledge shared changes one word in the agent. Note that neither scope is
  gitignored for free — in this very repo `.claude/agent-memory-local/` is not matched by
  any ignore rule, so "not meant for version control" is an intent the project still has to
  enforce. Three rules hold this together and each one is a failure mode if dropped: the
  Write/Edit that `memory` enables is bounded only by each agent's own body — guard ships
  nothing that refuses such a write (see "A stored verdict is invisible when it is wrong"
  below); a remembered claim is re-checked before it is relied on, since memory records where
  to look and never what is true; and nothing in guard reads or writes those directories, so a
  user with auto memory disabled loses accumulated knowledge and nothing else.
- **The router has no memory.** A remembered habit ("this project rarely writes Korean") is
  indistinguishable from a judgment about this turn, and routing is the step nothing else
  checks. Its question is about one turn; anything carrying the last five can answer it from
  the wrong one, silently, at the step nothing else checks. This is also why no agent may be
  held open across turns — see the `reuse` removal above.
- **The router is not the place to save on model.** `agents/turn-router.md` defaults to `opus`.
  Every other agent in the set is paid for by a decision this one makes, so a cheap router
  that misreads a turn saves nothing: it either omits the agent that would have caught the
  defect, or spends a whole subagent for each agent it named on material that was not
  there. The second compounds — it is what teaches the user to wave the recommendation
  through unread, after which the omissions stop being caught either. The triage itself is
  a short read of two files, so the model is the cheap part of it. There is no per-project
  override: a config key here could only be tuned in one direction, and that direction's
  failure is invisible — a router that stops naming an agent looks exactly like a turn with
  nothing in it.
- **An agent that is told to ask needs `SendMessage` in its `tools:`, and the router must not
  have it.** `tools` is an allowlist when present
  (`wiki/ref/claude-code-subagent-frontmatter.md`), so the audit agents list `SendMessage` and
  the router does not. It is there for the fallback ask — a transcript range that was
  compacted away, a term the agent cannot place, a sentence a translator cannot render without
  deciding what it meant. The auditor definitions had said "ask the main session where to
  look" long before there was a tool to ask with. The discipline they already carry is what keeps that
  safe — ask for a pointer, then look yourself, because an answer from the turn's author is
  a claim, not evidence. The router is excluded on purpose: it triages what it was handed
  and has nothing to negotiate.
- **The agent settings are now the ONLY thing that runs an audit on Claude, and that is a
  loss worth naming.** There used to be a per-agent command — a `skills/<agent>/SKILL.md`
  entry point plus a `UserPromptExpansion` matcher passing the agent name to `cmd_verify` in
  argv — which ignored the switch entirely, on the argument that refusing
  `/guard:korean-corrector` because it is `off` takes away the only way to check the very
  thing a project keeps off by default. The skills were deleted and the rest is gone with
  them: the matchers, the `verify` verb, `cmd_verify`, and `AuditAgent.verify_command`.

  Two facts to carry into any attempt to restore it. **A matcher without a command file of
  the same name is inert** — the host answers `Unknown command` before the hook runs, silently
  (probed; `wiki/ref/claude-code-userpromptexpansion-needs-a-command-file.md`), which is how
  these four matchers sat orphaned rather than erroring. And **`pending_verify_prompt_id` is
  still written by every Stop** although nothing on Claude reads it: the Codex adapter matches
  the `/guard:claims-auditor` prompt prefix in `_handle_prompt` and reads the marker there, so
  Codex kept its on-demand path when Claude lost its — and a marker maintained only from the
  day a host regains one is a marker that is wrong on that day.
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
- **Only executable code settles a claim about behavior — v0.65.3.** Reported from use: in a
  real session the auditor caught six errors in a turn and passed two claims sourced to
  javadoc, which the user caught instead ("javadoc 믿으면 안되는데"). The rule is stated as a
  property of the evidence rather than of the author, and aimed at the auditor in the second
  person: prose about code describes intent at the moment it was written, the code moves and
  the prose does not follow, so behavior is verified against the statements that execute and
  prose is a pointer to where to look. Two carve-outs keep it from swallowing the cases where
  prose is the subject — a claim *about* the prose is checked against the file, and saved
  references still settle how something outside this repository behaves.

  **What this change does NOT do, measured.** Six A/B trials against the definition it
  replaced produced **no verdict change** — not one claim flipped between supported and
  unsupported. Fixtures: a javadoc that lies outright; the truth two call-hops away in another
  file; prose evidence never announced as such; the real session's shape reproduced (a *true*
  conclusion resting on javadoc); the same with the citation pointing at the executing line so
  no range-mismatch tell existed; and a fresh domain the rule does not name, run with each
  definition in its own subagent that was never told an A/B was underway. The last two exist
  because earlier trials were compromised — the rule's examples had quoted the fixture almost
  verbatim, handing the auditor an answer key, and a single agent ran both arms knowing what
  was being compared. Both flaws were removed and the result held.

  The prior text already carried "inferring what a function does from ... a comment ... or a
  docstring without reading the body" and "a cited `file:line` that does not actually
  establish the claim counts as unsupported", and on every fixture those two were enough. So
  do not restate this section as a detection improvement; the honest claim is narrower. What
  it adds, and what the trials did show, is that the stale comment gets reported **as its own
  finding** rather than only as the reason a claim failed — the answer that inherited a wrong
  comment is a different problem from one that invented the behavior, the correction belongs
  partly in the comment, and without that line the next reader walks into the same trap.

  The reported miss is therefore probably not a missing rule. In that session the auditor
  applied the surrounding rules correctly and still let the javadoc claims through, and what
  distinguished them is that their conclusions were *true* — checking the conclusion found
  nothing to disagree with. Hence the two-step test (does the cited location execute; do
  those statements establish the claim **as written**), which routes around conclusion-checking
  entirely, and the named shapes it catches: a guarantee credited to the wrong unit, and prose
  broader than the body under it. Whether that helps is unproven — it is stated because the
  failure it targets is real and was observed, not because a trial demonstrated the fix.

- **The router fetches its own roster — v0.65.4.** The Stop hook printed a
  `candidates:` line naming the eligible agents and their modes. It was read by the router
  and by nobody else, yet it landed in the MAIN agent's context on every routed turn: the
  main agent dispatches the router and then follows whatever sections the report names, so
  the roster it held in between informed no decision of its own.

  Two costs, and the second is the reason this changed rather than being left as waste. The
  list is paid for on every routed turn by a reader that never acts on it. And it is an
  invitation to act: a main agent holding the eligible set can dispatch from it directly and
  skip the router, which is the one shortcut that removes triage from the loop without
  looking like a failure — the agents still run, they just all run.

  So the hook now prints the `candidates` verb and the router runs it. That is possible
  because a subagent's Bash carries the PARENT session's `CLAUDE_CODE_SESSION_ID` (verified
  in 2.1.239: a subagent echoed the main session's id, not one of its own), so the verb needs
  no argument and the dispatch grew no field for guard's own bookkeeping — the roster line got
  shorter, not longer. The verb calls the same `_eligible_agents` the hook would have, so the
  two cannot disagree about which switches are on, and filters to `reads="turn"` because the
  file-reading agents are dispatched around the router and naming one would offer the router
  a key its caller opens no section for.

  The cost is `Bash` on an agent that had `Read` only, which was a real property worth
  keeping: a pure triage step cannot wander into the repository. `agents/turn-router.md` now says
  `Bash` is for this one command and that the answer and request files are the only files it
  reads. That is an instruction, not an enforcement — the honest trade is a weaker sandbox on
  the router in exchange for the roster never reaching the agent that could misuse it, and
  the misuse the roster enables is the one nothing downstream detects.

  Two failure shapes had to stay distinguishable, since both would otherwise reach the router
  as silence: no session id (an installation problem, or the `--continue`/bare-`--resume`
  carve-out where the env var holds the startup id) and an empty roster. Both print on stderr,
  and the router is told to report either in one line and pick nothing rather than fall back
  to the candidate sections in its own definition as though they were the roster.

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

  Two consequences. The profile is `memory: user` — the only `user`-scoped store in guard,
  where every other one is `project` — because it describes a person rather than a checkout. And it is only ever written from what
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
- **The audits run on the English, and the translation is made after them.** Not the obvious
  order, and the reason is measured: the auditors are weaker on non-English prose. The same
  answer, translated, drew findings that its original passed clean — twice, from two different
  agents. Auditing the English and translating afterwards is how the user's language stops
  costing them the audit, and it is also why the Korean pair runs after everything else rather
  than beside it: neither has an input until the English is corrected. This used to be stated in
  the closeout file itself; it is rationale, and the closeout now carries rules only.
- **The Korean the user reads is written by an agent that did not write the English.**
  `korean-translator`, ordered before `korean-corrector` in the roster and dispatched at step 2
  of `Presenting the result`. The arrangement it replaces — the main session translating its own
  answer file — is what produced 직역, and the mechanism is not laziness: an author translating
  their own paragraph follows the sentences they just wrote, so English clause order and
  dictionary-first word choice survive into Korean that is fluent, grammatical, and not what
  anyone writes. Measured on a real turn: the Korean read as an English document with Korean
  words laid over it, and `korean-corrector` passed it on 번역체 while repairing three 복합문.
  Its axis 2 does name literal-translation artifacts — forced English word order, calques,
  `~에 대한` noun stacks — so the gap is not that the axis is missing. It is that the axis works at
  the phrase and the repair discipline works at the phrase too: "change only what a finding
  names", one `Edit` per finding, "do not rewrite the file". Document-level 직역 is not a phrase
  anywhere; it is every phrase being individually defensible, and the corrector's own body
  forbids the re-authoring that would fix it. One run does not prove an agent cannot see this —
  that argument comes from the spec text, not from the count.

  Four things this rests on, and each one is a way it could quietly stop being worth having:

  - *It translates from the English, never over a draft.* Handing it the author's literal
    Korean would anchor it to the wording it exists to avoid, so when it is named the caller
    does not translate at all. Step 2 branches on that rather than adding a pass after itself.
  - *Fidelity is the boundary, not a caution.* Free translation is licence over wording and
    sentence shape only; every claim, number, hedge and identifier survives. A sentence it
    cannot render without deciding what the author meant is asked about (`SendMessage`) or left
    plain and reported — never smoothed into an assertion the English did not make.
  - *The corrector still runs after it.* Writer and reader of the same file, which is guard's
    pattern everywhere else. A translator judging its own output is the failure this plugin is
    about.
  - *There is no switch on either half.* An earlier version shipped `korean-translator` `off`
    like every other agent, and `off` there did not mean "no translation" — it meant the author
    translates, i.e. the defect. A setting whose off-state is the bug is not a setting. So both
    it and `korean-corrector` carry `fixed_mode` instead: no config key, `settings set` refuses
    the name, and `guard-candidates` prints `fresh` from the roster. The pair moves together
    because it is one step; a corrector that could be switched off behind a translator that
    could not would ship Korean nothing had read.

    The cost of a switch-free agent is that it could make guard speak on a turn where every
    switch is `off`, which is the silence "every switch ships off" buys. `_eligible_agents`
    prevents that: the riders are dropped unless a SWITCHABLE **turn-reading** agent got
    through both gates. Not "any switchable agent" — a `comment-corrector`-only project has no
    answer file (`_reads_turn` decides that off the same list), so a translator there would
    conjure the file that configuration exists to avoid paying for. And only the riders are
    dropped, never the list, or that same project would lose its own agent.

  It has no `Edit`, so it cannot make a surgical unnoticed change to the English; what actually
  keeps that file read-only is its body ("you never edit it", "do not edit the answer file"),
  since a `Write` grant targets any path. A later audit of this turn reads the English, and a
  translator improving it while translating would put an unaudited change there.
- **`color` warns about the user's own files; it is not an identity.** The docs offer eight
  colors and nothing that says what they mean, so guard assigns them by what an agent can
  damage, not by which agent it is. **`yellow` means this agent edits files you wrote** and
  is worn by `comment-corrector` and `docs-finder` — the two that land unattended in a diff
  the user has to review, one rewriting comments in the source the turn just produced, the
  other adding files under the refs directory and rows to its index. **`red`** is the audit
  path — the auditors, `korean-translator`, `korean-corrector`, `agents-md-auditor`,
  `ext-docs-auditor`, and the router — where the worst case is a wrong finding rather than a
  wrong edit. `korean-translator` writes a file rather than finding anything and is still
  `red` for the same reason the corrector is: the file it writes is guard's own, and nobody
  has read it yet. A third colour,
  `cyan`, was for an agent read-only and outside the audit entirely; no shipped agent is one
  now.

  Two things follow, and the first is the one that looks like a mistake. `korean-corrector`
  edits in place and is `red`, not `yellow`, and that is deliberate: it edits the *answer
  file*, which exists to be corrected and which no one has read yet. Colouring it with the
  agent that rewrites your source would spend the warning on the one edit that needs none.
  And a new agent picks its colour from this rule rather than from wanting a fresh one —
  distinct-colour-per-agent was considered and is wrong here, because it makes the palette
  carry no information at exactly the moment there are enough agents for it to matter.

  This rule lives here because nothing enforces it. It is one word in a frontmatter file,
  invisible until the wrong agent is already running under a reassuring colour.
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
  adapter for the same reason. Closing that gap means
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

## User entry points: `commands/` vs `skills/`, and the settings fork

The split between the two directories is **by runtime, not by kind**. `commands/<name>.md` and
`skills/<name>/SKILL.md` both produce `/guard:<name>` in Claude Code, but the Codex manifest
registers only `./skills/`, so putting a Claude-only entry point in `commands/` is what makes
it one Codex no longer offers — and then refuses.

Whichever directory it sits in, an entry point reaches the CLI as
`${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py` — substituted in a plugin skill's content and in
its `allowed-tools` rules alike (`wiki/ref/claude-code-skill-substitutions.md`). Never by
climbing out with `${CLAUDE_SKILL_DIR}/../..`: that depth is a bet on where the file sits, and
the file has moved.

`/guard:settings` is the one entry point that does **not** run in the main session. It carries
`context: fork` with `agent: general-purpose`, and the reason is cost: a session late in its
life re-pays for its whole context on every turn, so a settings exchange held there is charged
against the conversation the user actually came for. A forked skill does not inherit that
conversation — `context: fork` is not `/subtask` (`wiki/ref/claude-code-skill-fork-context.md`)
— so the body and the exchange both stay out of it. Two things follow, beyond the
`GUARD_SETTINGS_SKILL` marker covered above.

**The body is long on purpose, and that is not the usual smell.** With the fork it is paid for
once, by the agent that needs it, and never by the conversation the user came for — so the
question for anything in it is "does this run use it", not "is the file short". The real
constraint is the `context: fork` warning: a forked skill needs an actionable task, so
reference material has to sit inside instructions rather than replace them.

**It stays `background`, which is the default and must remain so.** Only background agents
appear in the interactive panel, and that panel is how the user opens the transcript and keeps
adjusting settings by talking to the agent (`wiki/ref/claude-code-subagent-resume.md`).
Foreground would take the tokens out of the main context and hand back nothing the user could
continue.

## Config (`.claude/guard.local.json`)

Parsed by `_load_config`; fail-open to defaults. Only keys whose value matches the
default's type are honored; unknown
keys are ignored and a missing or malformed file falls back to every default.
`guard.local.json.example` ships at the plugin root.

Keys: one `AgentMode` per agent, named after that agent — `claims-auditor`,
`deferrals-auditor`, `clarity-auditor`, `comment-corrector`, `agents-md-auditor`,
**all default `off`** — which together
are the only control over whether guard says anything unasked. `docs-finder` and
`ext-docs-auditor`, `korean-translator` and `korean-corrector` are shipped agents with no key
here; the invariants above say why, and
`settings set` refuses both names rather than writing a key nothing reads. See the
invariants above for why the value is a mode rather than a boolean, why `reuse` was removed
and what reviving it would cost, and why they all ship off. A value that is not a mode word reads as `off` — the safe
direction, since the alternative is guard acting on a setting the user did not write.

One subtlety `_load_config` must keep: an `AgentMode` default round-trips through JSON as a
plain `str`, and `isinstance("fresh", AgentMode)` is False, so the accepted type is widened
to `str` for those keys. Without that widening every mode in the file is dropped and only
the session state is ever honored — which is exactly the bug this shape introduced once.

There is deliberately **no key for the router's model**. `agents/turn-router.md` pins `opus`, and a
config key could only ever be turned one way in practice — cheaper — which is the way whose
failure cannot be seen: a router that stops naming an agent produces exactly the output of a
turn with nothing in it, and the audit that never ran is the failure guard exists to prevent.
Every agent brings its own model and effort from its own frontmatter in `agents/`, which is
also where its criteria live; a second copy in guard's config would let the two disagree about
the same agent.

`audit-turn` / `audit-plan` (string, `"on"` by default; `"off"`, or any off-word, or a JSON
boolean) — the state each session's turn audit and plan gate **open** in. They seed
`audit_paused` / `plan_audit_paused` in `state/<sid>.json` and nothing else: `guard` and
`guard-plan` write that state, never this file, so the setting is the project's answer and the
toggle is one session's. An absent or unreadable value reads as `on`, the opposite fallback
direction from the agent modes, which fall back to `off` — an unreadable agent mode would run an
agent nobody named, while an unreadable switch here can only leave guard auditing, and that is
what an absent key already does. Two keys and not one: the two audits run at different moments
on different material, and wanting turns checked is not wanting every plan held. Why the default
is `on`, and what that costs, is the session-mute invariant above.

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

`knowledge_dir` (list of strings, default `[]`; a bare string is accepted as one entry) —
where the project records what its **deployed** system looks like: topology, environments,
runbooks. Read by `paths._knowledge_dirs` for `design-environment` and by nothing else, and
nothing derives a write path from it, which is why it is deliberately NOT confined to the
project the way `refs_dir` is: this material routinely lives in a knowledge base outside the
repository, so an absolute path and a `~` are the expected shapes. Order is precedence. A list
because the knowledge is normally split — one directory per system, per team, or per source.

It had no CLI surface at all until v0.113.0, and that is the failure worth recording. The key
was honored by `_load_config`, read by `_knowledge_dirs`, and printed by the
`knowledge-dirs` subcommand — which only prints. `settings show` did not list it, `settings
set` refused it, and the settings command forbids hand-editing the file in bold while calling
the CLI the file's only supported writer. So the one documented way to configure it was the one
way the documentation prohibits. Nothing failed: every piece worked, and the missing piece was
a branch nobody wrote. `docs-finder` has an explicit "no key, deliberately" comment beside its
absence; this had none, which is the difference between a decision and an omission and the
reason a new key should carry one either way.

`set` replaces the whole list rather than appending, because order is precedence and an
append-only verb leaves no way to reorder or drop one entry. The value is stored as written
rather than filtered to what exists — configuring a directory before creating it is normal, and
filtering would discard the setting with nothing on screen to say so. Instead `show` names any
entry that does not resolve, and it is the ONLY place that happens: `_knowledge_dirs` drops a
bad entry silently because it runs on a dispatch, where the agent reading the list was not built
to act on a warning. `_knowledge_dir_entries` exists so both audiences share one normalization;
duplicating the `~`-and-relative rules is how the two would come to disagree.

`settings unset <key>` is the only way a key leaves the file, and it exists because `set`'s
preserve-everything rule has no other exit. A key guard stopped honoring — `exempt_skills`,
`audit_gate` — is invisible to `show`, ignored by `_load_config`, and carried forward by
every `set` indefinitely; since the file may only be written through this CLI, without this
verb the only way to clear one is the hand-edit the settings skill forbids. Two things about
its shape are deliberate. It deletes **any** key, live or dead, rather than pruning what it
judges stale: guard cannot know which keys a newer version owns, so a downgraded user's
config would be silently destroyed. And deleting an agent switch goes through the same
step a `set` does — the session's cached mode is reset to the default — because reverting a
switch is a change to what guard does now, not just to the file.

## One audit, two paths: the entry splits, the agent does not

`claims-auditor` was written for one caller. When `report-router` began routing standalone
documents — today an `interviewer` brief — it dispatched that same agent at a file, and every
sentence in the body about "the turn", the transcript, the request and the extraction fallback
became a statement about an input that does not exist on that path. The same was true of
`deferrals-auditor` and `clarity-auditor`.

The rule that came out of it: **split at the ENTRY, never at the agent.** All three shared
audits are one agent behind two `context: fork` skills.

### Why not two agents, which was built first

The first fix was two agent definitions per audit, generated from a shared criteria partial.
It works, it shipped, and it was taken back out — for a reason no generation scheme can
address: **an agent's memory directory is named after the agent.** Two definitions are two
memories. Whatever `turn-claims-auditor` learned about where this repository keeps its evidence
was invisible to `report-claims-auditor`, which relearned it — or did not — and the two drifted
with nothing reporting the drift. For `clarity-auditor` the same mechanism is worse still,
because what lives in its `memory: user` directory is the **reader profile**: two copies would
be two `user`-scoped directories and neither would be the reader's.

So the agent stays one and each path gets a skill whose body is the input-gathering task —
`skills/audit-{turn,report}-{claims,deferrals,clarity}/`. The runtime split is exactly the one
this needs: **the agent definition is the system prompt and the skill body is the task**
(`wiki/ref/claude-code-skill-fork-context.md`), and `agent:` accepts a plugin-scoped
`guard:claims-auditor` (probed, `wiki/ref/claude-code-skill-invocation-paths.md`).

### The judgments that really do differ, and where they live

Two of the three audits have a point where the paths do not differ by degree — they reverse.
That is what originally argued for two agents, and it is the part the entry split has to
answer for.

- **The documentation rule (claims).** On a turn, a claim citing official docs must point at a
  local saved copy under the refs directory or it is unsupported — the session that wrote the
  turn is told by SessionStart to save one, so its absence is a defect. On a document the same
  rule fails *every* citation in *every* brief; `agents/interviewer.md` tells the interviewer
  "You cannot save a copy, so the URL is the whole citation".
- **A deferral handed to a person (deferrals).** On a turn, "your call" is legitimate outright:
  the user was there and being asked is the point. In a document nobody was, so the same
  sentence is the author deferring on their own behalf unless the text records the question
  actually being put to someone.

Neither needs a second definition. **The agent states the shared part of the rule and says in
so many words that the reversing part is its skill's to settle**, and each skill settles it.
What the agent must not do is state one path's answer as the rule and leave the other skill
contradicting it silently — a reader of the agent would then have two rules and no way to tell
which was authoritative. `clarity-auditor` has no such point; nothing about what makes an
explanation followable differs by path, and its skills carry gathering only.

The rest of what differs is gathering, and gathering is what a skill is for. History is absent
on the document path by construction rather than missing — `cmd_inputs._inputs_for_file` prints
no transcript and no turn id, because a brief is written inside a subagent's own conversation
that the main session's transcript does not contain. The turn skills' `SendMessage` fallback is
right there and wrong here: the main session did not write the brief and did not watch the
interview, so its account is not the author's testimony but a third party recalling something
it never saw. Triage differs too — the shapes that let a turn pass without opening the
repository (an acknowledgement, a question back, a report of an action just taken) do not occur
in a document written to be read later, so the claims audit has no early exit there, and "a
proposal is not nothing verifiable", an easily-misapplied exemption on the turn path, is the
*normal case* on the other.

### Details that were decided rather than defaulted

**The agents name no skill.** They say a skill hands them the task, not which one. An agent
cannot check which skill forked it, so a name there buys nothing at runtime and rots silently
when a skill is renamed — nothing errors, the sentence just becomes false. The names live where
they are checked: the roster, and `dev/check-entries.py`.

**The descriptions are as short as a description gets: "Invoked by guard only."** A skill
description is loaded into every session's context whether or not guard ever runs, so its cost
is paid on every turn of every project that installs the plugin. What it normally buys is the
model recognising when to invoke the skill — and none of guard's audit skills need that. Every
one of them is named, verbatim, by whatever summons it: the router prints `audit-turn-claims`
and the caller invokes that name from its closeout section, and the plan gate prints "Run the
`guard:audit-plan` skill over the plan" (`cmd_plan_gate.py`). A user typing
`/guard:audit-plan` is matching the name too, not the description. So the line has exactly one
job left — keeping the model from choosing the skill for itself — and it does that in four
words.

That job is not optional, which is why the field is short rather than empty. A description
that described the review got twelve agents dispatched over a plan nobody had approved
(measured), and naming the triggering hook puts the trigger back: a model that has just left
plan mode reads `ExitPlanMode` as its cue. What is *not* the alternative is
`disable-model-invocation: true` — it would shut guard out as well, and guard is the only
thing that should invoke these.

**`background` is `true` on all six audit skills, and no longer splits by path.** Both routers
dispatch every audit in one message and neither caller edits the file until the last report is
in, so there is no order for a blocking invocation to hold and `false` would only serialise what
the template asks to overlap. It was `false` on the three `audit-turn-*` skills for one version
(v0.110.0 above, and v0.112.0 for why the serial order went away) — the mechanism worked; what it
enforced stopped being wanted.

The tool-set question is settled and is not what decides this: these agents carry
`Read, Grep, Glob, Bash, SendMessage` and the background filter keeps all five. What a
backgrounded fork actually loses is `Agent`, which none of them uses.

**So the roster field is `turn_entry` / `report_entry`, not `turn_agent` / `report_agent`.** An
entry is a skill for the three shared audits and the agent's own name for the rest; the
invariant that survives is that the name the router prints is the name the caller invokes, and
the router's own report template says which tool. `dev/check-entries.py` resolves an entry
against `agents/<name>.md` **and** `skills/<name>/SKILL.md` for that reason.

The document path keeps one caution the turn path does not need, in the clarity skill: the
profile describes the person the session talks to, and a document is read later, possibly by
someone else. The skill tells the agent to say which reader a finding was calibrated for rather
than to invent a second one.

### What the generation step was, and why it is gone

While the shared audits ran as two agents each, most of both bodies was identical and two
hand-maintained copies drift silently — a document auditor quietly judging by last month's
standard is not a failure anything reports. So the criteria lived once in
`dev/agent-src/partials/` and `dev/build-agents.py` inlined them into both at build time, with
the generated files committed because installation copies the repo tree and there is no build
step at install time.

The obvious alternative had been a shipped criteria file the agents read at dispatch, resolved
by a CLI verb the way `turn-closeout.md` is. It was rejected for one reason worth keeping
on record, because it applies to anything guard might later ask an agent to load: **a
referenced file is a file an agent can decline to read, and nothing reports the decline.** An
agent definition is loaded into the agent by the host; a `Read` it was told to perform is a
step it can skip, and the skip is invisible in the report. Mitigations were considered — a hard
precondition, a `criteria: read` field in the report mirroring `inference:` — and they make a
skip *visible* rather than impossible.

Two constraints from that period are worth keeping if a build step ever comes back. **The
template language must not be one**: whole-file inclusion and a single derived substitution, no
conditionals and no expressions, because the moment the mechanism can make decisions the two
outputs can diverge *inside* the shared partial, which is what it exists to prevent. And
**sources must live outside `agents/`**: a plugin's `agents/` directory is scanned recursively,
and the skip rules that drop a malformed project or user agent do not apply to a plugin agent —
missing `name`, or YAML that does not parse, still loads it under its filename
(`wiki/ref/claude-code-plugin-agents-directory-discovery.md`). A template under `agents/` would
not be ignored; it would register as a real, broken agent, and `.tmpl.md` is not protection
because extension filtering is undocumented.

The entry split removed the duplication, so `dev/agent-src/` and `dev/build-agents.py` are gone.
`dev/check-entries.py` keeps the half of that script that was never about generation.

### The switch key, and the checks

**The switch key did not move, and must not.** `claims-auditor` is what a project writes in
`guard.local.json`. `_load_config` honours only keys present in `DEFAULT_CONFIG` and warns
about nothing else, and `_agent_mode` then falls back to that default — `off`. Renaming the key
to follow an entry point would silently switch the audit off for every project that had
configured it. So the key names the audit, `turn_entry` / `report_entry` name the entry points,
and `agents._path_entry` is the single translation, called only by `cmd_candidates`. Downstream
of that call the entry name is the only string in play: the router's report, the closeout file
section its caller opens, and the `subagent_type` or skill name that caller invokes are all the
same string.

This is why `_agent_id` and `_instance_name` were deleted rather than kept: both prefixed
whatever they were handed, both were only ever handed a roster key, and both would now emit a
`subagent_type` and an instance name matching nothing. That trap survives the deletion as a
rule — nothing but `_path_entry` may derive a dispatchable identity from a key.

**`--doc` replaced a rule the document router had to remember.** `guard-candidates --doc` maps
each eligible audit through `report_entry` and drops the ones that return `None`, so the Korean
pair is simply never offered on that path. The paragraph telling `report-router` to refuse them
by name is now a note about why they are absent rather than an instruction it has to follow.

**Checks, since this repository has no CI.** `uv run dev/check-entries.py` fails if a
`turn_entry` / `report_entry` matches neither `agents/<name>.md` nor `skills/<name>/SKILL.md`,
or if the file it does match declares a different `name:` in its frontmatter. Those are the two
ways the Python roster and the markdown definitions can disagree, and both are silent at
runtime: a dispatch to a `subagent_type` that matches no file, or an invocation of a skill that
does not exist, finds nothing rather than raising, and a frontmatter `name:` that disagrees with
the path registers the definition under a name nobody invokes. Exercised by breaking them
deliberately. Nothing runs it on its own; it belongs in a repo-local pre-commit hook and in the
recipe below.

Codex keeps the bare `claims-auditor`
throughout: it has no document path, and its installed
`.codex/agents/guard_claims_auditor.toml` stays in a user's project across plugin upgrades
while `hook_codex.py` hardcodes that name — renaming one without the other points the hook at
an agent the project does not have.

## Manual testing

**Everything the hook does is deterministic and runs without the CLI or auth.** That is new:
the router used to be a real `claude` child, so testing meant tolerating a model's
nondeterminism and a 5-11s wait per turn. It is a subagent now, so the hook's whole job is
eligibility plus text generation, and every case below is an exact assertion.

What this recipe can no longer check is the routing itself — whether the router picks the
right agents. That lives in `agents/turn-router.md` and is exercised by using guard, not by this
script. What it does check is that the router is *asked* correctly: the right candidates,
the same turn-record path for every agent, and nothing offered that is set to `off`.

```bash
export CLAUDE_PROJECT_DIR=/tmp/guard-test/proj
# Override these two as well, and do not skip it. A shell inside a project that already runs
# guard has them exported by that project's SessionStart, and `settings` resolves its project
# from `GUARD_PROJECT_DIR` (never from `CLAUDE_PROJECT_DIR`, which no Bash command receives).
# Leave them and the recipe's `settings set` lines silently rewrite the REAL project's
# `guard.local.json` — every switch in it — while the assertions below still read as passing.
export GUARD_PROJECT_DIR=/tmp/guard-test/proj
export GUARD_REFS_DIR=/tmp/guard-test/proj/refs
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

# ARM THE SESSION EXPLICITLY, even though `audit-turn` defaults to on and this project has no
# config file. The default is not the assertion: a project that ships `audit-turn: off`, or a
# state file left behind by an earlier run, makes every `run` below silent for the WRONG reason
# and each assertion that expects a recommendation passes as (EMPTY) while testing nothing.
# `toggle-cli` takes its argument in argv and its session id from the ENVIRONMENT, so both are
# set per command.
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli on > /dev/null

# `toggle-cli` is what the `guard` shell command wraps, and the only way to the mute from a
# shell prompt (`settings set audit-turn` also moves it, but through the config).
# The last two are the reason this verb exists: it must never be silent, because a person is
# reading it and silence reads as success. Both must PRINT and exit non-zero.
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli status   # -> one line; exit 0
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli on       # -> "audits ON for this session." and
                                                   #    NOTHING about which agents — the
                                                   #    router names those, per turn
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli status   # -> the SAME sentence as the line above;
                                                   #    a difference here means the report
                                                   #    path and the write path have drifted
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli off      # -> "audits OFF ... `guard on` to arm."
CLAUDE_CODE_SESSION_ID=s1 GUARD_TOGGLE_NAME=gd "$H" toggle-cli off   # -> "`gd on` to arm."
CLAUDE_CODE_SESSION_ID= "$H" toggle-cli on; echo "exit=$?"      # -> stderr; exit=1
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli bogus; echo "exit=$?" # -> stderr; exit=1

# The shell command's own wiring: SessionStart writes a PATH line into $CLAUDE_ENV_FILE.
# Run it more than once — SessionStart has no matcher, so it fires on compact and fork too,
# and a blind append would add the same line once per compaction.
ENVF=$(mktemp); CLAUDE_ENV_FILE=$ENVF
for i in 1 2 3; do echo '{"session_id":"s1"}' | "$H" session-start > /dev/null; done
grep -c 'export PATH=' "$ENVF"      # -> 1, not 3
# And the point of an executable over a function: it survives into a subprocess.
sh -c ". $ENVF; sh -c 'CLAUDE_CODE_SESSION_ID=s1 guard status'"   # -> one line
python3 -c "import json;print(json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'))['audit_paused'])"
#   -> False. Every case below assumes it.

# All switches off (the shipped default): NOTHING is emitted, but the pending target must
# still be recorded: Codex's on-demand path reads it, and a marker maintained only from the
# day a host regains one is a marker that is wrong on that day.
# Check the TRACE, not just the emptiness: an armed session with no switches records
# `none_eligible`, and a muted one records `skip_paused` instead — the two are indistinguishable
# from stdout alone, which is how a mute reason can masquerade as this case.
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
#   -> one imperative plus fields: the closeout path, the turn dir, the answer and request
#      files, the `candidates` COMMAND (never the roster itself — the router runs it), and
#      the transcript + turn id. Nothing here describes what an agent does, how to dispatch
#      it, or what to do with its report — those are the closeout file's, and the router's answer
#      is what names the sections.
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/p1.md"
#   -> the second section reads "Not collected" and carries the ask for earlier evidence
#      plus the ban on the main agent's own case for the claim. Nothing collected it.

# The roster must never offer a switched-off agent. The closeout file is the second bound: a key
# the router invents has no section to follow. The roster is not in the Stop output any more,
# so this is checked where the router now reads it — and note the FILTER: the verb prints only
# the turn-reading agents, so a `comment-corrector` that is on must NOT appear here.
# Use a SETTABLE agent for this: the Korean pair has no switch, so `settings set
# korean-corrector off` is refused and would assert nothing.
"$H" settings set deferrals-auditor off --session s1
run p2 "Redis는 Postgres보다 항상 빠릅니다."   # -> the `candidates:` line, unchanged by the switch
CLAUDE_CODE_SESSION_ID=s1 "$H" candidates     # -> audit-turn-claims=fresh (+ the Korean pair),
                                              #    and no deferrals-auditor
# The line prints the ENTRY POINT, not the switch key. `claims-auditor` is what the user sets
# and must never appear here; `audit-turn-claims` is what the router names and its caller
# invokes. A regression in `_path_entry` shows up as the key leaking into this output.
CLAUDE_CODE_SESSION_ID=s1 "$H" candidates | grep -qx 'claims-auditor=fresh' && \
  echo 'REGRESSION: the switch key reached the router'
# The document path: same eligibility, mapped through `report_entry`. The Korean pair must be
# absent — that mapping is what replaced the paragraph telling the document router to refuse
# them by name, so if they appear here the router has nothing left to stop it naming them.
CLAUDE_CODE_SESSION_ID=s1 "$H" candidates --doc  # -> audit-report-claims=fresh, nothing else
# The two failure shapes must not both be silence: one is an installation problem, the other
# a real (if unexpected) answer, and the router is told to report each in one line.
CLAUDE_CODE_SESSION_ID= "$H" candidates       # -> stderr: no CLAUDE_CODE_SESSION_ID; exit 0
CLAUDE_CODE_SESSION_ID=nosuch "$H" candidates # -> stderr: nothing switched on; exit 0

# Every entry point the roster names must resolve to a file that declares that same name.
# This is the one assertion that does not need a session: run it from the plugin, and break it
# deliberately once (point a `turn_entry` at a skill that does not exist) to confirm it is not
# passing as a no-op.
(cd "$CLAUDE_PLUGIN_ROOT" && uv run dev/check-entries.py)  # -> every entry resolves; exit 0

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
echo '{"session_id":"s1","prompt_id":"pq","prompt":"korean-corrector는 켜줘"}' | "$H" user-prompt
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/pq.request.md"   # -> header, then the prompt verbatim
run pq "Turned it on."      # -> `turn dir:` once, then `{turn dir}/pq.md` and `{turn dir}/pq.request.md`
run pnone "Turned it on."   # -> same shape MINUS `request file:` (no user-prompt ran)
# There is no `verify` verb any more, and no per-agent command on Claude. The marker below is
# still written because Codex reads it.
"$H" verify claims-auditor < /dev/null   # -> no output, exit 0 (unknown verb, fails open)

# The answer file is gated on the agents that READ it. With only `comment-corrector` on,
# `user-prompt` says nothing and the dispatch carries no `answer file:` line — that agent
# reads source files. On-demand audits still work: the record holds guard's verbatim
# response section plus a note saying the turn was never told to write into it.
"$H" settings set claims-auditor off --session s1
"$H" settings set comment-corrector on --session s1
echo '{"session_id":"s1","prompt_id":"pc","prompt":"rename a variable"}' | "$H" user-prompt   # -> nothing
echo "{\"session_id\":\"s1\",\"prompt_id\":\"pc\",\"tool_input\":{\"file_path\":\"$CLAUDE_PROJECT_DIR/src/cache.py\"}}" | "$H" post-edit
run pc "Renamed it."   # -> the direct block only: closeout and `files to audit` — and NO
                       #    router block at all, so no `answer file:` and no `candidates:`
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

# The two edited lists must stay disjoint and must not cross-trigger. `notes.md` above lands
# in NEITHER; `AGENTS.md` and `CLAUDE.md` land in the agent-doc list only. Three things to
# check here, and the first is the one a per-bucket reset would break.
"$H" settings set agents-md-auditor fresh --session s1
printf '# x\n' > "$CLAUDE_PROJECT_DIR/AGENTS.md"
buckets(){ python3 -c "import json;d=json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'));print(d['edited_files'],d['edited_agent_docs'],d['edited_refs'])"; }
edit(){ echo "{\"session_id\":\"s1\",\"prompt_id\":\"$1\",\"tool_input\":{\"file_path\":\"$CLAUDE_PROJECT_DIR/$2\"}}" | "$H" post-edit; }

edit pa src/cache.py; edit pa notes.md; edit pa AGENTS.md; buckets
#   -> [cache.py] [AGENTS.md] []: notes.md is in no bucket

# The one collision the ORDER of the bucket tests exists to settle. Both of these are inside
# the refs dir, and one is named AGENTS.md — it must NOT reach agents-md-auditor.
# No `settings set` here: `ext-docs-auditor` has no switch, and the refs block is emitted off
# `edited_refs` alone.
mkdir -p "$CLAUDE_PROJECT_DIR/wiki/ref"
printf '# refs\n\n| File | Subject | Source |\n| --- | --- | --- |\n| v.md | x | y |\n' \
  > "$CLAUDE_PROJECT_DIR/wiki/ref/AGENTS.md"
printf '# v\n' > "$CLAUDE_PROJECT_DIR/wiki/ref/v.md"
edit pr wiki/ref/v.md; edit pr wiki/ref/AGENTS.md; edit pr AGENTS.md; buckets
#   -> [] [AGENTS.md] [wiki/ref/v.md, wiki/ref/AGENTS.md]
#      The project AGENTS.md is an agent doc; the refs index is a ref.
run pr "Saved a reference."  # -> the refs block, ext-docs-auditor with only the two refs paths
run pa "Did both."      # -> ONE direct block, comment-corrector then agents-md-auditor,
                        #    each with only its own paths, and no `answer file:` line

edit pb AGENTS.md; buckets
#   -> [] [AGENTS.md]: a new turn resets BOTH lists, so cache.py does not ride along
run pb "Docs only."     # -> agents-md-auditor alone

# Off is off, even with a file waiting for it.
"$H" settings set agents-md-auditor off --session s1
edit pc AGENTS.md
run pc "Docs only."     # -> empty: comment-corrector has no source file, the other is off

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

# `reuse` is gone. The word must not be accepted as a mode, and neither must the two aliases
# that used to mean it — silently resolving one to `fresh` would answer a different question
# than the user asked. Check all three, and check a config file that still holds the old value.
"$H" settings set claims-auditor reuse --session s1   # -> error naming off/fresh
"$H" settings set claims-auditor keep --session s1    # -> same
"$H" settings set claims-auditor resume --session s1  # -> same
# Then hand-edit `.claude/guard.local.json` to put `"claims-auditor": "reuse"` back, and:
"$H" settings show --session s1
#   -> claims-auditor: off. A stale `reuse` in the file is not a mode word, so it reads as
#      off rather than as the agent being on — the safe direction.
echo '{"session_id":"s1"}' | "$H" session-start
#   -> NO instance line. There is no held-open agent left to announce.

# The switch-free agents. The two Korean ones ride along and must never make guard speak on
# their own; the two ext-docs ones may reach no switch-driven path at all, and the refs block
# must survive a config with everything off — that is the point of them having no switch.
"$H" settings set korean-translator fresh --session s1  # -> error: not a settable key
"$H" settings set korean-corrector fresh --session s1   # -> same
for k in claims-auditor deferrals-auditor clarity-auditor comment-corrector \
         agents-md-auditor; do
  "$H" settings set $k off --session s1
done
"$H" settings set docs-finder fresh --session s1
#   -> error listing the settable keys: not a config key, and must stay refused
"$H" settings set ext-docs-auditor fresh --session s1   # -> same
"$H" settings list
#   -> six agent lines and refs_dir. Neither `docs-finder` nor `ext-docs-auditor` appears,
#      and there is no router_model line.
echo '{"session_id":"s1"}' | "$H" session-start
#   -> the refs rule only: no agent is on, so no closeout line.
edit pr2 wiki/ref/v.md
echo "{\"session_id\":\"s1\",\"prompt_id\":\"pr2\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"done.\",\"stop_hook_active\":false}" | "$H" stop
#   -> the refs block ALONE, naming ext-docs-auditor; trace outcome: refs. Every switch is
#      off, which is exactly the case a switch in front of this agent would have silenced.
echo '{"session_id":"s1","prompt_id":"pr2"}' | "$H" user-prompt
#   -> nothing: `_reads_turn` is false with every turn-reading agent off, and the refs block
#      carries file paths rather than the answer file.

# The `verify` verb is gone, and so is every per-agent matcher. What must stay true is that
# the manifest carries no matcher without a command file behind it — an orphan is inert and
# silent, so nothing else would report it.
python3 -c "
import json
h = json.load(open('plugins/guard/hooks/hooks.json'))['hooks']
print(h.get('UserPromptExpansion'))   # -> None; guard registers no expansion matcher
"

# The two audit switches. Each one is BOTH a config key and a seed for the live session, and
# the state key it seeds is inverted from it — so check the state, not only the printed line: a
# `set audit-turn off` that wrote `audit_paused = False` would print exactly what was asked for
# and do the opposite.
"$H" settings set audit-turn off --session s1
python3 -c "import json;print(json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'))['audit_paused'])"
#   -> True
run pmute "Redis is always faster."     # -> (EMPTY); trace: skip_paused, NOT none_eligible
CLAUDE_CODE_SESSION_ID=s1 "$H" toggle-cli on > /dev/null
"$H" settings show --session s1
#   -> `audit-turn: on (this session; project setting off)`. Both halves, because the toggle
#      does not write the file and the file no longer describes the session.
"$H" settings unset audit-turn --session s1     # -> back to the default ('on'), session too
python3 -c "import json;print(json.load(open('$CLAUDE_PROJECT_DIR/.claude/guard/state/s1.json'))['audit_paused'])"
#   -> False
"$H" settings set audit-plan false --session s1   # a JSON-style word is accepted, like `off`
"$H" settings set audit-turn sometimes --session s1   # -> error naming on/off; nothing written
"$H" settings unset audit-plan --session s1

# Unknown keys and unknown values are both rejected outright rather than silently accepted.
"$H" settings set audit_gate off --session s1   # -> error listing the settable keys;
#   `audit_gate` was the old off/ask/auto gate in front of the switches and must stay rejected
"$H" settings set claims-auditor maybe --session s1  # -> error naming off/fresh

# `unset` is the only way a key leaves the file. It must handle the key that is not there,
# the key guard does not honor, and the live switch whose instance has to stand down.
"$H" settings unset nope --session s1            # -> "nothing to remove", lists keys present
python3 -c "import json,pathlib;p=pathlib.Path('$CLAUDE_PROJECT_DIR/.claude/guard.local.json');d=json.loads(p.read_text());d['exempt_skills']=[];p.write_text(json.dumps(d))"
"$H" settings unset exempt_skills --session s1   # -> "guard does not honor that key"
"$H" settings unset korean-corrector --session s1
#   -> "back to the default ('off')", then the settings, then the stand-down note for
#      `guard-korean-corrector`. Reverting a switch is a change to what guard does, so it
#      owes the same note a `settings set ... off` does.

# The mutating CLI verbs refuse without the marker; reads still work.
(unset GUARD_SETTINGS_SKILL; "$H" settings set claims-auditor off; "$H" settings unset refs_dir; "$H" settings show)

# A HOOK must obey CLAUDE_PROJECT_DIR even when a stale GUARD_PROJECT_DIR is in the
# environment. This is the nested-session case and it is not exotic: guard exports
# GUARD_PROJECT_DIR into its own session's Bash, so any `claude` started from there — a
# nested run, or `cd ../other-repo && claude` — inherits the first project's path.
mkdir -p /tmp/guard-test/other/.claude
cp "$CLAUDE_PROJECT_DIR/.claude/guard.local.json" /tmp/guard-test/other/.claude/   # else it is silent
echo '{"session_id":"sx","prompt_id":"px","prompt":"q"}' \
  | CLAUDE_PROJECT_DIR=/tmp/guard-test/other GUARD_PROJECT_DIR=/tmp/guard-test/proj "$H" user-prompt
#   -> names a file under /tmp/guard-test/other. If it says /tmp/guard-test/proj, the
#      precedence in `_project_dir` has been flipped back and one project is writing its
#      turn records into another.
```

## `interviewer`, and what actually keeps a subagent conversation free

Measured 2026-08-26 against claude 2.1.246, in a throwaway git project driven from a second
tmux/Herdr pane with `GUARD_TRACE=1`, `--plugin-dir` on the working tree, and
`claims-auditor`/`deferrals-auditor` set to `fresh`. The pane's environment was checked empty
of `GUARD_PROJECT_DIR` / `GUARD_REFS_DIR` / `GUARD_TOGGLE_CLI` / `CLAUDE_CODE_SESSION_ID`
first — a pane inherits the launching shell's environment, and this repository's own sessions
export three of those.

The session was armed with `guard on`, a background subagent named `chat` was spawned, and its
transcript was opened from the interactive panel with `↓` then `Enter`. Four messages were sent
to it that way, one of which asked it for a confident factual claim — material `claims-auditor`
exists for.

Three results, and the second is the one the design rests on.

**`UserPromptSubmit` does not fire for a message sent into a subagent's transcript.** Zero
`user-prompt` trace records for all four, and the answer-file count did not move. So `cmd_turn`
never names a file, which is correct: there is no `Stop` coming to fill one.

**`Stop` DOES fire in the main session when the exchange finishes, and guard's own origin test
is what skips it.** Every one of the four produced:

```
stop  skip_nonhuman_turn  origin_kind=task-notification
```

No router, no auditors, no record. This is worth stating precisely because the obvious
explanation is wrong: it is **not** that guard registers no `SubagentStop` hook. The hook that
fires is `Stop`, in the main session, and the only thing standing between it and a full audit
is `_turn_identity`'s `origin_kind != "human"` skip — written for a different purpose (guard's
own dispatch causes background completions, and auditing those loops). Two ways that closes
with nothing failing: registering `SubagentStop`, or the host ceasing to emit `origin` for
these turns, since an ABSENT kind still audits by design. Anything that makes a conversational
subagent a supported workflow has to treat that skip as load-bearing.

**`PostToolUse` fires for the subagent's writes, and the edit is then silently dropped.** This
is a defect, not a property to rely on. Asking `chat` to create a file produced:

```
post-edit  edited_recorded  prompt_id=b273f957-…  bucket=edited_files  file=probe_edit.py
```

— recorded under the last MAIN-session `prompt_id`, which was already spent. `cmd_stop` reads
`_edited_files(state, prompt_id, …)` with the current turn's id, so any later turn gets `[]`
and `comment-corrector` is never dispatched over that file. Verified directly against the
state file the run produced: same id returns the file, a fresh id returns nothing.

The mirror case — a subagent editing while a main turn is genuinely in flight, so the live id
is recorded and a corrector is dispatched at files from a conversation the main session never
saw — follows from the same code path but was **not** measured.

`interviewer` is written around the first two results and around the third being unfixed: it is
allowed to write, so its edits are in that gap. Its body confines it to one file and forbids
touching source, which is a rule in prose, not an enforced boundary.

One more thing the trace showed, unrelated to subagents: `UserPromptSubmit` fires for
`task-notification` turns too and names an answer file, which `Stop` then skips. The run ended
with 8 files in `turns/<sid>/` for 2 audited turns. Harmless, but it is why a file count is not
a turn count.

## `deferrals-auditor` and the by-running blind spot

The agent definitions ship into other people's repositories, so nothing in them may name a
path from this one. That constraint is why the by-running rule reads the way it does — it
tells the agent how to *find* a project's testing documentation (README/CONTRIBUTING, a
`docs/` or `dev/` file, a Makefile target, a CI workflow, a test directory, a compose file)
rather than naming a file. An earlier revision named `dev/design.md` and guard's own
`/guard:*` surface directly; that is a bug in a plugin, not a shortcut, and it was removed.

The history is worth keeping here because it is the reason the rule is phrased as pressure
rather than as a category:

- The original definition actively forbade the check — a comment saying verdicts are
  "settled by READING the repository, not by running it", and `runtime data not yet
  available` sitting in the legitimate list. The auditor was not failing to reason; it was
  following the spec, and it quoted the spec back as its reason.
- Adding a third category (`Resolvable by running`) flipped one dispatch from `pass` to
  `violations`, but that single flip is weak evidence: a later re-run of the same
  variant at the same model gave a different verdict, so run-to-run variance is on the
  order of the effect being measured. Any claim of the form "variant X at model Y is
  better" needs repetitions, recorded models (`--output-format json` reports
  `modelUsage`), and a fixture without ambiguous cases.
- **Model is not the lever.** Measured against a fixture deferring "실제 Codex 세션에서 훅이
  뜨는지" in this repository — `codex` installed, the recipe two sections below this one —
  four dispatches passed it: Sonnet and Opus, before and after the rule was hoisted into
  the agent's opening framing. The `model` parameter on the Agent tool does override the
  definition's `model:` frontmatter (each run self-reported `Claude Sonnet 5` /
  `claude-opus-5[1m]`), so this was a real comparison, not a mislabelled one.
- Both models reduced the question to the easier one — "is the answer stored in this
  project?" — and answered no. Sonnet: "external to the repo". Opus: "outside the
  repository". Neither opened the testing docs; tool-call counts were 2 and 3. Moving the
  rule earlier in the body did not help and the tool-call count went *down*.

**Resolved 2026-08-22, and the earlier heading above is wrong — the lever was the spec and
the memory, not the model.** Two things had to be fixed together. The definition stopped
forbidding the check (see the bullet above), and three memory entries had to be deleted: the
agent had written down "deferrals that need a live runtime are legitimate scope for this
project" and was citing that entry back as its reason. Two of the three were written *during*
the verification runs, so the experiment was reinforcing the bug it was measuring. The
definition now forbids storing a remembered `legitimate` at all, and says why the direction
is asymmetric.

After both fixes, four dispatches — two fixtures × Sonnet/Opus — all returned `violations`,
against four `pass` before. So the "one agent cannot hold both questions" hypothesis is
rejected, and neither of the two candidate fixes (a forced output obligation, a separate
execution-availability agent) is needed. Opus went further than Sonnet on both fixtures
rather than merely matching it — it caught a second deferral Sonnet let stand — which is why
the definition now pins `model: opus`.

**Do not reuse a fixture this file describes.** The first re-run came back `violations` and
was worthless: the auditor read the bullet above, which quotes the fixture's Korean sentence
and says the recipe is "two sections below this one". The load-bearing run was a fresh
fixture (a toggle deferral) that this file does not label as a fixture anywhere — its file
list confirms it never opened `design.md` at all, and it still reached the answer by reading
`guard_hook.py`, concluding the CLI runs headless, and reproducing it. Writing an experiment
up here makes the write-up an answer key for the next round of the same experiment; a new
fixture is the only way around it.

**Three of the four runs ran guard's own hooks**, in throwaway directories, having been told
not to. They bounded themselves (scratchpad only, no repository or real-project writes) and
disclosed it unprompted. The reproduction improved the verdicts — one run matched its
observations line-by-line against the `_audit_paused` branch in `cmd_stop`. The contract in
the definition was widened to match, since a rule broken independently at two models for good
reasons is not a rule.

## Picking a model for an agent: the one comparison that was actually run

Every agent's `model:` is a claim that this job needs that tier, and most of guard's are
argued from the failure mode alone. Two are not: `docs-finder` (then named
`ext-docs-fetcher`) and `ext-docs-auditor` were run head-to-head on `sonnet` and `opus` before
the field was set. This records what the runs
showed, so the next person can disagree with evidence rather than taste. Both agents' bodies
were handed to a `general-purpose` subagent as the prompt, identical between arms, with only
the model differing.

**`ext-docs-auditor` — eight saved references, five carrying project content.** Ground truth was
established by hand first: two files had the content behind a `## Bearing on <project>`
heading, three had it with no heading at all, one had a project-named heading over content
that was actually general, and two were clean.

Both models found all five, and both independently reported the sixth as *arguable* with the
right reasoning — the heading is the violation, the prose under it is not. On the axis the
agent exists for, they tie, and the cheaper model would be defensible.

The tie broke elsewhere. One of the two "clean" files states its whole substance — a four-row
value table plus a behavior sentence — in the documentation's voice with nothing quoted.
`opus` flagged it and named the single table row a re-fetch would be needed to confirm.
`sonnet` reported the file clean. In the other direction `sonnet` had two catches `opus`
missed: a quoted passage about `StrEnum` being used to support an unquoted claim about the
`str, Enum` mixin, and a source that is a tutorial site rather than a primary one. So this is
a preference and not a rout — but the file `sonnet` passed is the failure that matters, since
an unattributed table is precisely what gets cited later as documentation. `opus` also spent
fewer tokens on that run, finished sooner, and was better calibrated about what NOT to report
(it noticed a `Fetched:`/`Retrieved:` inconsistency across four files and explicitly declined
to score it as a finding).

**`docs-finder` — one question about a long documentation page**, both arms sandboxed to
their own refs directory so neither could touch the repository. Both produced a correct saved
excerpt with the right quotes, and both answered the question in the report.

The difference was in how they got there, and it is decisive for this agent. `WebFetch`
answers a prompt *against* a page rather than returning it, and on this page it returned a
paraphrase in which the section being asked about had been replaced by an unfollowed
cross-reference. `opus` noticed, refetched the raw `.md` with `curl`, and quoted from that.
`sonnet`'s report gives no sign it noticed. `opus` additionally recorded three things the page
does **not** say as absences inside the file, and explained why it saved nothing from a second
page it had cross-checked (it would have split the subject).

A paraphrase saved as documentation is worse than no file at all, because everything
downstream treats it as evidence — so the hazard `opus` caught is this agent's whole reason to
be careful. That finding also went into the agent definition itself, as a step: when the
passage does not come back quoted, get the source with `curl` and quote from that. A cheaper
model following that instruction may well close the gap; nobody has re-run it since the
instruction was added.

That run also predates the scope change that made this `docs-finder`: it was one external page,
with no repository search and no location-only reporting rule, so it measures the fetch half
alone.

**The field is `sonnet` as of 2026-08-25**, set by the maintainer. That is the arm this
comparison ruled against, on the paraphrase finding — but on the run that produced the
finding the `curl` step did not yet exist, so what is recorded above is no longer a
measurement of what ships. Re-running it is how this gets settled; until then the risk is
the one named above, that a paraphrase saved as documentation reads downstream as evidence.

**What to re-run before changing either field.** The ext-docs-auditor arm needs a ground-truth set
with both heading-marked and unmarked project content, and at least one file whose substance is
unattributed — that last case is what separated the models. The fetcher arm needs a long page
with a section a summarizer will drop, and it must be sandboxed to a scratch refs directory:
the agent writes, and an arm pointed at the real one leaves two competing references behind.

## A stored verdict is invisible when it is wrong

The failure, first, because the design only makes sense against it. `deferrals-auditor` wrote
into its own memory that deferrals needing a live runtime are legitimate, then cited that
entry back as its reason for passing exactly the deferral it exists to catch. Deleting the
entry did not hold — the next run wrote a fresh one. With a store available, the cheapest
move on any later turn is to match a stored pattern instead of re-deriving the judgement, and
a *wrong* stored verdict cannot be found by looking, because it suppresses the finding that
would have exposed it. Prose forbidding it was tried at two models and broken by both.

Three facts constrain the fix, all measured (2026-08-23, claude 2.1.239):

- **`memory:` grants Write and Edit, unscoped.** An ad-hoc agent declaring `tools: ["Read"]`
  with `memory: local` reported Write and Edit present and wrote successfully to an absolute
  path outside both the project and its memory directory. The docs' "so the subagent can
  manage its memory files" is the grant's purpose, not a restriction. The symmetric run
  without the field had `Read` alone and no Write tool to call.
- **A subagent's own `hooks:` frontmatter cannot enforce it.** The field exists, and the host
  ignores it for plugin subagents (as it does `permissionMode` and `mcpServers`).
- **A plugin's own hooks do reach subagents.** Tool events fire inside them and the payload
  carries `agent_type`; a plugin subagent reports the plugin-scoped name, observed as
  `guard:korean-corrector` when guard still ran a `PreToolUse` hook. Excerpt:
  `wiki/ref/claude-code-hooks-in-subagents.md`.

**A `pre-write` hook, denying a report-only agent's write outside a memory directory, was
built on these facts and then removed at the maintainer's direction (2026-08-25).** It is
recorded here because the facts above still hold and would otherwise invite rebuilding it.
`PreToolUse` on the write tools checked the payload's `agent_type` against a report-only set
and denied any target outside `agent-memory`/`agent-memory-local`; the rule was a location
rather than a per-agent path, since deriving each agent's own directory depends on how the
host names it. What remains is that `memory:` grants unscoped Write and Edit, and nothing in
guard refuses such a write: "reports; edits nothing" is a promise in each agent's body.

Note what the hook never covered, because it bears on the failure that opened this section.
It stopped a stray write; it could not stop a wrong verdict written *inside* the memory
directory, which is what actually happened. That part of the remedy is unaffected by the
removal: `project` puts the store in `.claude/agent-memory/`, which is tracked, so an entry
arrives in a pull request and is read by someone. Review was always the check on content.
`deferrals-auditor` additionally carries the asymmetric rule in prose — never store a
remembered `legitimate` — because that specific direction is the one that reproduces itself.

**Codex could not have expressed the rule either, which was checked rather than suspected.** Codex
lists `PreToolUse` and its decision can deny before a tool runs, but the event's payload is
`turn_id`, `tool_name`, `tool_use_id`, `tool_input` over the common fields — and carries
**no `agent_id` and no `agent_type`**; those two are documented for `SubagentStart` and
`SubagentStop` only. Excerpt: `wiki/ref/openai-codex-pretooluse-payload.md`, fetched
2026-08-23. So a hook registered there could not tell a report-only agent's write from any
other and would deny everything or nothing. `hooks.codex.json` is unchanged.

The remaining route is correlation: record identity at `SubagentStart`, which does carry
`agent_id`/`agent_type` plus the parent `session_id`, and look it up from `PreToolUse` by a
field both events share. One measurement decides whether that is possible at all — whether a
Codex subagent's `PreToolUse` reports the subagent's `session_id` or the parent's. If it
reports the parent's, nothing separates the subagent's writes from the main thread's and the
approach is dead. `codex-cli` is installed on this machine, so this is a measurement rather
than a question.

## The `/`-rooted search refusal, and why it is not the hook that was removed

`pre-search` (`PreToolUse` on `Bash|Grep|Glob`) denies a search whose root is `/`. It exists
because the rule was already written down and unenforced: the user's global instructions say
never to run `find`, `grep`, `rg` or similar with `/` as the target. An instruction in a
CLAUDE.md is obeyed by a model that reads it and remembers it at the moment it composes the
command, which is not the same as always.

**It is not the removed `pre-write` hook wearing a new name, and the difference is the input
it reads.** `pre-write` classified the CALLER: it asked whether `agent_type` named a
report-only agent, and denied on identity. That is what made it unportable — Codex's
`PreToolUse` payload carries no `agent_type` (`wiki/ref/openai-codex-pretooluse-payload.md`)
— and identity is also what made it contentious enough to remove. `pre-search` classifies the
ARGUMENT: is this search rooted at `/`. Every host that reports `tool_name` and `tool_input`
can answer that, and the answer does not depend on who is asking. A rebuild check that stops
at "guard had a PreToolUse hook and it was removed" reaches the wrong conclusion here.

**Deny, not ask.** A deny reason reaches the model verbatim as the tool's `<error>` result —
measured, not assumed (`wiki/ref/claude-code-pretooluse-deny-reason-visibility.md`) — so the
refusal can name the narrower search and be acted on in the same turn. `ask` would put a
dialog in front of a call that is almost always a slip, handing the decision to the user who
did not write the command. Confirmed live: the refused `find / -name sample.txt` returned the
reason word for word, and the session re-ran it bounded without further prompting.

**The reason names the fix, not just the prohibition.** The same measurement says a deny
reason is weighed as tool output rather than as instruction, which is why the entry under
"must not come back" forbids a deny reason that redirects to another AGENT — that redirect is
declinable. Naming a narrower path is different in kind: it is not asking the session to
dispatch anything, and the session was already trying to search. Without it the predictable
sequel is the same walk retried one top-level directory at a time.

**What it does not do.** It denies the root of a search, not searches it dislikes. `/etc`,
`/usr`, `/Users/...` all pass — they are bounded, and deciding which bounded directories a
project may read is not guard's business. Denied: a bare `/`, the slash runs (`//`), `/.` and
`/..`, and any glob whose FIRST path segment carries a wildcard (`/*`, `/**`, `/*.py`,
`/**/*.py`) — all of which descend from the root.

**It was never registered on Claude until v0.112.0, and that is the failure worth recording.**
`cmd_search.py` shipped in v0.78.1, `guard_hook.py` had the `pre-search` verb, the hook table in
this document listed `PreToolUse (Bash|Grep|Glob)` — and `hooks/hooks.json` had no `PreToolUse`
entry at all, so on Claude Code the rule was dead code for fourteen versions. Codex enforced it
the whole time, because `hooks.codex.json` routes every event through one adapter with matcher
`*` and the adapter dispatches on `hook_event_name`: registration there is not per-rule, so a
rule reaches Codex the moment the adapter calls it. Claude's manifest is per-event, and that is
the entry someone has to remember.

Nothing failed loudly. Every unit of it was correct in isolation and the design doc described a
hook that existed, which is exactly why reading either the code or the doc confirmed it worked.
What would have caught it is asking the host: the only honest test of a hook is a session that
triggers it. So when adding a rule to a `cmd_*.py`, check `hooks/hooks.json` for the event and
matcher in the same change — and for the Codex side, check that the adapter's dispatch actually
reaches the new call.

That last clause is wider than it first shipped, and the widening is the useful record here.
The original test was "strip a trailing glob segment", which caught `/*` and `/**` and missed
`/**/*.py` — the ordinary way anyone actually writes a root-anchored glob. The audit that
found it also found the mirror-image bug in `_VALUE_FLAGS`: `-prune` and `-print0` were listed
among the value-taking flags, and since a match there skips the NEXT token too, `find -print0
/` and `find . -prune / -name y` both walked the root unrefused. Both holes shared one shape —
a rule that covered the spelling in the example and not the spelling in use — and neither was
visible from the passing test matrix, because the matrix had been written from the same
examples as the code. The cases are in it now.

**Coverage beyond the three names in the rule.** `fd`, `ag`, `ack` and `locate` are matched
too. A rule that knew only `find`/`grep`/`rg` would be stepped around without anyone
intending to — whoever types `fd` types it because it is the tool they use. Matching is on
the basename of the command word, so `/usr/bin/find` and an alias-bypassing `\find` both
count, and each segment of a compound command (`a && b`, `a | b`) is read separately so a
root search that is not the first command is still caught. Option-taking flags are skipped
with their values, which is what keeps `grep -f / pattern src` and `find . -newer / -name x`
from being misread as root searches.

**It fails open, twice over.** A command `shlex` cannot split (an unbalanced quote) produces
no verdict rather than a guess, and every other internal failure is silent. guard does not
block because its own parser broke — a search it cannot read is one it cannot make a claim
about either.

Verified live against `claude 2.1.246` with `--plugin-dir`, in a throwaway project, from a
second pane: `find / -name "sample.txt"` was blocked with the reason quoted back verbatim,
and `find /private/tmp/... -name "sample.txt"` plus `grep -rn hello .` both ran untouched. A
46-case matrix over the parser (26 deny, 20 allow, including the fail-open case) passes; the
last eleven cases were added by the audit described above and each one failed before the fix.

## Codex: hooks must be trusted, or guard is silent

Installing and enabling guard under Codex is not enough to make it run. Codex skips
plugin-bundled hooks until the user reviews and trusts the current hook definition
(`wiki/ref/openai-codex-hooks-2026-08-14.md`), and it says nothing when it skips them — so
the symptom is a plugin that reports `installed, enabled` and does absolutely nothing.

Measured on 2026-08-22 with `codex-cli 0.147.0`, in an isolated `CODEX_HOME`: after
`codex plugin marketplace add <repo>` and `codex plugin add guard@studykit-plugins`,
`codex plugin list` showed `installed, enabled 0.53.0` and neither `codex exec` nor an
interactive session created `.codex/guard/` at all. The same run with
`--dangerously-bypass-hook-trust` wrote the session state, the trace and three turn records.
Nothing was wrong with guard.

Two things follow. When testing the Codex side, pass that flag or trust the hooks first, or
you are measuring hook trust rather than guard. And when a user reports that guard does
nothing under Codex, this is the first thing to ask about — ahead of `$guard:setup`, which
installs only the named agent and cannot affect hooks.

## Testing against the real CLI

`--plugin-dir <path>` loads the plugin for one session, so guard can be exercised by a real
`claude` without installing it. Two things make the results readable: `--debug-file <path>`
records every hook firing and the exact `additionalContext` the host received, and
`GUARD_TRACE=1` gives guard's own view in `trace.log`. Assert on the trace and the state
tree, not on what the model said about them — a hook that silently did nothing leaves the
model free to claim it worked, which is exactly what happened once here.

```bash
cd /tmp/guard-cli-test/proj    # a git repo with .claude/guard.local.json
env -u GUARD_PROJECT_DIR -u GUARD_REFS_DIR GUARD_TRACE=1 claude -p "Reply with OK." \
  --plugin-dir /path/to/plugins/guard --model haiku --effort low \
  --no-session-persistence --max-turns 4 --debug-file /tmp/d.log
```

`env -u GUARD_PROJECT_DIR` is not optional when the test is launched from inside another
guard session's Bash — without it the child's hooks write into the PARENT's project. That is
the bug the case above pins; the flag keeps the test honest even after the fix.

An interactive path — one that needs a real session, such as the `guard` command reaching the
same `state/<sid>.json` the hooks write — needs a terminal, which `tmux` supplies:

```bash
tmux -f /dev/null new-session -d -s gt -x 200 -y 50 -c /tmp/guard-cli-test/proj
tmux send-keys -t gt 'claude --plugin-dir /path/to/plugins/guard --model haiku' Enter
tmux pipe-pane -o -t gt 'cat >> /tmp/pane.log'   # capture-pane can come back empty here
tmux send-keys -t gt '!guard off'; sleep 2; tmux send-keys -t gt Enter
```

Three traps worth knowing. Piping claude's stdout (`| tee`) takes away its TTY and it drops
straight to non-interactive mode, so the session exits immediately — use `pipe-pane` instead,
and note that `capture-pane` can come back empty against claude's TUI. A first-run directory
shows a trust dialog that eats the first Enter, so the prompt sent before it is lost. And a
tmux pane starts from the login PATH, which on macOS puts `/usr/bin/python3` (3.9) first —
harmless now that uv chooses the interpreter, but it is the environment that surfaced the bug
in the next section, so it is the one to test in.

**Pass `--permission-mode bypassPermissions`, not `auto`.** Measured 2026-08-22 against
claude 2.1.239, in a fresh directory driven from tmux. Under `auto` the very first
state-changing Bash call stops on `Do you want to proceed?` and the run stalls until
something answers it — the mode narrows prompts, it does not remove them. Under
`bypassPermissions` the same prompt count was zero and the pane header reads
`bypass permissions on`. The trust dialog is a separate gate and neither mode skips it: it is
suppressed only in non-interactive mode (`-p`, or a non-TTY stdout), which is exactly the
mode an interactive-only path cannot be tested in. So an interactive recipe still sends one
extra Enter, or runs in a directory already trusted.

### Why uv, and what it fixed

Both hook manifests and both scripts' shebangs run through `uv run --script`, and each script
carries a PEP 723 block pinning `requires-python = ">=3.11"`. `guide/adapter-guide.md` asks
for the uv invocation; the pin is what makes it load-bearing.

The bug it closes was measured on 2026-08-22, in a real session. With the old
`#!/usr/bin/env python3`, the interpreter is whatever comes first on the PATH of the process
the host launched the hook from. A tmux pane starts from the login PATH, which on macOS puts
`/usr/bin/python3` (3.9.6) first, and every hook died with `ImportError: cannot import name
'StrEnum'` — the session showing `Stop hook error: Failed with non-blocking status code` and
a traceback. The single-file `guard_hook.py` failed identically before the package split
(same import, same line), so this was shipped behaviour rather than a consequence of the
layering.

Two things about that failure were worse than they look. It is **not** fail-open in the sense
the rest of guard means: a traceback in the transcript on every hook of every turn is the
loudest possible failure, repeated. And because the hook printed nothing, the model was free
to narrate success — in the observed run it answered "이 세션에서 비활성화했습니다" to a
`/guard:toggle off` — the slash command, since removed — whose hook had in fact crashed and
changed nothing. That is the general
hazard behind the rule in the CLI-testing section: assert on the trace, not on the answer.

uv resolves an interpreter satisfying the pin, so the same tmux pane — `python3` still 3.9.6,
`uv` on the PATH at /opt/homebrew/bin — now runs the hooks correctly: `/guard:toggle off`
recorded `toggle/set paused: true` plus both control-command skips, `audit_paused` is `True`,
and the pane shows no hook error. Cost: about 9ms per invocation (10 runs, 0.267s under uv
vs 0.176s direct), and the 100-case regression suite runs in 1.7s total.

What uv does not fix is an environment with neither a modern `python3` nor `uv`. There the
failure is `env: uv: No such file or directory`, exit 127 — one line instead of a traceback,
still broken. uv is a stated install requirement rather than something guard degrades around.

Directly unit-testable without any subprocess, and the split widened this considerably —
each module below imports without pulling in the hook entry point: `turnrec._write_turn_response`
(the fallback header present, response exact, parent dir created, an existing non-empty
file left alone, and a read-only dir returning None rather than raising),
`transcript._turn_identity(path, prompt_id)` on a
fixture JSONL (a typed prompt, a `task-notification`, a slash command, a prompt_id absent
from the file), `_safe_project_subdir(project_dir, value)` on its rejection cases (`"."`,
`".."`, `".claude/guard"`, `"../elsewhere"`, `"/etc"` — all None; a plain subdirectory
resolves), `agents._eligible_agents(state, edited, agent_docs, refs)` on the file-reading
prerequisite (each bucket gates only its own agent), `agents._edited_bucket(path, refs_dir)`
on a source file, an `AGENTS.md`, a `CLAUDE.md`, a plain `.md` that must land in no bucket,
a file inside the refs dir, and the refs dir's OWN `AGENTS.md`, which must land in
`edited_refs` and never in `edited_agent_docs`, `state._read_state` on a file holding every
bucket key (each must survive the round trip),
`config._parse_mode` / `config._agent_mode` on the aliases and on a junk value (which must
read as `off`), `config._load_config` on a mode written into the file (it must survive the
type gate — see the Config section), `dispatch._plugin_root` from an install where the
closeout file is present and from one where it is not, and `dispatch._router_context` /
`dispatch._agent_pointer`, which must never name an agent outside the eligible list and must
name the closeout path exactly once each.
