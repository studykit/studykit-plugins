# guard — contributor notes

`guard` supports Claude Code and Codex. `scripts/guard_hook.py` is the entry point and only
that — the subcommand table and `main()`; the implementation is the `scripts/guard_core/`
package. Runtime payload parsing and hook output stay in host adapters.

**Open `dev/design.md` before changing anything here.** It is not auto-loaded, and it owns the
mechanics: the module layering, the hook table, the storage schema, the runtime facts verified
against the real CLI, the config reference, and the manual-testing recipe. Most of what
follows is a pointer into it rather than a second copy.

## What guard is

**guard makes no model call, and asks for none when a turn ends.** The turn audit is the
USER's to start: `/guard:audit-turn` forks `guard:turn-router`, which reads the turn and names
which of guard's audit agents would actually find something in it, with a reason for each. The
caller dispatches those together and applies nothing until they have all reported, so every
audit judges the same text and overlapping findings are reconciled in one pass. Then one
further round, over the corrections and limited to the audits that produced them, because a
correction is prose no audit has read. guard audits nothing itself, and every audit criterion
lives in an agent definition under `agents/`.

The trigger moved off the Stop hook in v0.118.0, and the reason was the hit rate: a router was
asked for on every turn that had an answer file and the common answer was `none`, so the usual
cost of the feature was a subagent per turn reporting that there was nothing to do — and a
recommendation that arrives whether or not it is wanted is one the user learns to wave through.
What the hook still does is the half a user cannot do afterwards: record the turn verbatim
while it is fresh, and name the file the answer is written to. `dev/design.md` has the argument
and what it gave up.

`/guard:audit-turn`, `/guard:audit-report` and `/guard:translate-turn` are
`disable-model-invocation: true` — the user's and only the user's. That is the other half of the same fix: an entry the model can reach is an
audit that can still arrive unasked, and a description in every session's standing context is
an invitation to reach for it. The three `audit-turn-*` / `audit-report-*` skills stay
model-invocable and must, since each router names them for its CALLER to invoke.

Two shipped agents sit outside all of that and have no switch: `docs-finder`, which the main
agent selects from its own description, and `ext-docs-auditor`, which the Stop hook names off
the refs files the turn wrote. Anything below that says "the turn" or "the response" is about
the audited path.

The two names no longer rhyme, and that is the shape rather than drift: the finder searches
wider than it writes — saved references, the repository's own documentation, any configured
knowledge directory — while the auditor's subject is still only the refs copies. It reports
WHERE a document is and never what it says, because a gist in its report is a second version
of the document for the caller to disagree with.

Two agents are one step rather than an audit: `korean-translator` writes the Korean version of
a finished English answer, and `korean-corrector` then judges what it wrote. **Neither has a
switch**, and neither runs unasked: `/guard:translate-turn` is the user's entry to both, the
same shape and for the same reason as `/guard:audit-turn` — `disable-model-invocation: true`,
so the model cannot reach it and its description never enters a session's context.

The turn is delivered in ENGLISH now. Translating from the closeout on every turn that carried
substance was a subagent per turn spent whether or not the Korean was going to be read, which
is the cost that moved the audit off the Stop hook in v0.118.0 — the same argument, one release
later, about the other automatic dispatch. What replaced it is one command and one exception:
the closeout still re-runs the translator after an audit corrects a turn that ALREADY has a
translation, because that document exists, the user asked for it, and the audit has just made
their copy wrong.

The switchless part is unchanged and still deliberate: how well a translation reads must not
depend on a config key, and `off` would put the session back to translating its own text, which
is the arrangement that produced 직역. What is opted into is whether a translation happens at
all, and that is a request, not a setting.

**Neither is routed on the turn path** (`routed` is per path, and holds only `report` for the
translator and nothing for the corrector). The translator was the router's one pick the answer
file could not evidence — the language had to be inferred from the request. The corrector is
handed over by the translator's own report, which is the one place the fact it turns on — the
translation now exists — is actually known. A document still routes the translator, because
there the caller states in the dispatch who will read it. `dev/design.md` has why an author
cannot translate their own text, what the translator must not move while doing it, and why a
turn's translation is rewritten after an audit rather than translated once.

Every agent switch ships `off`: guard installed is guard available, not guard running. The two
audit switches (`audit-turn`, `audit-plan`) do not agree with each other, and that is the
design rather than an oversight: absent from the config, `audit-turn` reads as `off` and
`audit-plan` as `on`. What `audit-turn` arms is no longer an automatic audit but the discipline
one needs — the answer file named at the start of every turn, the turn recorded at the end — and
that is still charged per turn, so the user arms it for the stretch of work that wants it. The
plan gate fires only at `ExitPlanMode`, where the cost is rare and letting a deferral through is
paid for by the whole implementation after it. They are the value each session OPENS in; `guard`
/ `guard-plan` then move that session alone.

