"""Tests for the GitHub issue relationships CLI (inline-intent flow)."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from issue.cache import relationship_operations_from_intent  # noqa: E402
from functools import partial  # noqa: E402

from issue.github.cache import GitHubIssueCache  # noqa: E402
from issue.dispatch import RELATIONSHIPS, run_intent  # noqa: E402

github_issue_relationships_main = partial(run_intent, RELATIONSHIPS)
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from issue.github.gh import GitHubRepository  # noqa: E402


def repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def issue_payload() -> dict[str, object]:
    return {
        "number": 44,
        "title": "Cached issue",
        "state": "OPEN",
        "stateReason": None,
        "body": "Cached body.",
        "labels": [],
        "updatedAt": "2026-05-14T00:00:00Z",
        "comments": [],
    }


def rest_issue(number: int, issue_id: int) -> dict[str, object]:
    return {
        "id": issue_id,
        "number": number,
        "title": f"Issue {number}",
        "state": "open",
        "state_reason": None,
        "updated_at": "2026-05-14T00:00:00Z",
    }


def gh_issue_view_args(issue: int | str, fields: str) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        fields,
    )


def gh_api_args(*args: str) -> tuple[str, ...]:
    return ("gh", "api", *args)


def write_config(project: Path) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
issue_id_format: github
""".lstrip(),
        encoding="utf-8",
    )


def test_relationship_intent_helper_builds_add_remove_operations() -> None:
    operations = relationship_operations_from_intent(
        {
            "parent_add": "#28",
            "blocked_by_add": ["#33", "#34"],
            "blocked_by_remove": ["#60"],
            "blocking_add": ["#45"],
        },
        target_kind="issue",
        target_id="44",
    )
    assert [(op.action, op.relationship, op.target_ref, op.replace_parent) for op in operations] == [
        ("add", "parent", "#28", False),
        ("add", "blocked_by", "#33", False),
        ("add", "blocked_by", "#34", False),
        ("remove", "blocked_by", "#60", False),
        ("add", "blocking", "#45", False),
    ]


def test_relationship_intent_helper_supports_replace_and_remove_parent() -> None:
    replace_ops = relationship_operations_from_intent(
        {"parent_replace": "#28"}, target_kind="issue", target_id="44",
    )
    assert len(replace_ops) == 1
    assert replace_ops[0].relationship == "parent"
    assert replace_ops[0].action == "add"
    assert replace_ops[0].replace_parent is True

    remove_ops = relationship_operations_from_intent(
        {"parent_remove": True}, target_kind="issue", target_id="44",
    )
    assert len(remove_ops) == 1
    assert remove_ops[0].relationship == "parent"
    assert remove_ops[0].action == "remove"
    assert remove_ops[0].target_ref == ""


def test_relationship_intent_helper_rejects_conflicting_parent_flags() -> None:
    import pytest

    with pytest.raises(Exception):
        relationship_operations_from_intent(
            {"parent_add": "#28", "parent_replace": "#29"},
            target_kind="issue",
            target_id="44",
        )


def test_relationship_intent_helper_supports_epic_scalar_handlers() -> None:
    add_ops = relationship_operations_from_intent(
        {"epic_add": "TEST-10"}, target_kind="issue", target_id="TEST-5",
    )
    assert [(op.action, op.relationship, op.target_ref) for op in add_ops] == [
        ("add", "epic", "TEST-10"),
    ]

    replace_ops = relationship_operations_from_intent(
        {"epic_replace": "TEST-11"}, target_kind="issue", target_id="TEST-5",
    )
    assert replace_ops[0].relationship == "epic"
    assert replace_ops[0].action == "add"
    assert replace_ops[0].replace_parent is False

    remove_ops = relationship_operations_from_intent(
        {"epic_remove": True}, target_kind="issue", target_id="TEST-5",
    )
    assert remove_ops[0].relationship == "epic"
    assert remove_ops[0].action == "remove"
    assert remove_ops[0].target_ref == ""


def test_relationship_intent_helper_rejects_conflicting_epic_flags() -> None:
    import pytest

    with pytest.raises(Exception, match="conflicting epic"):
        relationship_operations_from_intent(
            {"epic_add": "TEST-10", "epic_replace": "TEST-11"},
            target_kind="issue",
            target_id="TEST-5",
        )


def test_relationship_intent_helper_combines_parent_and_epic_independently() -> None:
    operations = relationship_operations_from_intent(
        {"parent_add": "TEST-50", "epic_add": "TEST-10"},
        target_kind="issue",
        target_id="TEST-5",
    )
    by_relationship = {op.relationship: op for op in operations}
    assert by_relationship["parent"].target_ref == "TEST-50"
    assert by_relationship["epic"].target_ref == "TEST-10"


