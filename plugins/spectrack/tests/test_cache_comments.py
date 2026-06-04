"""Tests for the agent-facing Jira issue body-file comment append CLI."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from functools import partial  # noqa: E402

from issue.dispatch import COMMENTS, run_intent  # noqa: E402

jira_issue_comments_main = partial(run_intent, COMMENTS)
from command import CommandRequest, CommandResult  # noqa: E402
from config import load_workflow_config  # noqa: E402
from issue.jira.cache import JiraDataCenterIssueCache  # noqa: E402
from issue.jira.client import jira_data_center_site_from_provider_config  # noqa: E402


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult | list[CommandResult]]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        if isinstance(response, list):
            if not response:
                return CommandResult(request=request, returncode=127, stderr="unexpected command")
            return response.pop(0)
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def write_jira_config(project: Path, *, extra_settings: str = "") -> None:
    path = project / ".spectrack" / "config.yml"
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


def jira_issue_payload(*, body: str = "Cached body.") -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "Support Jira Data Center",
            "description": body,
            "labels": ["workflow", "jira"],
            "created": "2026-05-15T09:00:00.000+0900",
            "updated": "2026-05-15T10:00:00.000+0900",
            "status": {"name": "In Progress", "statusCategory": {"key": "indeterminate"}},
            "comment": {"comments": []},
            "issuelinks": [],
        },
    }


def remote_links_payload() -> list[dict[str, object]]:
    return [
        {
            "id": 1,
            "relationship": "mentioned in",
            "object": {"title": "Design note", "url": "https://example.com/design"},
        }
    ]


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


def _seed_cached_issue(project: Path) -> None:
    site = jira_site(project)
    cache = JiraDataCenterIssueCache.for_project(project)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )


def _write_body_file(project: Path, body: str, *, name: str = "comment.md") -> Path:
    path = project / name
    path.write_text(body, encoding="utf-8")
    return path


def test_jira_append_posts_comment_and_deletes_body_file(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Inline comment body.\n")
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps({"id": "30001", "body": "Inline comment body.\n"}),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--issue",
            "test-1234",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["operation"] == "append_comment"
    assert payload["kind"] == "jira"
    assert payload["issue"] == "TEST-1234"
    assert payload["state_changed"] is False
    assert payload["body_file_removed"] is True
    assert payload["issue_file"].endswith("/issues/TEST-1234/issue.md")
    assert "cache" not in payload
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    assert 'request = "POST"' in str(write_request.input_text)
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234/comment"' in str(write_request.input_text)
    assert '\\"body\\":\\"Inline comment body.\\\\n\\"' in str(write_request.input_text)
    assert not body_file.exists()


def test_jira_append_strips_body_file_frontmatter(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(
        tmp_path, "---\nschema_version: 2\n---\nInline comment body.\n"
    )
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps({"id": "30001", "body": "Inline comment body.\n"}),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
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
    assert payload["body_file_removed"] is True
    assert not body_file.exists()
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    assert '\\"body\\":\\"Inline comment body.\\\\n\\"' in str(write_request.input_text)


def test_jira_append_missing_body_file_fails(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cached_issue(tmp_path)
    runner = FakeRunner({})
    stderr = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(tmp_path / "missing.md"),
        ],
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "body file does not exist" in stderr.getvalue()
    assert runner.requests == []


def test_jira_append_preserves_body_file_on_freshness_block(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Inline comment body.\n")
    newer = jira_issue_payload(body="Newer provider body.")
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

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 3
    assert payload["status"] == "conflict"
    assert payload["reason"] == "provider_changed"
    assert all(not path.endswith("/.meta.json") for path in payload["reread_paths"])
    assert payload["body_file_removed"] is False
    assert body_file.exists()
    assert all(request.args != curl_write_args() for request in runner.requests)


def test_jira_append_applies_inline_state_transition(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      close: Done
      reopen: Reopen
""",
    )
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Closing comment.\n")
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_args(jira_transitions_url()): result(
                curl_args(jira_transitions_url()),
                stdout=json.dumps({"transitions": [{"id": "31", "name": "Done"}]}),
            ),
            curl_write_args(): [
                result(curl_write_args(), stdout=json.dumps({"id": "30001"})),
                result(curl_write_args(), stdout=""),
            ],
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(body_file),
            "--state",
            "close",
            "--state-reason",
            "completed",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["state_changed"] is True
    assert payload["state"]["transition_name"] == "Done"
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"31\\"}' in str(request.input_text) for request in write_requests)
    assert not body_file.exists()


def test_jira_append_accepts_free_form_state_verb(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        extra_settings="""
    state_transitions:
      in-progress: In Progress
""",
    )
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Picking this up.\n")
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_args(jira_transitions_url()): result(
                curl_args(jira_transitions_url()),
                stdout=json.dumps({"transitions": [{"id": "21", "name": "In Progress"}]}),
            ),
            curl_write_args(): [
                result(curl_write_args(), stdout=json.dumps({"id": "30001"})),
                result(curl_write_args(), stdout=""),
            ],
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(body_file),
            "--state",
            "in-progress",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["state_changed"] is True
    assert payload["state"]["verb"] == "in-progress"
    assert payload["state"]["transition_name"] == "In Progress"
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"21\\"}' in str(request.input_text) for request in write_requests)
    assert not body_file.exists()
