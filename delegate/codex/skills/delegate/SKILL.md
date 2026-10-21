---
name: delegate
description: Have delegate-sizer split and size Codex workers, dispatch ready pieces together, have delegate-verifier check results, and record verdicts. Use when explicitly invoked as $delegate:delegate.
---

# Delegate

Delegate the instruction accompanying the user's `$delegate:delegate` invocation. Read it from
the user's message; there is no argument substitution. If it is missing, ask for it.
The sizer owns splitting, model/effort choices, and budgets; the verifier owns checking results
and proposing verdicts. You prepare prompts, dispatch, and record. Delegation does not expand
the user's permission to edit, publish, or send messages.

Resolve the plugin root three directories above this loaded `SKILL.md`'s directory. Below,
`ledger` means `uv run --script <absolute-plugin-root>/scripts/ledger.py --data-dir
<absolute-native-data-path>`. Take the native plugin-data path from the Delegate SessionStart
context; do not guess it or assume hook variables are exported in skill shell commands.
History is `ledger.jsonl` there (`DELEGATE_LEDGER` overrides only the history file); sizing
lessons are `sizer-lessons.md` beside it. Use `<command> --help` for ledger flags.
If storage context is absent, tell the user to enable/trust the hook and start a new session.
If either named agent is unavailable, tell the user to run `$delegate:delegate-setup` and
start a new session. Never run setup implicitly or imitate a missing role with a default agent.

## 1. Size

Call the available `spawn_agent` tool with `agent_type: "delegate-sizer"`. A summarized tool
listing may omit registered roles; try the named type if the schema permits custom roles.
It fixes `gpt-6.1-sol` / `high`; pass the same overrides when supported. Use fresh context
(`fork_turns: "none"` when exposed) so inheritance does not defeat explicit settings.
Give it:

- The original instruction verbatim, including constraints, and known relevant paths.
- The fully resolved ledger command and absolute sizing-lessons path; it may maintain only
  that lessons file, never a general memory store.
- The model/effort pairs the current spawn tool can apply and any override restrictions.
  Report uncertainty rather than guessing availability. The ceiling is `gpt-6-astra` / `high`.

Wait for one block per piece: `piece: <id>: <task>`, `scope`, `after`, `category`, `model`,
`effort`, `budget` in positive minutes, `probe`, and `why`. Confirm IDs are unique, dependency
IDs exist without cycles, writers' scopes do not overlap, and choices are supported within
the ceiling. If incomplete or invalid, return it to the sizer for correction; do not fill in
choices yourself. A blocked piece is given up, with its dependents held back. Sizing creates
no worker attempt or ledger verdict.

If the named role is rejected, its effective settings differ, or the schema cannot select
custom roles or apply explicit model/effort overrides, stop and report the limitation. Do not
reconfigure the host or start another CLI to work around it. Apply this to verifiers too.

## 2. Dispatch and budget

Keep a table of each piece's dependencies, current scope state, attempt count, worker ID,
start/deadline, and ledger IDs. A piece is ready only when all its `after` pieces have verified
usable results, including any verified small fix. Send all ready pieces in one batch of spawn
calls, up to the host's concurrency limit; queue the rest. Writers own disjoint scopes.
Keep the attempt label `<piece-id>-<attempt>` alongside the returned identifier. For a
`task_name` restricted to lowercase letters, digits, and underscores, use `<piece-id>_<attempt>`
(for example, `p1_1`); validate it against the actual schema before spawning. Attempt numbers
are 1 and 2; each piece gets at most two attempts.

Use the sizer's exact `model` and `reasoning_effort` in `spawn_agent`. Set `fork_turns: "none"`
where supported. Use `default`, or an available `worker`/`explorer` suited to the task. A
custom role may override spawn settings; use one only if its effective pair matches. Never
silently inherit another tier. Give each worker a self-contained prompt containing:

- The goal, relevant context, original constraints, and concrete acceptance criteria.
- Absolute input paths, its owned scope, forbidden edits, and the scope's starting state
  (baseline commit and any pre-existing changes). Capture that baseline before it starts.
- Its budget, requested report, and evidence/locations needed for verification.

Record the local clock at dispatch and compute its deadline as start plus budget. Before
launching workers, confirm the host exposes a native way to interrupt/stop an active agent.
If it does not, report that budgets cannot be enforced and do not dispatch.

