"""``post-edit`` (PostToolUse on the write tools).

Two independent jobs, both independent of the agent switches. It records a source file or an
agent instruction file written this turn — the lists the ``comment-corrector`` and
``agents-md-auditor`` recommendations are built from, kept in two buckets that must stay
disjoint (``agents._edited_bucket``). And it requires a file saved inside the refs directory
to be listed in that directory's ``AGENTS.md``, blocking until it is.
"""

from __future__ import annotations

import json
import sys

from pathlib import Path
from typing import Any

from .config import _load_config
from .paths import _project_dir, _project_rel, _refs_dir, _state_root, _trace
from .payload import _read_payload, _session_id
from .agents import _edited_bucket
from .state import _read_state, _write_state


# Cap on the files one turn may hand a file-reading agent. Past this the list stops
# being an audit target and becomes a sweep of the whole change: the agent must read
# every file in full to judge it — a comment against the code under it, an instruction
# file against what it points at — and the skills that dispatch these by hand ask the
# user to narrow at roughly this size for the same reason. Recording stops at the cap
# rather than dropping the oldest entries — the earliest edits of a turn are as worth
# auditing as the last, and a stable prefix keeps the recommendation reproducible.
EDITED_FILES_MAX = 20


def _record_edited_source(project_dir: Path, payload: dict, tool_input: Any,
                          config: dict[str, Any]) -> None:
    """Note a file this turn wrote, for a later file-reading agent's recommendation.

    Two lists, chosen by `_edited_bucket`: source files for `comment-corrector`, agent
    instruction files for `agents-md-auditor`. Anything else is not recorded — an agent
    handed a file its criteria say nothing about spends its context proving that.

    Only inside the project: an audit of a file outside the working tree is not this
    turn's work to fix. Files under guard's own state are excluded too — a turn slice is
    a record, not code, and guard's own `AGENTS.md` under the refs dir is an index the
    `post-edit` refs check already governs.

    Silent and best-effort. A miss here costs one skipped recommendation; a raise here
    would surface as a hook failure on an ordinary edit, which is far worse.
    """
    prompt_id = payload.get("prompt_id")
    session_id = _session_id(payload)
    if not isinstance(prompt_id, str) or not prompt_id or session_id is None:
        return
    target = _tool_target_path(project_dir, tool_input)
    if target is None:
        return
    bucket = _edited_bucket(target)
    if bucket is None:
        return
    try:
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
    except OSError:
        return
    if project not in target.parents or state_root in target.parents:
        return

    state = _read_state(project_dir, session_id, config)
    # A new turn resets BOTH lists off the one marker; without this, files from the
    # previous turn would ride along into this turn's recommendation. Resetting only the
    # bucket being written would leave the other holding the previous turn's files under
    # this turn's id, which is the same bug with an extra step.
    if state.get("edited_prompt_id") != prompt_id:
        state["edited_prompt_id"] = prompt_id
        state["edited_files"] = []
        state["edited_agent_docs"] = []
    files = state[bucket]
    if not isinstance(files, list):
        files = []
    path = str(target)
    if path in files or len(files) >= EDITED_FILES_MAX:
        return
    files.append(path)
    state[bucket] = files
    _write_state(project_dir, session_id, state)
    _trace(project_dir, session_id, "post-edit", "edited_recorded",
           prompt_id=prompt_id, bucket=bucket, file=target.name, count=len(files))


def _tool_target_path(project_dir: Path, tool_input: Any) -> Path | None:
    """Absolute, resolved target path of a mutating tool call, or None.

    Reads the path from the PreToolUse `tool_input` (`file_path` for
    Write/Edit/MultiEdit, `notebook_path` for NotebookEdit). Resolving means a
    relative path or `..` cannot smuggle a write past the path-based checks below.
    """
    if not isinstance(tool_input, dict):
        return None
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not isinstance(raw, str) or not raw:
        return None
    try:
        target = Path(raw)
        if not target.is_absolute():
            target = project_dir / target
        return target.resolve()
    except OSError:
        return None


def _targets_refs_dir(project_dir: Path, tool_input: Any, config: dict[str, Any]) -> bool:
    """True when a mutating tool's target path is inside the refs directory
    (`wiki/ref/` by default, or the validated `refs_dir` config path)."""
    target = _tool_target_path(project_dir, tool_input)
    if target is None:
        return False
    try:
        refs = _refs_dir(project_dir, config).resolve()
    except OSError:
        return False
    return target == refs or refs in target.parents


REFS_INDEX_NAME = "AGENTS.md"


# Files in the refs dir that are the index machinery itself, never indexed entries.
_REFS_INDEX_SKIP = {REFS_INDEX_NAME, "CLAUDE.md"}


def cmd_post_edit() -> int:
    """PostToolUse on the file-writing tools. Two jobs on the one payload.

    1. Record the source file, if that is what was written, against this turn — the
       list `comment-corrector` is pointed at when Stop recommends it. This is the event
       that actually sees the path, so nothing has to be reconstructed from a transcript
       later; Stop only reads back what accumulated here.
    2. Require a file saved inside the refs dir to be listed in the refs index
       (``AGENTS.md``). A saved reference nothing points at is a file the next reader
       never finds, so the index is the deliverable, not a courtesy. This fires *after*
       the write rather than blocking it: the natural order is save-then-index, and
       blocking the save would force an index entry for a file that does not exist yet.

    Job 2 blocks with ``decision: "block"`` so the reason returns to the model as work
    to finish; job 1 never emits anything. Silent in every other case — a write outside
    the refs dir, the index itself, or a file already listed.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0

    config = _load_config(project_dir)
    tool_input = payload.get("tool_input")
    _record_edited_source(project_dir, payload, tool_input, config)
    if not _targets_refs_dir(project_dir, tool_input, config):
        return 0
    target = _tool_target_path(project_dir, tool_input)
    if target is None or target.name in _REFS_INDEX_SKIP:
        return 0

    reason = refs_index_gap(project_dir, target, config)
    if reason is None:
        _trace(project_dir, None, "post-edit", "refs_listed", file=target.name)
        return 0

    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    _trace(project_dir, None, "post-edit", "refs_missing", file=target.name)
    return 0


def refs_index_gap(project_dir: Path, target: Path, config: dict[str, Any]) -> str | None:
    """The block reason when ``target`` is missing from the refs index, else None.

    Host-neutral so both adapters enforce one rule. Matching is by file name anywhere
    in the index text rather than by table structure: the index is prose a human
    maintains, and pinning the check to a column layout would fail the moment someone
    reformats it.
    """
    index = _refs_dir(project_dir, config) / REFS_INDEX_NAME
    try:
        if target.name in index.read_text(encoding="utf-8"):
            return None
    except OSError:
        pass  # No index yet: the first saved reference is what creates it.
    return (
        f"guard: `{target.name}` is saved but not listed in the reference index. "
        f"Add a row for it to `{_project_rel(project_dir, index)}` — file name, what "
        "it covers, and the source — so the next reader finds it without opening "
        "every file. Then continue."
    )
