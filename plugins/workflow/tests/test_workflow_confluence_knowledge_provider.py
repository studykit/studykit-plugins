"""Tests for the Confluence Data Center knowledge provider."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_confluence_knowledge_provider import (  # noqa: E402
    ConfluenceDataCenterKnowledgeNativeProvider,
)
from workflow_providers import (  # noqa: E402
    ProviderContext,
    ProviderDispatcher,
    ProviderOperationError,
    ProviderRequest,
    TRANSPORT_NATIVE,
    default_provider_registry,
)


BASE_URL = "https://wiki.example.internal"


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


def make_result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(
        request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr
    )


def write_confluence_config(
    project: Path,
    *,
    space: str | None = "ENG",
    parent_page_id: str | None = None,
    space_id: str | None = None,
) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    extra_lines = ""
    if space is not None:
        extra_lines += f"    space: {space}\n"
    if parent_page_id is not None:
        extra_lines += f'    parent_page_id: "{parent_page_id}"\n'
    if space_id is not None:
        extra_lines += f'    space_id: "{space_id}"\n'
    path.write_text(
        f"""version: 1
providers:
  issues:
    kind: github
  knowledge:
    kind: confluence
    site: {BASE_URL}
    deployment: data_center
{extra_lines}""",
        encoding="utf-8",
    )


def get_args(path: str) -> tuple[str, ...]:
    return (
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--request",
        "GET",
        "--config",
        "-",
        f"{BASE_URL}{path}",
    )


def write_args() -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--config", "-")


def page_payload(
    *,
    page_id: str = "42",
    title: str = "Page title",
    space: str = "ENG",
    version: int = 7,
    body: str | None = "<p>body</p>",
    labels: list[str] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "id": page_id,
        "title": title,
        "space": {"key": space},
        "version": {"number": version},
        "metadata": {
            "labels": {
                "results": [{"name": name} for name in (labels or ["design"])],
            }
        },
    }
    if body is not None:
        payload["body"] = {"storage": {"value": body, "representation": "storage"}}
    return payload


def make_provider(runner: FakeRunner) -> ConfluenceDataCenterKnowledgeNativeProvider:
    return ConfluenceDataCenterKnowledgeNativeProvider(runner=runner)


def make_request(
    project: Path,
    operation: str,
    payload: dict[str, Any] | None = None,
    *,
    artifact_type: str = "spec",
) -> ProviderRequest:
    return ProviderRequest(
        role="knowledge",
        kind="confluence",
        operation=operation,
        context=ProviderContext(project=project, artifact_type=artifact_type),
        payload=payload or {},
    )


def call(
    project: Path,
    operation: str,
    runner: FakeRunner,
    payload: dict[str, Any] | None = None,
    *,
    artifact_type: str = "spec",
) -> Any:
    provider = make_provider(runner)
    request = make_request(project, operation, payload, artifact_type=artifact_type)
    return provider.call(request).payload


# ---- get -----------------------------------------------------------------


def test_get_requests_full_expand_and_returns_canonical_page(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    expected_path = "/rest/api/content/42?expand=space,version,body.storage,metadata.labels"
    runner = FakeRunner(
        {get_args(expected_path): make_result(get_args(expected_path), stdout=json.dumps(page_payload()))}
    )

    response = call(tmp_path, "get", runner, payload={"page_id": "42"})

    assert response["page_id"] == "42"
    assert response["title"] == "Page title"
    assert response["body"] == "<p>body</p>"
    assert response["url"] == f"{BASE_URL}/pages/viewpage.action?pageId=42"
    assert response["confluence"]["deployment"] == "data_center"
    assert runner.requests[0].args == get_args(expected_path)


def test_get_without_body_drops_storage_expand_and_body(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    expected_path = "/rest/api/content/42?expand=space,version,metadata.labels"
    runner = FakeRunner(
        {
            get_args(expected_path): make_result(
                get_args(expected_path), stdout=json.dumps(page_payload(body=None))
            )
        }
    )

    response = call(tmp_path, "get", runner, payload={"page_id": "42", "include_body": False})

    assert "body" not in response
    assert runner.requests[0].args == get_args(expected_path)


def test_get_missing_page_id_raises(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="confluence:get: missing page_id"):
        call(tmp_path, "get", runner, payload={})


@pytest.mark.parametrize("alias", ["page", "id"])
def test_get_accepts_page_id_aliases(tmp_path: Path, alias: str) -> None:
    write_confluence_config(tmp_path)
    expected_path = "/rest/api/content/42?expand=space,version,body.storage,metadata.labels"
    runner = FakeRunner(
        {get_args(expected_path): make_result(get_args(expected_path), stdout=json.dumps(page_payload()))}
    )

    response = call(tmp_path, "get", runner, payload={alias: "42"})

    assert response["page_id"] == "42"


def test_cloud_deployment_surfaces_unprefixed_unsupported_message(tmp_path: Path) -> None:
    path = tmp_path / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""version: 1
providers:
  issues:
    kind: github
  knowledge:
    kind: confluence
    site: {BASE_URL}
    deployment: cloud
""",
        encoding="utf-8",
    )
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError) as info:
        call(tmp_path, "get", runner, payload={"page_id": "42"})
    assert (
        str(info.value)
        == "confluence cloud is not supported by this provider; use deployment: data_center"
    )


