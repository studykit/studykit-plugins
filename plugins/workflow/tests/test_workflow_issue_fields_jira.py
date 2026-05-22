"""Tests for the Jira issue body-less field mutation CLI."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_config import load_workflow_config  # noqa: E402
from workflow_jira_data_center_client import jira_data_center_site_from_provider_config  # noqa: E402
from issue.jira.cache import JiraDataCenterIssueCache  # noqa: E402
from workflow_providers import ProviderOperationError  # noqa: E402
from issue.jira.backend import JiraIssueFieldsError, fields_payload  # noqa: E402
from issue.legacy.issue_fields import main  # noqa: E402


_DROPPED_FIELD_KEYS = ("provider", "cache", "site", "operation", "role", "kind", "verified", "key")


def _assert_flat_field_envelope(payload: dict, *, issue_basename: str = "TEST-1234/issue.md") -> None:
    """Assert the flattened envelope contract for Jira field write payloads."""
    for dropped in _DROPPED_FIELD_KEYS:
        assert dropped not in payload, f"{dropped!r} should not be in payload"
    assert payload["issue"].endswith(issue_basename), payload["issue"]
    assert payload["cache_refreshed"] is True


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult | list[CommandResult]]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")
        if isinstance(response, list):
            if not response:
                return CommandResult(request=request, returncode=127, stderr="exhausted")
            return response.pop(0)
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def write_jira_config(project: Path, *, extra_settings: str = "") -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
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
"""
            + extra_settings
            + """
  knowledge:
    kind: github
issue_id_format: jira
"""
        ).lstrip(),
        encoding="utf-8",
    )


def jira_site(project: Path):
    config = load_workflow_config(project)
    assert config is not None
    return jira_data_center_site_from_provider_config(config.issues)


def jira_issue_payload(*, assignee: str | None = None, issuetype: str = "Task") -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "Support Jira Data Center",
            "description": "Cached body.",
            "labels": ["workflow", "jira"],
            "issuetype": {"name": issuetype},
            "assignee": {"name": assignee} if assignee else None,
            "created": "2026-05-15T09:00:00.000+0900",
            "updated": "2026-05-15T10:00:00.000+0900",
            "status": {"name": "In Progress", "statusCategory": {"key": "indeterminate"}},
            "comment": {"comments": []},
            "issuelinks": [],
        },
    }


def remote_links_payload() -> list[dict[str, object]]:
    return []


def curl_args(url: str) -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


def curl_write_args() -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--config", "-")


def jira_issue_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}"


def jira_remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def jira_transitions_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/transitions"


def jira_myself_url() -> str:
    return "https://jira.example.test/rest/api/2/myself"


def _seed_cache(project: Path, *, payload: dict[str, object] | None = None) -> None:
    site = jira_site(project)
    cache = JiraDataCenterIssueCache.for_project(project)
    cache.write_issue_bundle(
        site,
        payload if payload is not None else jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )


def _baseline_responses(write_results: list[CommandResult] | None = None) -> dict[tuple[str, ...], CommandResult | list[CommandResult]]:
    return {
        curl_args(jira_issue_url()): [
            result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
            result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
        ],
        curl_args(jira_remote_links_url()): result(
            curl_args(jira_remote_links_url()),
            stdout=json.dumps(remote_links_payload()),
        ),
        curl_write_args(): write_results if write_results is not None else [result(curl_write_args(), stdout="")],
    }


