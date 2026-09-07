# guard — contributor notes

`guard` supports Claude Code and Codex. `scripts/guard_hook.py` is the entry point and only
that — the subcommand table and `main()`; the implementation is the `scripts/guard_core/`
package. Runtime payload parsing and hook output stay in host adapters.

**Open `dev/design.md` before changing anything here.** It is not auto-loaded, and it owns the
mechanics: the module layering, the hook table, the storage schema, the runtime facts verified
against the real CLI, the config reference, and the manual-testing recipe. Most of what
follows is a pointer into it rather than a second copy.

## What guard is

**guard makes no model call, writes no file for an ordinary turn, and asks for nothing when
one ends.** Everything it does is entered by the user, and there are three entries:

- **`/guard:answer <question>`** — the only thing here that produces a document. The skill
  writes the answer to `.claude/answers/`, decides itself which audits have material in it,
  dispatches them, applies what they find, has the corrected English translated when the user
  reads another language, and hands over the finished file. The user's first sight of it is the
  audited version.
- **`/guard:audit-turn`** — over a reply the user has already read. It forks `guard:turn-router`,
  which names which audits would find something in the last turn a person opened; the caller
  runs them together and **reports**. It corrects nothing: that turn was printed before the
  audit was asked for, so there is no document a fix could reach.
- **`/guard:audit-report <path>`** — a standalone document that already exists. `report-router`
  triages it the way `turn-router` triages a turn.

All three are `disable-model-invocation: true` — the user's and only the user's. An entry the
model can reach is work that arrives unasked, and a description in every session's standing
context is an invitation to reach for it. The `audit-turn-*` / `audit-report-*` skills stay
model-invocable and must, since each router names them for its CALLER to invoke.

guard audits nothing itself, and every audit criterion lives in an agent definition under
`agents/`.

### Why the entries, and not a hook

The trigger came off the Stop hook in v0.118.0, the translation in v0.121.0, and the answer
file itself in v0.122.0 — three turns of one argument, each about hit rate. A router asked on
every turn usually answered `none`; a translation written on every turn was usually unread; an
answer file named on every turn turned "안녕" into a document. Work that arrives whether or not
it is wanted is work the user learns to wave through. `dev/design.md` has each argument and
what it gave up.

The v0.122.0 shape is what remains once that is applied all the way down: **`UserPromptSubmit`
is gone**, and Stop no longer records anything about a turn. The turn's text is cut out of the
transcript by `guard-inputs`, at the moment an audit is asked for — including the three skips
that decide what counts as a turn a person opened (non-human origin, guard's own control
commands, a user `!` command), which moved out of `cmd_stop` and into
`transcript._last_auditable_prompt_id`. Same judgment, paid per audit instead of per turn.

### What still runs on a hook

The **edited-file audits**, and they are not a triage question: the turn either edited a source
file, an agent instruction file, or a saved reference, or it did not. `PostToolUse` records the
three lists and Stop names `comment-corrector`, `agents-md-auditor` and `ext-docs-auditor` over
them. That is the whole of what Stop does now.

Also on `PostToolUse`, and unrelated to auditing: the **refs index gate**, which blocks until a
file saved under the refs directory is listed in that directory's index. It is a prohibition,
so it ignores every switch and the session mute.

`docs-finder` sits outside all of it and has no switch: the main agent selects it from its own
description, before stating how something behaves. It searches wider than it writes — saved
references, the repository's own documentation, any configured knowledge directory — and goes
to the network only when the subject is external and nothing local settles it. It reports WHERE
a document is and never what it says, because a gist in its report is a second version of the
document for the caller to disagree with.

`korean-translator` and `korean-corrector` are one step rather than an audit, and neither has a
switch: how well a translation reads must not depend on a config key. What is opted into is
whether a translation happens at all. On the answer path the skill decides it, on the language
it is answering in — a document the reader cannot read is not a deliverable — and it runs
AFTER the audit, so the translation is made once, from the corrected English. There is no
translation on the turn path: an ordinary turn produces no document, so there is nothing to
translate.

**Those two are not guard's definitions.** Since v0.125.0 they are USER-LEVEL agents — this
repository ships them from `global/agents/`, they install into the user's own agent directory,
and guard dispatches them by the bare name with no `guard:` prefix. They read a file and write
a file and were never handed guard's state, and the judgment they make has callers that have
nothing to do with guard; `dev/design.md` has the argument and what it costs. What it costs is
that guard can name an agent a machine has not installed, so both places that write the
dispatch say what to do when the name resolves to nothing.

