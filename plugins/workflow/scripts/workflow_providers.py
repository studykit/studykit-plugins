#!/usr/bin/env python3
"""Provider interface scaffold for workflow issue and knowledge operations.

The provider layer owns dispatch across provider kinds and transports. Native
wrappers are preferred first, and MCP providers are fallback transports.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from workflow_command import CommandRunner
from workflow_config import ProviderConfig, WorkflowConfig, WorkflowConfigError, load_workflow_config, normalize_role
from workflow_refs import ProviderReferenceError, normalize_provider_reference

ROLE_ISSUE = "issue"
ROLE_KNOWLEDGE = "knowledge"

TRANSPORT_NATIVE = "native"
TRANSPORT_MCP = "mcp"
TRANSPORT_PRIORITY = (TRANSPORT_NATIVE, TRANSPORT_MCP)

ISSUE_READ_OPERATIONS = frozenset({"get", "search", "comments", "logs"})
ISSUE_WRITE_OPERATIONS = frozenset(
    {
        "create",
        "update",
        "add_comment",
        "set_parent",
        "set_dependency",
        "apply_relationships",
        "close",
        "reopen",
    }
)
ISSUE_PROVIDER_OPERATIONS = ISSUE_READ_OPERATIONS | ISSUE_WRITE_OPERATIONS

KNOWLEDGE_READ_OPERATIONS = frozenset({"get", "search", "metadata", "links", "comments"})
KNOWLEDGE_WRITE_OPERATIONS = frozenset(
    {"create", "update", "set_metadata", "link", "add_comment"}
)
KNOWLEDGE_PROVIDER_OPERATIONS = KNOWLEDGE_READ_OPERATIONS | KNOWLEDGE_WRITE_OPERATIONS

CACHE_POLICY_DEFAULT = "default"
CACHE_POLICY_REFRESH = "refresh"
CACHE_POLICY_BYPASS = "bypass"
CACHE_POLICIES = {CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH, CACHE_POLICY_BYPASS}


class ProviderError(RuntimeError):
    """Base error for provider dispatch failures."""


class ProviderOperationError(ProviderError):
    """Raised when a provider operation is unsupported or malformed."""


class ProviderNotFoundError(ProviderError):
    """Raised when no provider transport is registered for a role and kind."""


class ProviderFreshnessError(ProviderError):
    """Raised when a provider write is blocked by stale cache metadata."""

    def __init__(self, message: str, *, result: Any | None = None):
        super().__init__(message)
        self.result = result

    def to_json(self) -> dict[str, Any]:
        if self.result is not None and hasattr(self.result, "to_json"):
            payload = self.result.to_json()
            if isinstance(payload, dict):
                return payload
        return {
            "ok": False,
            "status": "blocked",
            "message": str(self),
        }


@dataclass(frozen=True)
class ProviderContext:
    """Context shared by provider operations.

    ``cache_policy`` is a stable insertion point for the local provider read
    cache planned in #39. This scaffold preserves the value but does not
    implement caching.
    """

    project: Path
    artifact_type: str
    session_id: str | None = None
    cache_policy: str = CACHE_POLICY_DEFAULT

    def __post_init__(self) -> None:
        if self.cache_policy not in CACHE_POLICIES:
            choices = ", ".join(sorted(CACHE_POLICIES))
            raise ProviderOperationError(
                f"unsupported cache policy: {self.cache_policy}. Use one of: {choices}"
            )

    def to_json(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "project": str(self.project),
            "artifact_type": self.artifact_type,
            "cache_policy": self.cache_policy,
        }
        if self.session_id:
            result["session_id"] = self.session_id
        return result


@dataclass(frozen=True)
class ProviderRequest:
    """One provider operation request."""

    role: str
    kind: str
    operation: str
    context: ProviderContext
    payload: Mapping[str, Any] = field(default_factory=dict)
    transport: str | None = None

    def with_transport(self, transport: str) -> ProviderRequest:
        return replace(self, transport=transport)

    @property
    def normalized_role(self) -> str:
        return normalize_role(self.role)

    @property
    def is_write(self) -> bool:
        if self.normalized_role == ROLE_ISSUE:
            return self.operation in ISSUE_WRITE_OPERATIONS
        return self.operation in KNOWLEDGE_WRITE_OPERATIONS

    def to_json(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "role": self.normalized_role,
            "kind": self.kind,
            "operation": self.operation,
            "context": self.context.to_json(),
            "payload": dict(self.payload),
        }
        if self.transport:
            result["transport"] = self.transport
        return result


@dataclass(frozen=True)
class ProviderResponse:
    """Structured provider operation response."""

    role: str
    kind: str
    transport: str
    operation: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    cache_policy: str = CACHE_POLICY_DEFAULT

    def to_json(self) -> dict[str, Any]:
        return {
            "role": self.role,
            "kind": self.kind,
            "transport": self.transport,
            "operation": self.operation,
            "payload": dict(self.payload),
            "cache_policy": self.cache_policy,
        }





class ProviderTransport:
    """Base class for provider transport adapters."""

    role: str
    kind: str
    transport: str
    operations: frozenset[str]

    def __init__(self, *, kind: str, transport: str):
        self.kind = kind
        self.transport = transport

    def call(self, request: ProviderRequest) -> ProviderResponse:
        self._validate_request(request)
        handler = getattr(self, request.operation, None)
        if handler is None or not callable(handler):
            raise ProviderOperationError(
                f"{self.role} provider {self.kind}/{self.transport} does not implement "
                f"operation: {request.operation}"
            )
        payload = handler(request)
        if not isinstance(payload, Mapping):
            raise ProviderOperationError("provider operation returned non-mapping payload")
        return ProviderResponse(
            role=self.role,
            kind=self.kind,
            transport=self.transport,
            operation=request.operation,
            payload=payload,
            cache_policy=request.context.cache_policy,
        )

    def _validate_request(self, request: ProviderRequest) -> None:
        if request.normalized_role != self.role:
            raise ProviderOperationError(
                f"provider role mismatch: expected {self.role}, got {request.normalized_role}"
            )
        if request.kind != self.kind:
            raise ProviderOperationError(f"provider kind mismatch: expected {self.kind}, got {request.kind}")
        if request.operation not in self.operations:
            raise ProviderOperationError(
                f"unsupported {self.role} provider operation: {request.operation}"
            )


class IssueProvider(ProviderTransport):
    """Issue provider interface.

    Covered operations: create, update, get, search, comments, logs,
    add_comment, set_parent, set_dependency, close, and reopen.
    """

    role = ROLE_ISSUE
    operations = ISSUE_PROVIDER_OPERATIONS

    def create(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue create is not implemented")

    def update(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue update is not implemented")

    def get(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue get is not implemented")

    def search(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue search is not implemented")

    def comments(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue comments is not implemented")

    def logs(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue logs is not implemented")

    def add_comment(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue add_comment is not implemented")

    def set_parent(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue set_parent is not implemented")

    def set_dependency(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue set_dependency is not implemented")

    def apply_relationships(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue apply_relationships is not implemented")

    def close(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue close is not implemented")

    def reopen(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("issue reopen is not implemented")


class KnowledgeProvider(ProviderTransport):
    """Knowledge provider interface.

    Covered operations: create, update, get, search, metadata, links,
    comments, set_metadata, link, and add_comment.
    """

    role = ROLE_KNOWLEDGE
    operations = KNOWLEDGE_PROVIDER_OPERATIONS

    def create(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge create is not implemented")

    def update(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge update is not implemented")

    def get(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge get is not implemented")

    def search(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge search is not implemented")

    def metadata(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge metadata is not implemented")

    def links(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge links is not implemented")

    def comments(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge comments is not implemented")

    def set_metadata(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge set_metadata is not implemented")

    def link(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge link is not implemented")

    def add_comment(self, request: ProviderRequest) -> Mapping[str, Any]:
        raise ProviderOperationError("knowledge add_comment is not implemented")




class ProviderRegistry:
    """Registry of provider transports keyed by role, kind, and transport."""

    def __init__(self) -> None:
        self._providers: dict[tuple[str, str, str], ProviderTransport] = {}

    def register(self, provider: ProviderTransport) -> None:
        key = (provider.role, provider.kind, provider.transport)
        self._providers[key] = provider

    def resolve(
        self,
        *,
        role: str,
        kind: str,
        transport: str | None = None,
    ) -> ProviderTransport:
        normalized_role = normalize_role(role)
        transports = (transport,) if transport else TRANSPORT_PRIORITY
        for candidate_transport in transports:
            provider = self._providers.get((normalized_role, kind, candidate_transport))
            if provider is not None:
                return provider
        priority = ", ".join(transports)
        raise ProviderNotFoundError(
            f"no provider registered for role={normalized_role}, kind={kind}, transport={priority}"
        )


class ProviderDispatcher:
    """Dispatch provider operations through the registered transport layer."""

    def __init__(self, registry: ProviderRegistry):
        self.registry = registry

    def dispatch(self, request: ProviderRequest) -> ProviderResponse:
        provider = self.registry.resolve(
            role=request.role,
            kind=request.kind,
            transport=request.transport,
        )
        dispatched_request = request.with_transport(provider.transport)
        return provider.call(dispatched_request)


def default_provider_registry(*, runner: CommandRunner | None = None) -> ProviderRegistry:
    """Build the default provider registry.

    Implemented native transports are registered here. MCP fallback transports
    are intentionally resolved through the same registry once MCP adapters are
    available.
    """

    from workflow_github_issue_provider import GitHubIssueNativeProvider
    from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
    from workflow_confluence_knowledge_provider import (
        ConfluenceDataCenterKnowledgeNativeProvider,
    )

    registry = ProviderRegistry()
    registry.register(GitHubIssueNativeProvider(runner=runner))
    registry.register(JiraDataCenterIssueNativeProvider(runner=runner))
    registry.register(ConfluenceDataCenterKnowledgeNativeProvider(runner=runner))
    return registry


def request_from_config(
    config: WorkflowConfig,
    *,
    role: str,
    operation: str,
    artifact_type: str,
    payload: Mapping[str, Any] | None = None,
    session_id: str | None = None,
    transport: str | None = None,
    cache_policy: str = CACHE_POLICY_DEFAULT,
) -> ProviderRequest:
    """Build a provider request from a loaded workflow config."""

    normalized_role = normalize_role(role)
    provider_config = _provider_config_for_role(config, normalized_role)
    return ProviderRequest(
        role=normalized_role,
        kind=provider_config.kind,
        operation=operation,
        context=ProviderContext(
            project=config.root,
            artifact_type=artifact_type,
            session_id=session_id,
            cache_policy=cache_policy,
        ),
        payload=payload or {},
        transport=transport,
    )


def _provider_config_for_role(config: WorkflowConfig, role: str) -> ProviderConfig:
    if role == ROLE_ISSUE:
        return config.issues
    if role == ROLE_KNOWLEDGE:
        return config.knowledge
    raise ProviderOperationError(f"unsupported provider role: {role}")


def _optional_workflow_config(project: Path) -> WorkflowConfig | None:
    try:
        return load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise ProviderOperationError(str(exc)) from exc


def _required_payload_value(request: ProviderRequest, key: str) -> Any:
    value = request.payload.get(key)
    if value is None or value == "":
        raise ProviderOperationError(f"{request.operation} requires payload.{key}")
    return value


def _freshness_spec(payload: Mapping[str, Any], *, default_target: str) -> dict[str, Any] | None:
    raw = payload.get("freshness_check")
    if raw is None:
        raw = payload.get("check_freshness")
    if raw is None:
        raw = payload.get("freshness")
    if raw is None or raw is False:
        return None

    enabled = True
    target: Any = payload.get("freshness_target") or payload.get("freshness_scope") or default_target
    pending_new = _truthy(payload.get("pending_new")) or _truthy(payload.get("pending_new_artifact"))
    pending_new = pending_new or payload.get("provider_artifact_exists") is False

    if isinstance(raw, Mapping):
        if raw.get("enabled") is not None:
            enabled = _truthy(raw.get("enabled"))
        target = raw.get("target") or raw.get("scope") or target
        pending_new = (
            pending_new
            or _truthy(raw.get("pending_new"))
            or _truthy(raw.get("pending_new_artifact"))
            or raw.get("provider_artifact_exists") is False
        )
    elif isinstance(raw, str):
        normalized_raw = raw.strip().lower()
        if normalized_raw in {"0", "false", "no", "off"}:
            return None
        if normalized_raw not in {"1", "true", "yes", "on"}:
            target = raw

    if not enabled:
        return None

    normalized_target = _normalize_freshness_target(str(target))
    if normalized_target not in {"issue", "comments", "relationships"}:
        raise ProviderOperationError(f"unsupported freshness target: {target}")
    return {"target": normalized_target, "pending_new": pending_new}


def _normalize_freshness_target(target: str) -> str:
    normalized = target.strip().lower().replace("-", "_")
    aliases = {
        "body": "issue",
        "issue_body": "issue",
        "comment": "comments",
        "issue_comments": "comments",
        "relationship": "relationships",
        "issue_relationships": "relationships",
    }
    return aliases.get(normalized, normalized)


def _latest_provider_comment_timestamp(value: Any) -> str | None:
    comments = value
    if isinstance(comments, Mapping):
        nodes = comments.get("nodes")
        if isinstance(nodes, list):
            comments = nodes
    if not isinstance(comments, list):
        return None

    values = [
        str(timestamp)
        for comment in comments
        if isinstance(comment, Mapping)
        for timestamp in (
            comment.get("updatedAt"),
            comment.get("updated_at"),
            comment.get("createdAt"),
            comment.get("created_at"),
        )
        if timestamp
    ]
    if not values:
        return None
    return max(values)


def _payload_has_relationship_projection(payload: Mapping[str, Any]) -> bool:
    """Return true when a provider payload already carries relationship data."""

    relationship_keys = {
        "parent",
        "parentIssue",
        "parent_issue",
        "children",
        "subIssues",
        "sub_issues",
        "dependencies",
        "blocked_by",
        "blockedBy",
        "blocking",
        "blocks",
        "related",
    }
    return any(key in payload for key in relationship_keys)


def _optional_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, Mapping):
        nodes = value.get("nodes")
        if nodes is not None:
            return _string_list(nodes)
        name = value.get("name")
        return [str(name)] if name else []
    if isinstance(value, list | tuple | set):
        labels: list[str] = []
        for item in value:
            labels.extend(_string_list(item))
        return labels
    return [str(value)]


def _close_reason_from_state_reason(value: Any) -> str:
    text = _optional_string(value)
    if text and text.strip().lower().replace("_", "-") in {"not-planned", "not planned"}:
        return "not planned"
    return "completed"


def _relationship_action(value: Any) -> str:
    normalized = str(value).strip().lower().replace("-", "_")
    aliases = {
        "set": "add",
        "create": "add",
        "append": "add",
        "delete": "remove",
        "unset": "remove",
    }
    action = aliases.get(normalized, normalized)
    if action not in {"add", "remove"}:
        raise ProviderOperationError(f"unsupported GitHub relationship action: {value}")
    return action


def _relationship_values(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        return [value]
    if isinstance(value, list | tuple | set):
        return list(value)
    return [value]


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)
