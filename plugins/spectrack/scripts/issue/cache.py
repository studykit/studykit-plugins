#!/usr/bin/env python3
"""Local workflow provider read cache projections."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import frontmatter as frontmatter_lib


CACHE_ROOT_NAME = ".spectrack-cache"
SCHEMA_VERSION = 1
FINGERPRINT_LENGTH = 8
_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()


def fingerprint(value: Any) -> str:
    """Return a short stable fingerprint of a normalized cache payload.

    The first ``FINGERPRINT_LENGTH`` hex chars of the SHA-256 over a canonical
    JSON encoding (sorted keys, no insignificant whitespace). Used to detect
    whether a provider-side artifact changed since it was cached. The same value
    must be computed at cache-write time and at write-back check time, so callers
    must pass an already-normalized structure — never a raw provider payload.
    """

    canonical = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:FINGERPRINT_LENGTH]


def content_fingerprint(title: Any, body: Any) -> str:
    """Fingerprint of an issue's authored content (title + body)."""

    return fingerprint({"title": str(title or ""), "body": str(body or "")})


def comments_fingerprint(items: list[dict[str, str | None]]) -> str:
    """Fingerprint of a normalized ``[{id, updated_at}]`` comment-set list."""

    return fingerprint(items)


def relationships_fingerprint(compact: Mapping[str, Any]) -> str:
    """Fingerprint of a compact relationship projection (order-independent)."""

    return fingerprint(_canonical_relationships(compact))


def _canonical_relationships(compact: Mapping[str, Any]) -> dict[str, Any]:
    canonical: dict[str, Any] = {}
    for key, value in compact.items():
        if isinstance(value, list):
            canonical[key] = sorted(str(item) for item in value)
        else:
            canonical[key] = str(value)
    return canonical


class WorkflowCacheError(RuntimeError):
    """Base error for workflow cache failures."""


class WorkflowCacheMiss(WorkflowCacheError):
    """Raised when a cache projection does not exist."""


class WorkflowCacheCorrupt(WorkflowCacheError):
    """Raised when a cache projection exists but cannot be parsed."""


class WorkflowFreshnessConflict(WorkflowCacheError):
    """Raised when cache freshness metadata blocks a provider write."""

    def __init__(self, result: FreshnessCheckResult):
        super().__init__(result.message)
        self.result = result




@dataclass(frozen=True)
class PendingIssueRelationshipOperation:
    """Parsed pending provider-native relationship operation."""

    target_kind: str
    target_id: str
    path: Path
    action: str
    relationship: str
    target_ref: str
    replace_parent: bool = False

    @property
    def file_name(self) -> str:
        return self.path.name

    def to_json(self) -> dict[str, Any]:
        return {
            "target_kind": self.target_kind,
            "target_id": self.target_id,
            "file": self.file_name,
            "path": str(self.path),
            "action": self.action,
            "relationship": self.relationship,
            "target_ref": self.target_ref,
            "replace_parent": self.replace_parent,
        }


@dataclass(frozen=True)
class FreshnessMetadata:
    """Local cache fingerprint for one write-back target."""

    fingerprint: str | None
    path: Path | None = None
    target: str = "artifact"

    def to_json(self) -> dict[str, str | None]:
        result: dict[str, str | None] = {
            "target": self.target,
            "fingerprint": self.fingerprint,
        }
        if self.path is not None:
            result["path"] = str(self.path)
        return result


@dataclass(frozen=True)
class FreshnessCheckResult:
    """Result of comparing the cached fingerprint with current provider state."""

    ok: bool
    status: str
    message: str
    artifact: str
    cached_fingerprint: str | None = None
    provider_fingerprint: str | None = None

    def to_json(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "status": self.status,
            "message": self.message,
            "artifact": self.artifact,
            "cached_fingerprint": self.cached_fingerprint,
            "provider_fingerprint": self.provider_fingerprint,
        }