# ---- metadata ------------------------------------------------------------


def test_metadata_uses_label_expand_and_drops_body(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    expected_path = "/rest/api/content/42?expand=space,version,metadata.labels"
    runner = FakeRunner(
        {
            get_args(expected_path): make_result(
                get_args(expected_path), stdout=json.dumps(page_payload(body=None))
            )
        }
    )

    response = call(tmp_path, "metadata", runner, payload={"page_id": "42"})

    assert "body" not in response
    assert response["title"] == "Page title"
    assert runner.requests[0].args == get_args(expected_path)


# ---- search --------------------------------------------------------------


def search_url(cql: str, *, limit: int = 25, expand: str = "space,version") -> str:
    return f"/rest/api/content/search?cql={quote(cql, safe='')}&limit={limit}&expand={expand}"


def test_search_with_query_and_configured_space_builds_default_cql(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    cql = 'type = page AND space = "ENG" AND text ~ "OAuth"'
    path = search_url(cql)
    response_body = {"results": [page_payload(body=None)], "start": 0, "limit": 25, "size": 1}
    runner = FakeRunner({get_args(path): make_result(get_args(path), stdout=json.dumps(response_body))})

    response = call(tmp_path, "search", runner, payload={"query": "OAuth"})

    assert response["cql"] == cql
    assert response["size"] == 1
    assert response["results"][0]["page_id"] == "42"
    assert "body" not in response["results"][0]


def test_search_query_without_space_and_without_global_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, space=None)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="missing space scope"):
        call(tmp_path, "search", runner, payload={"query": "OAuth"})


def test_search_query_global_search_builds_unscoped_cql(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, space=None)
    cql = 'type = page AND text ~ "OAuth"'
    path = search_url(cql)
    runner = FakeRunner({get_args(path): make_result(get_args(path), stdout=json.dumps({"results": []}))})

    response = call(tmp_path, "search", runner, payload={"query": "OAuth", "global_search": True})

    assert response["cql"] == cql
    assert response["results"] == []


def test_search_raw_cql_without_space_when_space_configured_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match='raw cql must include explicit space = "ENG"'):
        call(tmp_path, "search", runner, payload={"cql": 'type = page AND text ~ "OAuth"'})


