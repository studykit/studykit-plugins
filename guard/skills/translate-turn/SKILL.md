---
name: translate-turn
# The autocomplete label, read by a person about to type it. Like the audit entries, this one
# is not in any session's standing context (`disable-model-invocation` below), so it can say
# plainly what the user is about to run.
description: Write the Korean version of the assistant turn that just finished, from its English answer file. Takes a turn id; with none, translates the turn guard recorded last.
argument-hint: '[turn id]'
# A NAMED argument, not `$ARGUMENTS` — an omitted named argument expands to the empty string
# while an omitted `$0` stays in the body as literal text, and omitting it is the normal case.
arguments: turn
# The user's, and only the user's, for the same reason the audit entries are. Translating ran
# from the turn closeout on every turn that delivered substance, which is a subagent per turn
# spent whether or not anyone was going to read the Korean. Moving the trigger to the user is
# half the fix; keeping the entry out of the model's reach is the other half, since a
# description sitting in every session's context is an invitation to translate unasked.
disable-model-invocation: true
---

# Translate the turn that just finished

## The turn

The turn id is `$turn`, and it is normally empty — the user asks about the turn they just
read rather than naming one. Run `guard-inputs $turn`; it is on your `PATH`.

With an id it resolves that turn. With nothing it resolves **the last turn guard recorded**,
which is the one the user means. Two of its lines are what you need:

- `answer file:` — the English document the turn was delivered as. The source.
- `translation file:` — where the Korean goes. Printed whether or not the file exists yet.

If `guard-inputs` fails, prints no answer file, or the answer file is empty, say so in one
line and stop. Do not go looking for guard's files yourself, and do not translate the reply
you can see in the conversation instead — that reply is a headline, not the answer.

## Then translate

Dispatch `guard:korean-translator` (subagent_type: `"guard:korean-translator"`) with those two
paths and nothing else: the answer file as its source, the translation file as the file it
writes. Give it no history, no repository paths, and no draft of your own to fix — it is not
allowed to derive its own target, so the destination has to arrive from you as a path.

Then do what its report tells you. It hands the translation on to the agent that checks it,
and that agent's report is the one that says the document is finished.

**You do not write any of the Korean yourself**, and you do not review the translator's word
choices — that is what the checking agent is for. Your own Korean at document length is the
arrangement this exists to avoid.

## Then reply

One line, in the user's language, plus the path to the translation. Do not summarise what the
document says and do not paste any of it. Then open it once: `open <path>` on macOS,
`xdg-open` on Linux, `start` on Windows.

If the turn already had a translation, this rewrote it from the English as it now stands —
say so in the same line, since a correction the user made in the meantime is now gone.
