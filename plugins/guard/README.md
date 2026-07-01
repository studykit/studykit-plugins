# guard

Keep Claude Code honest about technical claims, and keep it from editing your
project before you have actually approved the work.

**Claude Code only.**

## What it does

guard adds three layers of control over the assistant's responses and actions:

1. **Evidence-first output style** — an output style that requires every technical
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
   you are left alone. The review runs as a separate check, so it adds some latency
   and model usage to each turn.

3. **Approval gate** — guard blocks file-changing actions (Write/Edit and
   workspace-mutating shell commands) until you have given an explicit instruction
   to implement, in your own words. Discussion, planning, and questions never count
   as approval — only your message can grant it. Read-only and search actions are
   never blocked.

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

The evidence-first output style is applied **automatically while guard is enabled**
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

### The approval gate

While guard is on and a task is still under discussion, any attempt to change files
is denied with a note asking for a plan and your approval. Approve by saying so in
your own words — for example "go ahead", "implement it", or "apply the change".
Approval lasts until you steer the conversation to a new or undecided topic, at
which point the gate re-locks.

## Configuration

Configuration is optional. Create `.claude/guard.local.json` in your project:

```json
{
  "model": "haiku",
  "effort": "medium",
  "enabled": true
}
```

| Key | Meaning | Default |
| --- | --- | --- |
| `model` | Model the evidence review runs on | `"haiku"` |
| `effort` | Review reasoning effort (`low`/`medium`/`high`/`xhigh`/`max`) | `"medium"` |
| `enabled` | Session-start default for guard (evidence judge + approval gate) | `true` |

The evidence review always reads your repository to verify cited claims. A
`guard.local.json.example` file ships with the plugin as a starting point.

## Logs

guard keeps a per-session record of the conversation and its review results under
`.claude/guard/` in your project. Add `.claude/guard/` to your `.gitignore`.
