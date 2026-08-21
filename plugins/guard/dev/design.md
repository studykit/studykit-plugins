# guard — design detail

Deep reference for `guard` contributors. Not auto-loaded; open it when working on the
area it covers. `../AGENTS.md` is the always-loaded map and points here. The source
(`scripts/guard_hook.py`) is the truth for control flow — this file records *why* the
design is shaped this way and the runtime facts verified against the real CLI, not a
line-by-line walkthrough.

## Hook wiring (`hooks/hooks.json`)

| Event | Subcommand | Role |
| --- | --- | --- |
| `UserPromptSubmit` | `user-prompt` | Trace only. guard keeps no record of the prompt; the hook stays registered so a "guard said nothing" report can be told apart from a hook that never ran. |
| `UserPromptExpansion` (one matcher per agent: `claims-auditor`, `deferrals-auditor`, `korean-corrector`) | `verify <agent>` | On demand, dispatch **that agent** for the last completed turn. The agent name rides in argv, not in a dispatch input the model has to be trusted to honor. |
| `PostToolUse` (`Write\|Edit\|MultiEdit\|NotebookEdit`) | `post-edit` | Record a source file this turn wrote (the candidate list for a `comment-corrector` recommendation), then block when a file saved in the refs dir is not listed in that dir's `AGENTS.md`. |
| (called via Bash, not a hook) | `settings` | `guard:settings` skill (in-session) shows/sets guard.local.json settings; the four agent modes also apply to the live session's `state/<sid>.json` (session id from `--session`/`CLAUDE_CODE_SESSION_ID`). A mode change away from `reuse` also prints a stand-down note, the only channel guard has to a running instance. Every other key preserved; never the list key (`exempt_skills`). |
| (called via Bash, not a hook) | `exempt` | `guard:settings` skill records the user's confirmed `exempt_skills` selection (that key only). |
| `Stop` | `stop` | Write the response section of the turn record and mark the turn as the on-demand target — always. Then, when any agent is not `off`, emit `additionalContext` asking the main agent to dispatch `guard:router` over the record, carrying the eligible agents with their modes and this turn's paths. The router names sections of `hooks/context/dispatch-playbook.md`; the main agent follows those, completing the record's second section only if a named section asks for it. |
| `SessionStart` | `session-start` | Sweep state and turn records past retention, export `GUARD_REFS_DIR`, state the refs rule as session context, name the dispatch playbook once when any agent is on, and — when any agent is in `reuse` — state the standing reuse policy once. |
| (called via Bash, not a hook) | `transcript` | `index` / `turn` / `find` over the session transcript, for the audit agents. Writes an extract file and prints only its path plus a one-line summary; `--since` / `--until` / `--last` bound which turns are scanned. |
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
  defaults instead of injecting state.
- `turns/<sid>/<prompt_id>.md` — the response being audited, verbatim, written by guard at
  every Stop from the payload's `last_assistant_message`. That is the file's whole content;
  nobody appends to it. `<prompt_id>.ko-fix.md` beside it is where `korean-corrector` writes
  its rewrite.
- `extracts/<sid>/…` — whatever an agent pulled out of the transcript: `index.md`,
  `turn-<id>.md`, `find.md`, or a `--out` path it chose. Written by the `transcript`
  subcommand on request, never on a schedule, and swept with the rest of the session's
  state.
- `trace.log` — file-only debug trace (`GUARD_TRACE` truthy).

Not state, but part of the same picture: `hooks/context/dispatch-playbook.md` in the plugin
holds one section per agent — how to dispatch it, what its report means, what to do about
it — plus a `router` section. guard's hook output and the router both refer to it by section
name; nothing copies its text. `_playbook_path()` resolves it from the script's own location
rather than `CLAUDE_PLUGIN_ROOT`, because the same script is also the Codex adapter's
library and a plain CLI the settings skill runs over Bash, and only the hook case has that
variable set.

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
- **Turn anchor.** The anchor record is the one whose top-level `promptId == prompt_id`
  (a typed prompt: `origin={"kind":"human"}` + str content). Records derived from the turn
  carry `promptId=None`. guard reads the anchor and stops — `_turn_identity` needs the
  turn's kind, not its content — so the slice-boundary rules that used to matter here (the
  next different non-empty promptId ends the slice; `isMeta:true` records are guard's own
  feedback and are skipped) no longer bear on anything. They are recorded in case a future
  change needs to walk the turn again; do not re-add the walk without a reason.
