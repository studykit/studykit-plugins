# guard — contributor notes

`guard` supports Claude Code and Codex. Shared state/configuration helpers live in
`scripts/guard_hook.py`; runtime payload parsing and hook output stay in host adapters.
Requires Python 3.11+ (`enum.StrEnum`).

**guard makes no model call.** When a turn finishes it asks the main agent, through
`additionalContext`, to dispatch one subagent — `guard:router` — that reads the turn and
names which of guard's audit agents would actually find something in it, with a reason
for each; the main agent then dispatches those, concurrently. guard audits nothing itself,
and every audit criterion lives in an agent definition under `agents/`.

Where each piece of text lives is decided by how often it is paid for, and that split must
hold: `additionalContext` reaches the main agent on **every** routed turn, so it is one
imperative plus a list of fields (paths, which agents are on, each one's mode).
`agents/router.md` is read once per routed turn by the router alone, so it carries the
triage method, the cue per candidate, and the shape of the report.
`hooks/context/dispatch-playbook.md` is read only by whoever is sent to a section, so it
carries how to dispatch an agent and what to do with its report. The router's report names
the playbook and the sections to follow — which is why the playbook has no `router` section
and the main agent never reads one. Nobody re-types another home's text.

The router used to be a `claude -p` child guard spawned from the hook. It is worth
knowing why it is not, because the reasons are all still true: a spawned child blocked
the Stop hook for its whole runtime at the end of every turn, needed `--safe-mode` or
guard's own Stop hook fired inside it and recursed, needed an explicit tool denylist
because omitting `--allowedTools` leaves a child fully tooled, could not use `--bare`
without breaking OAuth users, and turned spawn/timeout/exit-code/parse into four failure
paths guard had to tell apart from a clean verdict. As a subagent, none of that exists.

1. **Audit recommendation** (Stop) — every turn is marked as the on-demand target, so the
   user-invoked `/guard:claims-auditor`, `/guard:deferrals-auditor`,
   `/guard:clarity-auditor`, `/guard:korean-corrector` and `/guard:comment-corrector` work
   whatever the settings
   say. The per-agent settings then decide what reaches the main agent unasked. Each
   is named after the agent it controls, so one string is the setting, the state key, the
   command, and the `subagent_type`. Every switch ships `off`: guard installed is guard
   available, not guard running, and with none on the hook emits nothing at all.

   The value is a mode, not a boolean — `off` / `fresh` / `reuse` — so how an agent runs
   is the same setting as whether it runs, and no separate reuse list can name an agent
   that is off. `reuse` holds one named instance (`guard-<agent>`) open for the session and
   resumes it with `SendMessage` instead of respawning, trading a new instance's per-turn
   independence for continuity; that is the user's call, not a default (`AgentMode` says
   why, `wiki/ref/claude-code-subagent-resume.md` says what the runtime guarantees). Three
   things follow and must not regress: the standing policy is stated once at SessionStart
   rather than in every recommendation; a mode change away from `reuse` is reported by the
   settings CLI, because guard has no other way to tell the session to stop addressing an
   instance guard itself cannot see; and the router is always fresh, since its question is
   about one turn and an instance carrying five can answer from the wrong one.

   The router chooses from the ELIGIBLE set, and eligibility is mechanical only: the
   mode being anything but `off`, plus — for a `reads="files"` agent — at least one source file the turn
   actually wrote. Everything requiring judgment is the router's.

   Four things must not regress:

   - The recommendation is `additionalContext`, never `decision: "block"`. The docs give
     both the same continuation and loop protections, but block reads as a hook error and
     a recommendation is guard working (`wiki/ref/claude-code-stop-hook-decision-control.md`).
   - It names **agents**, never guard's own skills. Those are
     `disable-model-invocation: true` because they are the user's entry point, so a hook
     must not reach through them.
   - The roster offers only the eligible set, and the playbook is the second bound: a key
     the router invents has no section to follow, so a switched-off agent stays unreachable
     even if the router names it anyway.
   - guard writes the turn record's **response** section itself, from the Stop payload's
     `last_assistant_message`. That is the text being audited, so it must not pass through
     the author's hands; the main session appends only what guard cannot see — the
     request, the tool activity, and earlier evidence the claims rest on. That second half
     is asked for as inclusion, never selection, because the author curating its own
     evidence is the failure that shape invites.
   - Nobody gathers the session's history. The record holds the response and nothing else;
     the agents that may need more (`needs_history`: the three auditors) get a transcript
     path, the turn id, and the `transcript` subcommand, and extract what they want into
     their own file. The main agent gathering it would put the largest cost of an audit in
     the context the user is talking to and would route the record of a turn through that
     turn's author. When extraction fails the agent may ask the main session, but that
     answer is testimony and its report has to say so.

   `clarity-auditor` is the one agent whose verdict depends on **who is reading**, and two
   things follow that must not be flattened into the others' shape. Its memory is `user`, not
   `local`: what it stores is a person — their field, their experience, their vocabulary —
   and none of that changes when they switch repositories, so relearning it per checkout
   would start every new project uncalibrated. And it degrades **loudly**: with no reader
   profile it says so and checks less (missing examples still, calibration not at all)
   rather than assuming a level. Assuming a beginner flags every technical term; assuming an
   expert passes everything; both are worse than a named gap, and the profile is established
   by `/guard:reader-profile` asking the user rather than by inferring anything from the
   repository — a repository says what the code is, never what its author knows.

   guard's other audit agents carry `memory: local`, so what they learn about a project stays in
   that checkout and out of version control. The docs recommend `project` and that is right
   for an agent a team wrote for itself; guard runs in other people's repositories, where
   creating files that turn up in their commits is a side effect nobody asked for. A team
   that wants it shared changes one word. Memory and `reuse` are
   different axes and neither replaces the other: memory is cross-session, curated and
   small — the conventions, where the answers live, a verdict the user overturned — while
   `reuse` is within-session and uncurated. Two consequences that must not be lost. The
   field silently enables Write and Edit, so each agent's body bounds them to its own
   memory directory and every "read-only" claim about the auditors is phrased that way.
   And memory tells an agent where to look, never what is true: a claim remembered as
   settled is still re-checked against the repository, or the auditors would start passing
   claims on their own past say-so. The router has no memory, on purpose — its answer must
   come from this turn, not from a habit.