def test_github_provider_rejects_epic_relationship_operation(tmp_path: Path) -> None:
    """epic_* intent reaching the GitHub provider must error with a clear message."""

    import pytest

    from issue.github.provider import GitHubIssueNativeProvider
    from issue.providers import ProviderContext, ProviderOperationError, ProviderRequest

    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-14T00:10:00Z")

    def runner(request: CommandRequest) -> CommandResult:
        return CommandResult(request=request, returncode=127, stderr=f"unexpected: {request.args}")

    provider = GitHubIssueNativeProvider(runner=runner)
    with pytest.raises(ProviderOperationError, match="unsupported GitHub relationship operation: epic"):
        provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="apply_relationships",
                context=ProviderContext(project=tmp_path, artifact_type="task"),
                payload={"issue": "44", "relationship_intent": {"epic_add": "#10"}},
            )
        )


def test_relationship_intent_helper_rejects_add_remove_overlap() -> None:
    import pytest

    with pytest.raises(Exception):
        relationship_operations_from_intent(
            {"blocked_by_add": ["#33"], "blocked_by_remove": ["#33"]},
            target_kind="issue",
            target_id="44",
        )


_DROPPED_RELATIONSHIP_KEYS = ("provider", "cache", "repository", "site", "operation", "role", "kind", "verified")


def _assert_flat_relationship_envelope(payload: dict, *, issue_basename: str) -> None:
    for dropped in _DROPPED_RELATIONSHIP_KEYS:
        assert dropped not in payload, f"{dropped!r} should not be in payload"
    assert payload["issue"].endswith(issue_basename), payload["issue"]


def test_relationships_cli_no_flag_returns_no_op(tmp_path: Path) -> None:
    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload(), fetched_at="2026-05-14T00:10:00Z")

    def runner(request: CommandRequest) -> CommandResult:
        raise AssertionError(f"unexpected command in no-op call: {request.args}")

    stdout = io.StringIO()
    code = github_issue_relationships_main(
        ["--project", str(tmp_path), "#44"],
        stdout=stdout,
        runner=runner,
    )
    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_flat_relationship_envelope(payload, issue_basename="44/issue.md")
    assert payload["cache_refreshed"] is False
    assert payload["applied"] == 0
    assert payload.get("no_changes") is True


def test_relationships_cli_dispatches_inline_intent(tmp_path: Path) -> None:
    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    # The relationships freshness check compares the cached relationship
    # fingerprint against the provider's current relationships. Seed the cache
    # to match the runner's relationship endpoints (child #45 present) so the
    # apply proceeds instead of conflicting.
    cache.write_issue_bundle(
        repo(),
        {**issue_payload(), "children": [{"number": 45}]},
        fetched_at="2026-05-14T00:10:00Z",
    )

    def runner(request: CommandRequest) -> CommandResult:
        if request.args == gh_issue_view_args(44, "number,updatedAt"):
            return CommandResult(request=request, returncode=0, stdout=json.dumps({"number": 44, "updatedAt": "2026-05-14T00:00:00Z"}))
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/45"):
            return CommandResult(request=request, returncode=0, stdout=json.dumps(rest_issue(45, 4500)))
        if request.args == gh_api_args(
            "-X",
            "POST",
            "repos/studykit/studykit-plugins/issues/44/sub_issues",
            "-F",
            "sub_issue_id=4500",
        ):
            return CommandResult(request=request, returncode=0, stdout=json.dumps(rest_issue(45, 4500)))
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/44"):
            return CommandResult(request=request, returncode=0, stdout=json.dumps(rest_issue(44, 4400)))
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/44/parent"):
            return CommandResult(request=request, returncode=404, stderr="not found")
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/44/sub_issues", "--paginate"):
            return CommandResult(request=request, returncode=0, stdout=json.dumps([rest_issue(45, 4500)]))
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/44/dependencies/blocked_by", "--paginate"):
            return CommandResult(request=request, returncode=0, stdout="[]")
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/44/dependencies/blocking", "--paginate"):
            return CommandResult(request=request, returncode=0, stdout="[]")
        return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")

    stdout = io.StringIO()
    code = github_issue_relationships_main(
        [
            "--project",
            str(tmp_path),
            "--type",
            "task",
            "--child",
            "#45",
            "#44",
        ],
        stdout=stdout,
        runner=runner,
    )
    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_flat_relationship_envelope(payload, issue_basename="44/issue.md")
    assert payload["cache_refreshed"] is True
    assert payload["applied"] == 1


def write_jira_config(project: Path) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """
version: 1
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: data-center
    api_version: 2
    project: TEST
    issue_type: Task
  knowledge:
    kind: github
issue_id_format: jira
""".lstrip(),
        encoding="utf-8",
    )


def test_jira_relationships_cli_no_flag_returns_flat_no_op(tmp_path: Path) -> None:
    jira_issue_relationships_main = partial(run_intent, RELATIONSHIPS)

    write_jira_config(tmp_path)

    def runner(request: CommandRequest) -> CommandResult:
        raise AssertionError(f"unexpected command in no-op call: {request.args}")

    stdout = io.StringIO()
    code = jira_issue_relationships_main(
        ["--project", str(tmp_path), "TEST-1234"],
        stdout=stdout,
        runner=runner,
    )
    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_flat_relationship_envelope(payload, issue_basename="TEST-1234/issue.md")
    assert payload["cache_refreshed"] is False
    assert payload["applied"] == 0
    assert payload.get("no_changes") is True