`audit-report`, `report-router` and the three `audit-report-*` skills are the **document**
path. Its subject is a standalone document rather than a finished turn, and no hook reaches it:
the user points `/guard:audit-report <path>` at a file and that router triages the document the
way `turn-router` triages a turn. Nothing in the hooks is involved, which is why the switches
and the mute live in `guard-candidates` — it is the only thing both routers run, and neither
has a hook in front of it to check them any more.

Nothing in this plugin produces a document for this path — the user names the file. `dev/design.md`
has why the surface was kept without a producer, and what it replaced.

`guard on` / `guard off` flips this session's mute from a shell prompt, without entering the conversation at all — the reason it is not a slash command. It leaves `audit-turn` alone, so muting the session you are in never changes what the next one does. SessionStart puts it on `PATH` through `$CLAUDE_ENV_FILE`, which is sourced rather than scanned for exports, so there is nothing to install and nothing left behind. It is an executable rather than a shell function so that subprocesses inherit it. `guard-plan` is its counterpart for the plan gate. `toggle-cli` is the one subcommand that must not fail open — a person is reading its output, so silence would read as success.

`handover` is the one skill here that is not about auditing anything. The user runs it to
write a session handover, and its last step records the file's path (`guard-handover`) — which
is the whole reason it lives in guard rather than beside it: the `/clear` handoff record is
already the one thing that survives a cleared conversation, and the offer to read the handover
rides in it. `dev/design.md` has why the skill records the path instead of the next session
scanning for one, and why the offer ignores the mute.

That same `PATH` carries `guard-candidates` and `guard-inputs`, which are the dispatched agents' and never the user's. Between them a turn audit's inputs are down to `- turn: <id>` — or nothing at all, since `guard-inputs` resolves the last recorded turn when the user names none — and a document audit's to `- file: <path>`. `dev/design.md` has why that beats printing the roster and the paths, and what each fallback line is for.

## Hard requirements

guard has no Python dependencies but it does need **uv**. Both hook manifests and both
scripts' shebangs go through `uv run --script`, as `guide/adapter-guide.md` requires, and the
PEP 723 block pins `requires-python = ">=3.11"` (`enum.StrEnum`).

That pin is the point, not paperwork. `#!/usr/bin/env python3` takes whatever is first on the
PATH of the process the host launched the hook from, which on macOS is 3.9 in any context
whose PATH comes from a login rather than an interactive shell — a tmux pane, for one. Every
hook then died with an ImportError and, having printed nothing, left the model free to report
a success it had not achieved. Measured in a real session; `dev/design.md` § "Why uv, and what
it fixed" has it.

## Invariants that fail silently

Each of these broke once, and none of them raises an error when it breaks. `dev/design.md`
carries the full set with the reasoning and the measurements; these are the ones that decide
how the code here is organised.

- `guard_core.config` is the ONLY reader of `GUARD_HOST`, once, at import.
- A definition that exists once per dispatch path is named `<path>-<what it does>` —
  `turn-router` / `report-router`. An entry-point skill is the same rule with the verb in
  front: `audit-turn` / `audit-report` for the path's own entry, `audit-turn-claims` /
  `audit-report-claims` for one audit on it, `translate-turn` for the one step on the turn path
  that is not an audit at all. A definition used on one path only, or
  outside the routers, keeps its bare name; do not prefix one speculatively.
- Split at the ENTRY, never at the agent. Every audit that runs on both dispatch paths —
  claims, deferrals, clarity — is ONE agent behind two `context: fork` skills, and the reason
  is memory: a memory directory is named after the agent, so two definitions are two memories
  and what one learns the other relearns. A judgment that genuinely differs by path goes in
  the skill, with the agent saying which judgment that is rather than picking a side; the
  refs-copy rule for a documentation claim and what it takes for a deferral handed to a person
  to stand are the two that do.
- A router-named skill's `description` is as short as it can be: the router names it and the
  caller invokes it by name, so the line never has to attract an invocation, and it is loaded
  into every session's context whether or not guard runs. The three ENTRY skills are the
  opposite case and are handled by the opposite means — `disable-model-invocation: true`,
  which keeps their descriptions out of that context entirely and leaves them free to say
  plainly what the user is about to run. `session-start` is then the only place a session
  learns those names, since a description it cannot see is a command it cannot name when the
  user asks for one in prose.
- A roster key names the AUDIT and is user-visible configuration; an ENTRY names what the
  caller invokes for that audit on one path. `agents._path_entry` is the ONLY place one
  becomes the other, and `cmd_candidates` is its only caller. An entry is an agent for some
  rows and a skill for others — whichever it is, the name the router prints is the
  name the caller invokes, and the router's own report template says with which tool. A key must never be renamed to follow an agent —
  `_load_config` honours only keys it knows, so a configured audit would silently read as its
  default. Nothing else may derive a dispatchable identity from a key.
