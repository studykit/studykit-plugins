"""Jira Cloud agile CLI request and guard tests."""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from agile.cli import main  # noqa: E402
from command import CommandRequest, CommandResult  # noqa: E402

SITE = "https://acme.atlassian.net"


class Runner:
    def __init__(self, responses: list[object]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        value = self.responses.pop(0)
        if isinstance(value, CommandResult):
            return CommandResult(request, value.returncode, value.stdout, value.stderr)
        return CommandResult(request, 0, json.dumps(value))

    def urls(self) -> list[str]:
        urls = []
        for request in self.requests:
            if "GET" in request.args:
                urls.append(request.args[-1])
            else:
                lines = (request.input_text or "").splitlines()
                urls.append(json.loads(next(line.split(" = ", 1)[1] for line in lines if line.startswith("url = "))))
        return urls

    def bodies(self) -> list[object]:
        result = []
        for request in self.requests:
            lines = (request.input_text or "").splitlines()
            for line in lines:
                if line.startswith("data-binary = "):
                    result.append(json.loads(json.loads(line.split(" = ", 1)[1])))
        return result


@pytest.fixture(autouse=True)
def credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JIRA_EMAIL", "user@example.test")
    monkeypatch.setenv("JIRA_API_TOKEN", "test-token")


def config(tmp_path: Path, kind: str = "jira", site: str = SITE) -> None:
    path = tmp_path / ".spectrack" / "config.yml"
    path.parent.mkdir()
    settings = f"    site: {site}\n" if kind == "jira" else ""
    path.write_text(f"version: 1\nproviders:\n  issues:\n    kind: {kind}\n{settings}  knowledge:\n    kind: github\nissue_id_format: {'jira' if kind == 'jira' else 'github'}\n")


def invoke(tmp_path: Path, runner: Runner, *args: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    status = main(["--project", str(tmp_path), *args], stdout=out, stderr=err, runner=runner)
    return status, out.getvalue(), err.getvalue()


@pytest.mark.parametrize("kind,site", [("github", SITE), ("jira", "https://jira.example.test")])
def test_refuses_non_cloud_before_request(tmp_path: Path, kind: str, site: str) -> None:
    config(tmp_path, kind, site)
    runner = Runner([])
    status, _, error = invoke(tmp_path, runner, "board", "list")
    assert status == 1 and ("Cloud" in error or "Jira" in error)
    assert not runner.requests


def test_token_pagination(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([{"issues": [{"key": "TEST-1"}], "nextPageToken": "abc"}, {"issues": [{"key": "TEST-2"}]}])
    status, output, _ = invoke(tmp_path, runner, "board", "issues", "7", "--all")
    assert status == 0
    assert [issue["key"] for issue in json.loads(output)["issues"]] == ["TEST-1", "TEST-2"]
    assert "nextPageToken=abc" in runner.urls()[1]
    assert all("/rest/software/1.0/" in url for url in runner.urls())


def test_offset_pagination(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([{"values": [{"id": 1}], "startAt": 0, "isLast": False},
                     {"values": [{"id": 2}], "startAt": 1, "isLast": True}])
    status, output, _ = invoke(tmp_path, runner, "sprint", "list", "7", "--all")
    assert status == 0 and len(json.loads(output)["values"]) == 2
    assert "startAt=1" in runner.urls()[1]


def test_board_create_and_filter_rollback(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([{"id": 42}, {"id": 7}])
    status, _, _ = invoke(tmp_path, runner, "board", "create", "--name", "Demo", "--type", "kanban", "--jql", "project = TEST")
    assert status == 0
    assert runner.urls() == [f"{SITE}/rest/api/3/filter", f"{SITE}/rest/agile/1.0/board"]
    assert runner.bodies()[0]["sharePermissions"] == []
    assert runner.bodies()[1]["filterId"] == 42
    failed = Runner([{"id": 42}, CommandResult(CommandRequest(("curl",)), 22, '{"errorMessages":["bad board"]}'), {}])
    status, _, error = invoke(tmp_path, failed, "board", "create", "--name", "Demo", "--type", "kanban", "--jql", "project = TEST")
    assert status == 1 and "bad board" in error
    assert failed.urls()[-1] == f"{SITE}/rest/api/3/filter/42"


def test_guards_before_request(tmp_path: Path) -> None:
    config(tmp_path)
    cases = [("issue", "rank", *[f"TEST-{n}" for n in range(51)], "--before", "TEST-99"),
             ("sprint", "create", "7", "--name", "a" * 30),
             ("board", "delete", "7"), ("sprint", "delete", "7"),
             ]
    for case in cases:
        runner = Runner([])
        status, _, _ = invoke(tmp_path, runner, *case)
        assert status != 0 and not runner.requests


def test_sprint_start_requires_dates(tmp_path: Path) -> None:
    config(tmp_path)
    with pytest.raises(SystemExit) as exc:
        invoke(tmp_path, Runner([]), "sprint", "start", "7")
    assert exc.value.code == 2


def test_kanban_guard_and_operation_routes(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([{"type": "scrum"}])
    status, _, error = invoke(tmp_path, runner, "board", "add", "7", "TEST-1")
    assert status == 1 and "kanban" in error and len(runner.requests) == 1
    for args, path, method in [
        (("issue", "estimate", "TEST-1", "--board", "7"), "/issue/TEST-1/estimation?boardId=7", "GET"),
        (("issue", "estimate", "TEST-1", "--board", "7", "3"), "/issue/TEST-1/estimation?boardId=7", "PUT"),
        (("epic", "remove", "TEST-1"), "/epic/none/issue", "POST"),
    ]:
        runner = Runner([{}])
        status, _, _ = invoke(tmp_path, runner, *args)
        assert status == 0 and runner.urls()[0].endswith(path)
        if method == "GET": assert "GET" in runner.requests[0].args
        else: assert f'request = "{method}"' in runner.requests[0].input_text