def check_provider_freshness(
    metadata: FreshnessMetadata | None,
    *,
    provider_fingerprint: str | None,
    artifact: str,
    pending_new: bool = False,
) -> FreshnessCheckResult:
    """Compare the cached fingerprint with the current provider fingerprint.

    A mismatch is reported as a ``conflict`` (the provider changed since the
    artifact was last fetched), not a hard error: callers refresh the cache,
    guide the operator to reread it, and offer an explicit overwrite. The
    fingerprint is provider-clock-independent, so there is no skew or precision
    false positive to defend against.
    """

    if pending_new:
        return FreshnessCheckResult(
            ok=True,
            status="pending_new",
            message=f"{artifact} is pending creation; no provider conflict check is required.",
            artifact=artifact,
            provider_fingerprint=provider_fingerprint,
        )

    if metadata is None or not metadata.fingerprint:
        return FreshnessCheckResult(
            ok=False,
            status="missing_fingerprint",
            message=(
                f"Cannot safely write {artifact}: no cached fingerprint to compare against. "
                "Fetch the issue before writing."
            ),
            artifact=artifact,
            cached_fingerprint=metadata.fingerprint if metadata else None,
            provider_fingerprint=provider_fingerprint,
        )

    if provider_fingerprint is None:
        return FreshnessCheckResult(
            ok=True,
            status="provider_fingerprint_unavailable",
            message=(
                f"{artifact} provider fingerprint is unavailable; no overwrite conflict "
                "could be detected."
            ),
            artifact=artifact,
            cached_fingerprint=metadata.fingerprint,
            provider_fingerprint=None,
        )

    if metadata.fingerprint != provider_fingerprint:
        return FreshnessCheckResult(
            ok=False,
            status="conflict",
            message=(
                f"{artifact} changed on the provider since it was last fetched "
                f"(cached {metadata.fingerprint}, provider {provider_fingerprint}). "
                "The cache was refreshed — reread it and reapply, or pass --overwrite to replace it."
            ),
            artifact=artifact,
            cached_fingerprint=metadata.fingerprint,
            provider_fingerprint=provider_fingerprint,
        )

    return FreshnessCheckResult(
        ok=True,
        status="fresh",
        message=f"{artifact} cache matches the provider; safe to write.",
        artifact=artifact,
        cached_fingerprint=metadata.fingerprint,
        provider_fingerprint=provider_fingerprint,
    )


def require_provider_freshness(
    metadata: FreshnessMetadata | None,
    *,
    provider_fingerprint: str | None,
    artifact: str,
    pending_new: bool = False,
) -> FreshnessCheckResult:
    """Return the freshness result or raise when a write-back conflicts."""

    result = check_provider_freshness(
        metadata,
        provider_fingerprint=provider_fingerprint,
        artifact=artifact,
        pending_new=pending_new,
    )
    if not result.ok:
        raise WorkflowFreshnessConflict(result)
    return result




