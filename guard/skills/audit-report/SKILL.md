---
name: audit-report
# The user's entry to the document path, and the counterpart of `audit-turn`. Both are
# `disable-model-invocation: true`, so this line is NOT in any session's standing context: it
# is the autocomplete label, read by a person who is about to type it, and nothing here has to
# deter a model that cannot reach it.
description: Audit a document — triage the file and run the audits that have material in it. Takes the file's path, and the language its reader reads when that is not English.
argument-hint: '<file path> [reader language]'
# Named arguments: the path is required and the language is optional, and an omitted named
# argument expands to the empty string rather than staying in the body as literal text
# (`wiki/ref/claude-code-skill-arguments.md`).
arguments: file language
# The user's, and only the user's. A document audit costs one router plus a fork per pick, and
# there is no event behind it — nothing produces a document for this path, so the only way it
# can be wanted is that somebody wants it. Left model-invocable, this description would sit in
# every session's context inviting the model to audit any file it happened to write, which is
# the same unasked-audit failure the turn path was rebuilt to remove.
#
# The three `audit-report-*` skills stay model-invocable, and must: the router names them for
# the CALLER to invoke, so blocking that would break the only path that dispatches them.
disable-model-invocation: true
# The agent is the system prompt and this file is the task
# (`wiki/ref/claude-code-skill-fork-context.md`). `report-router.md` holds the triage method
# and the report template; this file holds only what it is pointed at.
context: fork
agent: guard:report-router
# `false`, against the default: the report IS the next instruction, so the caller has to have
# it in the turn it asked for the audit in, and it keeps the full tool set.
background: false
---

# Triage a document

Report which audits are worth running on one document, by the method and in the format your
own definition specifies. It governs; this file only tells you what you are pointed at.

The two input lines your definition describes, as your invocation supplies them:

- file: `$file`
- language: `$language`

`language` is empty when the user named none, and that absence means what your definition says
it means: the document is not being delivered to a reader in another language, so there is
nothing to translate.

If no file was named, say that in one line and stop. Otherwise run `guard-inputs --file $file`
and go on as your definition says — the resolved path it prints is the one your answer carries.

`none` is a correct and frequent answer. The user asking for this audit is what makes the
triage happen; it is not what makes any pick material.
