---
name: toggle
description: 'Arm or mute guard''s automatic audit for this session only — a session starts muted, so `/guard:toggle on` is what arms it; `/guard:toggle off` mutes it again and a bare `/guard:toggle` flips. Use when you want this stretch of work audited, or when audits have become noise. The project''s own settings in guard.local.json are never touched. Claude Code only.'
argument-hint: '[on|off]'
disable-model-invocation: true
# This body never runs. guard's UserPromptExpansion hook does the whole job and then blocks
# the expansion, which ends the turn and shows its own message to the user — so no model is
# invoked, here or in a fork. The file exists because the host resolves `/name` against the
# command files BEFORE any hook runs: delete it and the matcher is silently disarmed, with
# `Unknown command` as the only symptom. See
# wiki/ref/claude-code-userpromptexpansion-needs-a-command-file.md.
#
# Deliberately NOT `context: fork`, unlike /guard:settings and /guard:statusline. A fork is
# the cheap way to run a body that must run — it avoids re-paying for the main session's
# accumulated context. There is no body to run here, so a fork would only add a cold agent
# spawn to relay a sentence the hook had already finished.
---

Arm or mute guard's automatic audit for this session. Handled entirely by guard's
`UserPromptExpansion` hook, which flips the session flag and reports the result itself.

Session state only — `.claude/guard.local.json` is never touched, so the project's own
settings are unchanged and every other session is unaffected. A session always starts
muted, so `on` is the arming direction; what this one ends as does not carry into the next.

While muted, guard recommends nothing when a turn ends and answers are not written to an
answer file. `/guard:settings` is where an agent is switched on for the project.
