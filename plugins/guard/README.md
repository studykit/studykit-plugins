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

2. **Evidence judge** — reviews a finished response on two axes, reading your
   repository to check. First, **unsupported claims**: if a
   load-bearing technical claim is stated as fact without adequate grounding, guard
   asks the assistant to ground it (or flag it as unverified). Second, **unjustified
   deferrals**: if the assistant punts on something the code would answer — "open
   question", "TBD", "deferred", "needs investigation", "결정 안 됨" — guard sends it
   back to read the code and resolve it. Genuine product/policy decisions that need
   you are left alone. By default the review runs **on demand** — you run
   [`/guard:judge`](#review-modes) when you want the last turn checked, so ordinary
   turns cost nothing extra. You can switch to a mode that reviews every turn: an
   in-session `guardian` subagent you can watch, or a separate headless check that
   blocks the turn (either adds latency and model usage per turn).

3. **Approval gate** — guard holds back the file-editing tools (Write/Edit/MultiEdit/
   NotebookEdit) until you approve the work. By default it asks you to approve the edit
   right when it happens, through Claude Code's own permission prompt; approving once
   opens the gate for the rest of that task. (You can switch to a stricter setting that
   blocks the edit outright until you approve in a message — see `edit_gate` below.)
   Discussion, planning, and questions never approve on their own. Shell commands,
   reads, and searches are never blocked.

The two checks are controlled independently, and both are set from one command,
`/guard:settings`: the approval gate is one setting (`edit_gate` — `ask` by default,
`deny` for the stricter workflow, or `off` to disable it), and the evidence judge is
governed by `judge_gate` — `manual` (the default) runs nothing automatically, so it is
the judge's practical off (see below).

guard also keeps a per-session record of the conversation and its review results
inside your project (see [Logs](#logs)).

## Requirements

- Claude Code with the `claude` CLI available on your `PATH` (guard's evidence
  review runs a separate, read-only `claude` check).
- Python 3.11 or newer on your `PATH` as `python3` (guard's hook dispatcher runs
  directly via its shebang).

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

guard exposes two commands:

- **`/guard:settings`** — view and change guard's settings for this project.
- **`/guard:judge`** — judge the last completed turn on demand.

### Configure guard

Run `/guard:settings` to see guard's current settings and change any of them. With no
arguments it shows the settings and lets you pick what to change; you can also name a
setting and value directly:

```
/guard:settings                     # show settings, then pick what to change
/guard:settings edit_gate off       # turn the approval gate off
/guard:settings edit_gate deny      # block unapproved edits instead of prompting
/guard:settings judge_gate headless # switch the evidence judge to headless
```

The settings it manages:

| Setting | Values | What it controls |
| --- | --- | --- |
| `edit_gate` | `ask` / `deny` / `off` | The approval gate (below). `off` disables it; `ask` (default) prompts you to approve an unapproved edit inline; `deny` blocks it. |
| `judge_gate` | `manual` / `subagent` / `headless` | How the evidence judge runs (below). `manual` by default. |
| `model` | a model name | Model the **headless** judge runs on. |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` | **Headless** judge reasoning effort. |
| `refs_dir` | a path, or empty | Where cited-doc copies are saved (see [Configuration](#configuration)). |
| `exempt_skills` | skill / command names | Skills whose turn the judge skips (see [Configuration](#configuration)). |

Changes take effect immediately and persist as the project default in
`.claude/guard.local.json` — `edit_gate` and `judge_gate` also switch the current session,
so you don't have to restart. `/guard:settings` is the only supported way to change these:
guard blocks direct writes to its own config, so nothing but your own action through
this command can weaken the guard.

### Review modes

The evidence judge runs in one of three modes, set with `/guard:settings judge_gate <mode>`:

- **manual** (default) — no automatic review; run `/guard:judge` when you want the last
  completed turn checked. Ordinary turns cost nothing extra. Since nothing runs unless
  you ask, this is also how you keep the evidence judge effectively off while the
  approval gate stays on.
- **subagent** — a `guardian` subagent reviews each finished turn in your session (so you
  can see it), reports anything it finds for the assistant to fix, and remembers the
  facts that passed. It does not block; it runs on the `guardian` agent's own model
  (Haiku by default).
- **headless** — the review runs as a separate, hidden `claude` check and **blocks** the
  turn until unsupported claims are grounded or resolvable deferrals are resolved.

All modes apply the same checks. `judge_gate` never affects the approval gate.

### Judge a turn on demand

Whatever the mode, you can review the last completed turn yourself at any time:

```
/guard:judge            # judge the last completed turn now
```

guard dispatches the `guardian` subagent to review that turn and report anything it
finds.

### The approval gate

While the approval gate is on and a task is still under discussion, any attempt to change
files is held back for your approval. How depends on `edit_gate` (below):

- **`ask` (default)** — you get Claude Code's permission prompt for the edit. Approve it
  and the gate opens for the rest of that task; reject it and the gate stays closed. The
  approval is your click on the prompt — the model cannot approve its own edit.
- **`deny`** — the edit is blocked outright with a note asking for a plan and your
  approval in a message, so nothing changes until you say so.

You can also approve in your own words at any time — for example "go ahead", "implement
it", or "apply the change". guard reads your message together with the recent
conversation, so a short "go ahead" counts when it clearly accepts a proposed plan — and
doesn't when it refers to something else.
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
  "edit_gate": "ask",
  "judge_gate": "manual",
  "exempt_skills": ["deep-research", "hindsight:review"],
  "refs_dir": "docs/refs"
}
```

| Key | Meaning | Default |
| --- | --- | --- |
| `model` | Model the **headless** review runs on | `"haiku"` |
| `effort` | **Headless** review reasoning effort (`low`/`medium`/`high`/`xhigh`/`max`) | `"medium"` |
| `edit_gate` | The approval gate (holds back the file-editing tools until you approve): `off` disables it, `ask` prompts you to approve an unapproved edit inline (and opens the gate for the rest of the task), `deny` blocks it until you approve in a message | `"ask"` |
| `judge_gate` | Session-start review mode for the evidence judge (`manual`/`subagent`/`headless`, see [Review modes](#review-modes)) | `"manual"` |
| `exempt_skills` | Skills / slash commands whose turn the review skips, named `plugin:skill` (leading `/` and case ignored) | `[]` |
| `refs_dir` | Project-relative folder where copies of cited official docs are saved. Empty means the git-ignored default `.claude/guard/refs/`; set a tracked path (e.g. `"docs/refs"`) to keep the collected references under git | `""` |

`model` and `effort` apply to the **headless** review only; the **subagent** review
runs on the `guardian` agent's own model and effort (Haiku / medium by default, set in
the agent definition). The evidence review always reads your repository to verify cited
claims. A `guard.local.json.example` file ships with the plugin as a
starting point.

Use `exempt_skills` for skills or slash commands whose output is a report or a relay
rather than claims about your codebase (e.g. a research skill) — guard won't review the
turn they run in. List each by the name you invoke after the slash, **including its
plugin namespace**: `hindsight:review`, or a bare name for an un-namespaced skill like
`deep-research`. guard's own `/guard:settings` and `/guard:judge` are always exempt.

When a response cites official documentation, the Grounded output style saves a
local copy of the cited content into the refs folder so the evidence stays
inspectable, and the review checks that the copy exists. By default that folder
(`.claude/guard/refs/`) is a per-machine cache you git-ignore; set `refs_dir` to a
tracked folder to collect those references in your repository instead — they are
then committed through your normal git workflow (guard never commits anything
itself).

You don't have to edit the file by hand. Run `/guard:settings` and pick `exempt_skills`
to review the current list and record which skills to exempt:

```
/guard:settings                     # then choose exempt_skills from the menu
```

## Logs

guard keeps records under `.claude/guard/` in your project: a full session
archive, one file per turn (your request, the commands run, and the response), and
a store of facts that passed review (each with its evidence). Facts verified in
earlier turns are reused as established evidence when reviewing later turns, so the
same thing isn't re-checked repeatedly. Add `.claude/guard/` to your `.gitignore`.
