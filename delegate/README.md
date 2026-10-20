# Delegate

Delegates work through a dedicated sizing agent, verifies the workers' results, and records
verdicts so later model choices improve. Runs in Claude Code and Codex.

The main session never picks a worker's model or effort: `delegate-sizer` splits and classifies
the instruction, reads past verdicts, and selects each worker's model and effort. The main
session follows those choices, verifies each result itself, and records pass, partial, or
fail. Capability failures go back to the sizer for at most one higher-tier retry; prompt and
environment failures do not raise the tier. If a verdict is wrong, ask for it to be amended.
A missing sizer or an unavailable choice stops the workflow rather than substituting one.
Delegation runs only when you invoke it.

Both editions require [`uv`](https://docs.astral.sh/uv/) on `PATH`.

## Claude Code

Install **delegate** from the **studykit-plugins** marketplace. There is no setup step: the
sizer ships with the plugin.

```text
/delegate:delegate Find which code owns settings validation and report its rules.
```

`delegate-sizer` runs on `opus` with high effort. Workers are sized on a ladder from
`haiku` / `low` to `fable` / `max`, limited to the models the session offers.

## Codex

Install **Delegate** from the **Studykit Plugins** marketplace. It needs access to
`gpt-6.1-sol` with high reasoning.

In a new Codex session, open `/hooks` and review/trust Delegate's storage hook. It supplies
the native plugin-data path; it does not write files or perform delegation. Then run once
after installing or updating:

```text
$delegate:delegate-setup
```

This registers the named `delegate-sizer` in your Codex user configuration and installs its
definition in durable user state. Existing settings and user-edited definitions are preserved.
Start a new Codex session after setup so the custom agent becomes available.

```text
$delegate:delegate Find which code owns settings validation and report its rules.
```

`delegate-sizer` runs on `gpt-6.1-sol` / `high`. The worker ladder uses `gpt-6-luna`,
`gpt-6.1-sol`, and `gpt-6-astra`, subject to the models and efforts the current session
supports.

To inspect or remove the Codex configuration:

```text
$delegate:delegate-setup status
$delegate:delegate-setup remove
```

Run `remove` before uninstalling the plugin. It removes only the unchanged managed agent and
registration, preserving verdict history and sizing lessons. If setup detects a user-edited
definition or role, it reports the conflict and leaves it intact.

## History and lessons

Each host keeps its records in `ledger.jsonl` inside its own plugin data directory, shared
across projects; `DELEGATE_LEDGER` overrides the full ledger file path. The sizer keeps only
qualitative sizing lessons, each with supporting record IDs, in `sizer-lessons.md` beside it.
It never copies runs, counts, or verdicts into lessons, and removes lessons the ledger
contradicts. The sizer uses no other memory.

Claude Code deletes the plugin data directory when the plugin is uninstalled from its last
location, unless you uninstall with `--keep-data`.
