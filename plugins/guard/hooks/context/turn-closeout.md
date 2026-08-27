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

1. **Apply the findings to the answer file.** Each report says what its findings need; fix each
   where it is written, in the English, with `Edit`. A finding you are leaving unfixed stays
   unfixed on purpose and is named in your reply. Some ask you to **add** rather than correct —
   a definition, an example, a paragraph cut — and those go in the same way. A report that says
   the reader profile is MISSING is telling the user something, not you: relay it in one line
   (they establish one with `/guard:reader-profile`) and say it once, not every turn.

   Anything your dispatch asked for **after** this — a translation and whatever its own report
   hands off to — happens now, in the order it was given, before you write the reply below.
2. **Reply short.** What changed and why, a line or two per finding, then the path — with the
   router's reason for a pick relayed alongside what that pick found. **A clean audit is one
   line**; a paragraph celebrating it trains the user to skip the report that matters, and a pick
   that plainly misread the turn is worth saying so about rather than working around. Do not
   restate the answer and do not paste the file. Write the reply in the user's language. The path
   you name is the one the **user** reads: the translation when this turn made one, the answer
   file when it did not.
3. **Open that file, but only if an agent has read it**: `open <path>` on macOS, `xdg-open` on
   Linux, `start` on Windows. Once, at the end, after every correction has landed. Opening is not
   "here is where it is" — the user has the path from your reply — it is you putting a document
   in front of them, so doing it with text nothing checked presents an unchecked draft as a
   finished one.

   - A translation exists and an agent checked it → open the translation. This is the normal case
     on a turn that made one.
   - A translation exists and nothing read it → open nothing, name the path, and say it is
     unchecked and why. Whoever wrote it does not count as having read it. Do not open the
     English file in its place: it was checked, but it is not what this user reads.
   - There is no translation, and at least one agent audited the answer file → open the answer
     file. Here it is both the audited document and the one the user reads.
   - No agent read anything this turn → open nothing.

   And do not open a file you wrote during the audit, or start a new one for this report: an
   audit summary is worth a line in the reply, not a document.

**When the router picked nothing**, only step 2 applies. `none` means no agent had material
here, translation included. Reply in the user's language, name the answer file, and say nothing
about auditing: a turn that drew no agent is not news.