def test_search_raw_cql_with_ancestor_passes_through_verbatim(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    cql = 'space = "ENG" AND text ~ "PROJ-123" AND ancestor = 1000001'
    path = search_url(cql)
    runner = FakeRunner({get_args(path): make_result(get_args(path), stdout=json.dumps({"results": []}))})

    response = call(tmp_path, "search", runner, payload={"cql": cql})

    assert response["cql"] == cql
    encoded_url = runner.requests[0].args[-1]
    assert quote(cql, safe="") in encoded_url


def test_search_response_envelope_contains_required_keys(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    cql = 'type = page AND space = "ENG" AND text ~ "OAuth"'
    path = search_url(cql)
    response_body = {
        "results": [page_payload(body=None)],
        "start": 0,
        "limit": 25,
        "size": 1,
    }
    runner = FakeRunner({get_args(path): make_result(get_args(path), stdout=json.dumps(response_body))})

    response = call(tmp_path, "search", runner, payload={"query": "OAuth"})

    assert set(response) >= {"provider", "kind", "cql", "start", "limit", "size", "results", "confluence"}
    assert response["provider"] == "confluence"
    assert response["kind"] == "search"


def test_search_missing_query_and_cql_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="missing query or cql"):
        call(tmp_path, "search", runner, payload={})


# ---- create --------------------------------------------------------------


def test_create_posts_expected_storage_payload(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, parent_page_id="987654")
    response_body = page_payload(page_id="100", title="New page", body="<p>hi</p>")
    get_path = "/rest/api/content/100?expand=space,version,body.storage,metadata.labels"
    runner = FakeRunner(
        {
            write_args(): make_result(write_args(), stdout=json.dumps(response_body)),
            get_args(get_path): make_result(get_args(get_path), stdout=json.dumps(response_body)),
        }
    )

    response = call(
        tmp_path,
        "create",
        runner,
        payload={"title": "New page", "body": "<p>hi</p>"},
    )

    assert response["page_id"] == "100"
    write_request = runner.requests[0]
    assert write_request.args == write_args()
    body_text = str(write_request.input_text)
    assert 'request = "POST"' in body_text
    assert f'url = "{BASE_URL}/rest/api/content"' in body_text
    assert '\\"type\\":\\"page\\"' in body_text
    assert '\\"title\\":\\"New page\\"' in body_text
    assert '\\"space\\":{\\"key\\":\\"ENG\\"}' in body_text
    assert '\\"ancestors\\":[{\\"id\\":\\"987654\\"}]' in body_text
    assert '\\"body\\":{\\"storage\\":{\\"value\\":\\"<p>hi</p>\\",\\"representation\\":\\"storage\\"}}' in body_text


def test_create_uses_configured_space_when_payload_omits_space(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({write_args(): make_result(write_args(), stdout=json.dumps(page_payload()))})

    call(tmp_path, "create", runner, payload={"title": "T", "body": "B"})

    body_text = str(runner.requests[0].input_text)
    assert '\\"space\\":{\\"key\\":\\"ENG\\"}' in body_text


def test_create_with_only_space_id_is_rejected(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, space=None, space_id="123456")
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="missing space"):
        call(tmp_path, "create", runner, payload={"title": "T", "body": "B"})


def test_create_missing_title_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="missing title"):
        call(tmp_path, "create", runner, payload={"body": "B"})


def test_create_missing_body_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="missing body"):
        call(tmp_path, "create", runner, payload={"title": "T"})


def test_create_without_parent_omits_ancestors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({write_args(): make_result(write_args(), stdout=json.dumps(page_payload()))})

    call(tmp_path, "create", runner, payload={"title": "T", "body": "B"})

    body_text = str(runner.requests[0].input_text)
    assert "ancestors" not in body_text


# ---- update --------------------------------------------------------------