def test_set_type_puts_fields_issuetype_via_default_mapping(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    runner = FakeRunner(_baseline_responses())

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="set-type",
        issue="TEST-1234",
        new_type="bug",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"issuetype\\":{\\"name\\":\\"Bug\\"}' in str(request.input_text) for request in write_requests)


def test_set_type_uses_configured_artifact_issue_types_override(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    artifact_issue_types:
      bug: Defect
""",
    )
    _seed_cache(tmp_path)
    runner = FakeRunner(_baseline_responses())

    fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="set-type",
        issue="TEST-1234",
        new_type="bug",
        runner=runner,
    )

    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"issuetype\\":{\\"name\\":\\"Defect\\"}' in str(request.input_text) for request in write_requests)


def test_set_type_surfaces_jira_rest_error_verbatim(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    responses = _baseline_responses(write_results=[
        result(
            curl_write_args(),
            stderr='HTTP 400: {"errorMessages":["Issue type transition not allowed"]}',
            returncode=22,
        ),
    ])
    runner = FakeRunner(responses)

    with pytest.raises(Exception) as excinfo:
        fields_payload(
            project=tmp_path,
            artifact_type="task",
            verb="set-type",
            issue="TEST-1234",
            new_type="epic",
            runner=runner,
        )
    assert "Issue type transition not allowed" in str(excinfo.value)


def test_set_type_rejects_unmapped_workflow_type(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    with pytest.raises(JiraIssueFieldsError, match="no Jira issuetype mapping"):
        fields_payload(
            project=tmp_path,
            artifact_type="task",
            verb="set-type",
            issue="TEST-1234",
            new_type="custom-unknown",
        )


def test_assign_me_resolves_via_myself_once(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    responses = _baseline_responses()
    responses[curl_args(jira_myself_url())] = result(
        curl_args(jira_myself_url()),
        stdout=json.dumps({"name": "studykit-svc", "displayName": "Studykit Service"}),
    )
    runner = FakeRunner(responses)

    fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="assign",
        issue="TEST-1234",
        user="me",
        runner=runner,
    )

    myself_calls = [request for request in runner.requests if request.args == curl_args(jira_myself_url())]
    assert len(myself_calls) == 1
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"assignee\\":{\\"name\\":\\"studykit-svc\\"}' in str(request.input_text) for request in write_requests)


def test_unassign_sets_fields_assignee_null(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path, payload=jira_issue_payload(assignee="alice"))
    runner = FakeRunner(_baseline_responses())

    fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="unassign",
        issue="TEST-1234",
        runner=runner,
    )

    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"assignee\\":null' in str(request.input_text) for request in write_requests)


def test_assign_refreshes_snapshot_frontmatter_with_new_assignee(tmp_path: Path) -> None:
    """End-to-end: after assign, the refreshed issue.md shows the new assignee.

    The writeback's `_refresh_cache` re-fetches the issue after the curl
    write succeeds and replays `write_issue_bundle`, so the second
    `curl_args(jira_issue_url())` response in the queue is what lands in
    the on-disk snapshot. Returning an assignee-bearing payload there
    asserts AC4 / AC1 hold without a manual `--cache-policy refresh`.
    """

    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    refreshed_payload = jira_issue_payload()
    refreshed_fields = refreshed_payload["fields"]
    assert isinstance(refreshed_fields, dict)
    refreshed_fields["assignee"] = {"name": "alice", "displayName": "Alice Anderson"}

    responses = _baseline_responses()
    responses[curl_args(jira_issue_url())] = [
        result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
        result(curl_args(jira_issue_url()), stdout=json.dumps(refreshed_payload)),
    ]
    runner = FakeRunner(responses)

    fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="assign",
        issue="TEST-1234",
        user="alice",
        runner=runner,
    )

    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    issue_md = cache.issue_file(jira_site(tmp_path), "TEST-1234")
    import frontmatter as frontmatter_lib

    parsed = frontmatter_lib.loads(issue_md.read_text(encoding="utf-8"))
    assert parsed.metadata["assignee"] == "Alice Anderson"


def test_reopen_uses_configured_reopen_transition(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      reopen: Reopen
""",
    )
    _seed_cache(tmp_path)
    responses = _baseline_responses(write_results=[
        result(curl_write_args(), stdout=""),
        result(curl_write_args(), stdout=""),
    ])
    responses[curl_args(jira_transitions_url())] = result(
        curl_args(jira_transitions_url()),
        stdout=json.dumps({"transitions": [{"id": "41", "name": "Reopen"}]}),
    )
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="reopen",
        issue="TEST-1234",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"41\\"}' in str(request.input_text) for request in write_requests)


