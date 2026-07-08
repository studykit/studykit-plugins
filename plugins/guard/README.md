# guard

Keep Claude Code honest about technical claims, and keep it from editing your
project before you have actually approved the work.

**Claude Code only.**

## What it does

guard adds three layers of control over the assistant's responses and actions:

1. **Grounded output style** — an output style that requires every technical
   claim to carry its evidence (a `file:line` reference, a command's output, a
   named doc/spec, or a measurement), and to mark anything unverified as an
   assumption instead of stating it as fact.

2. **Evidence judge** — while guard is on, it reviews each finished response on two
   axes, reading your repository to check. First, **unsupported claims**: if a
   load-bearing technical claim is stated as fact without adequate grounding, guard
   asks the assistant to ground it (or flag it as unverified). Second, **unjustified
   deferrals**: if the assistant punts on something the code would answer — "open
   question", "TBD", "deferred", "needs investigation", "결정 안 됨" — guard sends it
   back to read the code and resolve it. Genuine product/policy decisions that need
   you are left alone. By default the review runs **on demand** — you run
   [`/guard:audit`](#review-modes) when you want the last turn checked, so ordinary
   turns cost nothing extra. You can switch to a mode that reviews every turn: an
   in-session `guardian` subagent you can watch, or a separate headless check that
   blocks the turn (either adds latency and model usage per turn).

3. **Approval gate** — guard blocks the file-editing tools (Write/Edit/MultiEdit/
   NotebookEdit) until you have given an explicit instruction to implement, in your
   own words. Discussion, planning, and questions never count as approval — only
   your message can grant it. Shell commands, reads, and searches are never blocked.

Both the evidence judge and the approval gate are governed by one on/off switch
(on by default), toggled per session with the `turn` skill (see below).

guard also keeps a per-session record of the conversation and its review results
inside your project (see [Logs](#logs)).

## Requirements

- Claude Code with the `claude` CLI available on your `PATH` (guard's evidence
  review runs a separate, read-only `claude` check).

## Install

Install from the studykit marketplace, then enable the plugin:

```
/plugin marketplace add studykit/studykit-plugins
/plugin install guard
```

### The output style

The Grounded output style is applied **automatically while guard is enabled**
— you do not need to select it. Because guard forces this style, it takes
precedence over any other output style you have chosen (built-in or custom) for as
long as the plugin is enabled. Disable the plugin to return to your own output
style.

## Usage

### Turn guard on or off

guard is **on by default**. A single switch controls both the evidence judge and
the approval gate together. Toggle it per session with the `turn` skill:

```
/guard:turn on      # enable guard for this session
/guard:turn off     # disable both checks (the conversation log is still kept)
/guard:turn         # report the current state
```

Add `--project` to set the session-start default instead of the current session — e.g.
`/guard:turn --project off` writes `enabled: false` to `.claude/guard.local.json`
without changing this session. `--global` is reserved for a future user-level default.

### Review modes

By default guard reviews **on demand** — nothing runs automatically when a turn ends.
When you want the last completed turn checked, run:

```
/guard:audit            # audit the last completed turn now
```

guard dispatches the `guardian` subagent to review that turn and report anything it
finds. Nothing is checked until you ask, so ordinary turns cost nothing extra.

If you'd rather have every turn reviewed automatically, switch the mode per session with
the `mode` skill:

```
/guard:mode manual       # on-demand only, via /guard:audit (default)
/guard:mode subagent     # dispatch the guardian subagent to review every turn in-session
/guard:mode headless     # in-hook review that blocks each turn
/guard:mode              # report the current mode
```

- **manual** (default) — no automatic review; run `/guard:audit` when you want one.
- **subagent** — guard asks the assistant to dispatch a `guardian` subagent that reviews
  each finished turn in your session (so you can see it), reports anything it finds for
  the assistant to fix, and remembers the facts that passed. It does not block; it runs
  on the `guardian` agent's own model (Haiku by default).
- **headless** — the review runs as a separate, hidden `claude` check and **blocks** the
  turn until unsupported claims are grounded or resolvable deferrals are resolved.

All modes apply the same checks, and `/guard:audit` works in any mode. Set the
session-start default with the `mode` key in configuration (below), or interactively
with `/guard:mode --project <mode>` (writes the default without changing the current
session). `--global` is reserved for a future user-level default.

### The approval gate

While guard is on and a task is still under discussion, any attempt to change files
is denied with a note asking for a plan and your approval. Approve by saying so in
your own words — for example "go ahead", "implement it", or "apply the change".
guard reads your message together with the recent conversation, so a short
"go ahead" counts when it clearly accepts a proposed plan — and doesn't when it
refers to something else.
Approving a **plan in plan mode** also counts as approval — as long as the plan leaves
no in-scope work deferred (no "TBD", "later", or unresolved either/or choices). Approve
a plan that still defers work and the gate stays closed until you approve in your own
words, so you are never handed the keys on a half-finished plan.

Approval sticks with the current task: questions, refinements, corrections, and
follow-ups on the same work keep it in place. The gate only re-locks when you clearly
move on to a different, unrelated task — at which point you approve that one afresh.

The gate only guards your **tracked project source**. Writes elsewhere are never
blocked — anything outside your project directory (such as scratch files under the
temp dir), and git-ignored paths inside it: scratch and temp files, local config
(`*.local.*`), and skill-authored output such as a handoff document written to an
ignored `.handover/`. (guard's own config and state are the one exception: they stay
protected even though they're git-ignored, so nothing can quietly disable the guard.)

## Configuration

Configuration is optional. Create `.claude/guard.local.json` in your project:

```json
{
  "model": "haiku",
  "effort": "medium",
  "enabled": true,
  "mode": "manual",
  "exempt_skills": ["deep-research", "hindsight:review"]
}
```

| Key | Meaning | Default |
| --- | --- | --- |
| `model` | Model the **headless** review runs on | `"haiku"` |
| `effort` | **Headless** review reasoning effort (`low`/`medium`/`high`/`xhigh`/`max`) | `"medium"` |
| `enabled` | Session-start default for guard (evidence judge + approval gate) | `true` |
| `mode` | Session-start review mode (`manual`/`subagent`/`headless`, see [Review modes](#review-modes)) | `"manual"` |
| `exempt_skills` | Skills / slash commands whose turn the review skips, named `plugin:skill` (leading `/` and case ignored) | `[]` |

`model` and `effort` apply to the **headless** review only; the **subagent** review
runs on the `guardian` agent's own model and effort (Haiku / medium by default, set in
the agent definition). The evidence review always reads your repository to verify cited
claims. A `guard.local.json.example` file ships with the plugin as a
starting point.

Use `exempt_skills` for skills or slash commands whose output is a report or a relay
rather than claims about your codebase (e.g. a research skill) — guard won't review the
turn they run in. List each by the name you invoke after the slash, **including its
plugin namespace**: `hindsight:review`, `guard:turn`, or a bare name for an
un-namespaced skill like `deep-research`. guard's own `/guard:turn`, `/guard:mode`, and
`/guard:audit` are always exempt.

You don't have to edit the file by hand. Run `/guard:exempt` and guard shows the
skills available in your session, lets you pick which to exempt, and records your
choice into `exempt_skills` for you:

```
/guard:exempt                 # pick from the list interactively
/guard:exempt hindsight:review  # start with a skill already in mind
```

## Logs

guard keeps records under `.claude/guard/` in your project: a full session
archive, one file per turn (your request, the commands run, and the response), and
a store of facts that passed review (each with its evidence). Facts verified in
earlier turns are reused as established evidence when reviewing later turns, so the
same thing isn't re-checked repeatedly. Add `.claude/guard/` to your `.gitignore`.
