"""Tests for provider-owned issue publish CLIs."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from functools import partial  # noqa: E402

from issue.dispatch import COMMENTS, DRAFTS, WRITEBACK, run_intent  # noqa: E402

github_issue_comments_main = partial(run_intent, COMMENTS)
github_issue_drafts_main = partial(run_intent, DRAFTS)
github_issue_writeback_main = partial(run_intent, WRITEBACK)
jira_issue_drafts_main = partial(run_intent, DRAFTS)
from command import CommandRequest, CommandResult  # noqa: E402
from issue.github.cache import GitHubIssueCache  # noqa: E402
from issue.github.gh import DEFAULT_ISSUE_FIELDS  # noqa: E402
from issue.github.gh import GitHubRepository  # noqa: E402
from issue.jira.client import resolve_jira_data_center_site  # noqa: E402
from issue.jira.cache import JiraDataCenterIssueCache  # noqa: E402


class GitHubFakeRunner:
    def __init__(self) -> None:
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args[:3] == ("gh", "issue", "create"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="https://github.com/studykit/studykit-plugins/issues/51\n",
            )
        if request.args == _gh_issue_view_args(51, "title,body,labels,state,stateReason"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": "Draft issue",
                        "body": "Draft body.\n",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                        "state": "OPEN",
                        "stateReason": None,
                    }
                ),
            )
        if request.args == _gh_issue_view_args(51, ",".join(DEFAULT_ISSUE_FIELDS)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "number": 51,
                        "title": "Draft issue",
                        "state": "OPEN",
                        "stateReason": None,
                        "body": "Draft body.\n",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                        "comments": [],
                        "url": "https://github.com/studykit/studykit-plugins/issues/51",
                        "createdAt": "2026-05-14T00:00:00Z",
                        "updatedAt": "2026-05-14T00:00:00Z",
                        "closedAt": None,
                    }
                ),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/51"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"id": 5100, "number": 51, "updated_at": "2026-05-14T00:00:00Z"}),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/51/parent"):
            return CommandResult(request=request, returncode=404, stderr="not found")
        if request.args in {
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/sub_issues", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/dependencies/blocked_by", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/dependencies/blocking", "--paginate"),
        }:
            return CommandResult(request=request, returncode=0, stdout="[]")
        return CommandResult(request=request, returncode=127, stderr="unexpected command")


def _write_config(project: Path) -> None:
    config_path = project / ".spectrack" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
    path: wiki/spectrack
issue_id_format: github
commit_refs:
  enabled: true
  style: provider-native
""".lstrip(),
        encoding="utf-8",
    )


def _write_jira_config(
    project: Path,
    *,
    relationship_mappings: dict[str, dict[str, str]] | None = None,
) -> None:
    config_path = project / ".spectrack" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    text = """
version: 1
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: data-center
    api_version: 2
    project: TEST
    issue_type: Task
""".lstrip()
    if relationship_mappings:
        text += "    relationship_mappings:\n"
        for name, mapping in relationship_mappings.items():
            text += f"      {name}:\n"
            for key, value in mapping.items():
                text += f"        {key}: {value}\n"
    text += """  knowledge:
    kind: github
issue_id_format: jira
"""
    config_path.write_text(text, encoding="utf-8")


def _repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def _gh_issue_view_args(issue: int | str, fields: str) -> tuple[str, ...]:
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


def _gh_api_args(*args: str) -> tuple[str, ...]:
    return ("gh", "api", *args)


def _write_body_file(project: Path, body: str, *, name: str = "draft.md") -> Path:
    path = project / name
    path.write_text(body, encoding="utf-8")
    return path


def test_github_publish_creates_issue_and_deletes_body_file(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
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
    assert "operation" not in payload
    assert "verified" not in payload
    assert payload["issue"] == "51"
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True
    assert payload["issue_file"].endswith("/issues/51/issue.md")
    assert "cache" not in payload
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=_repo())
    assert cache.read_issue(_repo(), 51)["body"] == "Draft body.\n"
    assert not body_file.exists()
    assert runner.requests[0].args[:3] == ("gh", "issue", "create")


