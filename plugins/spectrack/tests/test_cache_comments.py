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

from issue.dispatch import COMMENTS, FETCH, run_intent  # noqa: E402

jira_issue_comments_main = partial(run_intent, COMMENTS)
jira_issue_fetch_main = partial(run_intent, FETCH)
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


def jira_issue_payload(
    *,
    body: str = "Cached body.",
    comments: list[dict[str, object]] | None = None,
) -> dict[str, object]:
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
            "comment": {"comments": comments or []},
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


def jira_comment_url(issue: str = "TEST-1234", comment_id: str = "30001") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/comment/{comment_id}"


def jira_remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def jira_transitions_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/transitions"


def _seed_cached_issue(
    project: Path,
    *,
    comments: list[dict[str, object]] | None = None,
) -> None:
    site = jira_site(project)
    cache = JiraDataCenterIssueCache.for_project(project)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(comments=comments),
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


def test_jira_update_comment_uses_provider_id_and_deletes_body_file(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    old_comment = {
        "id": "30001",
        "body": "Old resume.\n",
        "created": "2026-05-15T09:30:00.000+0900",
        "updated": "2026-05-15T09:30:00.000+0900",
        "author": {"displayName": "Studykit"},
    }
    updated_comment = {
        **old_comment,
        "body": "Updated resume.\n",
        "updated": "2026-05-15T10:05:00.000+0900",
    }
    _seed_cached_issue(tmp_path, comments=[old_comment])
    body_file = _write_body_file(tmp_path, "Updated resume.\n", name="resume.md")
    updated_issue = jira_issue_payload(comments=[updated_comment])
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): [
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload(comments=[old_comment]))),
                result(curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload(comments=[old_comment]))),
                result(curl_args(jira_issue_url()), stdout=json.dumps(updated_issue)),
            ],
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps(updated_comment),
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
            "update",
            "--issue",
            "TEST-1234",
            "--comment-id",
            "30001",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["operation"] == "update_comment"
    assert payload["kind"] == "jira"
    assert payload["issue"] == "TEST-1234"
    assert payload["comment_id"] == "30001"
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True
    assert not body_file.exists()
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    assert 'request = "PUT"' in str(write_request.input_text)
    assert f'url = "{jira_comment_url()}"' in str(write_request.input_text)
    assert '\\"body\\":\\"Updated resume.\\\\n\\"' in str(write_request.input_text)
    site = jira_site(tmp_path)
    comment_files = JiraDataCenterIssueCache.for_project(tmp_path).comment_files(site, "TEST-1234")
    assert [path.name for path in comment_files] == ["comment-2026-05-15T093000Z-30001.md"]
    cached = comment_files[0].read_text(encoding="utf-8")
    assert "provider_comment_id:" in cached
    assert "30001" in cached
    assert "Updated resume.\n" in cached


def test_jira_fetch_identifies_resume_comment_with_wiki_heading(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    resume_comment = {
        "id": "30001",
        "body": "h2. Resume\n\nCurrent state.\n",
        "created": "2026-05-15T09:30:00.000+0900",
        "updated": "2026-05-15T10:05:00.000+0900",
        "author": {"displayName": "Studykit"},
    }
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()),
                stdout=json.dumps(jira_issue_payload(comments=[resume_comment])),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_fetch_main(
        ["--project", str(tmp_path), "TEST-1234"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    issue = payload["issues"][0]
    assert issue["resume"]["comment_id"] == "30001"
    assert issue["resume"]["comment_file"].endswith("comment-2026-05-15T093000Z-30001.md")


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


# ---------------------------------------------------------------------------
# comment resume (idempotent Resume-comment upsert) — regression for bug #191
# ---------------------------------------------------------------------------


def _jira_resume_comment(
    comment_id: str,
    body: str,
    *,
    created: str = "2026-05-15T09:30:00.000+0900",
    updated: str = "2026-05-15T09:30:00.000+0900",
) -> dict[str, object]:
    return {
        "id": comment_id,
        "body": body,
        "created": created,
        "updated": updated,
        "author": {"displayName": "Studykit"},
    }


def test_jira_comment_resume_updates_existing_resume(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    old_resume = _jira_resume_comment("30001", "h2. Resume\n\nOld state.\n")
    _seed_cached_issue(tmp_path, comments=[old_resume])
    body_file = _write_body_file(tmp_path, "h2. Resume\n\nNew state.\n", name="resume.md")
    payload_with_resume = jira_issue_payload(comments=[old_resume])
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()), stdout=json.dumps(payload_with_resume)
            ),
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps(
                    {**old_resume, "body": "h2. Resume\n\nNew state.\n", "updated": "2026-05-15T10:05:00.000+0900"}
                ),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()), stdout=json.dumps(remote_links_payload())
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "resume",
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
    assert payload["operation"] == "update_comment"
    assert payload["comment_id"] == "30001"
    # The regression guard: exactly one in-place PUT, never a second POST.
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert len(write_requests) == 1
    assert 'request = "PUT"' in str(write_requests[0].input_text)
    assert f'url = "{jira_comment_url()}"' in str(write_requests[0].input_text)
    assert not body_file.exists()


def test_jira_comment_resume_creates_when_missing(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_cached_issue(tmp_path, comments=[])
    body_file = _write_body_file(tmp_path, "h2. Resume\n\nFirst state.\n", name="resume.md")
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()), stdout=json.dumps(jira_issue_payload(comments=[]))
            ),
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps(_jira_resume_comment("30009", "h2. Resume\n\nFirst state.\n")),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()), stdout=json.dumps(remote_links_payload())
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "resume",
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
    assert payload["operation"] == "append_comment"
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert len(write_requests) == 1
    assert 'request = "POST"' in str(write_requests[0].input_text)
    assert '\\"body\\":\\"h2. Resume' in str(write_requests[0].input_text)
    assert not body_file.exists()


def test_jira_comment_resume_rejects_non_resume_body(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Just an update, no heading.\n", name="note.md")
    runner = FakeRunner({})
    stderr = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "resume",
            "--issue",
            "TEST-1234",
            "--body-file",
            str(body_file),
        ],
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "h2. Resume" in stderr.getvalue()
    assert runner.requests == []
    assert body_file.exists()


def test_jira_comment_resume_reports_duplicate_resumes(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    first = _jira_resume_comment("30001", "h2. Resume\n\nOne.\n")
    second = _jira_resume_comment(
        "30002",
        "h2. Resume\n\nTwo.\n",
        created="2026-05-15T09:35:00.000+0900",
        updated="2026-05-15T09:35:00.000+0900",
    )
    _seed_cached_issue(tmp_path, comments=[first, second])
    body_file = _write_body_file(tmp_path, "h2. Resume\n\nThree.\n", name="resume.md")
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()),
                stdout=json.dumps(jira_issue_payload(comments=[first, second])),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()), stdout=json.dumps(remote_links_payload())
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "resume",
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
    assert payload["reason"] == "duplicate_resume_comments"
    assert sorted(payload["comment_ids"]) == ["30001", "30002"]
    assert payload["body_file_removed"] is False
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert write_requests == []
    assert body_file.exists()
