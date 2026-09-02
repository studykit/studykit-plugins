# guard turn closeout

How a routed turn is closed out once its audits have reported. **Nothing here is about any one
agent** — how to dispatch it, what its inputs are, and what its findings mean all travel with
the dispatch: the router's report for the agents it picked, guard's Stop hook for the ones it
names directly, and each agent's own report for what to do with what it found.

## The answer file

The **answer file** is where this turn's substance lives, **written in English** whatever
language the user reads. You wrote it during the turn; the reply you gave was short and named
this path. It is not a copy of something already delivered — it is the deliverable, which is
why the agents can still fix it.

Do not paste its contents into a reply. **Summarising it is the same failure in a shorter
form** — a bulleted digest, or a preview of how it opens, puts the unaudited answer in front of
the user just as effectively as quoting it, and it passes for brevity while doing so. If you
find the file empty or missing, guard filled it in from the response after the fact and said so
in a comment at the top; treat it as the answer anyway, and write it properly next time.

Everything around it is English too — what you write in a dispatch, what the agents report
back, what one agent says to another. Never relay an agent's English report to the user
untranslated: what changed goes in the answer file.

**You never write the user's language yourself, and you never decide whether it gets written.**
Both are the router's: when this turn is delivered in another language, it names the agent that
writes it and says what that agent gets. When it names none, this turn has no translation, and
the answer file is what you name. The one exception is the short line you type in the terminal
beside the path — a pointer, not the deliverable, which is why it stays short.

**You never gather the session's history.** It is in the transcript, and an agent that needs it
resolves and extracts it itself. If one fails to — the file is gone, a compaction dropped the
range — it may `SendMessage` you and ask; answer it with the **raw text**, the command and its
output as they were and the request as it was worded, not your account of what happened. Say
plainly that it came from you rather than from the transcript: you wrote the text being audited,
so anything you supply is testimony. If you cannot supply it either, say so and let it report on
what it has.

## Presenting the result

The agents have reported and the ones that edit have already edited. What is left is yours, in
this order:

1. **Apply the findings to the answer file.** Every audit reported before you changed anything,
   so you have all of them in hand and they all judged the same text: apply them in one pass, in
   the order your dispatch listed them. Where two land on the same sentence, write the one
   correction that satisfies both rather than applying one and then patching it. Each report says
   what its findings need; fix each where it is written, in the English, with `Edit`. A finding
   you are leaving unfixed stays unfixed on purpose and is named in your reply. Some ask you to **add** rather than correct —
   a definition, an example, a paragraph cut — and those go in the same way. A report that says
   the reader profile is MISSING is telling the user something, not you: relay it in one line
   (they establish one with `/guard:reader-profile`) and say it once, not every turn.

   Anything your dispatch asked for **after** this — a further round of audits, a translation and
   whatever its own report hands off to — happens now, in the order it was given, before you write
   the reply below. Your reply covers every round: a finding from the first round that the second
   round raised again is one finding, not two.
2. **Reply short.** What changed and why, a line or two per finding, then the path — with the
   router's reason for a pick relayed alongside what that pick found. **A clean audit is one
   line**; a paragraph celebrating it trains the user to skip the report that matters, and a pick
   that plainly misread the turn is worth saying so about rather than working around. Do not
   restate the answer and do not paste the file. Write the reply in the user's language. The path
   you name is the one the **user** reads: the translation when this turn made one, the answer
   file when it did not.
3. **Open the file you named**: `open <path>` on macOS, `xdg-open` on Linux, `start` on
   Windows. Once, at the end, after every correction has landed. Opening is not "here is where
   it is" — the user has the path from your reply — it is you putting a document in front of
   them, so what you open is the document this turn audited and then corrected.

   - A translation exists → open the translation. It is what this user reads, and the English
     file is not a stand-in for it however well it was checked.
   - There is no translation → open the answer file. Here it is both the audited document and
     the one the user reads.
   - The document you would open went through no audit → **dispatch the audit that was meant to
     read it**, apply what it finds the way step 1 does, and then open it. A dispatch that fell
     through is not a verdict on the text: the turn is still open and the file is still there,
     so the answer to a check that did not happen is to run it, not to hand over a document
     nobody will look at again. Only when it cannot run — refused, or failed a second time — do
     you open nothing, name the path, and say what is unchecked and why. Whoever wrote a file
     does not count as having read it, so a translation nothing audited is unchecked no matter
     how thoroughly the English was audited.

   And do not open a file you wrote during the audit, or start a new one for this report: an
   audit summary is worth a line in the reply, not a document.

**When the router picked nothing**, steps 2 and 3 apply. `none` means no agent had material
here, translation included — nothing is left unfixed and nothing is being withheld as
unchecked, so name the answer file and open it. The unchecked case above is for a turn whose
audit skipped the document, not for a turn that had no audit to skip. Say nothing about
auditing either way: a turn that drew no agent is not news.
