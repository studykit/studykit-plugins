# Claude Code — plugin `agents/` directory discovery (recursion and skip rules)

Source: https://code.claude.com/docs/en/sub-agents.md
Retrieved: 2026-08-27

## Recursive scanning, and how it differs for plugins vs. project/user scope

> Claude Code scans `.claude/agents/` and `~/.claude/agents/` recursively, so you can
> organize definitions into subfolders such as `agents/review/` or `agents/research/`. The
> subdirectory path doesn't affect how a subagent is identified or invoked, because identity
> comes only from the `name` frontmatter field.

> Plugin `agents/` directories are also scanned recursively. Unlike project and user scopes,
> a subfolder inside a plugin's `agents/` directory becomes part of the [scoped
> identifier](#invoke-subagents-explicitly): a file at `agents/review/security.md` in plugin
> `my-plugin` registers as `my-plugin:review:security`.

So: any Markdown file anywhere under a plugin's `agents/` tree — including nested
subdirectories — is discovered, not only files directly in `agents/`. For a plugin, unlike
project/user scope, the subfolder path becomes part of the registered scoped name.

## Which files are skipped, and how

From the "Subagent files Claude Code skips" section, stated for project/user/managed/
`--add-dir` `agents` directories:

> Claude Code skips a file in a project, user, or managed `agents` directory, or in one under
> a directory you add with `--add-dir`, without reporting it in the session, when the
> frontmatter has any of these problems:
>
> * **No `name`**: Claude Code treats the file as documentation kept beside your agents.
> * **A `name` that starts with `-` or contains `:`**: Claude Code skips the file and writes
>   an error to the debug log. See the `name` row in the table above.
> * **A `name` but no `description`**: Claude Code skips the file and writes the reason to
>   the debug log.
> * **YAML that doesn't parse**: Claude Code reads no fields from the file, skips it, and
>   writes the parse error to the debug log.
>
> To see the debug log, run Claude Code with `--debug`.

Immediately after, the page states a **different rule for plugin subagents**:

> A [plugin subagent](/docs/en/plugins-reference#agents) whose frontmatter has no `name` or
> doesn't parse still loads, under its filename.

This is a documented divergence: for project/user/managed agents, "no `name`" or "YAML that
doesn't parse" causes the file to be silently skipped (treated as incidental documentation).
For a **plugin's** `agents/` directory, those same two conditions do NOT cause a skip — the
file still loads, registered under its filename instead of a `name` field.

The frontmatter-field table also states, for the `name` field generally:

> Names can't contain `:`, which is reserved for [plugin-scoped
> identifiers](/docs/en/plugins) such as `my-plugin:reviewer`. Claude Code doesn't load a
> file whose name contains one and logs an error to the debug log.

## Naming / file-extension rules

The page's examples use `.md` files throughout (e.g. `.claude/agents/code-reviewer.md`), and
the plugins-reference page states plugin agent "File format: Markdown files describing agent
capabilities." Neither page states whether a non-`.md` file (or a `.md`-suffixed template
file with a different extension pattern, e.g. `foo.tmpl.md`) is excluded by extension, nor
whether files are filtered by extension at all versus attempted as agent definitions
regardless of name. This is not stated by either source.

## Derived observation

Combining the "scanned recursively" statement with the "plugin subagent... still loads,
under its filename" statement (both above): a plugin's `agents/` directory is treated as a
flat pool of candidate files gathered recursively, where the file's *position* in the tree
feeds only the scoped identifier (via subfolder path) and the file's *content* only opts out
of loading through a parse failure elsewhere documented as skip-worthy for other scopes (a
`name` starting with `-` or containing `:`) — since those two skip conditions are not
overridden by the plugin-specific carve-out sentence, they still apply to plugin agents too.
