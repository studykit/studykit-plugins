"""Regression tests for ``issue new`` / ``issue update`` CLI JSON shape.

The writeback paths (``issue new`` and ``issue update`` on both GitHub and
Jira) must not surface the provider wrapper fields ``operation`` and
``verified``: ``plugins/workflow/scripts/issue/cli_output.py`` already
classifies both as drop-on-output for the flatten path, and the writeback
paths must match that contract even though they bypass
``flatten_provider_envelope``.

These tests pin the contract end-to-end via the same fake runners the
broader writeback tests use, so a future regression that leaks
``operation`` or ``verified`` back into the writeback payload fails here
explicitly. The freshness-drift ``status == "blocked"`` branch is also
covered to confirm the targeted key removal did not touch the blocked
response shape (which echoes the provider payload as-is) or its exit
code (3).
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from issue.legacy.issue_new import main as issue_new_main  # noqa: E402
from issue.legacy.issue_update import main as issue_update_main  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402

from test_workflow_cache_issue_drafts import (  # noqa: E402
    GitHubFakeRunner,
    GitHubUpdateIssueRunner,
    JiraFakeRunner,
    _jira_curl_get_args,
    _jira_issue_payload,
    _jira_write_args,
    _write_body_file,
    _write_config as _write_github_config,
    _write_jira_config,
)
from test_workflow_cache_writeback import (  # noqa: E402
    _seed_cached_issue as _seed_jira_cached_issue,
    curl_args as _jira_get_args,
    curl_write_args as _jira_put_args,
    jira_issue_payload as _jira_writeback_issue_payload,
    jira_issue_url as _jira_writeback_issue_url,
    jira_remote_links_url as _jira_writeback_remote_links_url,
    remote_links_payload as _jira_writeback_remote_links_payload,
    write_jira_config as _write_jira_writeback_config,
)
from test_workflow_cache_issue_drafts import _seed_cached_issue as _seed_github_cached_issue  # noqa: E402


# Keys the writeback payloads MUST surface (subset contract on success).
_GITHUB_PUBLISH_EXPECTED_KEYS = frozenset(
    {
        "kind",
        "issue",
        "issue_file",
        "body_file",
        "body_file_removed",
        "cache_refreshed",
    }
)
_GITHUB_UPDATE_EXPECTED_KEYS = frozenset(
    {
        "kind",
        "issue",
        "state_changed",
        "state",
        "issue_file",
        "body_file",
        "body_file_removed",
        "cache_refreshed",
    }
)
_JIRA_PUBLISH_EXPECTED_KEYS = frozenset(
    {
        "kind",
        "issue",
        "key",
        "issue_file",
        "body_file",
        "body_file_removed",
        "cache_refreshed",
        "subtask_parent",
    }
)
_JIRA_UPDATE_EXPECTED_KEYS = frozenset(
    {
        "kind",
        "issue",
        "key",
        "state_changed",
        "state",
        "issue_file",
        "body_file",
        "body_file_removed",
        "cache_refreshed",
    }
)


def _assert_no_wrapper_keys(payload: dict[str, object]) -> None:
    assert "operation" not in payload, payload
    assert "verified" not in payload, payload


def test_github_publish_writeback_json_omits_operation_and_verified(tmp_path: Path) -> None:
    _write_github_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = issue_new_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--label",
            "workflow",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_no_wrapper_keys(payload)
    assert _GITHUB_PUBLISH_EXPECTED_KEYS.issubset(payload.keys())
    assert payload["kind"] == "github"
    assert payload["issue"] == "51"
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True


def test_github_update_writeback_json_omits_operation_and_verified(tmp_path: Path) -> None:
    _write_github_config(tmp_path)
    _seed_github_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Updated body.\n", name="update.md")
    runner = GitHubUpdateIssueRunner()
    stdout = io.StringIO()

    code = issue_update_main(
        [
            "--project",
            str(tmp_path),
            "update",
            "--issue",
            "72",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_no_wrapper_keys(payload)
    assert _GITHUB_UPDATE_EXPECTED_KEYS.issubset(payload.keys())
    assert payload["kind"] == "github"
    assert payload["issue"] == "72"
    assert payload["state_changed"] is False
    assert payload["body_file_removed"] is True


def test_jira_publish_writeback_json_omits_operation_and_verified(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    issue_url = "https://jira.example.test/rest/api/2/issue/TEST-1234"
    remote_links_url = "https://jira.example.test/rest/api/2/issue/TEST-1234/remotelink"

    runner = JiraFakeRunner(
        {
            _jira_write_args(): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps({"id": "10001", "key": "TEST-1234"}),
            ),
            _jira_curl_get_args(issue_url): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps(_jira_issue_payload()),
            ),
            _jira_curl_get_args(remote_links_url): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps([]),
            ),
        }
    )
    stdout = io.StringIO()

    code = issue_new_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--label",
            "workflow",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_no_wrapper_keys(payload)
    assert _JIRA_PUBLISH_EXPECTED_KEYS.issubset(payload.keys())
    assert payload["kind"] == "jira"
    assert payload["issue"] == "TEST-1234"
    assert payload["key"] == "TEST-1234"
    assert payload["body_file_removed"] is True


class _JiraUpdateRunner:
    """Inline runner for the Jira update happy-path JSON shape test.

    Mirrors ``test_workflow_cache_writeback.FakeRunner`` but stays
    local so this regression module is self-contained for the Jira
    update happy path.
    """

    def __init__(self, responses: dict[tuple[str, ...], object]) -> None:
        self._responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self._responses.get(request.args)
        if response is None:
            return CommandResult(
                request=request,
                returncode=127,
                stderr=f"unexpected command: {request.args}",
            )
        if isinstance(response, list):
            if not response:
                return CommandResult(
                    request=request,
                    returncode=127,
                    stderr=f"unexpected command (exhausted): {request.args}",
                )
            return response.pop(0)
        return response


def _result(args: tuple[str, ...], stdout: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(
        request=CommandRequest(args=args),
        returncode=returncode,
        stdout=stdout,
    )


def test_jira_update_writeback_json_omits_operation_and_verified(tmp_path: Path) -> None:
    _write_jira_writeback_config(tmp_path)
    _seed_jira_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Updated body.\n", name="update.md")

    issue_url = _jira_writeback_issue_url()
    remote_links_url = _jira_writeback_remote_links_url()

    runner = _JiraUpdateRunner(
        {
            _jira_get_args(issue_url): [
                _result(
                    _jira_get_args(issue_url),
                    stdout=json.dumps(_jira_writeback_issue_payload()),
                ),
                _result(
                    _jira_get_args(issue_url),
                    stdout=json.dumps(
                        _jira_writeback_issue_payload(body="Updated body.\n")
                    ),
                ),
            ],
            _jira_put_args(): _result(_jira_put_args(), stdout=""),
            _jira_get_args(remote_links_url): _result(
                _jira_get_args(remote_links_url),
                stdout=json.dumps(_jira_writeback_remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = issue_update_main(
        [
            "--project",
            str(tmp_path),
            "update",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    _assert_no_wrapper_keys(payload)
    assert _JIRA_UPDATE_EXPECTED_KEYS.issubset(payload.keys())
    assert payload["kind"] == "jira"
    assert payload["issue"] == "TEST-1234"
    assert payload["key"] == "TEST-1234"
    assert payload["state_changed"] is False
    assert payload["body_file_removed"] is True


def test_github_update_freshness_drift_blocked_branch_is_unchanged(tmp_path: Path) -> None:
    """The freshness-drift ``status == "blocked"`` branch must remain
    unchanged by the targeted writeback-payload cleanup.

    The blocked branch echoes the provider payload verbatim (with
    ``body_file`` / ``body_file_removed`` overlaid) and returns exit code
    3. The fix to the success result dict must not touch this branch, so
    we pin its observable contract: ``status``, ``reason``,
    ``reread_required``, body-file echo fields, and the body file stays
    on disk.
    """

    _write_github_config(tmp_path)
    _seed_github_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Updated body.\n", name="update.md")
    # provider_issue_updated_at newer than the seeded cache triggers the
    # freshness drift branch.
    runner = GitHubUpdateIssueRunner(provider_issue_updated_at="2026-05-15T00:00:00Z")
    stdout = io.StringIO()

    code = issue_update_main(
        [
            "--project",
            str(tmp_path),
            "update",
            "--issue",
            "72",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 3
    assert payload["status"] == "blocked"
    assert payload["reason"] == "stale_cache"
    assert payload["reread_required"] is True
    assert payload["body_file"] == str(body_file)
    assert payload["body_file_removed"] is False
    assert body_file.exists()