- Nothing resolves a plugin path by counting `__file__` parents.
- Where a piece of text lives is decided by how often it is paid for: hook output is read on
  every turn that has an answer file, `hooks/context/turn-closeout.md` by that same turn when
  it delivers it, and `agents/turn-router.md` once per AUDIT — which now means once per time
  the user asks for one, the rarest of the three. Nobody re-types another home's text, and
  nothing in the closeout file describes routing.
- **Delivering a turn dispatches nothing, and the closeout names no agent for it.**
  Everything an audit needs travels with the dispatch — each router's report template,
  `_agent_pointer`'s lead on the no-router path — and what its findings mean travels in its own
  report, which is why the file-editing audits end each finding in a disposition (apply / move
  / decide). The file named the translator between v0.118.0 and v0.121.0, when translating was
  the caller's own decision taken on a fact only the caller held; `/guard:translate-turn` took
  that decision back to the user, and the name came out with it. The one agent the file still
  names is that same translator in the AUDIT section, re-run over a translation that already
  exists — which is not a decision at all, since the document is there and the audit just made
  it wrong. What the closeout holds otherwise is the turn: the answer file is the deliverable,
  the reply is short and in the user's language, the file opened is the one the user reads, and
  an audit's findings go into the English first. The rule stays as narrow as it can be: an
  agent named here for the normal path is either a second authority over a decision already
  made or a lookup that belongs in a report — see `dev/design.md` for the turn that cost.
- guard writes the turn record's **response** section itself, verbatim from the Stop payload —
  it is the text being audited, so it must not pass through the author's hands. The main
  session appends only what guard cannot see, and that half is asked for as inclusion, never
  as selection.
- Nobody gathers the session's history. The agents that need more are handed a transcript path
  and extract what they want themselves.
- One user question gets exactly one answer file. Nothing else in an audit may become a
  document.
- Only a turn a person typed is recorded as auditable. A non-human origin guard has never
  seen must still skip, while an *absent* origin must still be recorded — guard noisy is
  recoverable, guard silently dormant is not. guard's own control turns skip too, and that
  list has to include every entry whose turn is a RELAY — the audits and
  `/guard:translate-turn`: an unmatched one becomes the pending target itself, so the next
  audit would read guard's report of the last one.
- Hook output is `additionalContext`; the refs-index gap is the one `decision: "block"`
  that means unfinished work. The `/`-rooted search refusal is a `PreToolUse` `deny` and is
  the only thing guard forbids outright rather than recommends — it gates a tool ARGUMENT,
  never a caller's identity, which is what separates it from the removed hook below.
- It names **agents**, never guard's own skills — those are the user's entry point, so a hook
  must not reach through them.
- The three edited-file lists stay disjoint, and the refs test runs first, by location.
- `guard-candidates` is where a switch and the mute are enforced for BOTH routers — neither
  has a hook in front of it any more — and `cmd_stop` enforces them for what guard says
  unasked. Neither is redundant: drop the check in the command and `guard off` silences the
  hook while every audit the user can invoke keeps running. The Codex adapter needs the same
  check on the one path that can start an audit there (`_handle_prompt`).
- Two things ignore the agent switches AND the session mute, because both are prohibitions
  rather than opinions: the refs-index check and the `/`-rooted search refusal. A mute that
  could lift a prohibition would not be one.
- The session mute is two-valued and visible, and the shell toggle writes session state only —
  never the config. The persistence lives in `audit-turn` / `audit-plan`, which say what a
  session opens in and nothing else; do not let the toggle start writing them, and if the
  indicator ever becomes unshippable, drop the mute rather than let it go invisible.
- A `/clear` inherits both switches from the session it replaced, plus the handover file that
  session recorded, and that is the ONLY boundary that inherits anything — every other start
  reads the settings. It carries a session
  that DIFFERS from those settings, in either direction, which is why the comparison is
  against the config rather than against "armed". The predecessor is named by the
  `SessionEnd` record rather than inferred from file times, the record is single-use and
  expiring, and the adoption is announced. Weaken any one of those four and this becomes the
  persistent gate wearing a different name; `dev/design.md` has the measurements.
- The handoff record's two halves — the switches and the handover — are written and read
  INDEPENDENTLY. Collapse them into one "is there anything to carry" test and the record is
  still written, the checked half still survives, and the other half is simply absent.
- guard always exits 0 and fails open.

## Deliberately not enforced

`memory:` grants Write and Edit silently and the host does not scope the grant, so an agent
that reports and never edits *can* write anywhere; nothing refuses it. "Reports; edits
nothing" is a promise in each agent's body.

