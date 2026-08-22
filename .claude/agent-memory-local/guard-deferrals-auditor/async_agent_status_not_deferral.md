---
name: async-agent-status-not-deferral
description: Turns that dispatch a background Agent/Task and say "will let you know when done" are status updates, not resolvable deferrals
metadata:
  type: project
---

In the guard plugin's own repo (studykit-plugins), many turns dispatch async subagents (via the
`Agent` tool, e.g. `guard:clarity-auditor`, `guard:router`) and the visible response is something
like "저장 중이며, 완료되면 알려드리겠습니다" (saving, will notify when done).

This is not a deferral of a factual matter the repo could answer — the tool result for an async
agent explicitly instructs the dispatching turn not to report, assume, or predict the subagent's
results until a completion notification arrives. There is nothing in the repository to look up;
the "unknown" is the not-yet-finished state of a task the assistant itself just started.

**How to apply:** when a response says it dispatched a background agent and will report back,
do not flag this as a resolvable deferral. Only flag if the response also punts a *separate*,
independently-answerable factual question (e.g. "not sure which file handles X") that isn't about
the pending subagent's own output.