def test_github_publish_strips_body_file_frontmatter(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(
        tmp_path, "---\ntitle: nope\n---\nDraft body.\n", name="draft.md"
    )
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--label",
            "workflow",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["issue"] == "51"
    assert "verified" not in payload
    assert payload["body_file_removed"] is True
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=_repo())
    assert cache.read_issue(_repo(), 51)["body"] == "Draft body.\n"
    assert not body_file.exists()


def test_github_publish_preserves_body_on_relationship_failure(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
            "--related",
            "100",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 1
    assert payload["issue"] == "51"
    assert "verified" not in payload
    assert payload["body_file_removed"] is False
    assert payload["body_file"] == str(body_file)
    assert body_file.exists()
    relationships = payload["relationships"]
    assert relationships["status"] == "failed"
    assert "related" in relationships["error"]
    assert relationships["intent"] == {"related_add": ["100"]}


def test_github_publish_missing_body_file_fails(tmp_path: Path) -> None:
    _write_config(tmp_path)
    runner = GitHubFakeRunner()
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(tmp_path / "missing.md"),
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "body file does not exist" in stderr.getvalue()
    assert runner.requests == []


class GitHubAppendCommentRunner:
    """Fake runner for github_issue_comments append flow."""

    def __init__(
        self,
        *,
        conflict_target: str | None = None,
        state_after: str = "OPEN",
        state_reason_after: object = None,
    ) -> None:
        self.requests: list[CommandRequest] = []
        # ``conflict_target`` ("issue" or "comments") makes the matching
        # provider fingerprint diverge from the seeded cache, which drives the
        # freshness conflict path. ``None`` keeps every target fresh.
        self.conflict_target = conflict_target
        self.state_after = state_after
        self.state_reason_after = state_reason_after
        self.posted_bodies: list[str] = []
        self.state_calls: list[str] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args == _gh_remote_args(_tmp_project_from_args(request)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args == _gh_issue_view_args(72, "number,title,body"):
            body = "Provider-changed body." if self.conflict_target == "issue" else "Cached body."
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {"number": 72, "title": "Issue with appended comment", "body": body}
                ),
            )
        if request.args == _gh_issue_view_args(72, "number,comments"):
            comments = (
                [
                    {
                        "id": "IC_provider_only",
                        "url": "https://github.com/studykit/studykit-plugins/issues/72#issuecomment-9900001",
                        "author": {"login": "studykit"},
                        "body": "Provider-side comment.\n",
                        "createdAt": "2026-05-14T00:05:00Z",
                        "updatedAt": "2026-05-14T00:05:00Z",
                    }
                ]
                if self.conflict_target == "comments"
                else []
            )
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"number": 72, "comments": comments}),
            )
        if request.args[:3] == ("gh", "issue", "comment"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            self.posted_bodies.append(body_file.read_text(encoding="utf-8"))
            return CommandResult(request=request, returncode=0)
        if request.args[:3] == ("gh", "issue", "close"):
            self.state_calls.append("close")
            return CommandResult(request=request, returncode=0)
        if request.args[:3] == ("gh", "issue", "reopen"):
            self.state_calls.append("reopen")
            return CommandResult(request=request, returncode=0)
        if request.args == _gh_issue_view_args(72, "state,stateReason"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": self.state_after, "stateReason": self.state_reason_after}),
            )
        if request.args == _gh_issue_view_args(72, ",".join(DEFAULT_ISSUE_FIELDS)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "number": 72,
                        "title": "Issue with appended comment",
                        "state": self.state_after,
                        "stateReason": self.state_reason_after,
                        "body": "Cached body.",
                        "labels": [{"name": "task"}],
                        "comments": [
                            {
                                "id": "IC_kwDOQplzFM8AAAABCKrz_g",
                                "url": "https://github.com/studykit/studykit-plugins/issues/72#issuecomment-7700001",
                                "author": {"login": "studykit"},
                                "body": self.posted_bodies[-1] if self.posted_bodies else "Comment body.\n",
                                "createdAt": "2026-05-14T00:01:00Z",
                                "updatedAt": "2026-05-14T00:01:00Z",
                            }
                        ],
                        "updatedAt": "2026-05-14T00:01:00Z",
                    }
                ),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/72"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"id": 7200, "number": 72, "updated_at": "2026-05-14T00:01:00Z"}),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/72/parent"):
            return CommandResult(request=request, returncode=404, stderr="not found")
        if request.args in {
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/sub_issues", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/dependencies/blocked_by", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/dependencies/blocking", "--paginate"),
        }:
            return CommandResult(request=request, returncode=0, stdout="[]")
        return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")


