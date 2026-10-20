---
name: delegate
description: Have delegate-sizer choose a Codex worker's model and effort, dispatch the work, verify the result, and record its verdict. Use when explicitly invoked as $delegate:delegate.
---

# Delegate

Delegate the instruction accompanying the user's `$delegate:delegate` invocation. Read it from the
user's message; there is no argument substitution. If the instruction is missing, ask for it.
`delegate-sizer` splits and sizes the work. You prepare worker prompts, verify results, and
record verdicts; you never choose a worker's model or effort yourself. Delegation does not
expand the user's permission to edit, publish, or send messages.

Resolve the plugin root three directories above this loaded `SKILL.md`'s directory, then find
its `scripts/ledger.py`. Run it with its concrete
absolute path using `uv run --script <ledger-path> <command> ...`. Below, `ledger` means that
command. Use the native plugin-data path supplied by the Delegate SessionStart hook as
`--data-dir <absolute-path>` in every ledger command. Below, that option is part of `ledger`.
Use `<command> --help` for other flags. History lives in that directory's `ledger.jsonl`;
`DELEGATE_LEDGER` overrides the history file only. Qualitative sizing lessons live in
`sizer-lessons.md` beside it. Do not guess a data directory or assume hook variables are set
in skill shell commands. If the storage context is missing, tell the user to enable/trust the
Delegate hook and start a new session. If the named sizer is unavailable, tell the user to run
this plugin's `$delegate:delegate-setup` and start a new session; do not run setup implicitly.

## Size

Call the available `spawn_agent` tool with `agent_type: "delegate-sizer"`. A summarized tool
description may omit registered custom roles; do not infer absence from that omission.
The named custom agent's configuration fixes `gpt-6.1-sol` / `high`; pass those same settings
explicitly if the schema permits overrides, and use a fresh context (`fork_turns: "none"`
when supported). If the host rejects the named type, cannot run it, or reports a different
effective configuration, stop and tell the user. Never imitate it with a default agent,
read its ladder to size the work yourself, or install or reconfigure agents during this
invocation. If the tool schema cannot select custom agent types, report that limitation.

Give the sizer:

- The user's instruction verbatim, including constraints.
- The ledger command with the script path fully resolved to an absolute path.
- The absolute `sizer-lessons.md` path in the native plugin-data directory; the sizer may read
  and maintain only that lessons file, never a general Codex memory store.
- The model/effort pairs the current spawn tool can actually apply; report uncertainty rather
  than guessing availability, and respect the host's override restrictions.
- Any known relevant input paths.

Wait for its answer: one block per piece with `piece`, `category`, `model`, `effort`, `probe`,
and `why`, plus which pieces are independent. Use its decisions as given. If the answer is
incomplete, blocked, or chooses an unsupported pair, report the problem instead of filling in
or substituting a choice. Sizing produces no worker verdict or ledger run of its own.

## Dispatch

Use Codex's available `spawn_agent` tool with each piece's sizer-selected `model` and
`reasoning_effort` explicitly. Never silently fall back to inheritance or another pair.
When its schema exposes `fork_turns`, set it to `"none"` so a full-history fork does not
override the selection. Use `default`, or an available `worker` or `explorer` suited to the
task. A custom agent can override spawn settings: use it only if its effective model and
effort match your choice. Follow the actual tool schema instead of copying Claude's
`Agent`, `effort`, `general-purpose`, or `fork` arguments.

Give the subagent a prompt it can act on without this conversation:

- Goal, relevant context, and concrete acceptance criteria.
- Absolute input paths, where to look, and what it must not touch.
- Requested result and the locations or evidence needed to verify it.

Dispatch only jobs the sizer marked independent concurrently, within the host's limit. Give
writers disjoint scopes. If the host cannot apply the selected settings, stop and explain;
do not change user configuration or start a separate CLI process as a workaround.
Wait for completion with the available subagent wait tool (such as `wait_agent` or `wait`);
an accepted spawn is not a finished result. Use the returned agent identifier when inspecting
or continuing that agent. Record the effective model and effort if the host reports them;
if they differ from the request, disclose it and do not attribute the result to the requested
tier. Never estimate token usage or duration from an agent's prose.

## Verify and record

Check the acceptance criteria yourself: read diffs, run the project's relevant tests or build,
and open cited code or sources. Find validation instructions in the target project's README,
CONTRIBUTING, documentation, Makefile, CI workflows, or test directories. The subagent's
own report is evidence to inspect, not proof.

Assign one verdict per attempted worker dispatch:

- `pass`: usable as delivered and meets the criteria.
- `partial`: needs a small fix you made or misses a part.
- `fail`: wrong, unverifiable, or requires redoing.

For a miss, choose one cause: `capability` (a clear, complete prompt exceeded the model),
`instruction` (your prompt was missing, ambiguous, or wrong), or `environment` (tools,
availability, permissions, or network blocked the work). A rejected spawn is an environment
failure, not evidence of weak reasoning. Be honest about instruction failures.

```sh
ledger add --category <category> --task "<one-line task>" \
  --agent-type <type> --model <model> --effort <effort> \
  --verdict <pass|partial|fail> [--cause <cause>] --reason "<why>" \
  [--tokens <reported-count>] [--duration-ms <reported-duration>] [--retry-of <id>]
```

Record every worker attempt, including retries. Omit usage fields the host does not provide. If
recording fails, preserve and report the result and the logging error; do not rerun the task
to recreate a record.

Retry at most once per piece. For a capability failure, dispatch `delegate-sizer` again with
the original instruction and constraints, the failed piece, model/effort, failure evidence,
record ID, available pairs, absolute ledger command, and the same lessons-file path. Require
it to select a higher tier; you do not decide the increase. If it cannot, report the blocker. For an instruction failure,
repair the prompt at the same model/effort. For an environment failure, retry only after
resolving the blocker. Link the retry to the first record using `--retry-of`. Report a second
failure with both record IDs.

Return the result, selected model/effort and the sizer's reason (including any probe), subagent
identifier, verified verdict and reason, and record ID for each piece. If the user disputes a
verdict, append their correction:

```sh
ledger amend <id> --verdict <verdict> [--cause <cause>] --reason "<user's reason>"
```

Amendments replace the verdict in later recall without deleting its history.
