# guard — contributor notes

`guard` supports Claude Code and Codex. `scripts/guard_hook.py` is the entry point and only
that — the subcommand table and `main()`; the implementation is the `scripts/guard_core/`
package. Runtime payload parsing and hook output stay in host adapters.

**Open `dev/design.md` before changing anything here.** It is not auto-loaded, and it owns the
mechanics: the module layering, the hook table, the storage schema, the runtime facts verified
against the real CLI, the config reference, and the manual-testing recipe. Most of what
follows is a pointer into it rather than a second copy.

## What guard is

**guard makes no model call.** When a turn finishes it asks the main agent, through the Stop
hook's `additionalContext`, to dispatch one subagent — `guard:router` — which reads the turn
and names which of guard's audit agents would actually find something in it, with a reason for
each. The main agent dispatches those, concurrently. guard audits nothing itself, and every
audit criterion lives in an agent definition under `agents/`.

Everything guard recommends, it recommends at turn end. Two shipped agents sit outside that
path entirely and have no switch: `ext-docs-fetcher`, which the main agent selects from its
own description, and `ext-docs-auditor`, which the Stop hook names off the refs files the turn
wrote. Anything below that says "the turn" or "the response" is about the routed path.

Every switch ships `off`, and a session additionally starts muted. guard installed is guard
available, not guard running.

`interviewer` is not part of any of that. It is a background agent the **user** talks to directly, in
its own transcript, and it answers to nobody here: no switch, no hook, no router, and guard never
dispatches it. It exists because a turn audited is a turn that cost a router call plus whatever
the router named, and thinking out loud should not cost that — a message sent inside a subagent's
transcript fires no `UserPromptSubmit`, and the `Stop` it does fire in the main session carries a
non-human origin, so guard's own skip catches it. **That skip is the only thing keeping it free.**
Registering a `SubagentStop` hook, or relaxing the origin test, closes this with nothing failing;
`dev/design.md` has the measurement. `interviewer`'s deliverable is one brief file, written when
the user closes the interview and never before, and its final message to the main session is
that path and nothing else — the file is the handoff, so a summary beside it would be a second
version to disagree with.

It ships **no command**. `@agent-guard:interviewer` is documented to guarantee a given subagent
runs, lands it in the background panel, and keeps a running one reachable — so a command would
only be a second, driftable way to say the same thing. What that entry point does not settle is
the opening prompt, which the main agent still writes; the agent's own body has to carry that.

`guard on` / `guard off` flips the session mute from a shell prompt, without entering the conversation at all — the reason it is not a slash command. SessionStart puts it on `PATH` through `$CLAUDE_ENV_FILE`, which is sourced rather than scanned for exports, so there is nothing to install and nothing left behind. It is an executable rather than a shell function so that subprocesses inherit it. `guard-plan` is its counterpart for the plan gate. `toggle-cli` is the one subcommand that must not fail open — a person is reading its output, so silence would read as success.

That same `PATH` carries `guard-candidates` and `guard-inputs`, which are the dispatched agents' and never the user's. Between them the routed dispatch is down to `- turn: <id>`. `dev/design.md` has why that beats printing the roster and the paths, and what each fallback line is for.

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
- Nothing resolves a plugin path by counting `__file__` parents.
- Where a piece of text lives is decided by how often it is paid for: hook output is read on
  every routed turn, `agents/router.md` once per routed turn by the router alone,
  `hooks/context/dispatch-playbook.md` only by whoever is sent to a section. Nobody re-types
  another home's text, and nothing in the playbook describes routing.
- guard writes the turn record's **response** section itself, verbatim from the Stop payload —
  it is the text being audited, so it must not pass through the author's hands. The main
  session appends only what guard cannot see, and that half is asked for as inclusion, never
  as selection.
- Nobody gathers the session's history. The agents that need more are handed a transcript path
  and extract what they want themselves.
- One user question gets exactly one answer file. Nothing else in an audit may become a
  document.
- Only a turn a person typed is audited. A non-human origin guard has never seen must still
  skip, while an *absent* origin must still audit — guard noisy is recoverable, guard silently
  dormant is not.
- The recommendation is `additionalContext`; the refs-index gap is the one `decision: "block"`
  that means unfinished work. The `/`-rooted search refusal is a `PreToolUse` `deny` and is
  the only thing guard forbids outright rather than recommends — it gates a tool ARGUMENT,
  never a caller's identity, which is what separates it from the removed hook below.
- It names **agents**, never guard's own skills — those are the user's entry point, so a hook
  must not reach through them.
- The three edited-file lists stay disjoint, and the refs test runs first, by location.
- Two things ignore the agent switches AND the session mute, because both are prohibitions
  rather than opinions: the refs-index check and the `/`-rooted search refusal. A mute that
  could lift a prohibition would not be one.
- The session mute is session-only, two-valued and visible. Do not grow it back into the
  persistent gate that was removed; if the indicator ever becomes unshippable, drop the mute
  rather than let it go invisible.
- A `/clear` inherits both switches from the session it replaced, and that is the ONLY
  boundary that inherits anything — `startup` opens muted. The predecessor is named by the
  `SessionEnd` record rather than inferred from file times, the record is single-use and
  expiring, and the adoption is announced. Weaken any one of those four and this becomes the
  persistent gate wearing a different name; `dev/design.md` has the measurements.
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
- A persistent `audit_gate` in front of the per-agent switches.
- A `reuse_agents` list separate from the per-agent mode, or an `exempt_skills` list.
- A `.ko-fix.md` rewrite file beside the answer.
- A `UserPromptExpansion` matcher with no command file of that name behind it: the host
  answers `Unknown command` before the hook runs, silently, which is how every one of guard's
  matchers ended up orphaned. guard registers none now — the session mute is a shell command
  (`guard`), not a slash command, so nothing has to keep a matcher and a command file in
  step. There is no per-agent on-demand command on Claude either; Codex keeps its own path,
  which is why the turn marker is still written on every Stop.
- A slash command for the session mute. Flipping guard is not something to say to the model:
  it cost a turn, and it cost a command file whose body never ran.
- A command that spawns `interviewer`. It was written and removed the same day: `@`-mention
  already guarantees the agent runs, so all the command added was a copy of the agent's own
  description and a standing instruction placed in a file that only speaks for one turn.

## Codex

Different by necessity: its transcript is not a stable hook interface, so its adapter keeps
its own turn record, and it has one named agent rather than a set — a router that can only
forward to that same agent decides nothing, so Codex recommends the whole eligible set,
unrouted and correspondingly noisier. Projects run `$guard:setup` once to install it. State is
host-specific, under `.claude/guard/` or `.codex/guard/`.

## Editing this plugin

The source is the truth for control flow, and its comments carry the *why* next to the code.
When editing, record what must not regress — do not restate function bodies here.

`agents/*.md`, `skills/*/SKILL.md`, `commands/*.md` and every string the hooks inject at
runtime are installed into repositories that are not this one, so they must not name this
repo's paths, documents, or measurements. Those belong here or in `dev/`.

## Testing

There is no automated suite. `dev/design.md` § "Manual testing" is the recipe — run it end to
end after changing hook output, state, eligibility, or the dispatch text, and read its
comments: several steps exist to stop the assertions from passing as silent no-ops.

`dev/fixtures/` holds answers with known defects planted in them, for exercising an audit
agent against a ground truth rather than against whatever the last turn happened to produce.
