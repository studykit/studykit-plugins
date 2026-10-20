---
description: Hand an instruction to a subagent on a model and effort sized to it, verify what comes back, and record whether the subagent did the work well so later choices learn from it.
argument-hint: <instruction>
disable-model-invocation: true
---

# Delegate

The user wants this done by a subagent, not by you:

$ARGUMENTS

If no instruction follows, ask for one.

You do not decide which model or effort the work gets — the `delegate:delegate-sizer` agent
does, and you dispatch on its decision as given. Your part is what neither the sizer nor the
worker can do: write a prompt the worker can act on cold, judge what it hands back, and write
that judgment down. Delegating does not widen what the user has allowed you to edit, publish,
or send.

The ledger is how the next sizing gets better than this one. Run it as:

```sh
uv run --script "${CLAUDE_PLUGIN_ROOT}/scripts/ledger_claude.py" --data-dir "${CLAUDE_PLUGIN_DATA}" <command> ...
```

`<command> --help` lists the flags. The rest of this file calls that `ledger`. History lives in
`ledger.jsonl` in that data directory; `DELEGATE_LEDGER` overrides the history file only. The
sizer's lessons file is `${CLAUDE_PLUGIN_DATA}/sizer-lessons.md`.

## 1. Size

Dispatch the `delegate:delegate-sizer` agent with:

- the instruction above, verbatim;
- the `ledger` command above, exactly as written here;
- the lessons file path above;
- the models the Agent tool's `model` parameter offers you;
- paths to the files the work concerns, if you know them.

It returns one block per piece of work — category, model, effort, whether it is a probe, and
why — and says which pieces can run together. Take the model and effort as they are. If the
sizer is not available, or its answer is incomplete or names a model you cannot use, stop and
tell the user rather than sizing the work yourself. Sizing produces no ledger record of its own.

## 2. Dispatch

For each piece, call the Agent tool with the sizer's `model` and `effort`. Use
`general-purpose` unless an available agent type fits the work better. Never `fork`: a fork
runs on your own model and effort and ignores both parameters, which defeats the sizing.

The worker starts with none of this conversation. Its prompt must carry:

- the goal and why it matters, in a sentence or two;
- what "done" means, concretely enough that you can check it — this is what you will verify
  against;
- where to look, as paths; hand a large input over as a file path, not pasted;
- what it must not touch;
- what to return: the result, and for each claim, where it can be checked.

Pieces the sizer marked independent go out in one message so they run concurrently. Give
workers that write disjoint scopes.

## 3. Verify

Judge the result against the "done" you wrote, by checking, not by reading its report:

- changed files — read the diff;
- code — run the tests or the build the project uses; find them from a README, a CONTRIBUTING
  section, a Makefile target, a CI workflow, or a test directory;
- claims about code or sources — open the cited location and confirm it says that.

Give one verdict per piece:

- `pass` — meets "done", usable as delivered.
- `partial` — usable after a small fix you made, or missing a part.
- `fail` — wrong, unverifiable, or you had to redo it.

For `partial` and `fail`, give one cause:

- `capability` — the prompt was clear and complete; the model could not do it.
- `instruction` — your prompt was ambiguous, missing context, or wrong.
- `environment` — tools, permissions, or the network stood in the way.

Be honest about `instruction`. Blaming the model for your own prompt pushes every later run
onto a tier it does not need.

## 4. Record

Record every run, the retries too, with the category the sizer gave:

```sh
ledger add --category <category> --task "<one line: what was asked>" \
  --agent-type <type> --model <model> --effort <effort> \
  --verdict <pass|partial|fail> [--cause <cause>] --reason "<one line: why this verdict>" \
  [--tokens <n>] [--duration-ms <n>] [--retry-of <id>]
```

Take `--tokens` and `--duration-ms` from the worker's completion notice when it reports them;
never estimate them. `add` prints the record's id. If recording fails, report the result and
the error; do not rerun the work to recreate a record.

## 5. On failure

- `capability` → dispatch the sizer again for that piece with everything from §1, plus the
  model and effort that failed, what failed, and the record id; it must choose a higher tier.
  Retry once on its answer, with `--retry-of <id>`.
- `instruction` → fix the prompt and retry on the same model and effort.
- `environment` → fix what stood in the way, or tell the user what did.

Do not retry more than once per piece. A second failure goes to the user, with both records.

## 6. Report

Tell the user, per piece: the model and effort with the sizer's reason, the verdict and its
reason, the record id, and the result itself. If the user disputes a verdict, record theirs:

```sh
ledger amend <id> --verdict <verdict> [--cause <cause>] --reason "<their reason>"
```

An amendment counts in `recall` in place of your verdict.
