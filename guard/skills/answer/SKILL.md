---
name: answer
# Not in any session's standing context — see `disable-model-invocation` below — so this line
# is read by a person choosing it from autocomplete and can simply say what it does.
description: Answer a question as a document, audited before you see it. Writes the answer to a file, runs the audits that have material in it, applies what they find, and hands you the finished file.
argument-hint: '<question>'
# A NAMED argument, not `$ARGUMENTS`: the question is the whole input and an empty one has to
# read as empty rather than leaving `$0` in the body as literal text.
arguments: question
# The user's, and only the user's. An ordinary turn writes no file at all, and this is the
# entry that changes that — left model-invocable, its description would sit in every session's
# context inviting the model to turn ordinary questions into documents on its own initiative,
# which is the exact complaint this whole lane was built to fix.
disable-model-invocation: true
---

# Answer as an audited document

The user wants this question answered as a **document they can keep**, checked before they
read it. Run every step below, in this order, and do not report back until step 7.

Dispatching an agent hands control back and you are re-entered when it reports; that is the
normal shape here and not a stopping point. What must hold is that the user sees the document
once, audited — never a draft, never a progress note standing in for the deliverable.

Do not run this shape for anything else. An ordinary reply stays an ordinary reply.

## 1. Open the file first

Write the answer to `.claude/answers/<YYYY-MM-DD>-<short-slug>.md`, relative to the project
root. Create the directory if it is not there. The slug is three or four words from the
question, lowercase and hyphenated.

The date prefix is not decoration: it keeps the directory sorted, and it makes it impossible
for an answer to land on a filename that means something else to another tool.

If a file of that name already exists, add `-2`, `-3` and so on. Never overwrite one — an
earlier answer is a document the user may still be holding.

## 2. Write the answer, in ENGLISH

The file **is** the answer, not a record of one. Write the whole substance there: what you
found, what it means, what you recommend, what you are unsure of.

English, whatever language the user writes to you in. A translation comes later in this
procedure and it is written by an agent whose whole job that is; your own prose at document
length in another language is not what this produces.

**Cite as you go, not afterwards.** The audit in step 4 requires a claim about how anything
outside this repository behaves to point at a saved local copy of the source, so dispatch
`guard:docs-finder` (subagent_type: `"guard:docs-finder"`) while you are drafting, whenever you
are about to state a behaviour you did not read this turn. Finding the document after the draft
is written means writing the citation twice.

Claims about this repository are settled by the code. Read it and cite what you read.

## 3. Decide which audits to run

Run `guard-candidates --doc`; it is on your `PATH`. Each line it prints is one available audit
as `entry=mode`. If it prints nothing, or says the session is muted, stop and tell the user —
do not audit around it and do not guess at a roster.

**`--doc` is not optional.** Bare, the command answers for the turn path and names the
`audit-turn-*` entries; what you are auditing is a document, and those entries would send the
audits looking for a turn that does not exist. The entries it prints with `--doc` are the ones
to invoke, exactly as printed.

`korean-translator` appears in that list and is **not** an audit. Skip it here and in step 4 —
step 6 dispatches it, after the corrections are in, which is the only order that does not hand
the user a translation of text the audits were about to change.

You are the party that just wrote the text, so you know things a fresh reader could not
recover from it: which claims came from a document you actually opened this turn, which came
from recollection, which judgment you passed over without saying so. Use that.

**Ask which audits you can rule OUT, with a reason — not which are worth running.** An audit
you cannot rule out, runs. Silence includes it.

The direction matters because of who is asking. A fresh router may answer "nothing here needs
checking" and often should; you are the author, and the same answer from you is the one party
with a reason to want it. So the burden sits on exclusion: name the audit, name what is absent
from the document that it needs, and only then drop it. If you cannot write that sentence
honestly, the audit runs.

A document of any substance will usually run all of them. That is the expected outcome, not a
failure to triage.

## 4. Run them, together

Invoke each surviving audit as a SKILL, by the entry name `guard-candidates --doc` printed for
it, prefixed with `guard:` — passing the answer file's absolute path and nothing else. No
instructions of your own about what to look for: the criteria are each agent's own, and a hint
from you is the author steering the audit.

The document-path entries are the right ones and not an approximation. What you wrote is read
later by someone who was not in this conversation, so a claim with no evidence *in the text* is
a defect however you happened to verify it — crediting this turn's tool activity would let an
under-evidenced document ship.

Dispatch them **concurrently, in one message**, and change nothing until every one has
reported. They read the same file and none of them writes it, so they wait for nothing; you
wait for all of them, so that two findings on the same sentence become one correction rather
than a correction and a patch.

## 5. Apply what they found

Fix each finding where it is written, in the English, with `Edit`. Some ask you to **add**
rather than correct — a definition, an example, a paragraph that was cut — and those go in the
same way.

A finding you are leaving unfixed stays unfixed on purpose and is named in your reply.

A report that says the reader profile is MISSING is telling the user something, not you: relay
it in one line, once.

Then run ONE more round: dispatch again, concurrently, exactly those audits whose findings you
actually applied — an audit you changed nothing for is finished — and apply that round the same
way. Stop there. A correction is prose no audit has read, which is why there is a second round;
the second round's corrections are the same by the same argument, which is why there is no
third.

## 6. Translate, if the user does not read English

The document is English and the user asked for a deliverable. If you are answering them in
another language, they cannot read what you just produced, so the translation is part of
finishing this — not a separate request.

Dispatch `korean-translator` (subagent_type: `"korean-translator"`) with two inputs and nothing
else: the answer file as its source, and the same path with `.ko` before the extension as the
file it writes. It may not derive its own target, so that path has to arrive from you. Give it
no history, no repository paths, and no draft of your own to fix.

**The name carries no `guard:` prefix because the agent is not guard's.** It is a user-level
definition, installed once for every project on the machine, which is why the same two agents
serve translations that have nothing to do with this skill. If no agent of that name exists in
this session, stop here: hand over the English file and say in one line that the translator is
not installed. Do not translate a document of this length yourself — that is the outcome step 2
already refused, arrived at from the other end.

Then do what its report tells you.

The order is deliberate. The translation is made from the corrected English, once — nothing
here hands the user a document and then invalidates it.

## 7. Hand it over

Reply in the user's language: one line saying it is done, the path, and what the audits changed
— a line or two per finding, with your reason for running that audit alongside what it found. A
clean audit is one line.

Do not paste the file and do not summarise its contents: a digest in the reply is the document
delivered twice, and the second copy is the one nobody can correct.

Then open it, once: `open <path>` on macOS, `xdg-open` on Linux, `start` on Windows. Open the
file the user reads — the translation when there is one, the answer file otherwise.
