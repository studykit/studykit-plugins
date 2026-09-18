"""The per-session state file, ``state/<sid>.json``.

Holds the agent modes as of this session, the plan gate state, the files this
session has edited since the last file-audit checkpoint
(``edited_prompt_id`` / ``edited_files`` / ``edited_agent_docs`` / ``edited_refs`` /
``edited_docs``), their per-path source evidence (``edited_provenance``),
``last_audited_prompt_id`` / ``last_audited_fingerprint``, ``pending_verify_prompt_id``,
``transcript_path``, and
``updated_at``.

Both the ``default`` dict and the ``keys`` tuple in ``_read_state`` are the schema, and a new
key must be added to BOTH. A key missing from ``keys`` is written by whoever set it and then
dropped on the very next read, which looks exactly like the writer never ran — that is how
``edited_refs`` behaved for its first hour of existence.
"""

from __future__ import annotations

import hashlib
import json

from pathlib import Path
from typing import Any

from .config import AUDIT_PLAN_KEY, _agent_mode, _audit_on
from .paths import _now_iso, _state_file
from .agents import SETTABLE_AGENTS


def _read_state(project_dir: Path, session_id: str, config: dict[str, Any]) -> dict[str, Any]:
    default = {
        **{key: str(_agent_mode(config, key)) for key in SETTABLE_AGENTS},
        # The last file-checkpoint snapshot. The token is the hash printed to the checkpoint
        # skill; the paths and hashes let completion remove only revisions that were actually
        # reviewed. A file edited while reviews are running stays pending.
        "file_checkpoints": {},
        # Legacy once-per-turn fields retained while old state files age out. Stop no longer
        # dispatches file audits, so these are not written by current code.
        "last_audited_prompt_id": "",
        "last_audited_fingerprint": "",
        # The most recent auditable turn's id. CODEX ONLY as of v0.122.0 — that adapter keeps
        # its own turn record because its transcript is not a stable hook interface, so it has
        # nowhere else to resolve "the turn just finished" from. Claude stopped writing it when
        # the Stop hook stopped recording turns; there, `guard-inputs` walks the transcript
        # instead. It stays in this shared module, and in the preserved-key list below, because
        # `hook_codex` reads and writes it through these two functions: drop it and the Codex
        # marker is silently erased on the next write.
        "pending_verify_prompt_id": "",
        # The session's transcript, recorded at SessionStart, whose payload carries it. It is
        # the HOST's path and guard will not guess at the host's storage layout, so it has to
        # be taken from a payload; it is a session-long fact, so once is enough.
        "transcript_path": "",
        # Files written since the last checkpoint, accumulated by PostToolUse and read by the
        # explicit `audit-files` entry. `edited_prompt_id` is diagnostic only: it records the
        # most recent turn that added an edit and never scopes the queue. Four lists — the split is by
        # which agent can judge the file (source code for `comment-corrector`, instruction
        # files for `agents-md-auditor`, saved references for `ext-docs-auditor`, ordinary
        # documents for `doc-auditor`), while "which turn was this" is the same question for
        # all of them and a second marker could only drift from the first.
        "edited_prompt_id": "",
        "edited_files": [],
        "edited_agent_docs": [],
        "edited_refs": [],
        "edited_docs": [],
        "edited_truncated": {},
        # Per-path evidence for the current edit lists. Native file tools name an exact
        # target; shell detection infers targets from a worktree diff. The distinction lets
        # Stop state Bash candidates conditionally instead of asserting that a worktree-wide
        # diff proves this session wrote them.
        "edited_provenance": {},
        # The plan audit keeps a config key and is a SEPARATE state key, because it is the
        # one audit that is NOT invoked by the user: `exit-plan` blocks an approved plan on
        # its own, so whether a session opens with that gate armed is a real question a
        # project can answer in advance — which is exactly what the turn side stopped being.
        "plan_audit_paused": not _audit_on(config, AUDIT_PLAN_KEY),
        # Which plan this session has already audited, as a hash of the plan text. The
        # ExitPlanMode hook lets a plan through once its audit is recorded here and blocks
        # it otherwise; hashing the CONTENT rather than setting a flag is what makes a
        # revised plan a new plan — edit it after the audit and the hash no longer matches,
        # so the next ExitPlanMode is blocked again and the audit runs against what the user
        # will actually see.
        "plan_audited_hash": None,
        # Has this session already been told where the turn closeout file is? The path is
        # static for the whole install, so the Stop block repeats it only until something has
        # stated it once: `session-start` sets this when it names the file, and clears it when
        # it does not (a session that opened muted was never told), so the first armed turn
        # supplies it and no later turn pays for it again. SessionStart fires on `compact` too
        # on both hosts, which is what makes this safe against a compaction dropping the line —
        # the event that re-states the path is the same event that re-sets the flag.
        "updated_at": None,
    }
    path = _state_file(project_dir, session_id)
    if not path.is_file():
        return default
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return default
    if not isinstance(data, dict):
        return default
    keys = (*SETTABLE_AGENTS, "last_audited_prompt_id", "last_audited_fingerprint",
            "pending_verify_prompt_id", "file_checkpoints",
            "transcript_path", "plan_audit_paused", "plan_audited_hash",
            "edited_prompt_id", "edited_files",
            "edited_agent_docs", "edited_refs", "edited_docs", "edited_truncated",
            "edited_provenance",
            "updated_at")
    default.update({k: data[k] for k in keys if k in data})
    return default


