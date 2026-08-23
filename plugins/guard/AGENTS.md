# guard — contributor notes

`guard` supports Claude Code and Codex. `scripts/guard_hook.py` is the entry point and only
that — the subcommand table and `main()`; the implementation is the `scripts/guard_core/`
package, one module per layer, described in `dev/design.md`. Runtime payload parsing and hook
output stay in host adapters.

guard has no Python dependencies but it does need **uv**. Both hook manifests and both
scripts' shebangs go through `uv run --script`, as `guide/adapter-guide.md` requires, and the
PEP 723 block pins `requires-python = ">=3.11"` (`enum.StrEnum`). That pin is the point, not
paperwork: `#!/usr/bin/env python3` takes whatever is first on the PATH of the process the
host launched the hook from, which on macOS is /usr/bin/python3 (3.9) in any context whose
PATH comes from a login rather than an interactive shell — a tmux pane, for one. Every hook
then died with an ImportError traceback in the user's session, and having printed nothing it
left the model free to report success it had not achieved. Measured, in a real session, and
fixed by letting uv choose the interpreter.

Two invariants the module split exists to hold, both of which broke once: `guard_core.config`
is the ONLY reader of `GUARD_HOST` and reads it once at import, and nothing resolves a plugin
path by counting `__file__` parents — the split moved code a level deeper and silently
rewrote every playbook path guard printed. `dev/design.md` has the layering and the reasons.

**guard makes no model call.** When a turn finishes it asks the main agent, through
`additionalContext`, to dispatch one subagent — `guard:router` — that reads the turn and
names which of guard's audit agents would actually find something in it, with a reason
for each; the main agent then dispatches those, concurrently. guard audits nothing itself,
and every audit criterion lives in an agent definition under `agents/`.

guard recommends at **two** events, not one. The turn-end path above is the bulk of it;
`ext-docs-fetcher` (item 2) is also reachable at the other end, before an answer exists, off a
policy announced once at SessionStart. Anything below that says "the turn" or "the response"
is about the turn-end path.

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
   `/guard:clarity-auditor`, `/guard:korean-corrector`, `/guard:comment-corrector`,
   `/guard:agents-md-auditor`, `/guard:ext-docs-fetcher` and `/guard:ext-docs-auditor` work whatever
   the settings say. The per-agent settings then decide what reaches the main agent unasked. Each
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
   mode being anything but `off`, plus — for a file-reading agent — at least one file of
   its own kind that the turn actually wrote. Everything requiring judgment is the
   router's.

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
   - Nobody gathers the session's history. The record holds the response, and beside it
     guard saves the user's request verbatim for the ROUTER alone — materiality is relative
     to what was asked, and it is the one judgment that cannot be made from the answer by
     itself. Kept as a sibling file, not a section, so the correctors never edit the user's
     own words; no audit agent is given it, and the router may only ever use it to name
     FEWER agents, never as the reason to name one. Both are named relative to a `turn dir`
     the dispatch spells once — the router is never told how to BUILD a guard path, because
     that prose would be a second copy of the storage layout and a drifted copy clears every
     turn silently. Beyond those two,
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

   Three agents never go through the router — `comment-corrector`, `agents-md-auditor` and
   `ext-docs-auditor`. Their input is a file list, not the answer, so triage could only restate
   what eligibility already decided: a file list is not a diff, and reading those files shows
   their current state, never what this turn changed in them. Two of them carry a second
   reason of their own.

   `agents-md-auditor` is the first, and its
   findings are the one kind the main agent must not apply on autopilot: deleting a section
   from an `AGENTS.md` usually means moving its content into a deeper doc that does not
   exist yet, and creating that document is a change nobody asked for. So the playbook
   splits its report in two — the deletions and pointer fixes that need no new file, and
   the findings that need the user's decision — and the agent itself is forbidden from
   writing the documents it recommends. An auditor that "fixed" a bloated instruction file
   by inventing three new ones would have destroyed content under the name of an audit.

   `ext-docs-auditor` is the second, and it is the same hazard in a different directory. A saved
   reference exists to be a faithful copy of something external, so the finding it is built
   for — a passage that is really about this repository — is fixed by MOVING that passage,
   not deleting it, and the destination is usually a design note that does not exist yet. It
   has no network on purpose: a page that reads differently today says nothing about whether
   the excerpt was honest when it was taken, and an auditor that could fetch would do the
   fetcher's job instead of its own, leaving nothing to check the fetcher.

   **The auditors that keep a store carry `memory: project`, and what bounds their writing is
   a hook rather than the absence of the field.** Removing `memory:` was the previous answer
   and it is worth knowing why it is not the current one. The field silently grants Write and
   Edit and the host does not scope that grant, so an agent whose description ends "Reports;
   edits nothing" cannot make that true by declaring a tool list; the only boundary left was
   prose in each body, and prose lost. `deferrals-auditor` stored the conclusion that
   live-runtime deferrals are legitimate and cited its own note back as the reason for passing
   exactly the deferral it exists to catch. Deleting the note did not hold, because the next
   run wrote a fresh one: with a store available the cheapest move is always to match a stored
   pattern instead of re-deriving the judgement, and a wrong stored verdict is invisible by
   construction — it suppresses the finding that would have exposed it.

   Taking the store away stopped that but cost the thing a store is for, so the enforcement
   moved out of the definitions instead. `pre-write` (`PreToolUse`) denies a report-only
   agent's write to anything outside an agent-memory directory, which makes "reports; edits
   nothing" a fact about what the runtime permits rather than a sentence each body repeats —
   and an agent cannot widen it by editing its own file. The scope is `project` rather than
   `local` for the **review**, not for the sharing: an entry that lands in the project's diff
   is caught by whoever reads the diff, which is the only thing that has ever caught a wrong
   one.

   What did not change is what belongs in a store: where the answers live, never what is
   true. A remembered verdict is re-derived rather than cited, and "already confirmed
   earlier" is not confirmation wherever it is read. `reuse` is a different axis and is
   unaffected — within-session, uncurated, forgotten when the session ends. The router has no
   memory at all: its answer must come from this turn, not from a habit.

   `clarity-auditor` is `user` rather than `project`, alone in that, because what it stores is
   not its own work — the reader profile is written by the user through
   `/guard:reader-profile` and the agent only reads it, and a person does not change when they
   switch repositories. `ext-docs-auditor` has no `memory:` at all, and neither corrector does;
   each frontmatter carries its own reason.