def _read_frontmatter_markdown(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not _FRONTMATTER_HANDLER.detect(text):
        raise WorkflowCacheCorrupt(f"missing markdown frontmatter: {path}")
    try:
        frontmatter_text, body = _FRONTMATTER_HANDLER.split(text)
    except ValueError as exc:
        raise WorkflowCacheCorrupt(f"unterminated markdown frontmatter: {path}") from exc
    if body.startswith("\n"):
        body = body[1:]
    data = _loads_frontmatter_mapping(frontmatter_text, path)
    return data, body




def pending_relationship_operations_from_mapping(
    data: Mapping[str, Any],
    *,
    path: Path,
    target_kind: str,
    target_id: str,
) -> list[PendingIssueRelationshipOperation]:
    """Normalize declarative or operation-list relationship intent."""

    operations: list[PendingIssueRelationshipOperation] = []
    raw_operations = data.get("operations")
    if raw_operations is not None:
        if not isinstance(raw_operations, list):
            raise WorkflowCacheCorrupt(f"pending relationship operations must be a list: {path}")
        for item in raw_operations:
            operations.append(
                _pending_relationship_operation_from_mapping(
                    item,
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                )
            )

    operations.extend(
        _pending_relationship_operations_from_declarative(
            data,
            path=path,
            target_kind=target_kind,
            target_id=target_id,
        )
    )

    if not operations:
        raise WorkflowCacheCorrupt(f"pending relationships file has no operations: {path}")
    return operations


def _pending_relationship_operation_from_mapping(
    item: Any,
    *,
    path: Path,
    target_kind: str,
    target_id: str,
) -> PendingIssueRelationshipOperation:
    if not isinstance(item, Mapping):
        raise WorkflowCacheCorrupt(f"pending relationship operation must be a mapping: {path}")
    relationship = _normalize_relationship_name(
        _required_relationship_value(item, path, "relationship", "type", "kind")
    )
    action = _normalize_relationship_action(item.get("action") or item.get("op") or "add", path)
    target_ref = _relationship_target_ref(item, path)
    replace_parent = bool(item.get("replace_parent") or item.get("replaceParent"))
    if relationship == "parent" and action == "add" and not (
        item.get("replace_parent") is not None or item.get("replaceParent") is not None
    ):
        replace_parent = True
    return PendingIssueRelationshipOperation(
        target_kind=target_kind,
        target_id=target_id,
        path=path,
        action=action,
        relationship=relationship,
        target_ref=target_ref,
        replace_parent=replace_parent,
    )


def _pending_relationship_operations_from_declarative(
    data: Mapping[str, Any],
    *,
    path: Path,
    target_kind: str,
    target_id: str,
) -> list[PendingIssueRelationshipOperation]:
    operations: list[PendingIssueRelationshipOperation] = []
    ignored = {"schema_version", "updated_at", "fetched_at", "operations"}

    if "parent" in data:
        operations.extend(
            _declarative_relationship_values(
                data["parent"],
                relationship="parent",
                path=path,
                target_kind=target_kind,
                target_id=target_id,
                default_replace_parent=True,
            )
        )

    if "children" in data:
        operations.extend(
            _declarative_relationship_values(
                data["children"],
                relationship="child",
                path=path,
                target_kind=target_kind,
                target_id=target_id,
            )
        )

    dependencies = data.get("dependencies")
    if isinstance(dependencies, Mapping):
        if "blocked_by" in dependencies or "blockedBy" in dependencies:
            operations.extend(
                _declarative_relationship_values(
                    dependencies.get("blocked_by") or dependencies.get("blockedBy"),
                    relationship="blocked_by",
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                )
            )
        if "blocking" in dependencies or "blocks" in dependencies:
            operations.extend(
                _declarative_relationship_values(
                    dependencies.get("blocking") or dependencies.get("blocks"),
                    relationship="blocking",
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                )
            )
    elif dependencies is not None:
        raise WorkflowCacheCorrupt(f"pending relationship dependencies must be a mapping: {path}")

    for key, relationship in (("blocked_by", "blocked_by"), ("blockedBy", "blocked_by"), ("blocking", "blocking"), ("blocks", "blocking"), ("related", "related")):
        if key in data:
            operations.extend(
                _declarative_relationship_values(
                    data[key],
                    relationship=relationship,
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                )
            )

    unknown = sorted(str(key) for key in data if key not in ignored and key not in {"parent", "children", "dependencies", "blocked_by", "blockedBy", "blocking", "blocks", "related"})
    if unknown:
        raise WorkflowCacheCorrupt(f"unsupported pending relationship fields in {path}: {', '.join(unknown)}")
    return operations


def _declarative_relationship_values(
    value: Any,
    *,
    relationship: str,
    path: Path,
    target_kind: str,
    target_id: str,
    default_replace_parent: bool = False,
) -> list[PendingIssueRelationshipOperation]:
    if value is None:
        return []
    if isinstance(value, Mapping) and any(key in value for key in ("add", "remove", "delete", "unset")):
        operations: list[PendingIssueRelationshipOperation] = []
        for key, action in (("add", "add"), ("remove", "remove"), ("delete", "remove"), ("unset", "remove")):
            if key in value:
                parsed = _declarative_relationship_values(
                    value[key],
                    relationship=relationship,
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                    default_replace_parent=default_replace_parent,
                )
                if action == "remove":
                    parsed = [
                        PendingIssueRelationshipOperation(
                            target_kind=operation.target_kind,
                            target_id=operation.target_id,
                            path=operation.path,
                            action="remove",
                            relationship=operation.relationship,
                            target_ref=operation.target_ref,
                            replace_parent=operation.replace_parent,
                        )
                        for operation in parsed
                    ]
                operations.extend(parsed)
        return operations
    if isinstance(value, list | tuple | set):
        result: list[PendingIssueRelationshipOperation] = []
        for item in value:
            result.extend(
                _declarative_relationship_values(
                    item,
                    relationship=relationship,
                    path=path,
                    target_kind=target_kind,
                    target_id=target_id,
                    default_replace_parent=default_replace_parent,
                )
            )
        return result

    action = "add"
    replace_parent = default_replace_parent
    if isinstance(value, Mapping):
        action = _normalize_relationship_action(value.get("action") or value.get("op") or action, path)
        replace_parent = _relationship_bool(value, "replace_parent", "replaceParent", default=replace_parent)
    target_ref = _relationship_target_ref(value, path)
    return [
        PendingIssueRelationshipOperation(
            target_kind=target_kind,
            target_id=target_id,
            path=path,
            action=action,
            relationship=relationship,
            target_ref=target_ref,
            replace_parent=replace_parent,
        )
    ]


_INLINE_RELATIONSHIP_SOURCE = Path("<inline>")
_LIST_RELATIONSHIPS = ("blocked_by", "blocking", "child", "related")


def relationship_operations_from_intent(
    intent: Mapping[str, Any],
    *,
    target_kind: str,
    target_id: str,
    source_path: Path | None = None,
) -> list[PendingIssueRelationshipOperation]:
    """Build relationship operations from a CLI-style flat intent dict.

    Recognized keys (all optional):

    - ``parent_add``: ref — add parent (errors at provider if a parent already
      exists; use ``parent_replace`` to overwrite).
    - ``parent_replace``: ref — set parent, replacing any existing parent.
    - ``parent_remove``: True — detach the current parent. The provider
      resolves the current parent from cache; if no parent exists, the
      operation is dropped (idempotent no-op).
    - ``epic_add`` / ``epic_replace`` / ``epic_remove``: parallel scalar
      semantics for the Epic Link customfield (Jira only).
    - ``blocked_by_add`` / ``blocked_by_remove``: list of refs.
    - ``blocking_add`` / ``blocking_remove``: list of refs.
    - ``child_add`` / ``child_remove``: list of refs.
    - ``related_add`` / ``related_remove``: list of refs.

    Parent and epic intents are each mutually exclusive within their own
    group, but a parent_* flag may coexist with an epic_* flag. For list
    relationships, the same ref cannot appear in both add and remove.
    Returns an empty list when the intent has no actionable entries.
    """

    path = source_path if source_path is not None else _INLINE_RELATIONSHIP_SOURCE
    operations: list[PendingIssueRelationshipOperation] = []

    operations.extend(
        _scalar_relationship_operations(
            intent,
            relationship="parent",
            target_kind=target_kind,
            target_id=target_id,
            path=path,
        )
    )
    operations.extend(
        _scalar_relationship_operations(
            intent,
            relationship="epic",
            target_kind=target_kind,
            target_id=target_id,
            path=path,
        )
    )

    for relationship in _LIST_RELATIONSHIPS:
        add_refs = _intent_list(intent.get(f"{relationship}_add"))
        remove_refs = _intent_list(intent.get(f"{relationship}_remove"))
        overlap = sorted(set(add_refs) & set(remove_refs))
        if overlap:
            raise WorkflowCacheError(
                f"{relationship} ref(s) cannot be in both add and remove: {overlap}"
            )
        for ref in add_refs:
            operations.append(
                PendingIssueRelationshipOperation(
                    target_kind=target_kind,
                    target_id=target_id,
                    path=path,
                    action="add",
                    relationship=relationship,
                    target_ref=ref,
                    replace_parent=False,
                )
            )
        for ref in remove_refs:
            operations.append(
                PendingIssueRelationshipOperation(
                    target_kind=target_kind,
                    target_id=target_id,
                    path=path,
                    action="remove",
                    relationship=relationship,
                    target_ref=ref,
                    replace_parent=False,
                )
            )

    return operations


def _scalar_relationship_operations(
    intent: Mapping[str, Any],
    *,
    relationship: str,
    target_kind: str,
    target_id: str,
    path: Path,
) -> list[PendingIssueRelationshipOperation]:
    add = _intent_scalar(intent.get(f"{relationship}_add"))
    replace = _intent_scalar(intent.get(f"{relationship}_replace"))
    remove = bool(intent.get(f"{relationship}_remove"))
    flags = [
        name
        for name, present in (
            (f"{relationship}_add", bool(add)),
            (f"{relationship}_replace", bool(replace)),
            (f"{relationship}_remove", remove),
        )
        if present
    ]
    if len(flags) > 1:
        raise WorkflowCacheError(
            f"conflicting {relationship} relationship flags: {', '.join(flags)}"
        )
    operations: list[PendingIssueRelationshipOperation] = []
    if add:
        operations.append(
            PendingIssueRelationshipOperation(
                target_kind=target_kind,
                target_id=target_id,
                path=path,
                action="add",
                relationship=relationship,
                target_ref=add,
                replace_parent=False,
            )
        )
    elif replace:
        operations.append(
            PendingIssueRelationshipOperation(
                target_kind=target_kind,
                target_id=target_id,
                path=path,
                action="add",
                relationship=relationship,
                target_ref=replace,
                replace_parent=relationship == "parent",
            )
        )
    elif remove:
        operations.append(
            PendingIssueRelationshipOperation(
                target_kind=target_kind,
                target_id=target_id,
                path=path,
                action="remove",
                relationship=relationship,
                target_ref="",
                replace_parent=False,
            )
        )
    return operations


def _intent_scalar(value: Any) -> str:
    if value in (None, "", False):
        return ""
    return str(value).strip()


def _intent_list(value: Any) -> list[str]:
    if value in (None, "", False):
        return []
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, Iterable):
        result: list[str] = []
        for item in value:
            if item in (None, "", False):
                continue
            text = str(item).strip()
            if text:
                result.append(text)
        return result
    text = str(value).strip()
    return [text] if text else []


