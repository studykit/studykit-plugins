# Claude Code — what drives automatic invocation of a skill vs a subagent

Source: https://code.claude.com/docs/en/skills.md and https://code.claude.com/docs/en/sub-agents.md (both fetched with `curl -sSL '<url>'`)
Retrieved: 2026-08-27

## Subagents: the description is the whole selection signal

From `sub-agents`:

> Each subagent runs in its own context window with a custom system prompt, specific tool
> access, and independent permissions. When Claude encounters a task that matches a
> subagent's description, it delegates to that subagent, which works independently and
> returns results.

> Claude uses each subagent's description to decide when to delegate tasks. When you create a
> subagent, write a clear description so Claude knows when to use it.

The frontmatter table, on the two required fields:

> | Field | Required | Description |
> | `description` | Yes | When Claude should delegate to this subagent |

A subagent with no description is not loaded at all:

> * **A `name` but no `description`**: Claude Code skips the file and writes the reason to the
>   debug log.

The page documents no other automatic-selection input — no trigger-phrase field, no path or
glob gate, and no stated length limit on `description`.

## Skills: the description also decides, and two further fields feed the same decision

From `skills`, the frontmatter table:

> | `description` | Recommended | What the skill does and when to use it. Claude uses this to
> decide when to apply the skill. If omitted, uses the first paragraph of markdown content.
> Put the key use case first: the combined `description` and `when_to_use` text is truncated
> at 1,536 characters in the skill listing to reduce context usage. |

> | `when_to_use` | No | Additional context for when Claude should invoke the skill, such as
> trigger phrases or example requests. Appended to `description` in the skill listing and
> counts toward the 1,536-character cap. |

> | `paths` | No | Glob patterns that limit when this skill is activated. Accepts a
> comma-separated string or a YAML list. When set, Claude loads the skill automatically only
> when working with files matching the patterns. Uses the same format as path-specific rules. |

On what is in context before invocation:

> | (default) | Yes | Yes | Description always in context, full skill loads when invoked |
> | `disable-model-invocation: true` | Yes | No | Description not in context, full skill loads when you invoke |
> | `user-invocable: false` | No | Yes | Description always in context, full skill loads when invoked |

> In a regular session, skill descriptions are loaded into context so Claude knows what's
> available, but full skill content only loads when invoked.

Also on the same page, `context: fork` and `agent` run a skill's body in a subagent:

> | `context` | No | Set to `fork` to run in a forked subagent context. |
> | `agent` | No | Which subagent type to use when `context: fork` is set. |

And `allowed-tools`, which has no subagent-frontmatter counterpart on the sub-agents page:

> | `allowed-tools` | No | Tools Claude can use without asking permission during the turn that
> invokes this skill. The grant clears when you send your next message. |

## The one piece of official guidance on a definition that is not being picked

From `skills`:

> If a skill seems to stop influencing behavior after the first response, the content is
> usually still present and the model is choosing other tools or approaches. Strengthen the
> skill's `description` and instructions so the model keeps preferring it, or use
> [hooks](/docs/en/hooks) to enforce behavior deterministically.

## What the pages do not say

Recorded as absences, since the question they were fetched for turns on them.

- Neither page states any **relative weighting** between a skill listing and the subagent
  listing at selection time, nor any ordering, priority, or preference between the two
  surfaces. Both are described as description-driven and nothing compares them.
- The sub-agents page states no character cap on `description` and no trigger-phrase or
  path-glob field; whether one exists undocumented is not addressed.
- Neither page gives a measurement or a rate for how often either surface is picked.

**Derived, not stated by either page:** the documented asymmetries in what feeds the automatic
decision run one way only — `when_to_use` and `paths` exist for skills and have no counterpart
in the subagent frontmatter table, while the 1,536-character cap on the combined
`description` + `when_to_use` listing text exists for skills and is not stated for subagents.
This rests on the two frontmatter tables quoted above and on the absence noted in the first
bullet.
