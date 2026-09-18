"""Plan-review policy and completion shared by host adapters.

Callers supply concrete project, session and plan values. This module does not parse host
payloads, command arguments or environment variables, and never dispatches a model itself.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any

from .config import ReviewAction, _load_config, _plan_review_action
from .state import _plan_audit_paused, _read_state, _write_state


@dataclass(frozen=True)
class PlanReviewDecision:
    status: str
    reviewer: ReviewAction | None = None


def plan_hash(plan: str) -> str:
    """Ignore edge whitespace, but require another review for every other content change."""
    return hashlib.sha256(plan.strip().encode("utf-8")).hexdigest()


def select_review(config: dict[str, Any], state: dict[str, Any], plan: str,
                  *, explicit: bool = False) -> PlanReviewDecision:
    if not plan.strip():
        return PlanReviewDecision("no_plan_text")
    # A direct user request is a fresh review, even when automatic reviews are muted or
    # this content was already audited. Neither condition cancels an explicit request.
    if not explicit:
        if _plan_audit_paused(state):
            return PlanReviewDecision("muted")
        if state.get("plan_audited_hash") == plan_hash(plan):
            return PlanReviewDecision("audited")
    action, configured = _plan_review_action(config)
    if not configured:
        return PlanReviewDecision("no_reviewer")
    if action is None:
        return PlanReviewDecision("invalid_plan_review")
    return PlanReviewDecision("review", action)


def read_plan(path: Path) -> tuple[Path, str]:
    resolved = path.expanduser().resolve(strict=True)
    plan = resolved.read_text(encoding="utf-8")
    if not plan.strip():
        raise ValueError("The plan file is empty")
    return resolved, plan


def prepare_review(project_dir: Path, session_id: str, path: Path) -> dict[str, Any]:
    resolved, plan = read_plan(path)
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    decision = select_review(config, state, plan, explicit=True)
    if decision.status == "invalid_plan_review":
        raise ValueError("plan_review must name an installed agent or skill other than audit-plan")
    result: dict[str, Any] = {"status": decision.status, "plan_path": str(resolved)}
    if decision.reviewer is not None:
        result["reviewer"] = {"kind": decision.reviewer.kind, "name": decision.reviewer.name}
    return result


def record_plan_audit(project_dir: Path, session_id: str, plan: str) -> str:
    if not plan.strip():
        raise ValueError("The plan file is empty")
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    digest = plan_hash(plan)
    state["plan_audited_hash"] = digest
    _write_state(project_dir, session_id, state)
    # State writes elsewhere intentionally fail open. An explicit completion must not
    # report success when its stamp was not saved.
    if _read_state(project_dir, session_id, config).get("plan_audited_hash") != digest:
        raise OSError("Could not persist the plan audit record")
    return digest
