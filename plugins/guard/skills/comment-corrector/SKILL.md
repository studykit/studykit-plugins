---
name: comment-corrector
description: "Audit source-code comments in the given files and fix what the audit finds: comments that only restate what the code already says, comments whose claims are false, and places where non-obvious intent or a hazard is left unrecorded. guard dispatches the comment-corrector subagent, which judges the comments in a fresh context and applies the fixes in place. Requires a file or directory argument. Claude Code only."
argument-hint: '<file | directory> [more paths…]'
disable-model-invocation: true
allowed-tools: Agent, Bash, Glob, Read
---

# Comment Audit

The work goes to the `guard:comment-corrector` subagent in a **fresh context**, and that
separation is the point. A comment's author cannot judge whether it was needed: the intent
is still in their head, so the comment reads as informative to them and as noise to
everyone else. If you wrote these comments earlier in the session, you are the least
reliable judge of them. A reader arriving cold is the only fair one.

That is also why you do not fix the comments yourself. The corrector judges and edits in
one pass, so the fix is made by the same cold reader that found the problem — not by the
author reinterpreting a finding.

## Arguments are required

This skill takes paths. With no argument, **ask which files to audit and stop** — do not
guess, and do not fall back to the diff or to files you touched this session. Auditing
the wrong files wastes a subagent and edits files the user did not ask about.

A directory argument means the source files under it. Expand it yourself (Glob, or `git
ls-files`) and pass the resulting file list, so the subagent spends its context reading
code rather than hunting for it. Skip vendored, generated, and minified files. If the
expansion is large — more than roughly 20 files — say how many you found and ask whether
to narrow before dispatching.

## Dispatch the corrector

Dispatch `guard:comment-corrector` with the Agent tool. Give it:

- the explicit list of files to fix;
- any instruction the user attached to the invocation (e.g. "only the new comments",
  "Python only"), passed through verbatim;
- nothing else. Do not summarize the files, pre-judge any comment, or tell the corrector
  what you think it will find — that is the bias the fresh context exists to avoid.

For many files, dispatch several correctors in parallel with disjoint file lists, in one
message. Disjoint matters for more than context: two correctors given the same file would
edit it concurrently. Keep each list small enough that the corrector can read every file
in full; it cannot judge a comment without the code under it.

## Relay the result

The edits are already in the files when the corrector reports. Your job is to make them
reviewable, not to redo them.

On a large audit the corrector may hand back a **path** to its full report instead of the
report itself, along with the counts, its worst finding, and what it left unfixed. That is
the intended shape — open the file if you need a detail, but relay from what it gave you
rather than pasting the whole report through.

Report what it found and what it changed, grouped as it grouped them, with each comment
quoted verbatim in its original language and the counts it reported. Then, separately and
plainly, **the items it did not fix** — a comment it judged wrong but could not repair, a
gap whose *why* it could not establish, a file it could not read in full. Those need the
user's attention and must not read as done.

One case deserves its own line in your summary, because it is the finding most easily lost:
when the corrector reports that a comment was right about the intent and the **code** is
what broke the invariant, say so explicitly as a live defect. The corrector deliberately
leaves such a comment alone rather than editing it into a description of a bug. Fixing the
code is a separate change the user has not asked for — but leaving them unaware of it is
not an option.

Do not re-edit the corrector's work. If you disagree with an edit it made, say which one
and why in one line and leave it to the user; they are reviewing the diff. Reverting it
yourself would put the author's judgment back in charge of the thing the fresh context was
meant to decide.

If the corrector reports nothing, relay that in one line. A clean result is the expected
outcome for a well-commented file, not a sign the audit failed.
