---
name: audit-turn
# The autocomplete label, read by a person about to type it. It is not in any session's
# standing context — see `disable-model-invocation` below — so unlike the `audit-turn-*`
# descriptions it has nothing to deter and can simply say what the command does.
description: Audit the assistant turn that just finished — triage it and run the audits that have material in it. Takes a turn id; with none, audits the turn guard recorded last.
argument-hint: '[turn id]'
# A NAMED argument, not `$ARGUMENTS`: an omitted named argument expands to the empty string
# while an omitted `$0` stays in the body as literal text, and omitting it is the normal case
# here (`wiki/ref/claude-code-skill-arguments.md`).
arguments: turn
# The user's, and only the user's, and this is the switch the whole redesign turns on. The turn
# audit was dispatched from the Stop hook on every turn that had an answer file, and the common
# result was a router reporting that there was nothing in the turn. Moving the trigger to the
# user is only half of that fix: left model-invocable, this description would sit in every
# session's context inviting the model to audit turns on its own initiative, which is the same
# unasked audit arriving by a different door. Disabled, it also keeps its own description out of
# that context, so the entry point costs nothing on a turn nobody audits.
#
# The three `audit-turn-*` skills stay model-invocable, and must: the router names them for the
# CALLER to invoke, so blocking that would break the only path that dispatches them. What keeps
# THEM from being chosen unasked is their own descriptions, which say nothing about what they
# audit.
disable-model-invocation: true
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). `turn-router.md` holds the triage method and
# the report templates, which are the same every time; this file holds only how to reach the
# turn it is triaging.
context: fork
agent: guard:turn-router
# `false`, against the default, and this is the one entry point where that matters: the report
# IS the next instruction, so the caller has to have it in the turn it asked for the audit in. A
# backgrounded router would hand the user's request back to them and deliver the routing later
# as a notification. It also keeps the full tool set, which a backgrounded fork does not get.
background: false
---

# Triage the turn that just finished

Report which audits are worth running on one finished assistant turn, by the method and in the
format your own definition specifies. It governs; this file only tells you how to reach the
turn.

## The turn

The turn id is `$turn`, and it is normally empty — the user asks about the turn they just
read rather than naming one. Run `guard-inputs $turn`; it is on your `PATH`.

With an id it resolves that turn. With nothing it resolves **the last turn guard recorded**,
which is the one the user means. Either way its first line is `turn: <id>`, and that id — not
the argument you were handed — is the one you put in your report: your caller passes it to
every audit you name, and an audit invoked with an empty id resolves a turn of its own.

Everything else you need is in that same output, as your definition describes.

## Then triage

If `guard-inputs` fails, prints no answer file, or the answer file is empty, say so in one line
and pick nothing — do not go looking for guard's files yourself.

Otherwise triage and report. Nothing is audited because it was asked for: the user asking is
what makes the triage happen, not what makes a pick material, and `none` is a correct and
frequent answer here too.
