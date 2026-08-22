# String substitutions in skill and command content

Source: https://code.claude.com/docs/en/skills.md (the `.md` endpoint of
https://code.claude.com/docs/en/skills — `slash-commands.md` redirects to the same page)
Retrieved: 2026-08-22

Excerpts are verbatim. They settle which placeholder a plugin skill or flat command file
may use to reach a script bundled elsewhere in the plugin.

## Commands and skills are the same mechanism

> **Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md`
> and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same
> way. Your existing `.claude/commands/` files keep working. Skills add optional features:
> a directory for supporting files, frontmatter to control whether you or Claude invokes
> them, and the ability for Claude to load them automatically when relevant.

## The substitution table

> | `$ARGUMENTS`            | All arguments passed when invoking the skill. If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`. |
> | `$ARGUMENTS[N]`         | Access a specific argument by 0-based index, such as `$ARGUMENTS[0]` for the first argument. |
> | `$N`                    | Shorthand for `$ARGUMENTS[N]`, such as `$0` for the first argument or `$1` for the second. |
> | `$name`                 | Named argument declared in the `arguments` frontmatter list. Names map to positions in order, so with `arguments: [issue, branch]` the placeholder `$issue` expands to the first argument and `$branch` to the second. |
> | `${CLAUDE_SESSION_ID}`  | The current session ID. Useful for logging, creating session-specific files, or correlating skill output with sessions. |
> | `${CLAUDE_EFFORT}`      | The current effort level: `low`, `medium`, `high`, `xhigh`, or `max`. Ultracode is not a distinct level and reports as `xhigh`. Use this to adapt skill instructions to the active effort setting. |
> | `${CLAUDE_SKILL_DIR}`   | The directory containing the skill's `SKILL.md` file. For plugin skills, this is the skill's subdirectory within the plugin, not the plugin root. Use this in bash injection commands to reference scripts or files bundled with the skill, regardless of the current working directory. |
> | `${CLAUDE_PROJECT_DIR}` | The project root directory. This is the same path hooks and MCP servers receive as `CLAUDE_PROJECT_DIR`. Use this to reference project-local scripts or files, such as `${CLAUDE_PROJECT_DIR}/.claude/hooks/helper.sh`, independent of where the skill is installed. |
> | `${CLAUDE_PLUGIN_ROOT}` | The plugin's installation directory. Substituted only in plugin skills. Use this to reference scripts or files bundled anywhere in the plugin, including resources shared between the plugin's skills. See plugin environment variables. |
> | `${CLAUDE_PLUGIN_DATA}` | The plugin's persistent data directory, which survives plugin updates. Substituted only in plugin skills. Use this to reference installed dependencies, generated files, or caches that must outlive an update. |

## Where the substitution happens

> Claude Code substitutes `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` in two places:
> the skill's markdown content, and Bash rules in the `allowed-tools` frontmatter. In a
> plugin skill, Claude Code substitutes `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}`
> in the same two places. Using the same variable in both places lets a skill run a bundled
> script without a permission prompt.

> The `${CLAUDE_PROJECT_DIR}` substitution requires Claude Code v2.1.196 or later.

## Bearing on guard

`${CLAUDE_PLUGIN_ROOT}` **is** substituted in a plugin skill's markdown content — the row
above says so, and the paragraph after the table names the content as one of the two places
it happens. `guide/adapter-guide.md` said the opposite ("No documented
`${CLAUDE_PLUGIN_ROOT}` skill-content substitution; use `${CLAUDE_SKILL_DIR}` for
skill-local files"); that line was corrected against this page.

The distinction the table draws is scope, not availability: `${CLAUDE_SKILL_DIR}` is the
skill's own subdirectory, `${CLAUDE_PLUGIN_ROOT}` is the plugin. guard's single CLI is
`scripts/guard_hook.py` at the plugin root, shared by every skill, which is exactly the
"resources shared between the plugin's skills" case the plugin-root row names. So
`commands/settings.md` reaches it as `${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py` rather
than climbing out with `${CLAUDE_SKILL_DIR}/../../`, and the path survives the file moving
between `skills/<name>/SKILL.md` and `commands/<name>.md`.

The merge excerpt is why moving `settings` from `skills/` to `commands/` changes nothing
the user sees: same `/guard:settings` invocation, same frontmatter, same
`disable-model-invocation`. A flat file gives up only the skill directory for bundled
files, which `settings` never had.
