---
name: audit-report-clarity
# Extremely short — see `audit-turn-claims` for why. guard's router names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<path to the document>'
context: fork
agent: guard:clarity-auditor
# `true`, the default, stated — see `audit-turn-clarity`: the audits are dispatched together and
# nothing is applied until they have all reported, so blocking would buy no ordering.
background: true
---

# Gather the inputs for a document, then audit it

Your subject is one standalone document — a brief, a research write-up, a design note. This
file tells you where its parts are; what makes an explanation followable is in your own
definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get
what you need.

## 1. Resolve the path

The document is at `$ARGUMENTS`. Run `guard-inputs --file $ARGUMENTS`; it is on your `PATH`.
It prints the resolved path, and use that rather than the one you were handed.

If it says there is no file at that path, say so in one line and stop. Do not go looking for
the document elsewhere, and do not audit the path itself as though it were the text.

It may also print a `knowledge dir` line. **That is not your input** — skip it.

If you were given no path at all, say that and stop.

## 2. There is no history, and that is the shape rather than a gap

`guard-inputs --file` prints no transcript and no turn id, deliberately: the document was not
written in a turn of the session that dispatched you. So the question this audit asks on the
turn path — "was this term already explained earlier in the conversation?" — has no
conversation to ask it of.

**Do not go looking for a transcript, and do not treat its absence as an extraction failure.**
Do not ask the main session what was already explained: it did not write this document and was
not present when it was written, so its answer is not the author's testimony but a third party
recalling something it never saw. The one thing worth asking it is *where to look* when a
reference in the document is ambiguous — then look yourself.

What replaces the history is the document. It was written to be read by someone who was not
there, so **everything its reader needs must be in it.** A term explained nowhere in the file
is unexplained, full stop — there is no earlier turn that could have covered it, and no credit
for context the reader does not have.

## 3. Triage

Read the document. If nothing in it could make a reader stuck — a bare list, a record of what
was said, a set of paths — report `verdict: pass` and stop here without opening the
repository.

The bar is low and this kind of document usually clears it: a document that explains, compares,
or walks through how something works is exactly the material this audit is for.

## 4. The repository

The working directory you were launched in. It settles one question and only one: whether a
name in the document is a real identifier the reader can go open, or a term the document
coined and owes an explanation for.

## Then audit

Against your reader profile, by the criteria in your definition.

**One caution about the profile on this path.** It describes the person your session talks to.
A document is read later, possibly by someone else, so where a finding turns on the reader's
own vocabulary rather than on the text, say which reader you judged it for. Do not invent a
second reader to judge against — report what you calibrated on and let the caller weigh it.

Report in the block your definition specifies, and change nothing but your own memory.
