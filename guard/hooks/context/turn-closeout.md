# guard turn closeout

Two different things happen here and they must not be confused. **Delivering the turn** happens
on every turn that has an answer file, and it is short. **Applying an audit** happens only when
the user asked for one, which is rare, and the router's report is what drives it.

**Nothing here is about any one audit** — how to dispatch it, what its inputs are, and what its
findings mean all travel with the dispatch: the router's report for the audits it picked, and
guard's Stop hook for the file-reading agents it names directly. The one agent this file does
name is the translator, and only because the decision to run it is the caller's rather than any
report's.

## The answer file

The **answer file** is where this turn's substance lives, **written in English** whatever
language the user reads. You wrote it during the turn; the reply you gave was short and named
this path. It is not a copy of something already delivered — it is the deliverable.

Do not paste its contents into a reply. **Summarising it is the same failure in a shorter
form** — a bulleted digest, or a preview of how it opens, puts the answer in the transcript a
second time just as effectively as quoting it, and it passes for brevity while doing so. If you
find the file empty or missing, guard filled it in from the response after the fact and said so
in a comment at the top; treat it as the answer anyway, and write it properly next time.

Everything around it is English too — what you write in a dispatch, what an agent reports back,
what one agent says to another. Never relay an agent's English report to the user untranslated:
what changed goes in the answer file, and the reply is in the user's language.

**You never write the user's language yourself.** The translation is written by the translator,
from the English, and dispatching it is yours — see below. Your own Korean, or any other
language you produce directly, is the arrangement that produced 직역.

**You never gather the session's history.** It is in the transcript, and an agent that needs it
resolves and extracts it itself. If one fails to — the file is gone, a compaction dropped the
range — it may `SendMessage` you and ask; answer it with the **raw text**, the command and its
output as they were and the request as it was worded, not your account of what happened. Say
plainly that it came from you rather than from the transcript: you wrote the text being audited,
so anything you supply is testimony. If you cannot supply it either, say so and let it report on
what it has.

## Delivering the turn

This is the whole of a normal turn's closeout, in this order:

1. **Translate, if the user reads a language other than English.** Dispatch
   `guard:korean-translator` (subagent_type: `"guard:korean-translator"`) with two inputs and
   nothing else: the **answer file** as its source, and the **translation file** as the file it
   writes — both paths were named in the block that sent you here. Give it no history, no
   repository paths, and no draft of your own to fix. Then do what its report tells you; it
   hands the translation on to the agent that checks it.

   You are the only party that knows the language, which is why this is yours. What it is not
   is automatic: translate substance being delivered to a reader — two ordinary sentences of
   explanation is enough — and not an acknowledgement, a bare list of paths, or a question back
   to the user with nothing else in it. There is nothing there to translate.

2. **Reply short**, in the user's language: one headline sentence plus the path the user reads —
   the translation when this turn made one, the answer file when it did not. Do not restate the
   answer and do not paste the file.

3. **Open the file you named**: `open <path>` on macOS, `xdg-open` on Linux, `start` on
   Windows. Once, at the end. Opening is not "here is where it is" — the user has the path from
   your reply — it is you putting the document in front of them, so what you open is the
   document they read: the translation when there is one, the answer file otherwise.

**Say nothing about auditing.** No audit ran, nothing is being withheld as unchecked, and a
turn that was not audited is not news. Do not offer one; the user starts an audit themselves
when they want it.

## When the user has asked for an audit

The router's report is the instruction — which audits ran, in which order their findings are
applied, and whether a second round is due. This section is only what no report can carry.

1. **Apply the findings to the answer file.** Every audit reported before you changed anything,
   so you have all of them in hand and they all judged the same text: apply them in one pass, in
   the order the report lists them. Where two land on the same sentence, write the one correction
   that satisfies both rather than applying one and then patching it. Each report says what its
   findings need; fix each where it is written, in the English, with `Edit`. A finding you are
   leaving unfixed stays unfixed on purpose and is named in your reply. Some ask you to **add**
   rather than correct — a definition, an example, a paragraph cut — and those go in the same
   way. A report that says the reader profile is MISSING is telling the user something, not you:
   relay it in one line and say it once, not every time.

   Anything the report asks for **after** this — a further round of audits — happens now, before
   the steps below. Your reply covers every round: a finding from the first round that the
   second round raised again is one finding, not two.

2. **Rewrite the translation, if this turn has one.** The file the user read was translated from
   the English as it stood before the audit, so every correction you just applied is missing
   from it. Dispatch `guard:korean-translator` again, exactly as step 1 of *Delivering the turn*
   says, over the same two paths — it rewrites the translation from the corrected source.

   Only you know this is needed. The audit read the English and the router never saw the
   translation, so an audited turn whose translation is left alone hands the user a document
   that is still wrong in the way the audit just found.

3. **Reply**, in the user's language: what changed and why, a line or two per finding, with the
   router's reason for a pick relayed alongside what that pick found. **A clean audit is one
   line**; a paragraph celebrating it trains the user to skip the report that matters, and a
   pick that plainly misread the turn is worth saying so about rather than working around.

4. **Open the corrected file the user reads** — the translation when there is one, the answer
   file otherwise — once, after every correction has landed. Never open a translation you did
   not rewrite in step 2: it is the pre-audit text, and opening it presents the defect as the
   answer.

   Do not open a file you wrote during the audit, and do not start one for this report: an audit
   summary is worth a line in the reply, not a document.

**When the router picked nothing**, there is nothing to apply, nothing to re-translate and
nothing new to open — the user already has the document from the turn itself. Say so in one
line and stop there. `none` means no audit had material here, not that something was skipped.
