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
back, what one agent says to another. The audits run against that English file, and the version
the user reads is made from it afterwards, at step 2. Never relay an agent's English report to
the user untranslated: what changed goes in the answer file, which is translated.

**You do not write the user's language yourself.** Every word of Korean the user reads comes
from `korean-translator` and is then checked by `korean-corrector`. Neither has a switch, so the
user cannot turn them off — but that is not the same as running on every turn: whether this turn
has substance being delivered to a reader is the router's call, made on `korean-translator`
alone. The one exception is the short line you type in the terminal beside the path — a pointer,
not the deliverable, which is why it stays short.

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

1. **Apply the findings to the answer file.** Fix each where it is written, in the English, with
   `Edit`. A finding you are leaving unfixed stays unfixed on purpose and is named in your
   reply. `audit-turn-clarity`'s are the one kind that ask you to **add** rather than correct —
   a definition, an example, a paragraph cut — and they go in the same way; if its report says
   the reader profile is MISSING, relay that in one line (the user establishes one with
   `/guard:reader-profile`) and say it only once, not every turn.
2. **Have it translated. You do not write the translation.** The corrected text goes to a **new
   file**: the answer file's path with `.md` replaced by `.<lang>.md` (`.ko.md` for Korean).
   **Dispatch `korean-translator` now** — alone, and with exactly two inputs: the answer file,
   which is its source, and that translation path, where it writes. No history and no repository
   paths. Hand it the two paths and let it write the file; a draft of your own in front of it
   anchors it to the wording it was brought in to avoid, which is what produces 직역. Relay any
   sentence it listed as translated-but-unsure, and answer it if it `SendMessage`s you mid-run —
   that is a question about what the English meant. The English file stays as it is: it is what a
   later audit of this turn reads.

   **Skip this step when the router did not name `korean-translator`** — including every turn
   answered in English, where it never appears. That is the router saying this turn has nothing
   worth translating, and the answer to it is no translation, not a translation you write
   instead.
3. **Check the translation.** Only when step 2 made one, and the translator's report is what
   tells you to: it ends in a `next` line naming `korean-corrector` and the file it wrote. The
   router never names this agent — when it read, the file did not exist. Dispatch it alone and on
   the **translation file** only: no history, and not the answer file, which is the English
   original and not what the user reads. It edits in place, so its corrections are already
   applied when it reports; relay any phrase it listed as unfixed.
4. **Reply short.** What changed and why, a line or two per finding, then the path — with the
   router's reason for a pick relayed alongside what that pick found. **A clean audit is one
   line**; a paragraph celebrating it trains the user to skip the report that matters, and a pick
   that plainly misread the turn is worth saying so about rather than working around. Do not
   restate the answer and do not paste the file. The path you name is the one the **user** reads:
   the translation when you made one, the answer file when you did not.
5. **Open the file, but only if an agent has read it**: `open <path>` on macOS, `xdg-open` on
   Linux, `start` on Windows. Once, at the end, after every correction has landed. Opening is not
   "here is where it is" — the user has the path from your reply — it is you putting a document
   in front of them, so doing it with text nothing checked presents an unchecked draft as a
   finished one.

   - Translation exists and `korean-corrector` ran on it → open the translation. The normal case
     on a turn that got one: the translator's `next` line always follows.
   - Translation exists and `korean-corrector` did **not** run → open nothing, name the path, and
     say the translation is unchecked and why. `korean-translator` having written it does not
     substitute: it is the author, and nothing has read it. Do not open the English file in its
     place — it was checked, but it is not what this user reads.
   - Answering in English, so there is no translation, and at least one agent audited the answer
     file → open the answer file. Here it is both the audited document and the one the user
     reads.
   - No agent read anything this turn → open nothing.

   And do not open a file you wrote during the audit, or start a new one for this report: an
   audit summary is worth a line in the reply, not a document.

**When the router picked nothing**, steps 1 through 3 and step 5 do not apply. `none` means no
agent had material here — `korean-translator` included, and with no translation the corrector
has no input either. Reply per step 4, in the user's language, naming the answer file, and say
nothing about auditing: a turn that drew no agent is not news.
