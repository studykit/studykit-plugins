"""Confluence Cloud page CLI request and guard tests."""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from command import CommandRequest, CommandResult  # noqa: E402
from confluence import api  # noqa: E402
from confluence.cli import main  # noqa: E402

SITE = "https://acme.atlassian.net"
DOC = {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": "hi"}]}]}


class Runner:
    def __init__(self, responses: list[object]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        return CommandResult(request, 0, json.dumps(self.responses.pop(0)))

    def calls(self) -> list[tuple[str, str]]:
        result = []
        for request in self.requests:
            if "GET" in request.args:
                result.append(("GET", request.args[-1]))
                continue
            fields = dict(line.split(" = ", 1) for line in (request.input_text or "").splitlines() if " = " in line)
            result.append((json.loads(fields["request"]), json.loads(fields["url"])))
        return result

    def bodies(self) -> list[object]:
        return [json.loads(json.loads(line.split(" = ", 1)[1]))
                for request in self.requests for line in (request.input_text or "").splitlines()
                if line.startswith("data-binary = ")]


@pytest.fixture(autouse=True)
def credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JIRA_EMAIL", "user@example.test")
    monkeypatch.setenv("JIRA_API_TOKEN", "test-token")


def config(tmp_path: Path, kind: str = "jira", site: str = SITE) -> None:
    path = tmp_path / ".spectrack" / "config.yml"
    path.parent.mkdir()
    settings = f"    site: {site}\n" if kind == "jira" else ""
    path.write_text(f"version: 1\nproviders:\n  issues:\n    kind: {kind}\n{settings}  knowledge:\n    kind: github\nissue_id_format: {'jira' if kind == 'jira' else 'github'}\n")


def invoke(tmp_path: Path, runner: Runner, *args: str) -> tuple[int, dict, str]:
    out, err = io.StringIO(), io.StringIO()
    status = main(["--project", str(tmp_path), *args], stdout=out, stderr=err, runner=runner)
    return status, json.loads(out.getvalue()) if out.getvalue() else {}, err.getvalue()


def page(version: int = 3, body: dict | None = None) -> dict:
    result = {"id": "42", "title": "Setup", "status": "current", "spaceId": "7", "parentId": "1",
              "version": {"number": version}, "_links": {"base": f"{SITE}/wiki", "webui": "/spaces/DOC/pages/42"}}
    if body is not None:
        result["body"] = {"atlas_doc_format": {"value": json.dumps(body), "representation": "atlas_doc_format"}}
    return result


@pytest.mark.parametrize("kind,site", [("github", SITE), ("jira", "https://jira.example.test")])
def test_refuses_non_cloud_before_request(tmp_path: Path, kind: str, site: str) -> None:
    config(tmp_path, kind, site)
    runner = Runner([])
    status, _, error = invoke(tmp_path, runner, "page", "get", "42")
    assert status == 1 and ("Cloud" in error or "Jira" in error)
    assert not runner.requests


def test_get_renders_markdown_through_converter(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([page(body=DOC), {"value": "hi\n"}])
    status, result, _ = invoke(tmp_path, runner, "page", "get", "42")
    assert status == 0
    assert result["body"] == "hi\n" and result["version"] == 3
    assert result["url"] == f"{SITE}/wiki/spaces/DOC/pages/42"
    assert runner.calls()[0] == ("GET", f"{SITE}/wiki/api/v2/pages/42?body-format=atlas_doc_format")


def test_get_adf_to_file_prints_metadata_only(tmp_path: Path) -> None:
    config(tmp_path)
    target = tmp_path / "page.json"
    runner = Runner([page(body=DOC)])
    status, result, _ = invoke(tmp_path, runner, "page", "get", "42", "--format", "adf", "--output", str(target))
    assert status == 0 and "body" not in result
    assert json.loads(target.read_text()) == DOC
    assert len(runner.requests) == 1


def test_update_refuses_stale_version(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([page(version=5, body=DOC)])
    status, _, error = invoke(tmp_path, runner, "page", "update", "42", "--title", "New", "--expected-version", "4")
    assert status == 1 and "version 5" in error
    assert len(runner.requests) == 1


def test_title_update_resends_current_body(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([page(version=3, body=DOC), page(version=4)])
    status, result, _ = invoke(tmp_path, runner, "page", "update", "42", "--title", "New", "--message", "rename")
    assert status == 0 and result["version"] == 4
    assert runner.calls()[1] == ("PUT", f"{SITE}/wiki/api/v2/pages/42")
    sent = runner.bodies()[0]
    assert sent["title"] == "New" and sent["status"] == "current"
    assert sent["version"] == {"number": 4, "message": "rename"}
    assert json.loads(sent["body"]["value"]) == DOC


def test_markdown_body_update_converts_to_adf(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config(tmp_path)
    monkeypatch.setattr(api, "markdown_to_adf", lambda text, runner=None: DOC)
    source = tmp_path / "body.md"
    source.write_text("hi\n")
    runner = Runner([page(version=3), page(version=4)])
    status, _, _ = invoke(tmp_path, runner, "page", "update", "42", "--body", str(source))
    assert status == 0
    assert runner.calls()[0] == ("GET", f"{SITE}/wiki/api/v2/pages/42")
    sent = runner.bodies()[0]
    assert sent["title"] == "Setup"
    assert sent["body"]["representation"] == "atlas_doc_format" and json.loads(sent["body"]["value"]) == DOC


def test_create_resolves_space_key(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([{"results": [{"id": "7", "key": "DOC"}]}, page(version=1)])
    status, result, _ = invoke(tmp_path, runner, "page", "create", "--space", "DOC", "--title", "Setup", "--parent", "1")
    assert status == 0 and result["id"] == "42"
    assert runner.calls()[0] == ("GET", f"{SITE}/wiki/api/v2/spaces?keys=DOC")
    assert runner.bodies()[0] == {"spaceId": "7", "status": "current", "title": "Setup", "parentId": "1"}


@pytest.mark.parametrize("flag,position", [("--parent", "append"), ("--before", "before"), ("--after", "after")])
def test_move_uses_v1_positional_move(tmp_path: Path, flag: str, position: str) -> None:
    config(tmp_path)
    runner = Runner([{"pageId": "42"}, page()])
    status, _, _ = invoke(tmp_path, runner, "page", "move", "42", flag, "99")
    assert status == 0
    assert runner.calls()[0] == ("PUT", f"{SITE}/wiki/rest/api/content/42/move/{position}/99")


def test_search_all_follows_v1_relative_cursor(tmp_path: Path) -> None:
    config(tmp_path)
    runner = Runner([
        {"results": [{"title": "a"}], "_links": {"next": "/rest/api/search?cursor=abc"}},
        {"results": [{"title": "b"}], "_links": {}},
    ])
    status, result, _ = invoke(tmp_path, runner, "page", "search", "type = page", "--all")
    assert status == 0 and [item["title"] for item in result["results"]] == ["a", "b"]
    assert runner.calls()[1] == ("GET", f"{SITE}/wiki/rest/api/search?cursor=abc")