def _write_state(project_dir: Path, session_id: str, state: dict[str, Any]) -> None:
    state["updated_at"] = _now_iso()
    path = _state_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        pass


def _edited_files(state: dict[str, Any], prompt_id: str, bucket: str) -> list[str]:
    """The pending files of one bucket, as recorded by PostToolUse.

    ``prompt_id`` remains in the signature for compatibility with callers on both host
    adapters; it no longer scopes the result. A file that was later deleted or moved leaves
    nothing to audit, and
    handing an agent a missing path would spend it on a read failure.
    """
    files = state.get(bucket)
    if not isinstance(files, list):
        return []
    return [f for f in files if isinstance(f, str) and f and Path(f).is_file()]


def _edit_source(state: dict[str, Any], path: str) -> str | None:
    """Whether a recorded path came from an exact native target or a shell diff."""
    provenance = state.get("edited_provenance")
    if not isinstance(provenance, dict):
        return None
    evidence = provenance.get(path)
    if not isinstance(evidence, dict):
        return None
    source = evidence.get("source")
    return source if source in ("native", "shell") else None


def _edited_fingerprint(state: dict[str, Any], prompt_id: str) -> str:
    """Hash the current contents of the retained pending edit set and overflow counts."""
    digest = hashlib.sha256()
    for bucket in ("edited_files", "edited_agent_docs", "edited_refs", "edited_docs"):
        for raw in _edited_files(state, prompt_id, bucket):
            path = Path(raw)
            digest.update(bucket.encode())
            digest.update(b"\0")
            digest.update(raw.encode(errors="surrogateescape"))
            digest.update(b"\0")
            try:
                with path.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
            except OSError:
                continue
    truncated = state.get("edited_truncated")
    if isinstance(truncated, dict):
        digest.update(json.dumps(truncated, sort_keys=True).encode())
    provenance = state.get("edited_provenance")
    if isinstance(provenance, dict):
        digest.update(json.dumps(provenance, sort_keys=True).encode())
    return digest.hexdigest()


def _plan_audit_paused(state: dict[str, Any]) -> bool:
    """Whether the plan audit is muted for this session.

    ``_read_state`` seeds this key from the config on every read, so a dict reaching here
    without one did not come from there, and
    the honest answer for a missing key is the config default — armed.
    """
    return state.get("plan_audit_paused") is True