2. **Documentation** (`ext-docs-fetcher`) — the one agent reachable from **both** ends of a turn,
   and the exception most rules above are phrased around. This project's evidence contract
   makes a doc-based claim save a local copy of what it cites; enforcement was at write time
   only, so nothing made those copies get *read*, and a question already answered on disk got
   answered from memory or a re-fetch instead.

   The agent looks in the refs directory first and reports the path, and fetches only when
   nothing saved covers the question — then it writes the excerpt, indexes it, and reports
   which of the two happened. It replaced two agents, and what the merge had to preserve is
   why: a read-only lookup used to report `none` and leave the session to remember to dispatch
   a fetcher, and that handoff was where a session gave up and answered from memory. The
   distinction the lookup existed to make now lives in the **report** — already saved, or
   newly fetched — so the caller still knows what it got. If that ever stops being reported
   the merge has failed, and the fix is to restore the distinction, not to split the agent.

   Three things must not regress:

   - **The prohibition is a hook; the redirect is a sentence. Both, not either.** `pre-fetch`
     denies `WebFetch`/`WebSearch` in the main conversation while this switch is on, because a
     standing instruction to delegate is skippable and leaves no trace when it is skipped. But
     a deny reason is delivered as the tool's error result and weighed as tool output, not as
     an instruction the session must obey (probe:
     `wiki/ref/claude-code-pretooluse-deny-reason-visibility.md`), so the hook alone enforces
     "do not fetch" and only suggests "dispatch this instead". The SessionStart line carries
     the redirect, and carries alone the half no hook can reach: answering from memory makes no
     tool call, so nothing fires and nothing can be denied. Deleting either one leaves a gap.
     Once is enough for the line because SessionStart registers no matcher and so fires on
     every source — `compact` among them — which restates it as soon as a compaction drops it
     (`wiki/ref/claude-code-hooks-session-env.md`).
   - **`pre-fetch` fails open inside every subagent.** The test is the presence of
     `agent_type`, not a match against the fetcher's name. A subagent cannot dispatch another
     agent — the host filters `Agent` out of every subagent's tool list — so denying its fetch
     would take the tool away and leave the replacement unreachable. That covers
     `ext-docs-fetcher` itself, whose whole job is to fetch, without naming it in a second
     place that could drift.
   - **The question goes over verbatim.** guard's saved copy of the request is written at
     `UserPromptSubmit` and addressed to the router; on the pre-answer path this agent is
     never handed it, so the main agent is its only source — and a question already condensed
     into search terms has lost what separates a reference from a lookalike.
   - **Suppressed on Codex, at the source.** `cmd_session_start` is core and the Codex adapter
     calls it directly; Codex ships one named agent and no fetcher, so without the
     `_HOST_IS_CODEX` gate the line forbids WebFetch and names no replacement.

   It is also the only *routed* agent that writes to the repository, which is why its playbook
   section ends by dispatching `ext-docs-auditor` on exactly what it saved. Nothing else would: on
   the pre-answer path no turn-end recommendation has run, on the turn-end path it has already
   gone out, and either way the agent that wrote the file must not grade it.

   **`ext-docs-fetcher` and `ext-docs-auditor` carry `opus` rather than the cheapest model that fits,
   and both were measured rather than assumed.** The comparison and what broke each tie are in
   `dev/design.md`; each agent's frontmatter carries the short version. Re-run it before
   changing either.

3. **Session mute** (`/guard:toggle`, UserPromptExpansion) — `audit_paused` in the session
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

