"""Tests for Jira issue cache carrier paths and draft parsing."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_jira_data_center_client import JiraDataCenterSite  # noqa: E402
from issue.jira.cache import (  # noqa: E402
    JiraDataCenterIssueCache,
    _comment_author_name,
    is_jira_issue_cache_body_path,
)
from issue.jira.snapshot import _jira_person_display_name  # noqa: E402


def jira_site() -> JiraDataCenterSite:
    return JiraDataCenterSite(base_url="https://jira.example.test", authority="jira.example.test")


def _jira_issue_payload(status_name: str) -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "Issue summary",
            "description": "Body.",
            "labels": [],
            "created": "2026-05-15T09:00:00.000+0900",
            "updated": "2026-05-15T10:00:00.000+0900",
            "status": {"name": status_name, "statusCategory": {"key": "indeterminate"}},
            "comment": {"comments": []},
            "issuelinks": [],
        },
    }


def test_jira_issue_cache_body_path_recognizer_matches_issue_md_and_comments(tmp_path: Path) -> None:
    issue_md = tmp_path / ".workflow-cache" / "issues" / "TEST-1234" / "issue.md"
    comment = tmp_path / ".workflow-cache" / "issues" / "TEST-1234" / "comment-2026-05-15T093000Z-1.md"
    issue_json = tmp_path / ".workflow-cache" / "issues" / "TEST-1234" / "issue.json"

    assert is_jira_issue_cache_body_path(issue_md, tmp_path)
    assert is_jira_issue_cache_body_path(comment, tmp_path)
    assert not is_jira_issue_cache_body_path(issue_json, tmp_path)
    assert not is_jira_issue_cache_body_path(tmp_path / "issue.md", tmp_path)
    assert not is_jira_issue_cache_body_path(
        tmp_path / ".workflow-cache" / "issues" / "TEST-1234" / "metadata.yml", tmp_path
    )


def test_jira_issue_cache_paths_are_provider_specific(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    assert cache.issue_dir(site, "test-1234") == (
        tmp_path / ".workflow-cache" / "issues" / "TEST-1234"
    )
    assert cache.issue_json_file(site, "TEST-1234").name == "issue.json"
    assert cache.issue_file(site, "TEST-1234").name == "issue.md"


def test_jira_read_issue_records_native_state(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _jira_issue_payload("In Progress"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    assert cache.read_issue(site, "TEST-1234")["state"] == "In Progress"


def test_jira_read_issue_state_round_trips_closed(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _jira_issue_payload("Closed"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    assert cache.read_issue(site, "TEST-1234")["state"] == "Closed"


def test_jira_write_issue_bundle_does_not_emit_metadata_file(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _jira_issue_payload("Open"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    issue_dir = cache.issue_dir(site, "TEST-1234")
    assert not (issue_dir / "metadata.yml").exists()


def test_jira_write_issue_bundle_response_omits_internal_json_paths(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    written = cache.write_issue_bundle(
        site,
        _jira_issue_payload("Open"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    # The native source JSON (issue.json / remote-links.json) must never be
    # surfaced; the internal .meta.json path may appear (it is dropped before
    # CLI output) but issue.md stays the readable projection.
    assert set(written) == {"issue_dir", "issue_file", "meta_file"}


def _payload_with_assignee(assignee: object) -> dict[str, object]:
    payload = _jira_issue_payload("Open")
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["assignee"] = assignee
    return payload


def test_read_issue_preserves_native_assignee(tmp_path: Path) -> None:
    # issue.md is now the pure body; the native assignee object round-trips
    # through issue.json and surfaces verbatim on read (no snapshot frontmatter).
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _payload_with_assignee({"displayName": "Alice Anderson", "name": "alice"}),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    payload = cache.read_issue(site, "TEST-1234")
    assert payload["assignee"] == {"displayName": "Alice Anderson", "name": "alice"}


@pytest.mark.parametrize(
    ("assignee_field", "expected"),
    [
        (
            {"displayName": "Alice Anderson", "name": "alice", "key": "alice-key", "accountId": "acc-1"},
            "Alice Anderson",
        ),
        ({"name": "alice", "key": "alice-key", "accountId": "acc-1"}, "alice"),
        ({"key": "alice-key", "accountId": "acc-1"}, "alice-key"),
        ({"accountId": "acc-1"}, "acc-1"),
    ],
)
def test_jira_person_display_name_falls_back_through_keys(
    assignee_field: dict[str, object],
    expected: str,
) -> None:
    assert _jira_person_display_name(assignee_field) == expected


def test_read_issue_assignee_is_null_when_unassigned(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _payload_with_assignee(None),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    payload = cache.read_issue(site, "TEST-1234")
    assert "assignee" in payload
    assert payload["assignee"] is None


def test_read_issue_assignee_is_null_when_field_absent(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    payload = _jira_issue_payload("Open")
    fields = payload["fields"]
    assert isinstance(fields, dict)
    assert "assignee" not in fields

    cache.write_issue_bundle(
        site,
        payload,
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    payload = cache.read_issue(site, "TEST-1234")
    assert "assignee" in payload
    assert payload["assignee"] is None


def test_comment_author_name_still_uses_shared_jira_display_name_fallback() -> None:
    assert _comment_author_name({"displayName": "Alice", "name": "alice"}) == "Alice"
    assert _comment_author_name({"name": "alice"}) == "alice"
    assert _comment_author_name({"key": "alice-key"}) == "alice-key"
    assert _comment_author_name({"accountId": "acc-1"}) == "acc-1"
    assert _comment_author_name(None) == "unknown"
    assert _comment_author_name({}) == "unknown"
    assert _comment_author_name("alice") == "alice"