A `PreToolUse` hook that refused those writes was built and then removed on request. It is
not in the list below, because it worked — it was not abandoned for failing. Read
`dev/design.md` for what the removal gave up before adding one back.

## Tried, and must not come back

Listed so a rediscovered idea is recognised rather than rebuilt. `dev/design.md` records what
each one cost.

- The router as a `claude -p` child process.
- Any hook that redirects by naming a replacement in a `PreToolUse` deny reason — a deny
  reason is weighed as tool output, which was measured.
- Judging inside the hook, or picking agents by lexical pattern.
- `audit_gate` (`off`/`ask`/`auto`) in front of the per-agent switches. `audit-turn` is a
  boolean in that position and is persistent, so the difference is no longer persistence: it is
  that there is no `ask` to reason about and that both of its states are on screen. Keep those
  two and this is a switch; lose either and it is the gate again. `dev/design.md` has the
  argument.
- A `reuse_agents` list separate from the per-agent mode, or an `exempt_skills` list.
- The `reuse` mode itself — one named instance per session, resumed on later turns. Removed
  once each agent's "If you are resumed" section was, since that section was the whole
  mitigation for what reuse costs: a verdict the instance got wrong stays in its history as
  settled. Reviving the mode means reviving those sections, and fixing what it took with it —
  instance names derived from the roster KEY rather than the agent name, which made every
  agent rename silently emit a stale name.
- `keep` / `resume` as aliases pointing at the on mode. They meant `reuse`; a user typing one
  is asking for what no longer exists, and answering with a different mode is worse than saying
  the value is not a mode. `fresh` is the opposite case and stays: it is the on mode's own
  former spelling, so every config file written before v0.116.0 says it, and dropping it would
  read those projects as `off`.
- A `.ko-fix.md` rewrite file beside the answer.
- A `UserPromptExpansion` matcher with no command file of that name behind it: the host
  answers `Unknown command` before the hook runs, silently, which is how every one of guard's
  matchers ended up orphaned. guard registers none now — the session mute is a shell command
  (`guard`), not a slash command, so nothing has to keep a matcher and a command file in
  step, and the on-demand audit is a real skill rather than a matcher.
- A slash command for the session mute. Flipping guard is not something to say to the model:
  it cost a turn, and it cost a command file whose body never ran.
- A command that launches an `@`-mentioned agent. Written and removed the same day for the one
  guard used to ship: `@`-mention already guarantees the agent runs, so all the command added
  was a copy of the agent's own description and a standing instruction placed in a file that
  only speaks for one turn.

## Codex

Different by necessity: its transcript is not a stable hook interface, so its adapter keeps
its own turn record, and it has one named agent rather than a set — a router that can only
forward to that same agent decides nothing, so there is no routing here: the whole eligible
set becomes one scope sentence handed to that agent. The audit is on demand on this host too,
and it has to be a prompt PREFIX (`$guard:audit-turn`, `/guard:audit-turn`) rather than a
skill, because a Codex command hook cannot launch an agent. Projects run `$guard:setup` once
to install the agent. State is host-specific, under `.claude/guard/` or `.codex/guard/`.

## Editing this plugin

The source is the truth for control flow, and its comments carry the *why* next to the code.
When editing, record what must not regress — do not restate function bodies here.

`agents/*.md`, `skills/*/SKILL.md`, `commands/*.md` and every string the hooks inject at
runtime are installed into repositories that are not this one, so they must not name this
repo's paths, documents, or measurements. Those belong here or in `dev/`.

**No agent file is generated any more.** There was a build step
(`dev/agent-src/` + `dev/build-agents.py`) while the shared audits ran as two agents each and
their criteria had to be inlined into both; the entry split removed the duplication it
existed to manage. `dev/design.md` keeps the argument, because the same pressure returns the
moment two definitions share a body.

## Testing

`uv run dev/check-entries.py` is the one thing close to a test: it fails if a roster entry
point matches neither `agents/<name>.md` nor `skills/<name>/SKILL.md`, or if the file it does
match declares a different `name:` in its frontmatter. That is the only place the Python roster
and the markdown definitions can be compared at all, and both failures are silent at runtime —
a dispatch or an invocation that matches nothing finds nothing rather than raising. Nothing
runs it for you; put it in a local pre-commit hook.

Beyond that there is no automated suite. `dev/design.md` § "Manual testing" is the recipe — run it end to
end after changing hook output, state, eligibility, or the dispatch text, and read its
comments: several steps exist to stop the assertions from passing as silent no-ops.

`dev/fixtures/` holds answers with known defects planted in them, for exercising an audit
agent against a ground truth rather than against whatever the last turn happened to produce.
`defective-brief.md` is the document-path counterpart — its planted defects are the ones that
path gets wrong, and it lists two things the agent must NOT report.