Every agent switch ships `off`: guard installed is guard available, not guard running.
`audit-plan` says what a session OPENS in for the plan gate — the one audit nobody invokes —
and there is no counterpart for the turn side: a session opens armed there, because every
entry on it is one the user types. `guard` / `guard-plan` then move that session alone, from a
shell prompt, without entering the conversation — which is why neither is a slash command. SessionStart puts them on `PATH` through `$CLAUDE_ENV_FILE`, which
is sourced rather than scanned for exports. `toggle-cli` is the one subcommand that must not
fail open: a person is reading its output, so silence would read as success.

That same `PATH` carries `guard-candidates` and `guard-inputs`, which are the dispatched
agents' and never the user's. **`guard-candidates` takes the path it is answering for**
(`--doc` for the document roster); bare, it answers for the turn path, and an answer-path
caller that omits the flag gets entries pointing at a turn that does not exist.

`handover` is the one skill here that is not about auditing anything. The user runs it to write
a session handover, and its last step records the file's path (`guard-handover`) — which is why
it lives in guard: the `/clear` handoff record is already the one thing that survives a cleared
conversation, and the pointer to the handover rides in it. The replacing session names the file
to the user (a `SessionStart` `systemMessage` — the only channel that reaches them) and reads it
without asking; that it is a read rather than an offer is the user's call, recorded in
`dev/design.md`.

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
  `turn-router` / `report-router`, and the plan critics `plan-coherence`, `plan-fit` and the
  rest. An entry-point skill is the same rule with the verb in front: `audit-turn` /
  `audit-report` for the path's own entry, `audit-turn-claims` / `audit-report-claims` /
  `audit-plan-deferrals` for one audit on it. `answer` keeps a bare name: it is not a path's
  audit entry but the thing that produces what one audits. A definition used on one path only,
  or outside the routers, keeps its bare name; do not prefix one speculatively. The plan
  critics were `design-*` until v0.123.0 and that prefix read as *visual* design, while the
  path is called plan everywhere else (`audit-plan`, `guard-plan`, the plan gate), so they
  follow it. Nothing derives these names — a rename is silent at runtime, so the whole set and
  `skills/audit-plan/SKILL.md` move together or not at all.
