#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Turn-end audit of the two document kinds this repository keeps getting wrong.

This is repo-local machinery, not part of any plugin: it enforces the rules in the root
`AGENTS.md` against the files that a session in *this* checkout edits. Nothing here ships.

Two buckets, two auditors, both defined in `.claude/agents/`:

- `AGENTS.md` / `CLAUDE.md`  -> `contributor-docs-auditor`
- `plugins/*/agents/*.md`    -> `plugin-agent-doc-auditor`

`PostToolUse` only records paths; the dispatch is asked for once, at `Stop`. Recording and
dispatching are split for two reasons. A turn usually edits the same file several times, and
an auditor pointed at a half-finished edit reports findings the next `Edit` already fixed.
And an audit request that arrives mid-turn competes with the work the user asked for, while
one that arrives at `Stop` lands when the turn is otherwise done.

Fail-open throughout, and every exit is 0: a broken audit trigger must not break an edit.

Facts this rests on (docs at `wiki/ref/`, cited in the index there):
- `${CLAUDE_PROJECT_DIR}` reaches this file from `settings.json`; `prompt_id` / `session_id`
  are common payload fields (`claude-code-hook-command-placeholders.md`).
- `Stop` takes `hookSpecificOutput.additionalContext` and keeps the conversation going, so
  the main agent can act on the text (`claude-code-stop-hook-decision-control.md`).
- `PostToolUse` fires for a subagent's writes as well (`claude-code-hooks-in-subagents.md`),
  which is wanted: a doc rewritten by a delegate needs auditing as much as one the main
  agent wrote.
