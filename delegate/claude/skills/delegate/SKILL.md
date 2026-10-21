---
description: Hand an instruction to subagents on a model and effort sized to it, have each result verified, and record whether the subagent did the work well so later choices learn from it.
argument-hint: <instruction>
disable-model-invocation: true
---

# Delegate

The user wants this done by subagents, not by you:

$ARGUMENTS

If no instruction follows, ask for one.

You do not decide how the work is split or which model and effort each part gets — the
`delegate:delegate-sizer` agent does, and you dispatch on its decision as given. You do not
judge the results either — the `delegate:delegate-verifier` agent checks them. Your part is
what none of them can do: write a prompt a worker can act on cold, keep the pieces in order and
on budget, decide what happens after a miss, and write it all down. Delegating does not widen
what the user has allowed you to edit, publish, or send.

The ledger is how the next sizing gets better than this one. Run it as:

```sh
uv run --script "${CLAUDE_PLUGIN_ROOT}/scripts/ledger_claude.py" --data-dir "${CLAUDE_PLUGIN_DATA}" <command> ...
```

`<command> --help` lists the flags. The rest of this file calls that `ledger`. History lives in
`ledger.jsonl` in that data directory; `DELEGATE_LEDGER` overrides the history file only. The
sizer's lessons file is `${CLAUDE_PLUGIN_DATA}/sizer-lessons.md`.

Never use `fork` for the sizer, a worker, or the verifier: a fork runs on your own model and
effort and ignores both parameters, which defeats the sizing.

## 1. Size

Dispatch the `delegate:delegate-sizer` agent with:

- the instruction above, verbatim;
- the `ledger` command above, exactly as written here;
- the lessons file path above;
- the models the Agent tool's `model` parameter offers you;
- paths to the files the work concerns, if you know them.

It returns one block per piece — id, scope, the pieces it comes `after`, category, model,
effort, budget, whether it is a probe, and why. Take them as they are. If the sizer is not
available, or its answer is incomplete or names a model you cannot use, stop and tell the user
rather than sizing the work yourself. Sizing produces no ledger record of its own.

## 2. Dispatch

A piece is ready when every piece in its `after` has passed. Send every ready piece in one
message so they run at the same time; as each one passes, send the pieces it unblocks. If two
ready pieces write and their scopes overlap after all, run them one after the other.

For each piece, call the Agent tool in the background with the sizer's `model` and `effort`,
and name the worker `<piece id>-<attempt>` so you can stop it. Use `general-purpose` unless an
available agent type fits the work better. Before sending a piece that writes, note its scope's
starting state — the commit, and any uncommitted changes inside the scope — so the verifier can
tell the worker's changes from what was already there.

The worker starts with none of this conversation. Its prompt must carry:

- the goal and why it matters, in a sentence or two;
- what "done" means, as criteria concrete enough to check one by one;
- its scope, as paths; hand a large input over as a file path, not pasted;
- what it must not touch — at least everything outside its scope;
- what to return: the result, and for each claim, where it can be checked.

Keep each worker's prompt exactly as sent; the verifier needs it verbatim.

### Budget

When a worker goes out, start its timer: a background shell command that sleeps for its budget
(`sleep <minutes × 60>`). When the timer ends and the worker has not, stop the worker with
`TaskStop` and its name. A stopped worker is an attempt like any other; verify what it left.

## 3. Verify

Dispatch `delegate:delegate-verifier` for each finished or stopped worker, with `model: opus`
and `effort: high` whatever tier the worker ran on. Give it:

- the worker's prompt, verbatim;
- the "done" criteria;
- the scope and its starting state;
- the worker's report, or for a stopped worker, that it was stopped at its budget.

Verifiers of independent pieces run at the same time.

The verifier returns each criterion with its evidence, a verdict, and a cause. Read the
evidence, not just the verdict: a criterion marked met with no command result or location is
not met. Overturn the verdict only where the evidence contradicts it, or where you know
something the verifier could not — what the user meant, a constraint you left out of the
prompt. When you overturn, say why in one line; the record keeps both.

## 4. Record

Record every attempt, the verifier's verdict as given, with the category the sizer gave:

```sh
ledger add --category <category> --task "<one line: what was asked>" \
  --agent-type <type> --model <model> --effort <effort> \
  --verdict <pass|partial|fail> [--cause <cause>] --reason "<the verifier's reason>" \
  [--tokens <n>] [--duration-ms <n>] [--retry-of <id>]
```

Take `--tokens` and `--duration-ms` from the worker's completion notice when it reports them;
never estimate them. `add` prints the record's id. If you overturned the verdict, amend it at
once:

```sh
ledger amend <id> --by dispatcher --verdict <verdict> [--cause <cause>] --reason "<why you overturned it>"
```

If recording fails, report the result and the error; do not rerun the work to recreate a
record.

## 5. After a miss

Each piece gets two attempts in all: the first, and one retry.

- `partial` that a small fix makes usable → make the fix yourself; no retry.
- `capability`, or stopped at its budget → dispatch the sizer again for that piece with
  everything from §1, plus the model and effort that failed, how it failed, and the record id.
  It must choose a higher tier or a longer budget; retry on its answer, with
  `--retry-of <id>`. If it says no tier is above, give up.
- `instruction` → fix the prompt and retry on the same model and effort.
- `environment` → fix what stood in the way and retry on the same model and effort, or give up
  and tell the user what stood in the way.

Before a retry of a piece that writes, tell the new worker what state its scope is in now.

When a piece's retry misses too, give it up. Giving up a piece means: do not do its work
yourself, do not dispatch the pieces that come `after` it, and let the pieces that do not
depend on it finish.

## 6. Report

Tell the user, per piece: the model and effort with the sizer's reason, the verdict and its
reason, the record id, and the result itself. For a piece given up, say so first, with every
record id it produced and what it left in its scope, and name the pieces that did not run
because of it.

If the user disputes a verdict, record theirs:

```sh
ledger amend <id> --verdict <verdict> [--cause <cause>] --reason "<their reason>"
```

An amendment counts in `recall` in place of the earlier verdict.