Wait with the available native agent wait tool (`wait_agent` or `wait`, following its schema).
Use bounded waits no longer than the nearest active deadline and the tool's maximum; keep
user updates timely. If the nearest deadline is shorter than the tool's minimum wait, use a
short clock wait and then inspect status. Check the actual clock and all worker statuses
after each return: one mailbox update can concern a different worker. A wait timeout ends
only the wait; it does not stop a worker or prove a budget overrun. Completion/acceptance
notifications must be distinguished. Do not use the wait call's elapsed duration as the
worker's runtime.

At the deadline, inspect status once more. If still active, stop the specific worker with the
host's native stop tool: `interrupt_agent` when exposed, or `close_agent` when that schema
supports stopping active agents. Follow the actual argument names and returned status. Do not
send a "please stop" prompt and assume it stopped. Confirm it is no longer running before
verification, a retry, or any dependent write; if confirmation fails, hold that scope and its
dependents and report the blocker. Also account for any still-running shell command it
started; interruption is not proof that subprocesses stopped. Preserve partial changes and
its report. A stopped worker is still an attempt and must be verified and recorded.

Record effective settings if the host supplies them. Disclose mismatches and do not credit
the requested tier. Never infer token counts or runtime from the worker's prose.

## 3. Verify

Dispatch the named `delegate-verifier` for each completed or confirmed-stopped attempt, using
fresh context and explicit `model: "gpt-6.1-sol"` / `reasoning_effort: "high"`, regardless of
the worker's tier. The named role fixes the same pair so every tier has the same judge.
If that pair is unavailable or the effective settings differ, report verification blocked;
do not downgrade or take over checking.
Independent verifiers may run concurrently within host limits. Give each:

- The worker prompt verbatim and the acceptance criteria.
- Its scope and captured starting state, including pre-existing or concurrent changes.
- The report, or notice of the budget stop and what it left behind; include rejection or
  environment evidence if the worker could not start.

Require each criterion's met/not-met status and evidence, verdict, cause, and reason. An
unsupported claim is not evidence. Ask for missing verification evidence without restarting
the worker. Overturn a verdict only where evidence contradicts it or you know a constraint
or user intent the verifier did not receive. Explain the correction; keep both judgments.
If verification cannot complete, report that blocker and hold dependents; never invent a
verifier verdict or rerun the worker just to obtain a record.

## 4. Record

Record every worker attempt, including rejected spawns and retries, with the sizer's category
and the verifier's verdict and reason as given:

```sh
ledger add --category <category> --task "<one-line task>" \
  --agent-type <type> --model <model> --effort <effort> \
  --verdict <pass|partial|fail> [--cause <cause>] --reason "<verifier reason>" \
  [--tokens <reported-count>] [--duration-ms <reported-duration>] [--retry-of <id>]
```

Omit usage fields the host does not supply. If you overturned the verdict, immediately append:

```sh
ledger amend <id> --by dispatcher --verdict <verdict> [--cause <cause>] --reason "<correction reason>"
```

If recording fails, preserve the result and report the error; never rerun work to recreate
its record. A rejected spawn is an environment failure, not evidence of weak reasoning.

## 5. After a miss

Each piece gets two worker attempts in total: the first and at most one retry.

- For a usable `partial` needing a small, in-scope fix, you may make that fix and have the
  verifier check it. Keep the original verdict, and record the verified correction with
  `amend --by dispatcher`; do not turn a redo into a small fix.
- For `capability`, or any worker stopped at its budget, dispatch the sizer again with the
  original handoff, same piece ID and scope, failed model/effort, failure/stop evidence, and
  record ID. Require a strictly higher supported tier; for an overrun also require a longer
  budget. If none exists below the ceiling, give the piece up. Never raise the tier yourself
  or accept a longer budget alone as the escalation.
- For `instruction`, repair the prompt and retry at the same tier and budget.
- For `environment`, resolve the blocker and retry at the same tier and budget, or give up.

Update the retry prompt with the scope's current state; partial work remains on disk. Link
its record with `--retry-of <first-id>`. Never split a retry to reset the attempt limit.
After a second miss, give up. Do not do an abandoned piece's work yourself, dispatch its
transitive dependents, or quietly accept partial leftovers as complete. Let unrelated pieces
finish. Report what remains in every abandoned scope.

## 6. Report

Per piece, return the result, selected pair and sizing reason (including any probe), worker
identifier, verified verdict/reason, and ledger IDs. Lead with abandoned or blocked pieces,
what they left behind, and the pieces that could not run because of them.
If the user disputes a verdict, record their correction:

```sh
ledger amend <id> --verdict <verdict> [--cause <cause>] --reason "<user reason>"
```

Amendments replace the verdict in later recall without deleting history.
