"""Tests for GitHub issue cache projections."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_REPO_ROOT = _PLUGIN_ROOT.parent.parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_cache import (  # noqa: E402
    FreshnessMetadata,
    WorkflowFreshnessConflict,
    check_provider_freshness,
    require_provider_freshness,
)
from workflow_github_issue_cache import GitHubIssueCache, is_github_issue_cache_body_path  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_github import DEFAULT_ISSUE_FIELDS, GitHubRepository  # noqa: E402
from workflow_providers import (  # noqa: E402
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_REFRESH,
    ProviderContext,
    ProviderDispatcher,
    ProviderRequest,
    default_provider_registry,
)


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def git_args(project: Path, *args: str) -> tuple[str, ...]:
    return ("git", "-C", str(project.resolve(strict=False)), *args)


def gh_issue_view_args(issue: int | str) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        ",".join(DEFAULT_ISSUE_FIELDS),
    )


def repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def external_repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="other", name="repo")


def test_github_issue_cache_body_path_recognizer_matches_issue_and_comment_layouts(tmp_path: Path) -> None:
    configured_issue = tmp_path / ".workflow-cache" / "issues" / "39" / "issue.md"
    configured_comment = tmp_path / ".workflow-cache" / "issues" / "39" / "comment-2026-05-13T112053Z-4440388606.md"
    external_issue = tmp_path / ".workflow-cache" / "github.com" / "other" / "repo" / "issues" / "39" / "issue.md"
    external_comment = (
        tmp_path
        / ".workflow-cache"
        / "github.com"
        / "other"
        / "repo"
        / "issues"
        / "39"
        / "comment-2026-05-13T112053Z-4440388606.md"
    )

    assert is_github_issue_cache_body_path(configured_issue, tmp_path)
    assert is_github_issue_cache_body_path(configured_comment, tmp_path)
    assert is_github_issue_cache_body_path(external_issue, tmp_path)
    assert is_github_issue_cache_body_path(external_comment, tmp_path)
    assert not is_github_issue_cache_body_path(configured_issue.with_name("metadata.yml"), tmp_path)
    assert not is_github_issue_cache_body_path(configured_issue.with_name("notes.md"), tmp_path)
    assert not is_github_issue_cache_body_path(
        tmp_path / ".workflow-cache" / "issues" / "39" / "comments" / "any.md", tmp_path
    )
    assert not is_github_issue_cache_body_path(
        tmp_path / ".workflow-cache" / "issues-pending" / "draft-1" / "issue.md", tmp_path
    )
    assert not is_github_issue_cache_body_path(tmp_path / "issue.md", tmp_path)


def issue_payload(
    *,
    body: str = "Raw issue body.",
    updated_at: str = "2026-05-13T12:00:00Z",
    project_items: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "number": 39,
        "title": "Add local cache for workflow provider reads",
        "state": "OPEN",
        "stateReason": None,
        "body": body,
        "labels": [{"name": "task"}, {"name": "workflow"}],
        "updatedAt": updated_at,
        "comments": [
            {
                "id": "IC_kwDOQplzFM8AAAABCKrz_g",
                "url": "https://github.com/studykit/studykit-plugins/issues/39#issuecomment-4440388606",
                "author": {"login": "studykit"},
                "body": "Raw provider comment body.",
                "createdAt": "2026-05-13T11:20:53Z",
                "updatedAt": "2026-05-13T11:21:00Z",
            }
        ],
        "parent": {"number": 28, "title": "Workflow plugin MVP", "state": "OPEN", "stateReason": None},
        "children": [{"number": 41, "title": "Create pending issues", "state": "OPEN", "stateReason": None}],
        "dependencies": {
            "blocked_by": [
                {"number": 32, "title": "Scaffold provider wrappers", "state": "CLOSED", "stateReason": "COMPLETED"}
            ],
            "blocking": [{"number": 36, "title": "Write flows", "state": "OPEN", "stateReason": None}],
        },
    }
    if project_items is not None:
        payload["projectItems"] = project_items
    return payload


def dispatch_get(tmp_path: Path, runner: FakeRunner, *, cache_policy: str = "default"):
    dispatcher = ProviderDispatcher(default_provider_registry(runner=runner))
    request = ProviderRequest(
        role="issue",
        kind="github",
        operation="get",
        context=ProviderContext(project=tmp_path, artifact_type="task", cache_policy=cache_policy),
        payload={"issue": 39},
    )
    return dispatcher.dispatch(request)


def test_gitignore_excludes_workflow_cache_root() -> None:
    assert "/.workflow-cache/" in (_REPO_ROOT / ".gitignore").read_text(encoding="utf-8")


def test_github_issue_cache_writes_flat_layout_with_frontmatter_freshness(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)

    write = cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-13T12:34:56Z")

    assert write.issue_dir == tmp_path / ".workflow-cache" / "issues" / "39"
    issue_text = write.issue_file.read_text(encoding="utf-8")
    assert "title: Add local cache for workflow provider reads" in issue_text
    assert "source_updated_at: '2026-05-13T12:00:00Z'" in issue_text
    assert "fetched_at: '2026-05-13T12:34:56Z'" in issue_text
    assert "relationships:\n  source_updated_at:" in issue_text
    assert "current:\n    parent: 28" in issue_text
    assert "children:\n    - 41" in issue_text
    assert "blocked_by:\n      - 32" in issue_text
    assert "\ncomments:\n" not in issue_text
    assert "# Issue" not in issue_text
    assert issue_text.endswith("Raw issue body.")

    assert not (write.issue_dir / "metadata.yml").exists()
    assert not (write.issue_dir / "comments").exists()
    assert not (write.issue_dir / "comments-pending").exists()

    comment_file = write.issue_dir / "comment-2026-05-13T112053Z-4440388606.md"
    assert comment_file.is_file()
    comment_text = comment_file.read_text(encoding="utf-8")
    assert "author: studykit" in comment_text
    assert "provider_comment_id: '4440388606'" in comment_text
    assert "provider_node_id: IC_kwDOQplzFM8AAAABCKrz_g" in comment_text
    assert "created_at: '2026-05-13T11:20:53Z'" in comment_text
    assert "updated_at: '2026-05-13T11:21:00Z'" in comment_text
    assert comment_text.endswith("Raw provider comment body.")

    relationships = cache.read_relationships(repo(), 39)
    assert relationships["fetched_at"] == "2026-05-13T12:34:56Z"
    assert relationships["parent"]["number"] == 28
    assert relationships["children"][0]["number"] == 41
    assert relationships["dependencies"]["blocked_by"][0] == {"number": 32}


def test_github_issue_cache_preserves_comments_when_provider_payload_omits_comments(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    initial = cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-13T12:34:56Z")
    comment_file = initial.issue_dir / "comment-2026-05-13T112053Z-4440388606.md"
    assert comment_file.is_file()
    initial_comment_text = comment_file.read_text(encoding="utf-8")

    payload = issue_payload(body="Body from targeted read.", updated_at="2026-05-13T13:00:00Z")
    payload.pop("comments")
    write = cache.write_issue_bundle(repo(), payload, fetched_at="2026-05-13T13:01:00Z")

    assert write.issue_dir == initial.issue_dir
    assert write.issue_file.read_text(encoding="utf-8").endswith("Body from targeted read.")
    assert comment_file.read_text(encoding="utf-8") == initial_comment_text


def test_github_issue_cache_writes_project_membership_status_to_frontmatter(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)

    project_items = [
        {
            "id": "PVTI_project_item",
            "project": {
                "owner": {"login": "studykit"},
                "number": 1,
                "title": "Workflow",
                "url": "https://github.com/orgs/studykit/projects/1",
            },
            "fieldValues": {
                "nodes": [
                    {
                        "field": {"name": "Status"},
                        "name": "In progress",
                    }
                ]
            },
        }
    ]

    write = cache.write_issue_bundle(
        repo(),
        issue_payload(project_items=project_items),
        fetched_at="2026-05-13T12:34:56Z",
    )

    issue_text = write.issue_file.read_text(encoding="utf-8")
    assert "projects:" in issue_text
    assert "owner: studykit" in issue_text
    assert "number: 1" in issue_text
    assert "title: Workflow" in issue_text
    assert "item_id: PVTI_project_item" in issue_text
    assert "status: In progress" in issue_text

    cached = cache.read_issue(repo(), 39, include_body=False, include_comments=False, include_relationships=False)
    assert cached["projects"] == [
        {
            "owner": "studykit",
            "number": 1,
            "title": "Workflow",
            "url": "https://github.com/orgs/studykit/projects/1",
            "item_id": "PVTI_project_item",
            "status": "In progress",
        }
    ]


def test_configured_repo_cache_is_shallow_and_external_repo_cache_is_namespaced(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())

    assert cache.issue_dir(repo(), 39) == tmp_path / ".workflow-cache" / "issues" / "39"
    assert (
        cache.issue_dir(external_repo(), 39)
        == tmp_path / ".workflow-cache" / "github.com" / "other" / "repo" / "issues" / "39"
    )


def test_cache_relationship_frontmatter_omits_pending_block(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload())
    issue_path = cache.issue_file(repo(), 39)

    text = issue_path.read_text(encoding="utf-8")
    assert "pending:" not in text


def test_cache_read_can_skip_raw_markdown_bodies(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    write = cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-13T12:34:56Z")
    comment_file = write.issue_dir / "comment-2026-05-13T112053Z-4440388606.md"
    assert comment_file.is_file()

    cached = cache.read_issue(repo(), 39, include_body=False, include_comments=True, include_relationships=False)

    assert "body" not in cached
    assert "body" not in cached["comments"][0]
    assert cached["comments"][0]["id"] == "4440388606"


def test_freshness_metadata_reads_from_issue_frontmatter(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    write = cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-13T12:34:56Z")

    issue_meta = cache.read_freshness_metadata(repo(), 39, target="issue")
    comments_meta = cache.read_freshness_metadata(repo(), 39, target="comments")
    relationships_meta = cache.read_freshness_metadata(repo(), 39, target="relationships")
    cached = cache.read_issue(repo(), 39, include_body=False, include_comments=False, include_relationships=False)

    assert issue_meta.path == write.issue_file
    assert issue_meta.source_updated_at == "2026-05-13T12:00:00Z"
    assert issue_meta.fetched_at == "2026-05-13T12:34:56Z"
    assert comments_meta.path == write.issue_file
    assert comments_meta.fetched_at == "2026-05-13T12:34:56Z"
    assert comments_meta.source_updated_at == "2026-05-13T11:21:00Z"
    assert relationships_meta.path == write.issue_file
    assert relationships_meta.fetched_at == "2026-05-13T12:34:56Z"
    assert relationships_meta.source_updated_at == "2026-05-13T12:00:00Z"
    assert cached["cache"]["issue_file"] == str(write.issue_file)
    assert cached["cache"]["fetchedAt"] == "2026-05-13T12:34:56Z"


def test_default_cache_policy_uses_cache_hit_without_remote_issue_view(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(repo(), issue_payload(body="Cached body."), fetched_at="2026-05-13T12:34:56Z")
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert response.payload["body"] == "Cached body."
    assert response.payload["cache"]["hit"] is True
    assert all(request.args[:3] != ("gh", "issue", "view") for request in runner.requests)


def test_default_cache_policy_miss_reads_remote_and_writes_cache(tmp_path: Path) -> None:
    remote = issue_payload(body="Remote body.")
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_issue_view_args(39): result(gh_issue_view_args(39), stdout=json.dumps(remote)),
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert response.payload["body"] == "Remote body."
    assert GitHubIssueCache.for_project(tmp_path).issue_file(repo(), 39).is_file()


def test_refresh_policy_bypasses_cache_and_overwrites_projection(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(repo(), issue_payload(body="Stale body."), fetched_at="2026-05-13T12:34:56Z")
    remote = issue_payload(body="Fresh body.", updated_at="2026-05-14T00:00:00Z")
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_issue_view_args(39): result(gh_issue_view_args(39), stdout=json.dumps(remote)),
        }
    )

    response = dispatch_get(tmp_path, runner, cache_policy=CACHE_POLICY_REFRESH)

    assert response.payload["body"] == "Fresh body."
    assert cache.read_issue(repo(), 39)["body"] == "Fresh body."


def test_bypass_policy_reads_remote_without_writing_cache(tmp_path: Path) -> None:
    remote = issue_payload(body="Bypass body.")
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_issue_view_args(39): result(gh_issue_view_args(39), stdout=json.dumps(remote)),
        }
    )

    response = dispatch_get(tmp_path, runner, cache_policy=CACHE_POLICY_BYPASS)

    assert response.payload["body"] == "Bypass body."
    assert not GitHubIssueCache.for_project(tmp_path).issue_file(repo(), 39).exists()


def test_corrupt_cache_entry_is_treated_as_miss(tmp_path: Path) -> None:
    cache = GitHubIssueCache.for_project(tmp_path)
    issue_file = cache.issue_file(repo(), 39)
    issue_file.parent.mkdir(parents=True, exist_ok=True)
    issue_file.write_text("not markdown frontmatter", encoding="utf-8")
    remote = issue_payload(body="Recovered body.")
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_issue_view_args(39): result(gh_issue_view_args(39), stdout=json.dumps(remote)),
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert response.payload["body"] == "Recovered body."
    assert cache.read_issue(repo(), 39)["body"] == "Recovered body."
