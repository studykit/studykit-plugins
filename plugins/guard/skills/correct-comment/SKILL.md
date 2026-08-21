---
name: audit-comment
description: "Audit source-code comments in the given files and fix what the audit finds: comments that only restate what the code already says, comments whose claims are false, and places where non-obvious intent or a hazard is left unrecorded. guard dispatches the comment-auditor subagent to judge the comments in a fresh context, then applies the findings. Requires a file or directory argument. Claude Code only."
argument-hint: '<file | directory> [more paths…]'
disable-model-invocation: true
allowed-tools: Agent, Bash, Glob, Read, Edit
---

# Comment Audit

Two phases: a subagent judges, then you fix.

The judging goes to the `guard:comment-auditor` subagent in a **fresh context**, and that
separation is the point. A comment's author cannot judge whether it was needed: the intent
is still in their head, so the comment reads as informative to them and as noise to
everyone else. If you wrote these comments earlier in the session, you are the least
reliable judge of them. A reader arriving cold is the only fair one.

## Arguments are required

This skill takes paths. With no argument, **ask which files to audit and stop** — do not
guess, and do not fall back to the diff or to files you touched this session. Auditing
the wrong files wastes a subagent and reports findings the user did not ask about.

A directory argument means the source files under it. Expand it yourself (Glob, or `git
ls-files`) and pass the resulting file list, so the subagent spends its context reading
code rather than hunting for it. Skip vendored, generated, and minified files. If the
expansion is large — more than roughly 20 files — say how many you found and ask whether
to narrow before dispatching.

## Phase 1 — dispatch the auditor

Dispatch `guard:comment-auditor` with the Agent tool. Give it:

- the explicit list of files to audit;
- any instruction the user attached to the invocation (e.g. "only the new comments",
  "Python only"), passed through verbatim;
- nothing else. Do not summarize the files, pre-judge any comment, or tell the auditor
  what you think it will find — that is the bias the fresh context exists to avoid.

For many files, dispatch several auditors in parallel with disjoint file lists, in one
message. Keep each list small enough that the auditor can read every file in full; it
cannot judge a comment without the code under it.

## Phase 2 — apply the findings

Report what the auditor found first, grouped as it grouped them, with each comment quoted
verbatim in its original language and the counts it reported. Then fix them, in the
auditor's own order — wrong comments first, because those are the ones actively misleading
a reader.

How to fix each kind:

- **Wrong** — correct the claim to what the code actually does. Never delete a wrong
  comment that was load-bearing: it is recording something real, so the fix is to make it
  true. When the comment was right about the *intent* and the code is what broke the
  invariant, the honest comment edit leaves a correct comment describing a live defect —
  so **you must tell the user about that defect explicitly**, not just leave the comment
  and move on. Fixing the code is a separate change they have not asked for; leaving them
  unaware of it is not an option.
- **Restates the code / the name / section labels** — delete. Do not rewrite a redundant
  comment into a better one; if the code already says it, nothing needs to say it again.
- **Vacuous** — delete, or replace with the fact it was gesturing at when you can state
  that fact concretely.
- **Missing** — write the comment. State the reason, constraint, or hazard, and nothing
  the code already shows. If you cannot establish the *why* from the code and repository,
  do not invent one: report that gap to the user and leave it unwritten. A fabricated
  rationale is worse than an absent one. When the finding is a gap the auditor reached
  through a vacuous marker (a bare `# TODO` over a stub), the marker is still vacuous —
  delete it if you can write the real comment, and leave it only when you cannot, since a
  bare marker at least tells the next reader that something is unfinished.

Two limits on this phase. **Comments only** — never change code, tests, or behavior to
satisfy a comment. And when a finding is one you disagree with, say so in one line and
leave that comment alone rather than applying a change you think is wrong; the auditor
judges, but it is not infallible.

Group the edits by file so the user reviews one coherent diff per file. The edits are
normal file edits: they go through whatever approval the project requires, like any other
change.

Close by listing what you fixed, what you left alone, and why — a one-liner each, not a
second report.

If the auditor reports nothing, relay that in one line and make no edits. A clean result
is the expected outcome for a well-commented file, not a sign the audit failed.
