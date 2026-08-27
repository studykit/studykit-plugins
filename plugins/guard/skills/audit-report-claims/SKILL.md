---
name: audit-report-claims
# Extremely short — see `audit-turn-claims` for why. guard's router names this skill and the
# caller invokes it by name, so the description never has to attract anything.
description: Invoked by guard only.
argument-hint: '<path to the document>'
context: fork
agent: guard:claims-auditor
# The default, stated — see `audit-turn-clarity` for why it is not `false`.
background: true
---

# Gather the evidence behind a document, then audit it

Your subject is one standalone document — a brief, a research write-up, a design note. This
file tells you where it is and what counts as evidence on this path; what makes a claim
supported is in your own definition, and it governs.

You have no conversation history — you were forked clean. Everything below is how you get what
you need.

## 1. Resolve the path

The document is at `$ARGUMENTS`. Run `guard-inputs --file $ARGUMENTS`; it is on your `PATH`. It
prints the resolved path, and use that rather than the one you were handed.

If it says there is no file at that path, say so in one line and stop. Do not go looking for the
document elsewhere, and do not audit the path itself as though it were the text.

It may also print a `knowledge dir` line. **That is not your input** — skip it. It points at
where a project records what its *deployed* system looks like, for a different agent.

If you were given no path at all, say that and stop.

## 2. There is no history, and that is the shape rather than a gap

`guard-inputs --file` prints no transcript and no turn id, deliberately: the document was not
written in a turn of the session that dispatched you. So there is no tool activity to credit and
no request to weigh the document against.

**Do not go looking for a transcript, and do not treat its absence as an extraction failure.**
Do not ask the main session what the document says or how it came to say it: it did not write
this document and was not present when it was written, so its account is not the author's
testimony but a third party recalling something it never saw. `SendMessage` it for one thing
only — *where to look* when a reference in the document is ambiguous, which of two candidate
paths a name means. Then look yourself.

**There was no user in front of this text.** A turn is an answer to somebody; a document is
written to be read later by someone who was not there. So you cannot discount a passage as "not
what was asked for", and you should not try.

## 3. Triage narrows what you check; it never ends the audit

Scan the document for its load-bearing claims. The shapes that let a turn pass unread — an
acknowledgement, a question back to the user, a report of an action just taken — do not occur
in a document written to be read later, so **there is no early exit here.** Find the claims,
then go and check them.

**A proposal is the normal case on this path, not an exception.** Expect `The reasoning under a
proposal` to be where most of your findings come from.

## 4. The repository is your only source

The working directory you were launched in. With no activity and no request, **the repository as
it stands now — plus any saved copy under the refs directory — is all that settles a claim.**
Open it.

## 5. Documentation citations: a URL and a quote, not a local copy

This is the ruling your definition defers to the skill. Here the standard is a source that
identifies itself — a URL plus a verbatim quote of the deciding passage — and a quote that
actually supports the claim.

A local saved copy under the refs directory is **better**: use it when one exists, and say so.
But **its absence is not a finding on this path.** The parties who write the documents you audit
here were never told to save one, so requiring it would fail every citation rather than find a
defect. A documentation claim with no source at all is unsupported exactly as any other uncited
claim would be.

## Then audit

By the criteria in your definition. Report in the block it specifies, and change nothing but
your own memory.