- **A background-agent completion opens its own transcript turn** (`origin.kind ==
  "task-notification"`, `promptSource: "system"`, NOT `isMeta`; verified 2.1.197). This is
  load-bearing: the recommendation asks the main agent to dispatch agents, each dispatch is
  a background task whose completion opens a turn, and recommending an audit *of that turn*
  would dispatch again without end. `cmd_stop` skips these (`skip_task_notification`).
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
- **Nobody gathers the session's history; agents extract it.** guard's record holds the
  response and nothing else. Everything around it — the request, this turn's tool activity,
  what an earlier turn established — is already in the transcript, and the agents that may
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
- **Text is stored where it is read, not where it is emitted.** Three homes, and the split
  is by how often each is paid for. `additionalContext` is paid in the main agent's context
  on *every* routed turn, so it carries only what changes per turn: the record path, which
  agents are on, each one's mode, the files this turn wrote, the rewrite path.
  `agents/router.md` is paid once per routed turn, in the router's own context, so it
  carries the triage method and the cue per candidate. `hooks/context/dispatch-playbook.md`
  is paid only by whoever is sent to a section, so it carries how to dispatch an agent,
  what its report means, and what to do about it — the text that reads identically every
  turn and is needed only for the agents actually picked.

  Two temptations to refuse. Printing each candidate's dispatch block in the hook output
  pays for four blocks on every turn to use at most four and usually none, since the common
  case is the router clearing the turn. Having the *router* write those blocks instead is no
  better: it makes an LLM re-type instructions it was handed, which is exactly where wording
  drifts from the file that owns it. The router names sections; the main agent reads them.
- **What bounds the dispatch is the playbook, not the roster.** A key the router invents
  has no section, so a switched-off agent stays unreachable even when it is named anyway.
  The roster is what stops it being reached for in the first place; the missing section is
  what stops it working.
- **The router's reason is part of the output, not decoration.** Each pick carries one
  sentence naming what in the response triggered it, quoted where possible, and the main
  agent is told to relay it. A recommendation nobody can second-guess is one that gets
  waved through, which is the failure this whole shape is built to avoid.
- **Control turns and exempt commands never get a recommendation.** `/guard:settings` and
  all of `/guard:{claims,deferrals}-auditor` / `/guard:korean-corrector` are skipped on
  BOTH sides: `_CONTROL_CMD_RE` matches the raw prompt at UserPromptSubmit, and `cmd_stop`
  skips them via `command_name` (extracted from the transcript's expanded
  `<command-name>/guard:settings</command-name>`). This second skip is load-bearing — a
  control turn's response is a one-line relay ("guard on") with no evidence, and without
  it Stop falsely blocked such a turn (session b30dbaec). The same `command_name` path
  skips any skill / slash command the user lists in `exempt_skills` — named with its
  plugin namespace (`plugin:skill`), since a user-invoked skill reaches the transcript as
  a namespaced `<command-name>` just like a command (skill output is not a body of
  technical claims to ground). `comment-corrector` is deliberately NOT in
  `_CONTROL_CMD_RE` — that skill relays findings about real files and reports edits made to
  them, so its turn stays auditable — and the regex's `(?=\s|$)` is what keeps
  `claims-auditor` from matching a bare `/claims`.
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
- **The per-agent settings are the only control, and each is named after its agent.**
  There is no gate in front of them. `audit_gate` (`off`/`ask`/`auto`) used to be one, and
  removing it removed a whole class of question — "the switch is on but is the gate open,
  and does `ask` mean the user is asked before or after routing" — that the user had to
  hold in their head to predict what guard would do. Now: an agent not `off` means it can
  be recommended; all four `off` means guard emits nothing and makes no model call, which
  is what `audit_gate off` used to mean. All four ship `off`, so installing guard does not
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
  The four audit agents carry `memory: local` — conventions, where the answers live, a
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
  last five can answer it from the wrong one, silently, at the step nothing else checks. It
  is also the cheapest agent in the set, so continuity buys the least there.
- **Reuse needs `SendMessage` in the agent's `tools:`, and the router must not have it.**
  `tools` is an allowlist when present (`wiki/ref/claude-code-subagent-frontmatter.md`), so
  the four audit agents list `SendMessage` and the router does not. This also fixes an older
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
- **The dispatch passes only what the agent cannot obtain itself.** That is the turn
  record's path, and for Korean a rewrite path — nothing more. Not the refs directory: the
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
- **The Korean corrector writes a file; the comment corrector edits in place.** Not an
  inconsistency — the inputs differ. `comment-corrector` is pointed at source files, so
  fixing means `Edit` on those files. `korean-corrector` is pointed at a turn record in
  guard's own state, which is a record of prose the assistant already emitted: editing it
  changes nothing anyone reads. So the correction has to be a new artifact, and
  `_korean_rewrite_file` puts it beside the record (`<prompt_id>.ko-fix.md`) rather than in
  the user's tree. guard never reads it back; only the main agent does, told the path in
  its dispatch text. Do not "unify" these two by giving the Korean agent `Edit`.
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
- **Assistant tool output is first-class evidence.** The turn record is required to carry
  what the assistant ran and what came back, because a claim that restates or follows from
  a command's output there is supported without a re-cite. Note what is no longer a rule: a
  user-run `!` command used to disqualify its whole turn, because its output records landed
  in guard's slice *after* the response an audit would judge, so the evidence arrived later
  than the claims. guard no longer cuts the slice — the main agent writes the record, and
  by then the `!` output either is or is not part of what it is describing. The skip is
  gone; do not re-add it without re-establishing the ordering problem it solved.
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
- **The config-mutating CLIs can weaken guard, and Bash is ungated.** `settings set
  claims-auditor off` and `exempt add <skill>` both reach guard's own configuration, and
  the model can invoke this script through Bash — nothing stops it. `_cli_write_allowed`
  requires a marker (`GUARD_SETTINGS_SKILL`) that only the user-invoked `guard:settings`
  skill sets, on the mutating verbs of both — covering only `exempt` would be theater,
  since switching an agent off is the easier move.
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