2. **Session mute** (`/guard:toggle`, UserPromptExpansion) — `audit_paused` in the session
   state, and the shape matters. It is session-only: it cannot write guard.local.json, so
   reaching for it mid-conversation can never change what the project does tomorrow. It is
   also *visible* — the `status` subcommand renders it as a status-line segment — and that
   is what separates it from the `audit_gate` this plugin deliberately removed. The old gate
   was a persistent three-valued layer in front of the switches whose state you could not
   see; this is one session boolean you can read off the screen. Do not grow it back into
   the old thing: no third value, no persistence, and if the indicator ever stops being
   available, the mute is the feature that should go rather than become invisible.

   Two consequences to keep. While muted, `stop` says nothing and `user-prompt` names no
   answer file — a file nothing will correct is a file the user should not be sent to. But
   the pending on-demand target and the answer file are still recorded, because muting the
   recommendation is not the same as refusing an audit the user asks for.

   guard cannot install the status line it wants: a plugin's `settings.json` honors only
   `agent` and `subagentStatusLine` (`wiki/ref/claude-code-statusline.md`). So `status`
   prints a segment for the user to compose into their own, `/guard:statusline` offers to
   wire it, and the segment prints **nothing** on any failure — a status line is the one
   place guard must never report an error.

3. **Post-edit** (PostToolUse on the write tools) — records the turn's edited source
   files for a later `comment-corrector` recommendation, and blocks until a file saved
   in the refs directory is listed in that directory's `AGENTS.md`. Both independent of
   the agent settings.

guard reads the transcript for two unrelated purposes, and keeping them apart matters. At
Stop it reads a single record to learn how the turn was *opened* (`_turn_identity`), and every
user of that is a skip: only a turn a person typed is audited, because guard audits an
answer to the *user*, and every other origin is machinery guard's own dispatch set in motion
— a background agent's completion, a subagent's `SendMessage` back — so auditing it loops
guard against itself; separately, a turn opened by one of guard's own control commands has
nothing to audit, and a turn opened by a user `!` command has nothing *correctable* — no
prompt means no `UserPromptSubmit`, so no answer file was ever named. The loop is not hypothetical: shipping the `task-notification` skip alone
left `peer` open, and one audit whose auditor messaged the session back cost the user two
extra rounds and, because the relay turn was handed an answer file of its own, ended with
the audit memo opened in place of the answer. Hence two rules. The skip covers every named
non-human kind rather than the kinds seen so far, and an absent kind still audits — guard
noisy is recoverable, guard silently dormant is not. And one user question gets exactly one
answer file, which is the file the correctors edit and the one the main agent opens; the
`UserPromptSubmit` draft path and the Stop dispatch name the same file, and nothing else in
the audit is allowed to become a document. Both sides of that path are gated on the agents
that actually read it, never on any switch being on — `comment-corrector` reads the source
files the turn wrote, so a project running only that one is never told to write an answer
file nobody opens. Separately, the `transcript` subcommand
slices turns out of the file on an agent's request — never on a schedule, and always into a
file rather than onto stdout.

Codex is different by necessity: its transcript is not a stable hook interface, so its
adapter keeps its own turn record, and it has one named agent rather than a set — a
router that can only forward to that same agent decides nothing, so Codex recommends the
whole eligible set, unrouted, and is correspondingly noisier. Projects must run
`$guard:setup` once to install it. State is host-specific under `.claude/guard/` or
`.codex/guard/`.

guard's user entry points sit in two directories and the split is by runtime, not by kind.
`commands/<name>.md` and `skills/<name>/SKILL.md` produce the same `/guard:<name>` in Claude
Code, but the Codex manifest registers only `./skills/`, so a Claude-only entry point in
`commands/` is one Codex no longer offers and then refuses. Whichever directory it sits in,
it reaches the CLI through `${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py` — substituted in a
plugin skill's content and its `allowed-tools` rules alike
(`wiki/ref/claude-code-skill-substitutions.md`). Never by climbing out with
`${CLAUDE_SKILL_DIR}/../..`: that depth is wrong the moment the file moves, and it has
moved.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI, the full design invariants, the config reference, and the manual-testing recipe.