def test_reopen_without_configured_transition_errors(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path)
    responses = _baseline_responses(write_results=[
        result(curl_write_args(), stdout=""),
    ])
    runner = FakeRunner(responses)

    with pytest.raises(ProviderOperationError) as excinfo:
        fields_payload(
            project=tmp_path,
            artifact_type="task",
            verb="reopen",
            issue="TEST-1234",
            runner=runner,
        )

    message = str(excinfo.value)
    assert "verb 'reopen'" in message
    assert "state_transitions.reopen" in message


def test_close_routes_through_state_transition_resolver(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      close: Done
      reopen: Reopen
""",
    )
    _seed_cache(tmp_path)
    responses = _baseline_responses(write_results=[
        result(curl_write_args(), stdout=""),
        result(curl_write_args(), stdout=""),
    ])
    responses[curl_args(jira_transitions_url())] = result(
        curl_args(jira_transitions_url()),
        stdout=json.dumps({"transitions": [{"id": "31", "name": "Done"}]}),
    )
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="close",
        issue="TEST-1234",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"31\\"}' in str(request.input_text) for request in write_requests)


def test_dynamic_verb_registers_custom_lifecycle(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      ship: Done
""",
    )
    _seed_cache(tmp_path)
    responses = _baseline_responses(write_results=[
        result(curl_write_args(), stdout=""),
        result(curl_write_args(), stdout=""),
    ])
    responses[curl_args(jira_transitions_url())] = result(
        curl_args(jira_transitions_url()),
        stdout=json.dumps({"transitions": [{"id": "55", "name": "Done"}]}),
    )
    runner = FakeRunner(responses)

    exit_code = main(
        ["--project", str(tmp_path), "ship", "TEST-1234"],
        stdout=io.StringIO(),
        stderr=io.StringIO(),
        runner=runner,
    )

    assert exit_code == 0
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"55\\"}' in str(request.input_text) for request in write_requests)


def test_unknown_verb_emits_friendly_error(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      close: Done
""",
    )

    with pytest.raises(SystemExit) as excinfo:
        main(["--project", str(tmp_path), "wontdo", "TEST-1234"])

    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert "wontdo" in captured.err
    assert "close" in captured.err
    assert "assign" in captured.err
    assert "state_transitions.wontdo" in captured.err


def test_reserved_verbs_work_without_state_transitions(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path, payload=jira_issue_payload(assignee="alice"))
    runner = FakeRunner(_baseline_responses())

    exit_code = main(
        ["--project", str(tmp_path), "unassign", "TEST-1234"],
        stdout=io.StringIO(),
        stderr=io.StringIO(),
        runner=runner,
    )

    assert exit_code == 0
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"assignee\\":null' in str(request.input_text) for request in write_requests)


def test_unassign_on_stale_cache_returns_blocked_envelope_and_exit_3(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cache(tmp_path, payload=jira_issue_payload(assignee="alice"))
    # Provider reports a newer updated than the cached projection's fetched_at.
    newer = jira_issue_payload(assignee="alice")
    newer["fields"]["updated"] = "2026-05-15T11:00:00.000+0900"  # type: ignore[index]
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(newer)),
                result(curl_args(jira_issue_url()), stdout=json.dumps(newer)),
            ],
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = main(
        ["--project", str(tmp_path), "unassign", "TEST-1234"],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert exit_code == 3, stderr.getvalue()
    payload = json.loads(stdout.getvalue())
    assert payload["status"] == "blocked"
    assert payload["reason"]
    assert payload["reread_required"] is True
    assert payload["reread_paths"]
    # No PUT/POST issued because the freshness gate blocked first.
    assert all(request.args != curl_write_args() for request in runner.requests)
