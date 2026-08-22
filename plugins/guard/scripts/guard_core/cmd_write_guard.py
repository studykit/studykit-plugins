"""``pre-write`` — PreToolUse, keeping a report-only agent's writes inside its memory.

The problem this exists for. Declaring ``memory:`` on a subagent silently grants it Write
and Edit; the host documents the grant's *purpose* ("so the subagent can manage its memory
files") but does not scope it, and a measurement confirmed an agent declaring only ``Read``
wrote to an absolute path outside both the project and its memory directory. So an agent
whose description says "Reports; edits nothing" cannot make that true by declaring a tool
list, and prose telling it to stay inside its memory directory was tried and broken: an
auditor wrote its own verdicts down and then cited the note instead of re-deriving the
judgement, which is invisible by construction because a wrong stored verdict suppresses the
finding that would expose it.

A subagent's frontmatter can carry ``hooks:``, which would be the natural home for this, but
the host ignores that field for plugin subagents. What does reach them is the plugin's own
hook manifest: tool events fire inside subagents and the payload carries ``agent_type``.
So the restriction lives here rather than in each definition, which also means an agent
cannot widen it by editing its own file.

The rule is a location, not a per-agent path. Any write under ``.claude/agent-memory/`` or
``.claude/agent-memory-local/`` is allowed; everything else is denied. Naming each agent's
own directory would mean depending on how the host derives that name from a plugin-scoped
agent, and the looser rule costs nothing that matters — one report-only agent writing into
another's memory is a curation problem, not the repository damage this guards against.

Fail open, like every other guard hook: an unreadable payload, an unknown agent, a path that
cannot be resolved all return silently and let the host's normal permission flow decide.
"""

from __future__ import annotations

import json
import sys

from pathlib import Path

from .agents import AGENT_NAMESPACE, AUDIT_AGENTS
from .paths import _project_dir, _trace
from .payload import _read_payload


# Agents that report and never edit. Kept as an explicit set rather than derived from
# `AUDIT_AGENTS`, because what separates these from the rest is not how they are routed but
# whether writing is part of the job: `korean-corrector` edits the answer file in place,
# `comment-corrector` edits the source files it was given, and `docs-fetcher` saves the
# reference it fetched. Restricting those three would mean encoding "the files handed to it
# this turn", which a PreToolUse hook has no way to know.
REPORT_ONLY_AGENTS = frozenset({
    "claims-auditor",
    "deferrals-auditor",
    "clarity-auditor",
    "agents-md-auditor",
    "refs-auditor",
})

# Both memory scopes, because the scope is a project's choice and the rule is about location.
_MEMORY_DIR_NAMES = ("agent-memory", "agent-memory-local")

_WRITE_TOOLS = frozenset({"Write", "Edit", "MultiEdit", "NotebookEdit"})

# The tool-input keys that carry a path. `NotebookEdit` uses `notebook_path`; the rest use
# `file_path`. A tool whose input has neither is not a write this hook can judge.
_PATH_KEYS = ("file_path", "notebook_path")


def _agent_name(payload: dict) -> str | None:
    """The bare agent name for a guard subagent, or None for anything else.

    `agent_type` is absent in the main conversation and carries the plugin-scoped name
    (`guard:claims-auditor`) inside a plugin subagent, so the namespace is stripped here
    rather than being matched against.
    """
    agent_type = payload.get("agent_type")
    if not isinstance(agent_type, str) or not agent_type.startswith(AGENT_NAMESPACE):
        return None
    name = agent_type[len(AGENT_NAMESPACE):]
    return name if name in AUDIT_AGENTS else None


def _target_paths(payload: dict) -> list[str]:
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return []
    found = []
    for key in _PATH_KEYS:
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            found.append(value)
    return found


def _inside_memory(target: str, project_dir: Path | None) -> bool:
    """Whether `target` lands in a memory directory.

    Resolved without touching the filesystem (`strict=False`) so a file that does not exist
    yet — the normal case for a first memory write — is judged the same as one that does.
    A relative path is resolved against the project root when the host gave one, and against
    the process cwd otherwise, which is what a relative path would mean to the tool anyway.
    """
    try:
        path = Path(target)
        if not path.is_absolute() and project_dir is not None:
            path = project_dir / path
        resolved = path.resolve()
    except (OSError, RuntimeError, ValueError):
        return True  # unresolvable: fail open rather than deny on a path we cannot read
    parts = resolved.parts
    for i, part in enumerate(parts):
        if part in _MEMORY_DIR_NAMES and i > 0 and parts[i - 1] == ".claude":
            return True
    return False


def _deny(reason: str) -> None:
    json.dump({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, sys.stdout)


def cmd_pre_write() -> int:
    """PreToolUse on the write tools. Deny a report-only agent writing outside memory.

    Silent for the main conversation, for guard's writing agents, and for any path already
    inside a memory directory — a hook that printed on every edit would be noise on the one
    path that is always fine.
    """
    payload = _read_payload()
    if payload is None:
        return 0
    if payload.get("tool_name") not in _WRITE_TOOLS:
        return 0

    # Traced on every write, not only on a deny. Whether this hook fires at all inside a
    # subagent, and whether the host populated `agent_type` when it did, is the one thing a
    # deny-only trace cannot tell you apart from "no agent ever tried" — and the difference
    # is the whole mechanism. `_trace` writes only when GUARD_TRACE is set.
    _trace(_project_dir(), None, "pre-write", "seen",
           agent=payload.get("agent_type"), tool=payload.get("tool_name"))

    name = _agent_name(payload)
    if name is None or name not in REPORT_ONLY_AGENTS:
        return 0

    project_dir = _project_dir()
    targets = _target_paths(payload)
    if not targets:
        return 0
    outside = [t for t in targets if not _inside_memory(t, project_dir)]
    if not outside:
        return 0

    _trace(project_dir, None, "pre-write", "deny", agent=name, paths=outside)
    _deny(
        f"guard: `{AGENT_NAMESPACE}{name}` reports and never edits, so it may write only "
        f"inside its own agent-memory directory. Blocked: {', '.join(outside)}. "
        "Put the finding in the report instead; the main agent applies it."
    )
    return 0