"""

from __future__ import annotations

import json
import os
import re
import sys

from pathlib import Path

# Cap on the files one turn may hand an auditor. Past this the list has stopped being an
# audit target and become a sweep: each auditor reads every file in full, plus whatever it
# points at.
FILES_MAX = 12

_SESSION_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")

# Filenames the host loads as standing instruction. Matched on the name because that is what
# the host looks for; every other markdown file in this repo is prose nobody is instructed by.
_CONTRIBUTOR_DOC_NAMES = frozenset({"agents.md", "claude.md"})

# Bucket -> the agent that audits it. The key is also the state-file key.
AUDITORS: dict[str, str] = {
    "contributor_docs": "contributor-docs-auditor",
    "plugin_agent_docs": "plugin-agent-doc-auditor",
}

_DISPATCH_LEAD = {
    "contributor_docs": (
        "This turn edited agent instruction files. Dispatch `{agent}` (Agent tool, "
        "`subagent_type: \"{agent}\"`) over the files below, then act on its report — "
        "fix what it finds, or say why a finding stands."
    ),
    "plugin_agent_docs": (
        "This turn edited plugin agent definitions, which install into other people's "
        "repositories. Dispatch `{agent}` (Agent tool, `subagent_type: \"{agent}\"`) over "
        "the files below, then act on its report — fix what it finds, or say why a finding "
        "stands."
    ),
}


# --------------------------------------------------------------------------- #
# payload / state
# --------------------------------------------------------------------------- #
def _payload() -> dict | None:
    try:
        raw = sys.stdin.read()
    except OSError:
        return None
    if not raw.strip():
        return None
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _project_dir(payload: dict) -> Path | None:
    raw = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd")
    if not isinstance(raw, str) or not raw:
        return None
    try:
        return Path(raw).resolve()
    except OSError:
        return None


def _session_id(payload: dict) -> str | None:
    sid = payload.get("session_id")
    if not isinstance(sid, str) or not sid:
        return None
    # Interpolated into a filename below, so anything that could escape the state
    # directory is rejected rather than sanitized.
    if ".." in sid or not _SESSION_ID_RE.match(sid):
        return None
    return sid


def _state_path(project_dir: Path, session_id: str) -> Path:
    # `.claude/tmp/` is already gitignored at any depth; this is per-session scratch.
    return project_dir / ".claude" / "tmp" / "doc-audit" / f"{session_id}.json"


def _read_state(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_state(path: Path, state: dict) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass


# --------------------------------------------------------------------------- #
# classification
# --------------------------------------------------------------------------- #
def _target(project_dir: Path, tool_input: object) -> Path | None:
    if not isinstance(tool_input, dict):
        return None
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not isinstance(raw, str) or not raw:
        return None
    try:
        target = Path(raw)
        if not target.is_absolute():
            target = project_dir / target
        # Resolved so a relative path or `..` cannot dodge the location tests below.
        return target.resolve()
    except OSError:
        return None


def _bucket(project_dir: Path, target: Path) -> str | None:
    """Which auditor's bucket this path belongs in, if any.

    Order matters: the name test runs first so that an `AGENTS.md` that happens to sit in a
    plugin's `agents/` directory is judged as the instruction file it is, not as an agent
    definition.
    """
    if project_dir not in target.parents:
        return None
    try:
        rel = target.relative_to(project_dir)
    except ValueError:
        return None
    parts = rel.parts
    # Session scratch and subagent memory stores are records, not documents.
    if ".claude" in parts or ".codex" in parts:
        return None
    if target.name.lower() in _CONTRIBUTOR_DOC_NAMES:
        # `wiki/ref/` keeps its index under the same name. That file is a table of saved
        # references doing its job, and the contributor-doc axes would fault it for it.
        if len(parts) >= 2 and parts[0] == "wiki" and parts[1] == "ref":
            return None
        return "contributor_docs"
    if (len(parts) == 4 and parts[0] == "plugins" and parts[2] == "agents"
            and target.suffix.lower() == ".md"):
        return "plugin_agent_docs"
    return None


# --------------------------------------------------------------------------- #
# subcommands
# --------------------------------------------------------------------------- #
def cmd_post_edit() -> int:
    payload = _payload()
    if payload is None:
        return 0
    project_dir = _project_dir(payload)
    session_id = _session_id(payload)
    prompt_id = payload.get("prompt_id")
    if project_dir is None or session_id is None:
        return 0
    if not isinstance(prompt_id, str) or not prompt_id:
        return 0
    target = _target(project_dir, payload.get("tool_input"))
    if target is None:
        return 0
    bucket = _bucket(project_dir, target)
    if bucket is None:
        return 0

    path = _state_path(project_dir, session_id)
    state = _read_state(path)
    # A new turn clears BOTH buckets off the one marker. Clearing only the bucket being
    # written would leave the other holding last turn's files under this turn's id.
    if state.get("prompt_id") != prompt_id:
        state = {"prompt_id": prompt_id}
    files = state.get(bucket)
    if not isinstance(files, list):
        files = []
    entry = str(target)
    if entry not in files and len(files) < FILES_MAX:
        files.append(entry)
        state[bucket] = files
        _write_state(path, state)
    return 0


def cmd_stop() -> int:
    payload = _payload()
    if payload is None:
        return 0
    # Re-entry guard: the dispatch this hook asks for runs inside the same turn, and Stop
    # fires again when it finishes. Continuing twice would ask for the audit of the audit.
    if payload.get("stop_hook_active") is True:
        return 0
    project_dir = _project_dir(payload)
    session_id = _session_id(payload)
    prompt_id = payload.get("prompt_id")
    if project_dir is None or session_id is None:
        return 0
    if not isinstance(prompt_id, str) or not prompt_id:
        return 0

    path = _state_path(project_dir, session_id)
    state = _read_state(path)
    if state.get("prompt_id") != prompt_id:
        return 0
    if state.get("dispatched_prompt_id") == prompt_id:
        return 0

    blocks: list[str] = []
    for bucket, agent in AUDITORS.items():
        files = state.get(bucket)
        if not isinstance(files, list) or not files:
            continue
        lead = _DISPATCH_LEAD[bucket].format(agent=agent)
        listing = "\n".join(f"- {f}" for f in files if isinstance(f, str))
        blocks.append(f"{lead}\n{listing}")
    if not blocks:
        return 0

    state["dispatched_prompt_id"] = prompt_id
    _write_state(path, state)
    json.dump({"hookSpecificOutput": {"hookEventName": "Stop",
                                      "additionalContext": "\n\n".join(blocks)}}, sys.stdout)
    return 0


_COMMANDS = {"post-edit": cmd_post_edit, "stop": cmd_stop}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in _COMMANDS:
        return 0
    try:
        return _COMMANDS[sys.argv[1]]()
    except Exception:
        # Fail open, silently. A traceback here would surface as a hook failure on an
        # ordinary edit, which costs more than the missed audit.
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