def _required_relationship_value(item: Mapping[str, Any], path: Path, *keys: str) -> Any:
    for key in keys:
        value = item.get(key)
        if value is not None:
            return value
    raise WorkflowCacheCorrupt(f"pending relationship operation is missing {keys[0]}: {path}")


def _relationship_target_ref(value: Any, path: Path) -> str:
    if isinstance(value, Mapping):
        for key in ("issue", "target", "target_ref", "ref", "number", "id"):
            raw = value.get(key)
            if raw is not None:
                text = str(raw).strip()
                if text:
                    return text
        raise WorkflowCacheCorrupt(f"pending relationship operation is missing target issue: {path}")
    text = str(value).strip()
    if not text:
        raise WorkflowCacheCorrupt(f"pending relationship target is empty: {path}")
    return text


def _normalize_relationship_name(value: Any) -> str:
    normalized = str(value).strip().lower().replace("-", "_")
    aliases = {
        "children": "child",
        "sub_issue": "child",
        "sub_issues": "child",
        "subissue": "child",
        "subissues": "child",
        "blockedby": "blocked_by",
        "blocked_by": "blocked_by",
        "depends_on": "blocked_by",
        "dependency": "blocked_by",
        "blocks": "blocking",
    }
    return aliases.get(normalized, normalized)


