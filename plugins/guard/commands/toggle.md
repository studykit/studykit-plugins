---
name: toggle
description: 'Arm or mute guard''s automatic audit for this session only — a session starts muted, so `/guard:toggle on` is what arms it; `/guard:toggle off` mutes it again and a bare `/guard:toggle` flips. Use when you want this stretch of work audited, or when audits have become noise. The project''s own settings in guard.local.json are never touched. Claude Code only.'
argument-hint: '[on|off]'
context: fork
model: haiku
disable-model-invocation: true
---

A guard hook has already done this — it flipped the session flag and printed the resulting
state above.

**Relay that line to the user and stop.** One line. Do not run anything, do not read guard's
state files, and do not explain the mechanism unless asked.

What it changed, for your own understanding: guard's automatic audit is armed or muted for
**this session only**. Nothing was written to `.claude/guard.local.json`, so nothing about
the project changed — and because every session STARTS muted, the next one starts muted too
whatever this one ended as. While muted, no audit is recommended when a turn ends and answers
are not written to an answer file — answer normally. The `/guard:*` commands still work if
the user asks for one audit.