def _gh_remote_args(project: Path) -> tuple[str, ...]:
    return ("git", "-C", str(project.resolve(strict=False)), "remote", "get-url", "origin")


def _tmp_project_from_args(request: CommandRequest) -> Path:
    args = request.args
    if len(args) >= 3 and args[0] == "git" and args[1] == "-C":
        return Path(args[2])
    return Path("/tmp")


def _seed_cached_issue(project: Path, issue_number: int = 72, *, updated_at: str = "2026-05-14T00:00:00Z") -> None:
    GitHubIssueCache.for_project(project, configured_repo=_repo()).write_issue_bundle(
        _repo(),
        {
            "number": issue_number,
            "title": "Issue with appended comment",
            "state": "OPEN",
            "stateReason": None,
            "body": "Cached body.",
            "labels": [{"name": "task"}],
            "updatedAt": updated_at,
            "comments": [],
        },
        fetched_at=updated_at,
    )


def test_github_append_posts_comment_and_deletes_body_file(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Comment body.\n", name="comment.md")
    runner = GitHubAppendCommentRunner()
    stdout = io.StringIO()

    code = github_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--type",
            "task",
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
    assert payload["operation"] == "append_comment"
    assert payload["kind"] == "github"
    assert payload["issue"] == "72"
    assert payload["state_changed"] is False
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True
    assert payload["issue_file"].endswith("/issues/72/issue.md")
    assert "cache" not in payload
    assert runner.posted_bodies == ["Comment body.\n"]
    assert runner.state_calls == []
    assert not body_file.exists()


def test_github_append_strips_body_file_frontmatter(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(
        tmp_path, "---\ntitle: nope\n---\nComment body.\n", name="comment.md"
    )
    runner = GitHubAppendCommentRunner()
    stdout = io.StringIO()

    code = github_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--type",
            "task",
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
    assert payload["body_file_removed"] is True
    assert runner.posted_bodies == ["Comment body.\n"]
    assert not body_file.exists()


def test_github_append_missing_body_file_fails(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    runner = GitHubAppendCommentRunner()
    stderr = io.StringIO()

    code = github_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--type",
            "task",
            "--issue",
            "72",
            "--body-file",
            str(tmp_path / "missing.md"),
        ],
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "body file does not exist" in stderr.getvalue()
    assert runner.requests == []


def test_github_append_preserves_body_file_on_freshness_block(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Comment body.\n", name="comment.md")
    runner = GitHubAppendCommentRunner(conflict_target="issue")
    stdout = io.StringIO()

    code = github_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--type",
            "task",
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
    assert payload["status"] == "conflict"
    assert payload["reason"] == "provider_changed"
    assert payload["reread_required"] is True
    assert all(not path.endswith("/.meta.json") for path in payload["reread_paths"])
    assert payload["body_file_removed"] is False
    assert payload["body_file"] == str(body_file)
    assert body_file.exists()
    assert runner.posted_bodies == []
    assert runner.state_calls == []


def test_github_append_applies_inline_state_change(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Closing comment.\n", name="comment.md")
    runner = GitHubAppendCommentRunner(state_after="CLOSED", state_reason_after="COMPLETED")
    stdout = io.StringIO()

    code = github_issue_comments_main(
        [
            "--project",
            str(tmp_path),
            "append",
            "--type",
            "task",
            "--issue",
            "72",
            "--body-file",
            str(body_file),
            "--state",
            "closed",
            "--state-reason",
            "completed",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["state_changed"] is True
    assert payload["state"]["operation"] == "close_issue"
    assert runner.state_calls == ["close"]
    assert runner.posted_bodies == ["Closing comment.\n"]
    assert not body_file.exists()


class GitHubUpdateIssueRunner:
    """Fake runner for github_issue_writeback update flow."""

    def __init__(
        self,
        *,
        conflict: bool = False,
        state_after: str = "OPEN",
        state_reason_after: object = None,
        labels_after: tuple[str, ...] = ("task",),
    ) -> None:
        self.requests: list[CommandRequest] = []
        # ``conflict=True`` returns provider content that diverges from the
        # seeded cache fingerprint, driving the freshness conflict path.
        self.conflict = conflict
        self.state_after = state_after
        self.state_reason_after = state_reason_after
        self.labels_after = labels_after
        self.edit_bodies: list[str] = []
        self.edit_titles: list[str | None] = []
        self.edit_label_args: list[tuple[str, ...]] = []
        self.state_calls: list[str] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args == _gh_remote_args(_tmp_project_from_args(request)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args == _gh_issue_view_args(72, "number,title,body"):
            body = "Provider-changed body." if self.conflict else "Cached body."
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {"number": 72, "title": "Issue with appended comment", "body": body}
                ),
            )
        if request.args == _gh_issue_view_args(72, "number,labels"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"number": 72, "labels": [{"name": "task"}]}),
            )
        if request.args[:3] == ("gh", "issue", "edit"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            self.edit_bodies.append(body_file.read_text(encoding="utf-8"))
            title = None
            if "--title" in request.args:
                title = request.args[request.args.index("--title") + 1]
            self.edit_titles.append(title)
            label_args = tuple(
                arg for arg in request.args if arg.startswith("--add-label") or arg.startswith("--remove-label")
            )
            self.edit_label_args.append(label_args)
            return CommandResult(request=request, returncode=0)
        if request.args == _gh_issue_view_args(72, "body"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"body": self.edit_bodies[-1] if self.edit_bodies else ""}),
            )
        if request.args == _gh_issue_view_args(72, "title,body"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": self.edit_titles[-1] if self.edit_titles else "",
                        "body": self.edit_bodies[-1] if self.edit_bodies else "",
                    }
                ),
            )
        if request.args == _gh_issue_view_args(72, "body,labels"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "body": self.edit_bodies[-1] if self.edit_bodies else "",
                        "labels": [{"name": name} for name in self.labels_after],
                    }
                ),
            )
        if request.args == _gh_issue_view_args(72, "title,body,labels"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": self.edit_titles[-1] if self.edit_titles else "",
                        "body": self.edit_bodies[-1] if self.edit_bodies else "",
                        "labels": [{"name": name} for name in self.labels_after],
                    }
                ),
            )
        if request.args[:3] == ("gh", "issue", "close"):
            self.state_calls.append("close")
            return CommandResult(request=request, returncode=0)
        if request.args[:3] == ("gh", "issue", "reopen"):
            self.state_calls.append("reopen")
            return CommandResult(request=request, returncode=0)
        if request.args == _gh_issue_view_args(72, "state,stateReason"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": self.state_after, "stateReason": self.state_reason_after}),
            )
        if request.args == _gh_issue_view_args(72, ",".join(DEFAULT_ISSUE_FIELDS)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "number": 72,
                        "title": self.edit_titles[-1] or "Issue title" if self.edit_titles else "Issue title",
                        "state": self.state_after,
                        "stateReason": self.state_reason_after,
                        "body": self.edit_bodies[-1] if self.edit_bodies else "Updated body.",
                        "labels": [{"name": name} for name in self.labels_after],
                        "comments": [],
                        "updatedAt": "2026-05-14T00:01:00Z",
                    }
                ),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/72"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"id": 7200, "number": 72, "updated_at": "2026-05-14T00:01:00Z"}),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/72/parent"):
            return CommandResult(request=request, returncode=404, stderr="not found")
        if request.args in {
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/sub_issues", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/dependencies/blocked_by", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/72/dependencies/blocking", "--paginate"),
        }:
            return CommandResult(request=request, returncode=0, stdout="[]")
        return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")