Keys: one boolean per agent, named after that agent — `claims-auditor`,
`deferrals-auditor`, `korean-corrector`, `comment-corrector`, **all default `false`** —
which together are the only control over whether guard says anything unasked. See the
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
cheaper or sharper than the plugin ships it. It is never validated against a list of names
(an alias, a full id, and a provider's own name are all legitimate, and the set moves).
Every agent the router names brings its own model and effort from its own frontmatter in
`agents/`, which is also where its criteria live — a second copy in guard's config would
let the two disagree about the same agent.

Getting the router's model wrong costs in both directions, which is why the default is left
to the agent rather than pinned to the cheapest thing that runs. A router that misses means
the audit silently never happens — the exact failure guard exists to prevent. A router that
cannot tell a backed claim from one that merely sounds backed names every agent every turn,
which is the same as naming none, because the user stops reading the recommendation.

`exempt_skills` (list of strings, default `[]`) — skills / slash commands whose turn Stop
skips, named with their plugin namespace (`plugin:skill`, e.g. `guard:settings`) or bare
for un-namespaced skills, matched leading-`/`-stripped and case-insensitively (guard's own
control commands are always exempt regardless). Manage it interactively with the
`guard:settings` skill (which records the user's chosen names via the `exempt` CLI); no
need to hand-edit.

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

# All four off (the shipped default): NOTHING is emitted, but the pending target must
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
#   -> STEP 1 routes and says to gather NOTHING yet: it names the playbook's `router`
#      section, dispatches guard:router with the record path and exactly two candidates
#      with their modes, and adds p1.ko-fix.md because korean-corrector is among them.
#      STEP 2 defers completing the record to the sections that ask for it.
#      There must be no unconditional "complete the record" step, and nothing here
#      describes what an agent does or how to dispatch it — that is the playbook's.
cat "$CLAUDE_PROJECT_DIR/.claude/guard/turns/s1/p1.md"
#   -> the second section reads "Not collected" and carries the ask for earlier evidence
#      plus the ban on the main agent's own case for the claim. Nothing collected it.

# The roster must never offer a switched-off agent. The playbook is the second bound: a key
# the router invents has no section to follow.
"$H" settings set korean-corrector off --session s1
run p2 "Redis는 Postgres보다 항상 빠릅니다."   # -> claims-auditor is the only candidate

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

# A background agent's completion must NOT draw a recommendation, or each audit dispatch
# recommends an audit of its own completion, without end.
anchor p5 task-notification '<task-notification>done</task-notification>'
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p5\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"the agent reported\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: skip_task_notification

# guard's own control turns and exempt skills are skipped by command name.
anchor p6 human '/guard:settings show'
echo "{\"session_id\":\"s1\",\"prompt_id\":\"p6\",\"transcript_path\":\"$T\",\"last_assistant_message\":\"guard on\",\"stop_hook_active\":false}" | "$H" stop
#   -> empty; trace: skip_exempt_skill

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

# On-demand dispatch must work with every agent OFF — the invariant most easily broken by
# a change to the recommendation path. No router is involved: the user already chose.
for k in claims-auditor deferrals-auditor korean-corrector; do
  "$H" settings set $k off --session s1
  echo '{"session_id":"s1"}' | "$H" verify $k; echo
done
echo '{"session_id":"s1"}' | "$H" verify comment-corrector  # no output: no turn-record command
"$H" verify bogus < /dev/null                               # unknown name -> no output at all

# Unknown keys and unknown values are both rejected outright rather than silently accepted.
"$H" settings set audit_gate off --session s1        # -> error naming the four agent keys
"$H" settings set claims-auditor maybe --session s1  # -> error naming off/fresh/reuse

# The mutating CLI verbs refuse without the marker; reads still work.
(unset GUARD_SETTINGS_SKILL; "$H" exempt add some-skill; "$H" settings set claims-auditor off; "$H" exempt list)
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
