---
name: toggle
description: 'Mute or unmute guard''s automatic audit for this session only — `/guard:toggle` flips it, `/guard:toggle off` mutes, `/guard:toggle on` restores. Use when audits are noise for the stretch of work you are in. The project''s own settings in guard.local.json are never touched. Claude Code only.'
argument-hint: '[on|off]'
disable-model-invocation: true
---

A guard hook has already done this — it flipped the session flag and printed the resulting
state above.

**Relay that line to the user and stop.** One line. Do not run anything, do not read guard's
state files, and do not explain the mechanism unless asked.

What it changed, for your own understanding: guard's automatic audit is muted or unmuted for
**this session only**. Nothing was written to `.claude/guard.local.json`, so the next session
starts from whatever the project decided. While muted, no audit is recommended when a turn
ends and answers are not written to an answer file — answer normally. The `/guard:*` commands
still work if the user asks for one audit.