def test_github_update_writes_body_and_deletes_body_file(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Updated body.\n", name="update.md")
    runner = GitHubUpdateIssueRunner()
    stdout = io.StringIO()

    code = github_issue_writeback_main(
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
    assert "operation" not in payload
    assert "verified" not in payload
    assert payload["kind"] == "github"
    assert payload["issue"] == "72"
    assert payload["state_changed"] is False
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True
    assert payload["issue_file"].endswith("/issues/72/issue.md")
    assert "cache" not in payload
    assert runner.edit_bodies == ["Updated body.\n"]
    assert runner.edit_titles == [None]
    assert runner.state_calls == []
    assert not body_file.exists()


def test_github_update_strips_body_file_frontmatter(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(
        tmp_path, "---\ntitle: nope\n---\nUpdated body.\n", name="update.md"
    )
    runner = GitHubUpdateIssueRunner()
    stdout = io.StringIO()

    code = github_issue_writeback_main(
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
    assert payload["body_file_removed"] is True
    assert runner.edit_bodies == ["Updated body.\n"]
    assert not body_file.exists()


def test_github_update_missing_body_file_fails(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    runner = GitHubUpdateIssueRunner()
    stderr = io.StringIO()

    code = github_issue_writeback_main(
        [
            "--project",
            str(tmp_path),
            "update",
            "--issue",
            "72",
            "--body-file",
            str(tmp_path / "missing.md"),
        ],
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "body file does not exist" in stderr.getvalue()
    assert runner.requests == []


def test_github_update_preserves_body_file_on_freshness_block(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Updated body.\n", name="update.md")
    runner = GitHubUpdateIssueRunner(conflict=True)
    stdout = io.StringIO()

    code = github_issue_writeback_main(
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
    assert payload["status"] == "conflict"
    assert payload["reason"] == "provider_changed"
    assert payload["reread_required"] is True
    assert all(not path.endswith("/.meta.json") for path in payload["reread_paths"])
    assert payload["body_file_removed"] is False
    assert payload["body_file"] == str(body_file)
    assert body_file.exists()
    assert runner.edit_bodies == []
    assert runner.state_calls == []


def test_github_update_applies_inline_state_change(tmp_path: Path) -> None:
    _write_config(tmp_path)
    _seed_cached_issue(tmp_path)
    body_file = _write_body_file(tmp_path, "Final body.\n", name="update.md")
    runner = GitHubUpdateIssueRunner(
        state_after="CLOSED",
        state_reason_after="COMPLETED",
        labels_after=("workflow",),
    )
    stdout = io.StringIO()

    code = github_issue_writeback_main(
        [
            "--project",
            str(tmp_path),
            "update",
            "--issue",
            "72",
            "--body-file",
            str(body_file),
            "--title",
            "Renamed issue",
            "--set-labels",
            "workflow",
            "--state",
            "closed",
            "--state-reason",
            "completed",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["state_changed"] is True
    assert payload["state"]["operation"] == "close_issue"
    assert runner.state_calls == ["close"]
    assert runner.edit_bodies == ["Final body.\n"]
    assert runner.edit_titles == ["Renamed issue"]
    assert runner.edit_label_args[-1] == ("--add-label", "--remove-label")
    assert not body_file.exists()


class JiraFakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]) -> None:
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        for key, value in self.responses.items():
            if request.args == key:
                return CommandResult(
                    request=request,
                    returncode=value.returncode,
                    stdout=value.stdout,
                    stderr=value.stderr,
                )
        return CommandResult(request=request, returncode=127, stderr=f"unexpected: {request.args}")


def _jira_curl_get_args(url: str) -> tuple[str, ...]:
    return (
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--request",
        "GET",
        "--config",
        "-",
        url,
    )


def _jira_write_args() -> tuple[str, ...]:
    return (
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--config",
        "-",
    )


def _jira_issue_payload(key: str = "TEST-1234") -> dict[str, object]:
    return {
        "id": "10001",
        "key": key,
        "fields": {
            "summary": "Published Jira issue",
            "description": "Body.\n",
            "labels": ["workflow"],
            "status": {"name": "Open"},
            "issuetype": {"name": "Task"},
            "created": "2026-05-14T00:00:00.000+0000",
            "updated": "2026-05-14T00:00:00.000+0000",
        },
    }


def test_jira_publish_creates_issue_inline_and_deletes_body_file(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    site = resolve_jira_data_center_site(tmp_path)
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

    code = jira_issue_drafts_main(
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
    assert "operation" not in payload
    assert "verified" not in payload
    assert payload["issue"] == "TEST-1234"
    assert payload["body_file_removed"] is True
    assert payload["issue_file"].endswith("issues/TEST-1234/issue.md")
    assert "cache" not in payload
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    assert cache.issue_json_file(site, "TEST-1234").is_file()
    assert not body_file.exists()
    assert runner.requests[0].args == _jira_write_args()


def test_jira_publish_fails_fast_when_relationship_mapping_missing(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")

    runner = JiraFakeRunner({})
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--body-file",
            str(body_file),
            "--related",
            "TEST-99",
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "Jira relationship 'related' is not configured" in stderr.getvalue()
    assert runner.requests == []
    assert body_file.exists()
    assert stdout.getvalue() == ""


class JiraPublishRelationshipFailureRunner(JiraFakeRunner):
    """Mirror of GitHub's post-create relationship failure shape for Jira.

    The Jira `create` and `create_issue_link` POSTs both hit curl with the
    same outer argv (``_jira_write_args()``); the destination URL lives in
    the curl --config stdin. This subclass routes the create POST to the
    success response and lets the link POST fall through to the default
    ``returncode=127`` raise that trips ``_publish_issue``'s
    ``except Exception`` handler.
    """

    def __call__(self, request: CommandRequest) -> CommandResult:
        if request.args == _jira_write_args() and "/issueLink" in (request.input_text or ""):
            self.requests.append(request)
            return CommandResult(
                request=request,
                returncode=127,
                stderr="unexpected: issueLink dispatch (intended to fail)",
            )
        return super().__call__(request)


def test_jira_publish_preserves_body_on_relationship_failure(tmp_path: Path) -> None:
    _write_jira_config(
        tmp_path,
        relationship_mappings={"related": {"link_type": "Relates", "direction": "outward"}},
    )
    body_file = _write_body_file(tmp_path, "Body.\n")
    issue_url = "https://jira.example.test/rest/api/2/issue/TEST-1234"
    remote_links_url = "https://jira.example.test/rest/api/2/issue/TEST-1234/remotelink"

    runner = JiraPublishRelationshipFailureRunner(
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

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--body-file",
            str(body_file),
            "--related",
            "TEST-99",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 1
    assert payload["issue"] == "TEST-1234"
    assert payload["body_file_removed"] is False
    assert payload["body_file"] == str(body_file)
    assert body_file.exists()
    relationships = payload["relationships"]
    assert relationships["status"] == "failed"
    assert relationships["intent"] == {"related_add": ["TEST-99"]}
    # Guard: the create POST must actually fire so a future regression that
    # short-circuits in the pre-create validator (the branch already covered
    # by test_jira_publish_fails_fast_when_relationship_mapping_missing) does
    # not silently pass this post-create regression test.
    assert runner.requests[0].args == _jira_write_args()
    link_writes = [
        r for r in runner.requests
        if r.args == _jira_write_args() and "/issueLink" in (r.input_text or "")
    ]
    assert len(link_writes) == 1


def test_jira_publish_epic_with_post_create_epic_link_is_rejected(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    runner = JiraFakeRunner({})
    stderr = io.StringIO()

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "epic",
            "--title",
            "New Epic",
            "--body-file",
            str(body_file),
            "--epic",
            "TEST-99",
        ],
        stdout=io.StringIO(),
        stderr=stderr,
        runner=runner,
    )

    assert code != 0
    assert "publish --epic cannot be combined with --type epic" in stderr.getvalue()
    assert runner.requests == []
    assert body_file.exists()


def test_jira_publish_accepts_assignee_user_and_sets_field_on_post(tmp_path: Path) -> None:
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

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--body-file",
            str(body_file),
            "--assignee",
            "alice",
        ],
        stdout=stdout,
        runner=runner,
    )

    assert code == 0
    write_request = runner.requests[0]
    assert write_request.args == _jira_write_args()
    assert '\\"assignee\\":{\\"name\\":\\"alice\\"}' in str(write_request.input_text)


def test_jira_publish_accepts_assignee_me_and_resolves_current_user(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    myself_url = "https://jira.example.test/rest/api/2/myself"
    issue_url = "https://jira.example.test/rest/api/2/issue/TEST-1234"
    remote_links_url = "https://jira.example.test/rest/api/2/issue/TEST-1234/remotelink"

    runner = JiraFakeRunner(
        {
            _jira_curl_get_args(myself_url): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps({"name": "studykit-svc", "displayName": "Studykit Service"}),
            ),
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

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--body-file",
            str(body_file),
            "--assignee",
            "me",
        ],
        stdout=stdout,
        runner=runner,
    )

    assert code == 0
    myself_calls = [r for r in runner.requests if r.args == _jira_curl_get_args(myself_url)]
    assert len(myself_calls) == 1
    write_requests = [r for r in runner.requests if r.args == _jira_write_args()]
    assert any(
        '\\"assignee\\":{\\"name\\":\\"studykit-svc\\"}' in str(r.input_text)
        for r in write_requests
    )


def test_github_publish_accepts_assignee_user_and_passes_to_gh_create(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
            "--assignee",
            "alice",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert "operation" not in payload
    assert "verified" not in payload
    create_request = next(r for r in runner.requests if r.args[:3] == ("gh", "issue", "create"))
    assert "--assignee" in create_request.args
    assert create_request.args[create_request.args.index("--assignee") + 1] == "alice"


def test_github_publish_accepts_assignee_me_and_resolves_current_login(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    base_runner = GitHubFakeRunner()

    me_args = _gh_api_args("user", "--jq", ".login")

    class _AssigneeMeRunner:
        def __init__(self) -> None:
            self.requests: list[CommandRequest] = []

        def __call__(self, request: CommandRequest) -> CommandResult:
            self.requests.append(request)
            if request.args == me_args:
                return CommandResult(
                    request=request,
                    returncode=0,
                    stdout="studykit-bot\n",
                )
            return base_runner(request)

    runner = _AssigneeMeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
            "--assignee",
            "me",
        ],
        stdout=stdout,
        runner=runner,
    )

    assert code == 0
    me_calls = [r for r in runner.requests if r.args == me_args]
    assert len(me_calls) == 1
    create_request = next(r for r in runner.requests if r.args[:3] == ("gh", "issue", "create"))
    assert "--assignee" in create_request.args
    assert create_request.args[create_request.args.index("--assignee") + 1] == "studykit-bot"
