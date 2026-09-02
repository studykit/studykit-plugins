---
name: statusline
description: 'Install guard''s audit indicator into the status line. Copies guard''s wrapper into the user''s own ~/.claude, points `statusLine` at it, and keeps whatever status line was already configured by chaining it. Use when the user wants the guard segment shown, or when it stopped appearing. Claude Code only.'
argument-hint: ''
# Forked for the same reason as `/guard:settings`: wiring one segment is a short exchange,
# but the main session may be carrying a large conversation and re-pays for all of it on
# every turn the exchange takes. `context: fork` does not inherit that conversation, so the
# body and the whole run stay out of it (wiki/ref/claude-code-skill-fork-context.md).
context: fork
model: sonnet
# The documented default, spelled out because this command asks before it writes and the
# background panel is where that asking now happens: `AskUserQuestion` is stripped from
# EVERY subagent, so the agreement below can only be reached in this agent's own transcript,
# which `background: true` is what makes openable. `Edit` and `Write` survive the background
# filter, so the write itself still works.
background: true
disable-model-invocation: true
---

guard cannot install a status line itself — a plugin's `settings.json` honors only `agent`
and `subagentStatusLine`, and the main `statusLine` is a user or project setting. What guard
ships instead is the **wrapper** that setting should point at, and installing it is your job
here: copy the wrapper out of the plugin, point the setting at the copy, and hand the status
line the user already had to the copy as its argument so they keep it.

**The copy is not a detail.** guard lives in a versioned cache directory that every plugin
update relocates, so a `statusLine` naming a path inside the plugin breaks on the next update
with no error anywhere — the row just goes quiet. The installed copy resolves guard at run
time, which is why it survives updates and why this command should not need running twice.

**This writes the user's own settings file.** Show the exact change and get explicit
agreement before touching it. A direct "add it" counts.

You are running in your own background context, so that exchange happens **here**, in this
transcript, which the user opens from the interactive panel — not in the conversation they
invoked you from. Ask in prose and wait; there is no question tool to reach for. If nobody
answers, leave the settings file alone and say what you would have changed.

## 1. Find the pieces

- **guard's wrapper**: `${CLAUDE_PLUGIN_ROOT}/shell/statusline.sh`. That substitution works in
  this body; it must NOT appear in anything you write to the settings file, which the host
  runs as a plain shell command with no plugin variables set.
- **guard's script**, for the probe below: `${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py`.
- **the current setting**: read `statusLine` from `~/.claude/settings.json`, then from
  `.claude/settings.json` and `.claude/settings.local.json` if the user setting is absent.
  Say which file you found it in; that is the one to change.

Check the segment works before proposing anything:

```sh
printf '{"session_id":"probe","workspace":{"project_dir":"<project root>"}}' \
  | "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" status
```

Expect one short field — `guard 3/3 · ⚐`, `guard 0/3 · ⚑`, `guard 0/0 · ⚐` and so on — or
nothing. If it prints nothing for a project with agents switched on,
stop and say so rather than installing a segment that will stay blank.

## 2. Install

Copy the wrapper to `~/.claude/guard-statusline.sh` and `chmod +x` it. Copy it verbatim — it
is a shipped file, not a template to fill in.

**If there is no status line yet**, the wrapper takes no argument and renders a plain default
line of its own (directory, branch, context, model) beside guard's segment:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/guard-statusline.sh"
  }
}
```

**If one already exists, chain it — never replace it.** The existing command string becomes
the wrapper's single argument, and the wrapper feeds it the same JSON on stdin and prints its
output after guard's segment:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/guard-statusline.sh '<the existing command>'"
  }
}
```

Quote it exactly as it was, and mind the quoting if the existing command itself contains
single quotes. Keep every other field of the `statusLine` object (`padding`,
`refreshInterval`) as it was.

**If `~/.claude/guard-statusline.sh` is already installed and the setting already points at
it**, the install is done: refresh the copy from the plugin (it may be newer) and change the
setting only if the chained argument no longer matches what the user wants shown.

## 3. Verify, then report

Run the installed wrapper the way the host will, with a mock payload — a status line that
fails prints nothing, so an unverified install is indistinguishable from a broken one:

```sh
printf '{"session_id":"probe","workspace":{"project_dir":"<project root>","current_dir":"<project root>"},"model":{"display_name":"Opus"},"context_window":{"remaining_percentage":62}}' \
  | ~/.claude/guard-statusline.sh
```

One non-empty line, guard's field first. If the chained command is in play, its output must
still be there too.

Then tell the user three things and stop:

- The fraction is *how many agents can run on the next finished turn* over *how many are
  switched on*: `guard 3/3` with three switched on and the session armed, `guard 0/3` when the
  session is muted, `guard 0/0` when nothing is switched on at all. So `guard on|off` moves
  the numerator for this session and `/guard:settings` moves the denominator — and the
  `audit-turn` setting there is which numerator a new session starts on — `off` unless the
  project changes it, so a new session usually opens on `0/n` until `guard on`.
- The flag is the plan gate, and it is always shown: filled `⚑` means plan audits are armed
  for this session, so an approved plan is held until it has been audited; outline `⚐` means
  they are off. Separate switch, own command — `guard-plan on|off` in a shell for this
  session, or the `audit-plan` setting for what every session starts as.
- Green means armed, dim means muted, on each half independently: a green fraction beside a
  dim flag is a session auditing turns with the plan gate off. Colour is the only difference
  between the two `0/0` states, so a terminal that drops it loses the mute there.
- The row updates on assistant messages, session start, `/compact` and permission-mode
  changes, not on the shell command that flips a switch: after `guard on` or `guard-plan on`
  the segment moves at the next message. If it ever goes blank, that is deliberate — the
  wrapper prints nothing rather than an error, because a status line is the wrong place to
  report a failure.
