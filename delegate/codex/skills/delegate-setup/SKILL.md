---
name: delegate-setup
description: Install, inspect, update, or remove the named delegate-sizer and delegate-verifier custom agents for the Delegate Codex plugin. Use when explicitly invoked as $delegate:delegate-setup.
---

# Delegate setup

Configure the named `delegate-sizer` and `delegate-verifier` used by this plugin. Read the user's requested operation
from the invocation: default to `install`; use `status` to inspect or `remove` to clean up.

Resolve the plugin root three directories above this loaded `SKILL.md`'s directory, then use
the concrete absolute path to `scripts/setup.py`:

```sh
uv run --script <absolute-setup-script> <install|status|remove>
```

Append `--data-dir <absolute-path>` using the native `PLUGIN_DATA` path supplied by the
Delegate SessionStart context. Do not assume that hook environment variables are present
in the shell. If the context is missing, ask the user to enable/trust this plugin's hook and
start a new session; do not invent a storage path.

`install` also updates an existing managed setup, including an older sizer-only setup. It
installs both bundled regular TOML files into that plugin-data directory and registers both
roles in the Codex home `config.toml`, preserving unrelated settings. It checks both roles
for conflicts before changing either. It never overwrites user-owned roles or edited agents.
Run `status` after installation and confirm `configured` and `up_to_date` are true. Report
each role's status from `agents` in the result and ask the user to start a new Codex session
so both become available. Both the sizer and verifier fix `gpt-6.1-sol/high`; the verifier's
settings do not depend on the worker tier. Do not claim
that this current session has reloaded either role.

`remove` removes only unchanged managed agents and role registrations, preserving delegation
history. Run it before uninstalling the plugin. If any command reports a conflict, explain
the actual conflict and stop; do not edit the config by hand, force replacement, or remove
user changes. If `uv` is missing, report that prerequisite instead of installing software.

An explicit setup invocation authorizes this plugin's agent registration, not unrelated
Codex settings or marketplace changes.
