Source: https://learn.chatgpt.com/docs/hooks
Retrieved: 2026-08-14

> Plugin hook commands receive these environment variables:
>
> `PLUGIN_ROOT` is a Codex-specific extension that points to the installed
> plugin root.
>
> `PLUGIN_DATA` is a Codex-specific extension that points to the plugin’s
> writable data directory.

> Installing or enabling a plugin doesn’t automatically trust its hooks; Codex
> skips plugin-bundled hooks until you review and trust the current hook definition.

> `UserPromptSubmit` and `Stop` do not support matchers; any configured matcher
> is ignored for those events.