def test_update_pre_fetches_then_increments_version(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    pre_path = "/rest/api/content/42?expand=space,version,body.storage"
    current = page_payload(version=7, body="<p>old</p>", title="Old title", space="OPS")
    updated = page_payload(version=8, body="<p>new</p>", title="New title", space="OPS")
    runner = FakeRunner(
        {
            get_args(pre_path): make_result(get_args(pre_path), stdout=json.dumps(current)),
            write_args(): make_result(write_args(), stdout=json.dumps(updated)),
        }
    )

    response = call(
        tmp_path,
        "update",
        runner,
        payload={"page_id": "42", "title": "New title", "body": "<p>new</p>"},
    )

    assert response["version"] == 8
    put_request = runner.requests[1]
    body_text = str(put_request.input_text)
    assert 'request = "PUT"' in body_text
    assert f'url = "{BASE_URL}/rest/api/content/42"' in body_text
    assert '\\"id\\":\\"42\\"' in body_text
    assert '\\"type\\":\\"page\\"' in body_text
    assert '\\"title\\":\\"New title\\"' in body_text
    assert '\\"space\\":{\\"key\\":\\"OPS\\"}' in body_text
    assert '\\"version\\":{\\"number\\":8}' in body_text
    assert '\\"body\\":{\\"storage\\":{\\"value\\":\\"<p>new</p>\\",\\"representation\\":\\"storage\\"}}' in body_text


def test_update_falls_back_to_current_title_and_body(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    pre_path = "/rest/api/content/42?expand=space,version,body.storage"
    current = page_payload(version=7, body="<p>old</p>", title="Old title")
    runner = FakeRunner(
        {
            get_args(pre_path): make_result(get_args(pre_path), stdout=json.dumps(current)),
            write_args(): make_result(write_args(), stdout=json.dumps(page_payload(version=8))),
        }
    )

    call(tmp_path, "update", runner, payload={"page_id": "42", "title": "Refreshed"})

    body_text = str(runner.requests[1].input_text)
    assert '\\"title\\":\\"Refreshed\\"' in body_text
    assert '\\"value\\":\\"<p>old</p>\\"' in body_text


def test_update_with_no_title_and_no_body_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    with pytest.raises(ProviderOperationError, match="nothing to update"):
        call(tmp_path, "update", runner, payload={"page_id": "42"})


def test_update_missing_version_in_pre_fetch_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    pre_path = "/rest/api/content/42?expand=space,version,body.storage"
    broken = {"id": "42", "title": "x", "space": {"key": "ENG"}}
    runner = FakeRunner({get_args(pre_path): make_result(get_args(pre_path), stdout=json.dumps(broken))})

    with pytest.raises(ProviderOperationError, match="missing current version"):
        call(tmp_path, "update", runner, payload={"page_id": "42", "title": "T"})


def test_update_missing_space_in_pre_fetch_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    pre_path = "/rest/api/content/42?expand=space,version,body.storage"
    broken = {"id": "42", "title": "x", "version": {"number": 1}}
    runner = FakeRunner({get_args(pre_path): make_result(get_args(pre_path), stdout=json.dumps(broken))})

    with pytest.raises(ProviderOperationError, match="missing space"):
        call(tmp_path, "update", runner, payload={"page_id": "42", "title": "T"})


def test_update_put_failure_with_409_surfaces_version_conflict(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    pre_path = "/rest/api/content/42?expand=space,version,body.storage"
    current = page_payload(version=7)
    runner = FakeRunner(
        {
            get_args(pre_path): make_result(get_args(pre_path), stdout=json.dumps(current)),
            write_args(): make_result(
                write_args(),
                returncode=22,
                stderr="curl: (22) The requested URL returned error: 409 Conflict",
            ),
        }
    )

    with pytest.raises(ProviderOperationError, match="confluence:update: version conflict"):
        call(tmp_path, "update", runner, payload={"page_id": "42", "title": "x"})


# ---- registry / unsupported ---------------------------------------------


def test_default_registry_resolves_confluence_native_knowledge_provider(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    registry = default_provider_registry(runner=runner)
    provider = registry.resolve(role="knowledge", kind="confluence")
    assert isinstance(provider, ConfluenceDataCenterKnowledgeNativeProvider)
    assert provider.transport == TRANSPORT_NATIVE


def test_unsupported_knowledge_operations_remain_inherited_errors(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    runner = FakeRunner({})
    dispatcher = ProviderDispatcher(default_provider_registry(runner=runner))
    for operation in ("links", "comments", "set_metadata", "link", "add_comment"):
        with pytest.raises(ProviderOperationError, match=f"knowledge {operation} is not implemented"):
            dispatcher.dispatch(
                ProviderRequest(
                    role="knowledge",
                    kind="confluence",
                    operation=operation,
                    context=ProviderContext(project=tmp_path, artifact_type="spec"),
                    payload={"page_id": "42"},
                )
            )
