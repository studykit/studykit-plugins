---
name: delegate-setup
description: Install, inspect, update, or remove the named delegate-sizer custom agent for the Delegate Codex plugin. Use when explicitly invoked as $delegate:delegate-setup.
---

# Delegate setup

Configure the named `delegate-sizer` used by this plugin. Read the user's requested operation
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

`install` also updates an existing managed setup. It installs the bundled regular TOML into
that plugin-data directory and registers `delegate-sizer` in the Codex home `config.toml`,
preserving unrelated settings. It never overwrites a user-owned role or edited sizer.
Run `status` after installation and confirm `configured` and `up_to_date` are true. Report
the model and effort from the result and ask the user to start a new Codex session so the
custom agent becomes available. Do not claim that this current session has reloaded it.

`remove` removes only the unchanged managed agent and role registration, preserving delegation
history. Run it before uninstalling the plugin. If any command reports a conflict, explain
the actual conflict and stop; do not edit the config by hand, force replacement, or remove
user changes. If `uv` is missing, report that prerequisite instead of installing software.

An explicit setup invocation authorizes this plugin's agent registration, not unrelated
Codex settings or marketplace changes.