def _normalize_relationship_action(value: Any, path: Path) -> str:
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
        raise WorkflowCacheCorrupt(f"unsupported pending relationship action in {path}: {value}")
    return action


def _relationship_bool(value: Mapping[str, Any], *keys: str, default: bool) -> bool:
    for key in keys:
        if key in value:
            raw = value.get(key)
            if isinstance(raw, bool):
                return raw
            if isinstance(raw, str):
                return raw.strip().lower() in {"1", "true", "yes", "on"}
            return bool(raw)
    return default


def _normalize_freshness_target(target: str) -> str:
    normalized = str(target).strip().lower().replace("-", "_")
    aliases = {
        "issue_body": "issue",
        "body": "issue",
        "comment": "comments",
        "issue_comments": "comments",
        "relationship": "relationships",
        "issue_relationships": "relationships",
    }
    return aliases.get(normalized, normalized)


def _dump_json(data: Mapping[str, Any]) -> str:
    return json.dumps(dict(data), indent=2, sort_keys=False, ensure_ascii=False) + "\n"


def _read_json_mapping(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise WorkflowCacheCorrupt(f"could not parse JSON: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise WorkflowCacheCorrupt(f"JSON must be a mapping: {path}")
    return value


def _read_yaml_mapping(path: Path) -> dict[str, Any]:
    return _loads_yaml_mapping(path.read_text(encoding="utf-8"), path)


def _loads_yaml_mapping(text: str, path: Path) -> dict[str, Any]:
    try:
        value = _parse_yaml_subset(text)
    except Exception as exc:
        raise WorkflowCacheCorrupt(f"could not parse YAML: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise WorkflowCacheCorrupt(f"YAML must be a mapping: {path}")
    return value


def _loads_frontmatter_mapping(text: str, path: Path) -> dict[str, Any]:
    try:
        value = _FRONTMATTER_HANDLER.load(text)
    except Exception as exc:
        raise WorkflowCacheCorrupt(f"could not parse YAML: {path}: {exc}") from exc
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise WorkflowCacheCorrupt(f"YAML must be a mapping: {path}")
    return value


def _require_schema(data: Mapping[str, Any], path: Path) -> None:
    if data.get("schema_version") != SCHEMA_VERSION:
        raise WorkflowCacheCorrupt(f"unsupported schema_version in {path}")


def _format_markdown(frontmatter: Mapping[str, Any], body: str) -> str:
    return f"---\n{_dump_frontmatter_yaml(frontmatter)}---\n\n{body}"


def _dump_frontmatter_yaml(data: Mapping[str, Any]) -> str:
    return _FRONTMATTER_HANDLER.export(dict(data), sort_keys=False) + "\n"


def _dump_yaml(data: Mapping[str, Any]) -> str:
    return "\n".join(_dump_mapping_lines(data, 0)) + "\n"


def _dump_mapping_lines(data: Mapping[str, Any], indent: int) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent
    for key, value in data.items():
        if isinstance(value, Mapping):
            lines.append(f"{prefix}{key}:")
            lines.extend(_dump_mapping_lines(value, indent + 2))
        elif isinstance(value, list):
            lines.append(f"{prefix}{key}:")
            lines.extend(_dump_list_lines(value, indent + 2))
        else:
            lines.append(f"{prefix}{key}: {_dump_scalar(value)}")
    return lines


def _dump_list_lines(values: Iterable[Any], indent: int) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent
    for value in values:
        if isinstance(value, Mapping):
            items = list(value.items())
            if not items:
                lines.append(f"{prefix}- {{}}")
                continue
            first_key, first_value = items[0]
            if isinstance(first_value, (Mapping, list)):
                lines.append(f"{prefix}- {first_key}:")
                lines.extend(_dump_nested_value(first_value, indent + 4))
            else:
                lines.append(f"{prefix}- {first_key}: {_dump_scalar(first_value)}")
            for key, nested_value in items[1:]:
                if isinstance(nested_value, Mapping):
                    lines.append(f"{prefix}  {key}:")
                    lines.extend(_dump_mapping_lines(nested_value, indent + 4))
                elif isinstance(nested_value, list):
                    lines.append(f"{prefix}  {key}:")
                    lines.extend(_dump_list_lines(nested_value, indent + 4))
                else:
                    lines.append(f"{prefix}  {key}: {_dump_scalar(nested_value)}")
        elif isinstance(value, list):
            lines.append(f"{prefix}-")
            lines.extend(_dump_list_lines(value, indent + 2))
        else:
            lines.append(f"{prefix}- {_dump_scalar(value)}")
    return lines


def _dump_nested_value(value: Any, indent: int) -> list[str]:
    if isinstance(value, Mapping):
        return _dump_mapping_lines(value, indent)
    if isinstance(value, list):
        return _dump_list_lines(value, indent)
    return [f"{' ' * indent}{_dump_scalar(value)}"]


def _dump_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    if re.fullmatch(r"[A-Za-z0-9_.@/+:-]+", text) and text.lower() not in {"null", "true", "false"}:
        return text
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


@dataclass(frozen=True)
class _YamlLine:
    indent: int
    text: str


def _parse_yaml_subset(text: str) -> Any:
    lines = _yaml_lines(text)
    if not lines:
        return {}
    index = 0

    def parse_block(indent: int) -> Any:
        nonlocal index
        if index >= len(lines) or lines[index].indent < indent:
            return {}
        if lines[index].text.startswith("- ") or lines[index].text == "-":
            return parse_list(indent)
        return parse_mapping(indent)

    def parse_mapping(indent: int) -> dict[str, Any]:
        nonlocal index
        result: dict[str, Any] = {}
        while index < len(lines):
            line = lines[index]
            if line.indent < indent:
                break
            if line.indent != indent:
                raise ValueError(f"unexpected indentation: {line.text}")
            if line.text.startswith("- ") or line.text == "-":
                break
            key, raw_value = _split_yaml_key_value(line.text)
            index += 1
            if raw_value is None:
                if index < len(lines) and lines[index].indent > indent:
                    result[key] = parse_block(lines[index].indent)
                else:
                    result[key] = None
            else:
                result[key] = _parse_scalar(raw_value)
        return result

    def parse_list(indent: int) -> list[Any]:
        nonlocal index
        result: list[Any] = []
        while index < len(lines):
            line = lines[index]
            if line.indent < indent:
                break
            if line.indent != indent or not (line.text.startswith("- ") or line.text == "-"):
                break
            raw_item = line.text[1:].strip()
            index += 1
            if not raw_item:
                if index < len(lines) and lines[index].indent > indent:
                    result.append(parse_block(lines[index].indent))
                else:
                    result.append(None)
                continue
            if ":" in raw_item and not _looks_like_scalar_with_colon(raw_item):
                key, raw_value = _split_yaml_key_value(raw_item)
                item: dict[str, Any] = {}
                if raw_value is None:
                    if index < len(lines) and lines[index].indent > indent:
                        item[key] = parse_block(lines[index].indent)
                    else:
                        item[key] = None
                else:
                    item[key] = _parse_scalar(raw_value)
                if index < len(lines) and lines[index].indent > indent:
                    extra = parse_mapping(lines[index].indent)
                    item.update(extra)
                result.append(item)
            else:
                result.append(_parse_scalar(raw_item))
        return result

    parsed = parse_block(lines[0].indent)
    if index != len(lines):
        raise ValueError("unparsed YAML content remains")
    return parsed


def _yaml_lines(text: str) -> list[_YamlLine]:
    result: list[_YamlLine] = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        stripped_comment = _strip_yaml_comment(raw).rstrip()
        if not stripped_comment.strip():
            continue
        indent = len(stripped_comment) - len(stripped_comment.lstrip(" "))
        result.append(_YamlLine(indent=indent, text=stripped_comment.strip()))
    return result


def _split_yaml_key_value(text: str) -> tuple[str, str | None]:
    if ":" not in text:
        raise ValueError(f"expected key/value line: {text}")
    key, raw_value = text.split(":", 1)
    key = key.strip()
    if not key:
        raise ValueError("empty key")
    raw_value = raw_value.strip()
    return key, raw_value if raw_value else None


def _looks_like_scalar_with_colon(text: str) -> bool:
    quote: str | None = None
    for index, char in enumerate(text):
        if char in {'"', "'"}:
            quote = char if quote is None else None if quote == char else quote
        if char == ":" and quote is None:
            return index + 1 < len(text) and not text[index + 1].isspace()
    return False


def _parse_scalar(value: str) -> Any:
    raw = value.strip()
    if raw == "null" or raw == "~":
        return None
    if raw.lower() == "true":
        return True
    if raw.lower() == "false":
        return False
    if raw.startswith('"') and raw.endswith('"'):
        return bytes(raw[1:-1], "utf-8").decode("unicode_escape")
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    if re.fullmatch(r"-?\d+", raw):
        try:
            return int(raw)
        except ValueError:
            return raw
    return raw


def _strip_yaml_comment(line: str) -> str:
    quote: str | None = None
    escaped = False
    for index, char in enumerate(line):
        if escaped:
            escaped = False
            continue
        if char == "\\" and quote == '"':
            escaped = True
            continue
        if char in {'"', "'"}:
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
            continue
        if char == "#" and quote is None and (index == 0 or line[index - 1].isspace()):
            return line[:index]
    return line


def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, raw_tmp = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
        text=True,
    )
    tmp = Path(raw_tmp)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            tmp.unlink()
        except OSError:
            pass
        raise


def _normalize_state(value: Any) -> str:
    if value is None:
        return "open"
    return str(value).strip().lower()


def _normalize_optional(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _normalize_state_reason(value: Any) -> str | None:
    text = _normalize_optional(value)
    return text.lower() if text is not None else None


def _label_names(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        nodes = value.get("nodes")
        if nodes is not None:
            return _label_names(nodes)
        name = value.get("name")
        return [str(name)] if name else []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Iterable):
        labels: list[str] = []
        for item in value:
            if isinstance(item, Mapping):
                name = item.get("name")
                if name:
                    labels.append(str(name))
            elif item is not None:
                labels.append(str(item))
        return labels
    return [str(value)]




def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")




def _safe_path_segment(value: str) -> str:
    text = str(value).strip().strip("/")
    if not text or text in {".", ".."} or "/" in text:
        raise WorkflowCacheError(f"unsafe cache path segment: {value}")
    return text


def _safe_file_segment(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", str(value)).strip(".-")
