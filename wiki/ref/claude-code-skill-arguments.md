# How a skill receives and handles arguments (Claude Code)

Source: https://code.claude.com/docs/en/skills.md (the `.md` endpoint of
https://code.claude.com/docs/en/skills), sections "Pass arguments to skills",
"Available string substitutions", "Frontmatter reference", "Using skill frontmatter
outside Claude Code"
Retrieved: 2026-08-23

Why this is saved: guard is considering moving its turn-end dispatch text out of the Stop
hook's `additionalContext` and into a model-invoked skill that is handed the turn's
`prompt_id` as an argument. Whether the MODEL (not only the user) can pass an argument, and
what happens when it passes none, decides whether that design can identify the turn at all.

## Both invocation paths carry arguments

> ### Pass arguments to skills
>
> Both you and Claude can pass arguments when invoking a skill. Arguments are available via
> the `$ARGUMENTS` placeholder.

> If you invoke a skill with arguments but the skill doesn't include `$ARGUMENTS`, Claude
> Code appends `ARGUMENTS: <your input>` to the end of the skill content so Claude still
> sees what you typed.

## The placeholders

> | `$ARGUMENTS`            | All arguments passed when invoking the skill. If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`. |
> | `$ARGUMENTS[N]`         | Access a specific argument by 0-based index, such as `$ARGUMENTS[0]` for the first argument. |
> | `$N`                    | Shorthand for `$ARGUMENTS[N]`, such as `$0` for the first argument or `$1` for the second. |
> | `$name`                 | Named argument declared in the `arguments` frontmatter list. Names map to positions in order, so with `arguments: [issue, branch]` the placeholder `$issue` expands to the first argument and `$branch` to the second. |

## What happens when an argument is missing — the two behaviours differ

> Indexed arguments use shell-style quoting, so wrap multi-word values in quotes to pass
> them as a single argument. For example, `/my-skill "hello world" second` makes `$0` expand
> to `hello world` and `$1` to `second`. The `$ARGUMENTS` placeholder always expands to the
> full argument string as typed.

> An indexed placeholder with no corresponding argument, such as `$2` when only one argument
> was passed, stays in the content unchanged. A named placeholder from the `arguments`
> frontmatter with no matching argument expands to an empty string.

## The two frontmatter fields involved

> | `argument-hint`            | No          | Hint shown during autocomplete to indicate expected arguments. Example: `[issue-number]` or `[filename] [format]`. |
> | `arguments`                | No          | Named positional arguments for `$name` substitution in the skill content. Accepts a space-separated string or a YAML list. Names map to argument positions in order. |

## Where these fields do not exist

> Claude Code accepts every field in the table above. Outside Claude Code, you can use only
> the fields in the Agent Skills spec:
>
> | Claude Code skills at any level, including plugin skills | Every field in the table above |
> | claude.ai skill uploads, the Skills API, and packaging with `package_skill.py` from anthropics/skills | `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` |

> If you include any field the spec doesn't allow, packaging or upload fails with a hard
> error instead of ignoring the field:
>
> ```
> Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name
> ```

> Claude Code-only body features, such as dynamic context injection, don't function in
> claude.ai chat or through the API.

## What guard takes from this

- A model-invoked skill can be handed the turn id, so the dispatch does not have to
  re-derive its target from session state.
- Use a NAMED argument (`arguments: [turn]` → `$turn`), not `$0`. An unpassed `$0` stays in
  the content as the literal text `$0`, which reads as data to the model; an unpassed named
  argument becomes empty, which a body can test for and report.
- `argument-hint`, `arguments`, `user-invocable` and `!` injection are Claude Code-only.
  Anything that must also work under Codex has to survive without them.
