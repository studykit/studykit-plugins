---
name: ext-docs-auditor
description: "Audit this project's saved reference files against what a reference may contain: a trustworthy source named, the content attributed rather than recalled, and nothing in them about this repository. guard dispatches the ext-docs-auditor subagent, which judges the files in a fresh context and reports. It edits nothing. Claude Code only."
argument-hint: '[file | directory] …'
disable-model-invocation: true
allowed-tools: Agent, Bash, Glob, Read
---

# Reference audit

The work goes to the `guard:ext-docs-auditor` subagent in a **fresh context**, and the separation
is not a formality. The person who saved a reference is the one person who cannot see what
went wrong with it: they know which sentences they added and which they copied, so the file
reads as a faithful excerpt to them and as a mix of excerpt and local reasoning to everyone
else. If you fetched or edited any of these files earlier in the session, you are the least
reliable judge of them.

## Which files

With **no argument**, audit the whole refs directory. Resolve it first:

```
!`"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" refs-dir`
```

`Glob` it for `*.md` and say how many files you found before dispatching. If the directory
does not exist or holds nothing, say so and stop.

With **file or directory arguments**, take exactly those.

A directory of references is audited **as one dispatch**, not one per file: the auditor's
axis 5 is whether two files now cover the same subject, and that judgment needs them side by
side. Above roughly 25 files, say how many you found and ask whether to narrow — past that
the auditor is reading more than it can hold and the report stops being specific.

## Dispatch the auditor

Dispatch `guard:ext-docs-auditor` with the Agent tool. Give it:

- the explicit list of files to audit;
- any instruction the user attached to the invocation ("only the project-content check",
  "skip the attribution findings"), passed through verbatim;
- nothing else. Do not summarize a file, pre-judge a section, or say what you expect it to
  find — that is the bias the fresh context exists to avoid.

## Relay the result

The auditor changes nothing, so every finding is still a decision. Report what it found,
grouped by file as it grouped them, quoting each passage verbatim in its original language.
Then split the findings, because they are not the same kind of work:

- **What you can fix now** — a section heading that labels general observations as this
  project's notes, a missing `Retrieved:` date, an absent index row, a duplicate row. These
  move no content and lose nothing. Make them, and say what you changed.
- **What needs a decision** — a passage that is genuinely about this repository. The fix is
  to move it somewhere, the auditor names where, and if that document does not exist yet,
  creating it is a change the user has not asked for. Name the finding and the destination
  and leave it.
- **What needs a fetch** — an assertion the file does not attribute to its source. Do not
  repair it from memory; that is the failure being reported. Say that confirming it means
  re-fetching the page, and leave it unless the user asks.

If the auditor reports a finding as **arguable**, relay it as arguable and say why it is
close. Do not promote it to a violation to make the report look decisive, and do not quietly
drop it either.

A clean audit is one line. For a directory of faithful excerpts that is the expected result,
not a sign the audit failed.