4. **Post-edit** (PostToolUse on the write tools) — records the files the turn edited for
   a later file-reading agent's recommendation, and blocks until a file saved in the refs
   directory is listed in that directory's `AGENTS.md`. Both independent of the agent
   settings.

   Three lists, not one, and they must stay disjoint (`_edited_bucket`): source files for
   `comment-corrector`, `AGENTS.md`/`CLAUDE.md` for `agents-md-auditor`, anything under the
   refs directory for `ext-docs-auditor`. A shared list would hand each agent files its criteria
   say nothing about — a comment judged against markdown, an instruction file judged against
   a `.py` — and a name landing in two would be audited twice under criteria only one of
   which applies. One turn marker governs all three, because "which turn was this" is the
   same question for each and a second marker could only drift from the first.

   The refs test is by **location and runs first**, and that order IS the disjointness. The
   refs directory's own index is named `AGENTS.md` and its shim `CLAUDE.md`, so by name alone
   both would go to `agents-md-auditor`, which would fault the index of a reference library
   for not being a map of the project's deeper docs. Inside the refs directory every markdown
   file is the refs auditor's, index included.

   Both jobs see a **subagent's** writes, not only the main agent's: tool events fire the same
   hooks inside a subagent and the payload carries `agent_id` / `agent_type`
   (`https://code.claude.com/docs/en/hooks`). The refs bucket depends on that entirely — the
   file lands there because `ext-docs-fetcher` saved it, not because the main agent did.

   `state._read_state` has a `default` dict AND a `keys` whitelist, and a new state key must
   be added to **both**. A key missing from `keys` is written and then dropped on the next
   read, which is indistinguishable from the writer never having run.

   `agents-md-auditor` matches on the **filename**, not the suffix. What makes one of these
   auditable is that a coding agent loads it as standing instruction, which is a property of
   the name the host looks for; every other markdown file in a repository is prose nobody is
   instructed by, and auditing one against what an instruction file may contain would flag
   an ordinary document for having content.

guard resolves the project root two ways, and merging them breaks one of the two. A **hook**
is handed `CLAUDE_PROJECT_DIR` and so never guesses: absent means a broken install, and
`_project_dir` returns None rather than writing state under whatever directory the host
launched in. A **CLI verb** invoked over Bash — `transcript`, `settings`, `refs-dir` — never
receives it (that variable reaches Bash only through an explicit `CLAUDE_ENV_FILE` export,
`wiki/ref/claude-code-hooks-session-env.md`). So SessionStart writes that export itself,
under guard's own name — `GUARD_PROJECT_DIR` — and `_cli_project_dir` reads it, falling back
to a walk up to the git root. Never export `CLAUDE_PROJECT_DIR`: the host owns that name and
other tooling reads its presence as "running inside a hook". The exports are append-once,
because SessionStart also fires on every compaction. The cwd is not an acceptable stand-in: an agent that had `cd`-ed into a
subdirectory wrote its extract to a second state tree there, which the root-anchored
`.gitignore` did not cover, and `settings show` from the same place reported a project with
every switch off. Both failures are silent, which is why the ignore patterns are also
`**/`-prefixed — the rule must not be the last thing standing between a session extract and
a commit.

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
that actually read it, never on any switch being on — the file-reading agents read the
files the turn wrote, so a project running only those is never told to write an answer
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

`/guard:settings` is the one entry point that does **not** run in the main session. It
carries `context: fork` with `agent: general-purpose`, and the reason is cost: a session
late in its life re-pays for its whole context on every turn, so a settings exchange held
there is charged against the conversation the user actually came for. A forked skill does
not inherit that conversation — `context: fork` is not `/subtask`
(`wiki/ref/claude-code-skill-fork-context.md`) — so the body and the exchange both stay out.
Three things follow.

**The body is long on purpose, and that is not the usual smell.** With the fork it is paid
for once, by the agent that needs it, and never by the conversation the user came for — so
the question for anything in it is "does this run use it", not "is the file short". The
`context: fork` warning is the real constraint: a forked skill needs an actionable task, so
reference material must sit inside instructions rather than replace them.

It stays **background**, which is the default and must remain so. Only background agents
appear in the interactive panel, and that panel is how the user opens the transcript and
keeps adjusting settings by talking to the agent (`wiki/ref/claude-code-subagent-resume.md`).
Foreground would take the tokens out of the main context and hand back nothing the user
could continue.

**Nothing enforces the CLI-only rule; the body asks for it.** A custom `tools: Bash` agent
would have made hand-editing `guard.local.json` impossible rather than forbidden, and that
was tried and dropped — one more agent definition to keep in step with a file that is
already the single home for this. `allowed-tools` is not the substitute: per the docs it
pre-approves and "does not restrict which tools are available". `disallowed-tools` does
remove tools, and the skill sets it, but whether that reaches inside a fork is undocumented
— so treat it as belt-and-braces and keep the standing prohibition in the body as the thing
actually holding. This is the same class of guarantee as `GUARD_SETTINGS_SKILL=1`, which a
model also sets: both prove the chain began at the user's entry point, never that no agent
could have gone around them.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI, the full design invariants, the config reference, and the manual-testing recipe.
