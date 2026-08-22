---
name: answer-file-amended-by-later-turn
description: guard turn-record files can be overwritten in place by a LATER turn in the same session; always check whether the given turn id's tool activity actually wrote the current file content before trusting it as verbatim.
metadata:
  type: project
---

In this repo's guard self-test sessions, a turn's answer file under
`.claude/guard/turns/<session>/<turn>.md` is sometimes patched by a *subsequent* turn
in the same session (a python `str.replace` on the file, e.g. to add a follow-up
measurement) — see session `0f38b566...`, turn `bcc71ae1` whose file was amended by
turn `457b86c4` moments later with a tmux-probe paragraph. The audit dispatch's stated
turn id can therefore lag the file's real current content.

**How to check:** run `transcript turn` for the given turn id; if a claim in the answer
file's text doesn't appear in that turn's own tool activity, use `transcript find` with
the exact phrase (no `--until`, or a generous `--last`) across the whole session — it
will surface the turn that actually wrote it, and you can extract *that* turn's tool
activity as the real evidence source. Don't assume divergence means fabrication; check
the later turn first.

**Numeric/count claims about "how many agents/turns reported X" are exactly the kind of
claim this session likes to overstate** — e.g. "이 세션에서만 세 에이전트가 그것을 보고했다
(deferrals-auditor가 두 번, clarity-auditor가 한 번)" turned out to be 2 reports (1
deferrals + 1 clarity), not 3, when checked against `transcript find` across the whole
session. Always recount from a `find` sweep rather than trusting the assistant's own
tally, especially when the claim contrasts "this session" vs "another session."

See [[gitignore_consolidation_turn]] for a fully-clean turn from the same project, as a
contrast case.

## Async subagent results can land mid-turn, after the turn's nominal timestamp

Turn `45417a98` (session `0f38b566...`) claimed "`3e6d8093` 감사에서 claims pass,
deferrals pass, clarity findings가 나왔다" for background claims/deferrals/clarity
audits dispatched two turns earlier. The turn's *index* timestamp (16:09:52) is the
prompt-start time, not when the answer was authored — the actual heredoc write of the
answer file happened later in the same promptId's tool sequence (confirmed at 16:11:48
by grepping raw jsonl lines for that `promptId` and checking each tool_result's own
`timestamp`). All three background results (deferrals 16:09:57, clarity 16:10:20, claims
16:10:54) had already arrived by then, and their verdicts (pass / pass / findings)
matched the claim exactly, including the specific recurrence detail clarity flagged.

**How to check:** don't rely on the `index` timestamp to decide whether an async result
"could have" arrived before the answer was written. Instead grep the raw `.jsonl` for
the dispatched agentId (from the launch tool_use) and for the turn's own `promptId`,
print each match's own `timestamp`, and compare — the answer-writing tool call's
timestamp is the real cutoff, not the turn's first timestamp.
