"""Regression tests for `_find_issue_link_id` direction handling.

Jira's REST API populates exactly one of ``outwardIssue`` / ``inwardIssue``
per ``issuelinks`` entry — the side that is *not* the current issue. The
populated field therefore depends on which end of the link the source issue
lives on, not on the mapping's nominal direction. ``_find_issue_link_id``
must match either populated field; see issue #131.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from issue.jira.provider import (  # noqa: E402
    _find_issue_link_id,
    _JiraRelationshipMapping,
    _ResolvedJiraRelationshipOperation,
)


def _operation(direction: str, *, target_issue: str = "TEST-200") -> _ResolvedJiraRelationshipOperation:
    mapping = _JiraRelationshipMapping(
        relationship="related",
        surface="issue_link",
        link_type="Relates",
        direction=direction,
    )
    return _ResolvedJiraRelationshipOperation(
        action="remove",
        relationship="related",
        target_ref=target_issue,
        mapping=mapping,
        target_issue=target_issue,
    )


def _issue_with_link(link: dict[str, Any]) -> dict[str, Any]:
    return {"fields": {"issuelinks": [link]}}


def _link(link_id: str, link_type: str, *, outward: str | None = None, inward: str | None = None) -> dict[str, Any]:
    entry: dict[str, Any] = {"id": link_id, "type": {"name": link_type}}
    if outward is not None:
        entry["outwardIssue"] = {"key": outward}
    if inward is not None:
        entry["inwardIssue"] = {"key": inward}
    return entry


@pytest.mark.parametrize(
    ("direction", "populated_side"),
    [
        ("outward", "outward"),
        ("outward", "inward"),
        ("inward", "outward"),
        ("inward", "inward"),
    ],
)
def test_find_issue_link_id_matches_either_populated_side(direction: str, populated_side: str) -> None:
    kwargs = {populated_side: "TEST-200"}
    issue = _issue_with_link(_link("9001", "Relates", **kwargs))

    link_id = _find_issue_link_id(issue, _operation(direction))

    assert link_id == "9001"


def test_find_issue_link_id_returns_none_when_link_type_mismatches() -> None:
    issue = _issue_with_link(_link("9001", "Blocks", outward="TEST-200"))

    assert _find_issue_link_id(issue, _operation("outward")) is None


def test_find_issue_link_id_returns_none_when_target_not_present() -> None:
    issue = _issue_with_link(_link("9001", "Relates", outward="TEST-999"))

    assert _find_issue_link_id(issue, _operation("outward")) is None