- Split at the ENTRY, never at the agent. Every audit that runs on more than one dispatch path
  — claims, deferrals, clarity — is ONE agent behind a `context: fork` skill per path, and the
  reason is memory: a memory directory is named after the agent, so two definitions are two
  memories and what one learns the other relearns. A judgment that genuinely differs by path
  goes in the skill, with the agent saying which judgment that is rather than picking a side;
  the refs-copy rule for a documentation claim and what it takes for a deferral handed to a
  person to stand are the two that do, and on the plan path clarity adds a third: WHO the
  reader is — the person deciding whether to approve it. Deferrals and clarity both run on
  three paths: the turn, a document, and — since v0.123.0 — the approved plan, through
  `audit-plan-deferrals` and `audit-plan-clarity`. The first replaced a `design-deferrals`
  agent asking the same question in almost the same words, which is exactly what this rule
  exists to prevent. What the plan path gained is the half the
  retired agent lacked — a deferral answerable by RUNNING the thing — and what it took on is
  that agent's store, held back by prose alone (`dev/agent-frontmatter-rationale.md`). The
  plan critics that ask a question nothing else asks are still agents of their own, so before
  adding one, check whether `claims-auditor`, `deferrals-auditor` or `clarity-auditor` already
  holds it.
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
- The Korean pair is dispatched UNPREFIXED. `guard:korean-translator` resolves to nothing —
  the definitions are user-level — and a dispatch that matches no agent finds nothing rather
  than raising. Nothing derives either name: the roster prints the bare entry and the `guard:`
  prefix belongs to whoever writes the dispatch, so the two writers that name this pair
  (`agents/report-router.md`'s template, `skills/answer/SKILL.md` § 6) spell it out and say
  why. Adding the prefix back to match the agents beside it in a template is silent.
- Nothing resolves a plugin path by counting `__file__` parents.
- Where a piece of text lives is decided by how often it is paid for. Hook output is read on
  every turn that edits a file; `agents/turn-router.md` and `skills/answer/SKILL.md` once per
  time the user asks. Nobody re-types another home's text.
- guard writes the turn's **response** file itself, cut from the transcript — it is the text
  being audited, so it must not pass through the author's hands. There is no longer a hook that
  does this: `guard-inputs` does it when an audit resolves a turn, and that is the only writer.
- **`/guard:answer` audits its document as a DOCUMENT** (`audit-report-*`), never as a turn. It
  reversed twice before settling, so the reasoning is worth keeping: crediting this turn's tool
  activity as evidence would let a claim with no support *in the text* ship, and the text is
  read later by someone who was not here. The turn's activity is not evidence for a deliverable.
- **The answer document is not written where guard sweeps.** `.claude/answers/` is outside the
  state root on purpose: `SessionStart` reaps `turns/` on a retention window, and a deliverable
  the user asked for must not expire. It also falls into no edited-file bucket
  (`agents._edited_bucket`), so it is never audited as a file the turn edited.
- Nobody gathers the session's history. The agents that need more are handed a transcript path
  and extract what they want themselves.
- One user question gets at most one document, and only `/guard:answer` makes one. An audit
  may never become a document — not a findings file, not a summary.
- Only a turn a person opened is auditable, and the test lives in
  `transcript._last_auditable_prompt_id`. A non-human origin guard has never seen must still
  skip, while an *absent* origin must still qualify — guard noisy is recoverable, guard
  silently finding nothing is not. guard's own control turns skip too, and that list must
  include every entry whose turn is a RELAY: the audit entries, and `answer`, whose reply is a
  path and whose substance is in a document the same turn already audited. An unmatched one
  becomes what the next `/guard:audit-turn` resolves to, and the real turn behind it is then
  unreachable.
- Hook output is `additionalContext`; the refs-index gap is the one `decision: "block"`
  that means unfinished work. The `/`-rooted search refusal is a `PreToolUse` `deny` and is
  the only thing guard forbids outright rather than recommends — it gates a tool ARGUMENT,
  never a caller's identity, which is what separates it from the removed hook below.
- It names **agents**, never guard's own skills — those are the user's entry point, so a hook
  must not reach through them.
- The three edited-file lists stay disjoint, and the refs test runs first, by location.
- `guard-candidates` is where a switch and the mute are enforced for every entry — none has a
  hook in front of it — and `cmd_stop` enforces them for what guard says unasked. It answers
  per PATH: `--doc` for the document roster, bare for the turn's. `/guard:answer` must pass
  `--doc`; without it the roster names turn entries that resolve a turn that does not exist.
  Neither is redundant: drop the check in the command and `guard off` silences the
  hook while every audit the user can invoke keeps running. The PLAN review is outside this and must stay
  outside: `audit-plan` invokes its critics by name and reads none of the per-agent switches,
  because a plan held for review is reviewed whole or not at all — half a review is worse than
  none, since what it passes over reads as checked. Whether a plan is held at all is
  `audit-plan` / `guard-plan`'s question, answered before the review starts. Do not give the
  plan entries a roster row. What the mute must NOT be is a
  project default — that was `audit-turn`, and it refused commands the user had just typed;
  the Codex adapter therefore checks no mute at all on its audit prefix, since that host has
  no `guard` command and so nothing but a setting could ever have set one.
- Two things ignore the agent switches AND the session mute, because both are prohibitions
  rather than opinions: the refs-index check and the `/`-rooted search refusal. A mute that
  could lift a prohibition would not be one.
- The session mute is two-valued and visible, and the shell toggle writes session state only —
  never the config. It has no setting behind it at all since v0.124.0: the persistence that is
  left is `audit-plan`, which says what a session opens in for the gate and nothing else. Do
  not let the toggle start writing it, do not give the turn mute a key again, and if the
  indicator ever becomes unshippable, drop the mute rather than let it go invisible. It is
  visible in two places — the status line and `settings show`'s first line — and neither is
  optional.
- A `/clear` inherits both switches from the session it replaced, plus the handover file that
  session recorded, and that is the ONLY boundary that inherits anything — every other start
  reads the settings. It carries a session that DIFFERS from the pair a fresh session lands on,
  in either direction. For the plan half that baseline is a config read, which is why the
  comparison is against the config rather than against a fixed idea of which state is
  noteworthy — a project setting `audit-plan: off` loses its `guard-plan on` the same way
  anyone else loses a `guard-plan off`. For the turn half the baseline is simply armed. The predecessor is named by the
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
- `audit_gate` (`off`/`ask`/`auto`) in front of the per-agent switches. What is left in that
  position is the session mute: a boolean, with no `ask` to reason about and both states on
  screen. Keep those two and it is a switch; lose either and it is the gate again.
  `audit-turn`, the setting that seeded it, is now in the same list — retired in v0.124.0. A
  default that opened a session muted was the gate itself once every entry became one the user
  types: `guard-candidates` reported the mute, so a typed `/guard:audit-turn` was refused by a
  config file. Do not add a key for it again; a project that wants guard quiet has the agent
  switches, which already ship `off`. `dev/design.md` has both arguments.
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
match declares a different `name:` in its frontmatter. An entry listed in its `EXTERNAL_ENTRIES`
is a user-level agent and is checked the other way round — the definition must exist to install
from, and the plugin must NOT also ship a copy of it. That is the only place the Python roster
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
