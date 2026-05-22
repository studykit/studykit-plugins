"""Tests for Jira issue cache carrier paths and draft parsing."""

from __future__ import annotations

import sys
from pathlib import Path

import frontmatter as frontmatter_lib
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


def test_jira_issue_frontmatter_records_native_state(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _jira_issue_payload("In Progress"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert parsed.metadata["state"] == "In Progress"


def test_jira_issue_frontmatter_state_round_trips_closed(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _jira_issue_payload("Closed"),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert parsed.metadata["state"] == "Closed"


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

    assert set(written) == {"issue_dir", "issue_file"}


def _payload_with_assignee(assignee: object) -> dict[str, object]:
    payload = _jira_issue_payload("Open")
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["assignee"] = assignee
    return payload


def test_snapshot_frontmatter_includes_assignee_display_name(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _payload_with_assignee({"displayName": "Alice Anderson", "name": "alice"}),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert parsed.metadata["assignee"] == "Alice Anderson"


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
def test_snapshot_frontmatter_assignee_falls_back_through_keys(
    tmp_path: Path,
    assignee_field: dict[str, object],
    expected: str,
) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _payload_with_assignee(assignee_field),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert parsed.metadata["assignee"] == expected


def test_snapshot_frontmatter_assignee_is_null_when_unassigned(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    cache.write_issue_bundle(
        site,
        _payload_with_assignee(None),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert "assignee" in parsed.metadata
    assert parsed.metadata["assignee"] is None


def test_existing_snapshot_payload_still_renders_without_assignee_field(tmp_path: Path) -> None:
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

    parsed = frontmatter_lib.loads(cache.issue_file(site, "TEST-1234").read_text(encoding="utf-8"))
    assert "assignee" in parsed.metadata
    assert parsed.metadata["assignee"] is None


def test_comment_author_name_still_uses_shared_jira_display_name_fallback() -> None:
    assert _comment_author_name({"displayName": "Alice", "name": "alice"}) == "Alice"
    assert _comment_author_name({"name": "alice"}) == "alice"
    assert _comment_author_name({"key": "alice-key"}) == "alice-key"
    assert _comment_author_name({"accountId": "acc-1"}) == "acc-1"
    assert _comment_author_name(None) == "unknown"
    assert _comment_author_name({}) == "unknown"
    assert _comment_author_name("alice") == "alice"
