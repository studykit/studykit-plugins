# Claude Code — Output styles

Source: https://code.claude.com/docs/en/output-styles
Retrieved: 2026-08-19

Saved for `plugins/guard/output-styles/simple.md`: the frontmatter schema, how
plugins ship styles, and the reminder/subagent behavior that constrains how the
style file must be written.

## Frontmatter

Verbatim from the docs' frontmatter table:

| Frontmatter | Purpose | Default |
| :--- | :--- | :--- |
| `name` | Name of the output style, if not the file name | Inherits from file name |
| `description` | Description of the output style, shown in the `/config` picker | None |
| `keep-coding-instructions` | Keep Claude Code's built-in software engineering instructions | `false` |
| `force-for-plugin` | Plugin output styles only: apply this style automatically whenever the plugin is enabled, without requiring users to select it. Overrides the user's `outputStyle` setting. If multiple enabled plugins set this, Claude Code uses the first one loaded. | `false` |

Only these four fields are documented. `name` and `description` are metadata;
the other two are behavioral.

## Plugins

> "[Plugins](/docs/en/plugins-reference) can also ship output styles in an
> `output-styles/` directory."

No `plugin.json` declaration is documented — the directory is the registration.
The docs never mention Codex, so output styles are documented as a Claude Code
feature only.

## How output styles work

Verbatim:

> - Claude Code adds each output style's custom instructions to the end of the
>   system prompt.
> - All output styles trigger reminders for Claude to adhere to the output style
>   instructions during the conversation.
> - Custom output styles leave out Claude Code's built-in software engineering
>   instructions, such as how to scope changes, write comments, and verify work,
>   unless `keep-coding-instructions` is set to `true`.

> "Output styles apply to the main conversation only: a subagent runs its own
> system prompt, so styles don't change how subagents respond. A fork is the
> exception, because it inherits the parent's full system prompt."

Three consequences for authoring a style file:

1. **The style is re-asserted mid-conversation**, not read once and forgotten —
   "all output styles trigger reminders". A rule the model can re-check against
   its own draft output benefits from this; a rule phrased as background
   rationale does not.
2. **Subagents do not inherit it.** guard's `simple-explainer` agent must carry
   its own copy of any rule that must hold there — the style cannot reach it.
   Forks are the one exception.
3. **`keep-coding-instructions: true` keeps the built-in coding instructions**,
   so the style coexists with them rather than replacing them; both are in the
   system prompt at once.

## Loading and timing

> "Output style is part of the system prompt, which Claude Code reads once at
> session start. Changes take effect after `/clear` or a new session."

An edited style file does not affect the running session.

User/project/policy styles live in `~/.claude/output-styles`, `.claude/output-styles`,
and the managed settings directory; the file name becomes the style name unless
`name` is set.
