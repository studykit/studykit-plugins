#!/usr/bin/env python3
"""GitHub Issues native provider implementation."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, replace
from typing import Any

from pathlib import Path

from issue.cache import (
    FreshnessMetadata,
    PendingIssueRelationshipOperation,
    WorkflowCacheError,
    WorkflowFreshnessConflict,
    relationship_operations_from_intent,
    require_provider_freshness,
)
from command import CommandRunner
from config import WorkflowConfigError, load_workflow_config
from issue.github.gh import (
    DEFAULT_ISSUE_FIELDS,
    add_issue_dependency,
    add_sub_issue,
    close_issue,
    comment_issue,
    create_issue,
    edit_issue,
    get_github_login,
    issue_assignees,
    issue_relationships,
    issue_body_edit_history,
    issue_events,
    issue_timeline,
    normalize_issue_number,
    remove_issue_dependency,
    remove_sub_issue,
    reopen_issue,
    resolve_github_repository,
    search_issues,
    update_issue_comment,
    view_issue,
)
from issue.github.cache import (
    GitHubIssueCache,
    _comment_fingerprint_items,
    _compact_relationships_for_frontmatter,
    _relationships_from_issue,
    comments_fingerprint,
    content_fingerprint,
    relationships_fingerprint,
)
from issue.providers import (
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_DEFAULT,
    TRANSPORT_NATIVE,
    IssueProvider,
    ProviderFreshnessError,
    ProviderOperationError,
    ProviderRequest,
    _close_reason_from_state_reason,
    _freshness_spec,
    _optional_string,
    _optional_workflow_config,
    _payload_has_relationship_projection,
    _relationship_action,
    _relationship_values,
    _required_payload_value,
    _search_limit,
    _string_list,
    _truthy,
)
from issue.refs import ProviderReferenceError, normalize_provider_reference

@dataclass(frozen=True)
class _ResolvedRelationshipOperation:
    action: str
    relationship: str
    target_issue: str
    replace_parent: bool = False

    def to_json(self) -> dict[str, Any]:
        return {
            "action": self.action,
            "relationship": self.relationship,
            "target_issue": self.target_issue,
            "replace_parent": self.replace_parent,
        }


def _github_search_result(item: Mapping[str, Any]) -> dict[str, Any]:
    """Project one ``gh issue list --json`` row to the shared search shape."""

    number = item.get("number")
    assignees: list[str] = []
    raw_assignees = item.get("assignees")
    if isinstance(raw_assignees, list):
        for entry in raw_assignees:
            if isinstance(entry, Mapping):
                login = entry.get("login")
                if isinstance(login, str) and login:
                    assignees.append(login)
            elif isinstance(entry, str) and entry:
                assignees.append(entry)
    return {
        "issue": str(number) if number is not None else "",
        "title": str(item.get("title") or ""),
        "state": str(item.get("state") or "").upper(),
        "assignees": assignees,
        "url": str(item.get("url") or ""),
    }


class GitHubIssueNativeProvider(IssueProvider):
    """Native GitHub Issues provider backed by ``issue/github/gh.py``."""

    def __init__(self, *, runner: CommandRunner | None = None):
        super().__init__(kind="github", transport=TRANSPORT_NATIVE)
        self.runner = runner

    def get(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        include_body = bool(request.payload.get("include_body", True))
        include_comments = bool(request.payload.get("include_comments", True))
        include_relationships = bool(request.payload.get("include_relationships", True))
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)

        if request.context.cache_policy == CACHE_POLICY_DEFAULT:
            try:
                return cache.read_issue(
                    repo,
                    issue,
                    include_body=include_body,
                    include_comments=include_comments,
                    include_relationships=include_relationships,
                )
            except WorkflowCacheError:
                pass

        raw_fields = request.payload.get("fields")
        fields = DEFAULT_ISSUE_FIELDS
        if isinstance(raw_fields, (list, tuple)):
            fields = tuple(str(field) for field in raw_fields)
        payload = view_issue(issue, project=request.context.project, fields=fields, runner=self.runner)
        if request.context.cache_policy != CACHE_POLICY_BYPASS:
            payload_for_cache = self._payload_with_relationship_projection(
                request,
                issue=issue,
                payload=payload,
            )
            cache.write_issue_bundle(repo, payload_for_cache)
        return payload

    def search(self, request: ProviderRequest) -> Mapping[str, Any]:
        query = str(_required_payload_value(request, "query"))
        limit = _search_limit(request.payload.get("limit"))
        raw = search_issues(
            query,
            project=request.context.project,
            limit=limit,
            runner=self.runner,
        )
        issues = [
            _github_search_result(item) for item in raw if isinstance(item, Mapping)
        ]
        return {"query": query, "issues": issues}

    def _payload_with_relationship_projection(
        self,
        request: ProviderRequest,
        *,
        issue: Any,
        payload: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        """Add provider-native relationships before writing relationship frontmatter.

        `gh issue view` does not expose the issue relationship REST resources
        that back the relationship projection. Cache writes therefore need an
        explicit relationship read even when the caller does not ask to return
        relationships in the provider response.
        """

        if _payload_has_relationship_projection(payload):
            return payload
        relationships = issue_relationships(
            issue,
            project=request.context.project,
            runner=self.runner,
        )
        return {**payload, **relationships}

    def create(self, request: ProviderRequest) -> Mapping[str, Any]:
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)

        title = str(_required_payload_value(request, "title"))
        body = str(_required_payload_value(request, "body"))
        labels = tuple(_string_list(request.payload.get("labels")))
        state = str(request.payload.get("state") or "open")
        state_reason = _optional_string(
            request.payload.get("state_reason") or request.payload.get("stateReason")
        )
        assignee = _optional_string(request.payload.get("assignee"))
        if assignee is not None and assignee.lower() == "me":
            assignee = get_github_login(project=request.context.project, runner=self.runner)

        created = create_issue(
            title=title,
            body=body,
            labels=labels,
            state=state,
            state_reason=state_reason,
            assignee=assignee,
            project=request.context.project,
            runner=self.runner,
        )
        issue_number = normalize_issue_number(created["issue"])
        refreshed = view_issue(issue_number, project=request.context.project, runner=self.runner)
        write_result = cache.write_issue_bundle(
            repo,
            self._payload_with_relationship_projection(
                request,
                issue=issue_number,
                payload=refreshed,
            ),
        )

        return {
            **created,
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def update(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        title = request.payload.get("title")
        body = request.payload.get("body")
        label_set = request.payload.get("label_set")
        if label_set is None:
            label_set = request.payload.get("labels")
        label_add = request.payload.get("label_add")
        label_remove = request.payload.get("label_remove")
        if label_set is not None and (label_add or label_remove):
            raise ProviderOperationError(
                "GitHub issue update cannot combine label_set with label_add or label_remove"
            )
        assignee = _optional_string(request.payload.get("assignee"))
        unassign = bool(request.payload.get("unassign"))
        if assignee is not None and unassign:
            raise ProviderOperationError(
                "GitHub issue update cannot combine assignee with unassign"
            )
        state = _optional_string(request.payload.get("state"))
        state_reason = _optional_string(
            request.payload.get("state_reason") or request.payload.get("stateReason")
        )
        normalized_state = state.lower() if state is not None else None
        if normalized_state is not None and normalized_state not in {"open", "closed"}:
            raise ProviderOperationError(
                f"unsupported GitHub issue state for update: {state}"
            )
        if (
            title is None
            and body is None
            and label_set is None
            and not label_add
            and not label_remove
            and assignee is None
            and not unassign
            and normalized_state is None
        ):
            raise ProviderOperationError(
                "GitHub issue update requires at least one of body, title, labels, "
                "assignee, state"
            )

        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        try:
            self._require_write_freshness(request, issue_number, default_target="issue")
        except ProviderFreshnessError as exc:
            return self._conflict_payload(
                request=request,
                repo=repo,
                cache=cache,
                issue_number=issue_number,
                operation="update_issue",
                target="issue",
                error=exc,
            )
        current_labels: tuple[str, ...] | None = None
        if label_set is not None:
            current = view_issue(
                issue_number,
                project=request.context.project,
                fields=("number", "labels"),
                runner=self.runner,
            )
            current_labels = tuple(_string_list(current.get("labels")))
        remove_assignees: tuple[str, ...] | None = None
        if unassign:
            remove_assignees = issue_assignees(
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )
        edited = edit_issue(
            issue_number,
            title=str(title) if title is not None else None,
            body=str(body) if body is not None else None,
            labels=tuple(_string_list(label_set)) if label_set is not None else None,
            current_labels=current_labels,
            add_labels=tuple(_string_list(label_add)) if label_add else None,
            remove_labels=tuple(_string_list(label_remove)) if label_remove else None,
            assignees=(assignee,) if assignee is not None else None,
            remove_assignees=remove_assignees,
            project=request.context.project,
            runner=self.runner,
        )

        state_result: Mapping[str, Any] | None = None
        if normalized_state == "closed":
            state_result = close_issue(
                issue_number,
                project=request.context.project,
                reason=_close_reason_from_state_reason(state_reason) if state_reason else "completed",
                runner=self.runner,
            )
        elif normalized_state == "open":
            state_result = reopen_issue(
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )

        metadata_changed = (
            label_set is not None
            or bool(label_add)
            or bool(label_remove)
            or assignee is not None
            or unassign
            or normalized_state is not None
        )
        if body is not None and not metadata_changed:
            # GitHub stores the body verbatim, so reuse the body we just wrote
            # as the cache projection instead of paying for a re-fetch.
            write_result = cache.promote_body(
                repo,
                issue_number,
                title=str(title) if title is not None else None,
                body=str(body),
            )
        else:
            refreshed = view_issue(issue_number, project=request.context.project, runner=self.runner)
            write_result = cache.write_issue_bundle(
                repo,
                self._payload_with_relationship_projection(
                    request,
                    issue=issue_number,
                    payload=refreshed,
                ),
            )
        return {
            "operation": "update_issue",
            "issue": issue_number,
            "verified": bool(edited.get("verified")) and (state_result is None or bool(state_result.get("verified"))),
            "edit": dict(edited),
            "state_changed": state_result is not None,
            "state": dict(state_result) if state_result is not None else None,
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def add_comment(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        body = _required_payload_value(request, "body")
        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)

        state = _optional_string(request.payload.get("state"))
        state_reason = _optional_string(
            request.payload.get("state_reason") or request.payload.get("stateReason")
        )
        normalized_state = state.lower() if state is not None else None
        if normalized_state is not None and normalized_state not in {"open", "closed"}:
            raise ProviderOperationError(
                f"unsupported GitHub issue state for append_comment: {state}"
            )

        for target in ("issue", "comments"):
            freshness_payload = dict(request.payload)
            freshness_payload["freshness_check"] = True
            freshness_payload["freshness_target"] = target
            try:
                self._require_write_freshness(
                    replace(request, payload=freshness_payload),
                    issue_number,
                    default_target=target,
                )
            except ProviderFreshnessError as exc:
                return self._conflict_payload(
                    request=request,
                    repo=repo,
                    cache=cache,
                    issue_number=issue_number,
                    operation="append_comment",
                    target=target,
                    error=exc,
                )

        posted = comment_issue(
            issue_number,
            body=str(body),
            project=request.context.project,
            runner=self.runner,
        )

        state_result: Mapping[str, Any] | None = None
        if normalized_state == "closed":
            state_result = close_issue(
                issue_number,
                project=request.context.project,
                reason=_close_reason_from_state_reason(state_reason) if state_reason else "completed",
                runner=self.runner,
            )
        elif normalized_state == "open":
            state_result = reopen_issue(
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )

        write_result = self._refresh_issue_bundle(request, repo, cache, issue_number)
        return {
            "operation": "append_comment",
            "issue": issue_number,
            "comment": dict(posted),
            "state_changed": state_result is not None,
            "state": dict(state_result) if state_result is not None else None,
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def update_comment(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        comment_id = _required_payload_value(request, "comment_id")
        body = _required_payload_value(request, "body")
        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)

        for target in ("issue", "comments"):
            freshness_payload = dict(request.payload)
            freshness_payload["freshness_check"] = True
            freshness_payload["freshness_target"] = target
            try:
                self._require_write_freshness(
                    replace(request, payload=freshness_payload),
                    issue_number,
                    default_target=target,
                )
            except ProviderFreshnessError as exc:
                return self._conflict_payload(
                    request=request,
                    repo=repo,
                    cache=cache,
                    issue_number=issue_number,
                    operation="update_comment",
                    target=target,
                    error=exc,
                )

        updated = update_issue_comment(
            comment_id,
            body=str(body),
            project=request.context.project,
            runner=self.runner,
        )
        write_result = self._refresh_issue_bundle(request, repo, cache, issue_number)
        return {
            "operation": "update_comment",
            "issue": issue_number,
            "comment_id": str(comment_id),
            "comment": dict(updated),
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def apply_relationships(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        issue_number = normalize_issue_number(issue)
        intent = request.payload.get("relationship_intent") or {}
        if not isinstance(intent, Mapping):
            raise ProviderOperationError("relationship_intent must be a mapping")

        operations_raw = relationship_operations_from_intent(
            intent,
            target_kind="issue",
            target_id=issue_number,
        )
        operations_raw = self._resolve_parent_remove_target(request, issue_number, operations_raw)

        if not operations_raw:
            return {
                "operation": "apply_relationships",
                "issue": issue_number,
                "applied": 0,
                "operations": [],
                "provider_results": [],
                "cache_refreshed": False,
                "no_changes": True,
            }

        operations = [
            _ResolvedRelationshipOperation(
                action=op.action,
                relationship=op.relationship,
                target_issue=self._resolve_github_issue_reference(request, op.target_ref),
                replace_parent=op.replace_parent,
            )
            for op in operations_raw
        ]
        return self._apply_relationship_operations(request, issue_number, operations)

    def _resolve_parent_remove_target(
        self,
        request: ProviderRequest,
        issue_number: str,
        operations: list[PendingIssueRelationshipOperation],
    ) -> list[PendingIssueRelationshipOperation]:
        if not any(
            op.action == "remove" and op.relationship == "parent" and not op.target_ref
            for op in operations
        ):
            return operations
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        current_parent = ""
        try:
            relationships = cache.read_relationships(repo, issue_number)
        except WorkflowCacheError:
            relationships = {}
        parent_ref = relationships.get("parent")
        if parent_ref not in (None, "", 0):
            current_parent = str(parent_ref)
        resolved: list[PendingIssueRelationshipOperation] = []
        for op in operations:
            if op.action == "remove" and op.relationship == "parent" and not op.target_ref:
                if not current_parent:
                    continue
                resolved.append(replace(op, target_ref=current_parent))
            else:
                resolved.append(op)
        return resolved

    def set_parent(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = normalize_issue_number(_required_payload_value(request, "issue"))
        parent = _required_payload_value(request, "parent")
        action = _relationship_action(request.payload.get("action") or request.payload.get("op") or "add")
        operations = [
            _ResolvedRelationshipOperation(
                action=action,
                relationship="parent",
                target_issue=self._resolve_github_issue_reference(request, parent),
                replace_parent=_truthy(request.payload.get("replace_parent") or request.payload.get("replaceParent")),
            )
        ]
        return self._apply_relationship_operations(request, issue, operations)

    def set_dependency(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = normalize_issue_number(_required_payload_value(request, "issue"))
        operations: list[_ResolvedRelationshipOperation] = []
        for key, relationship in (("blocked_by", "blocked_by"), ("blockedBy", "blocked_by"), ("blocking", "blocking"), ("blocks", "blocking")):
            if key not in request.payload:
                continue
            for value in _relationship_values(request.payload[key]):
                operations.append(
                    _ResolvedRelationshipOperation(
                        action=_relationship_action(request.payload.get("action") or request.payload.get("op") or "add"),
                        relationship=relationship,
                        target_issue=self._resolve_github_issue_reference(request, value),
                    )
                )
        if not operations:
            target = _required_payload_value(request, "dependency")
            operations.append(
                _ResolvedRelationshipOperation(
                    action=_relationship_action(request.payload.get("action") or request.payload.get("op") or "add"),
                    relationship="blocked_by",
                    target_issue=self._resolve_github_issue_reference(request, target),
                )
            )
        return self._apply_relationship_operations(request, issue, operations)

    def _apply_relationship_operations(
        self,
        request: ProviderRequest,
        issue_number: str,
        operations: list[_ResolvedRelationshipOperation],
    ) -> dict[str, Any]:
        if not operations:
            raise ProviderOperationError(f"no GitHub relationship operations found for issue #{issue_number}")
        self._validate_relationship_operations(operations)
        freshness_payload = dict(request.payload)
        freshness_payload.setdefault("freshness_check", True)
        freshness_payload.setdefault("freshness_target", "relationships")
        self._require_write_freshness(
            replace(request, payload=freshness_payload),
            issue_number,
            default_target="relationships",
        )

        applied: list[Mapping[str, Any]] = []
        for operation in operations:
            applied.append(self._dispatch_relationship_operation(issue_number, operation, request=request))

        relationship_location = self._refresh_relationship_projection(request, issue_number)
        target_refreshed, target_errors = self._refresh_relationship_targets(
            request, issue_number, operations
        )
        payload: dict[str, Any] = {
            "operation": "apply_relationships",
            "issue": issue_number,
            "applied": len(applied),
            "operations": [operation.to_json() for operation in operations],
            "provider_results": [dict(item) for item in applied],
            "cache_refreshed": True,
            "relationship_location": str(relationship_location),
        }
        if target_refreshed:
            payload["target_relationship_locations"] = target_refreshed
        if target_errors:
            payload["target_relationship_errors"] = target_errors
        return payload

    def _refresh_relationship_targets(
        self,
        request: ProviderRequest,
        source_number: str,
        operations: list[_ResolvedRelationshipOperation],
    ) -> tuple[dict[str, str], list[dict[str, str]]]:
        """Re-project ``relation.md`` for the far endpoint of each relationship.

        A GitHub sub-issue or dependency write mutates both endpoints — the
        parent gains a child, the blocker gains a "blocking" entry — so
        refreshing only ``source_number`` leaves every target's cached
        ``relation.md`` stale. Re-project each target that is already tracked
        locally; never materialize a target that was not cached before. The
        provider write has already succeeded for both sides, so a failed target
        *fetch* is reported rather than raised — it must not roll back the
        applied relationship.
        """

        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        refreshed: dict[str, str] = {}
        errors: list[dict[str, str]] = []
        seen: set[str] = {source_number}
        for operation in operations:
            target = operation.target_issue
            if not target or target in seen:
                continue
            seen.add(target)
            if not cache.has_issue_projection(repo, target):
                continue
            try:
                relationships = issue_relationships(
                    target,
                    project=request.context.project,
                    runner=self.runner,
                )
                location = cache.write_relationships_projection(repo, target, relationships)
            except Exception as exc:  # noqa: BLE001 — best-effort; report, do not roll back
                errors.append({"issue": target, "error": str(exc)})
            else:
                refreshed[target] = str(location)
        return refreshed, errors

    def _refresh_relationship_projection(self, request: ProviderRequest, issue_number: str) -> Path:
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        relationships = issue_relationships(
            issue_number,
            project=request.context.project,
            runner=self.runner,
        )
        return cache.write_relationships_projection(repo, issue_number, relationships)

    def _refresh_issue_bundle(
        self,
        request: ProviderRequest,
        repo: GitHubRepository,
        cache: GitHubIssueCache,
        issue_number: str,
    ):
        refreshed = view_issue(issue_number, project=request.context.project, runner=self.runner)
        return cache.write_issue_bundle(
            repo,
            self._payload_with_relationship_projection(
                request,
                issue=issue_number,
                payload=refreshed,
            ),
        )

    def _conflict_payload(
        self,
        *,
        request: ProviderRequest,
        repo: GitHubRepository,
        cache: GitHubIssueCache,
        issue_number: str,
        operation: str,
        target: str,
        error: ProviderFreshnessError,
        pending_files: list[str] | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "operation": operation,
            "issue": issue_number,
            "status": "conflict",
            "reason": "provider_changed",
            "message": (
                f"{operation} stopped: GitHub issue #{issue_number} {target} changed on the "
                "provider since it was last fetched. The cache was refreshed — reread the listed "
                "paths and reapply your change, or retry with --overwrite to replace the provider copy."
            ),
            "target": target,
            "conflict": error.to_json(),
            "reread_required": True,
            "reread_paths": self._reread_paths(cache, repo, issue_number, target=target),
            "overwrite_hint": "--overwrite",
        }
        if pending_files is not None:
            payload["pending_files"] = pending_files
        try:
            write_result = self._refresh_issue_bundle(request, repo, cache, issue_number)
        except Exception as refresh_exc:  # pragma: no cover - defensive reporting path
            payload["cache_refreshed"] = False
            payload["refresh_error"] = str(refresh_exc)
        else:
            payload["cache_refreshed"] = True
            payload["cache"] = write_result.to_json()
        return payload

    def _reread_paths(
        self,
        cache: GitHubIssueCache,
        repo: GitHubRepository,
        issue_number: str,
        *,
        target: str,
    ) -> list[str]:
        if target == "relationships":
            paths: list[Path] = [cache.relationships_file(repo, issue_number)]
        elif target == "comments":
            paths = [cache.issue_file(repo, issue_number), *cache.comment_files(repo, issue_number)]
        else:
            paths = [cache.issue_file(repo, issue_number)]
        return [str(path) for index, path in enumerate(paths) if path not in paths[:index]]

    def _validate_relationship_operations(self, operations: list[_ResolvedRelationshipOperation]) -> None:
        supported = {"parent", "child", "blocked_by", "blocking"}
        for operation in operations:
            if operation.relationship not in supported:
                raise ProviderOperationError(
                    f"unsupported GitHub relationship operation: {operation.relationship}"
                )
            if operation.action not in {"add", "remove"}:
                raise ProviderOperationError(
                    f"unsupported GitHub relationship action: {operation.action}"
                )

    def _dispatch_relationship_operation(
        self,
        issue_number: str,
        operation: _ResolvedRelationshipOperation,
        *,
        request: ProviderRequest,
    ) -> Mapping[str, Any]:
        if operation.relationship == "parent":
            if operation.action == "add":
                return add_sub_issue(
                    operation.target_issue,
                    issue_number,
                    project=request.context.project,
                            replace_parent=operation.replace_parent,
                    runner=self.runner,
                )
            return remove_sub_issue(
                operation.target_issue,
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )

        if operation.relationship == "child":
            if operation.action == "add":
                return add_sub_issue(
                    issue_number,
                    operation.target_issue,
                    project=request.context.project,
                            replace_parent=operation.replace_parent,
                    runner=self.runner,
                )
            return remove_sub_issue(
                issue_number,
                operation.target_issue,
                project=request.context.project,
                runner=self.runner,
            )

        if operation.relationship == "blocked_by":
            if operation.action == "add":
                return add_issue_dependency(
                    issue_number,
                    operation.target_issue,
                    project=request.context.project,
                            runner=self.runner,
                )
            return remove_issue_dependency(
                issue_number,
                operation.target_issue,
                project=request.context.project,
                runner=self.runner,
            )

        if operation.relationship == "blocking":
            if operation.action == "add":
                return add_issue_dependency(
                    operation.target_issue,
                    issue_number,
                    project=request.context.project,
                            runner=self.runner,
                )
            return remove_issue_dependency(
                operation.target_issue,
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )

        raise ProviderOperationError(f"unsupported GitHub relationship operation: {operation.relationship}")

    def _resolve_github_issue_reference(self, request: ProviderRequest, value: Any) -> str:
        raw = str(value).strip()
        if not raw:
            raise ProviderOperationError("GitHub relationship target issue reference is empty")
        config = _optional_workflow_config(request.context.project)
        if config is None:
            return normalize_issue_number(raw)
        try:
            ref = normalize_provider_reference(
                raw,
                config,
                role="issue",
                allow_bare_issue_number=True,
                runner=self.runner,
            )
        except ProviderReferenceError as exc:
            raise ProviderOperationError(str(exc)) from exc
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        native = ref.native
        ref_repo = (
            str(ref.authority).lower(),
            str(native.get("owner") or "").lower(),
            str(native.get("repo") or "").lower(),
        )
        current_repo = (repo.host.lower(), repo.owner.lower(), repo.name.lower())
        if ref.provider != "github" or ref.kind != "issue" or ref_repo != current_repo:
            raise ProviderOperationError(
                f"GitHub relationship target must be in the configured repository: {raw}"
            )
        return normalize_issue_number(native.get("number") or "")

    def close(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        issue_number = normalize_issue_number(issue)
        reason = str(request.payload.get("reason") or "completed")
        comment = request.payload.get("comment")
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        freshness_payload = dict(request.payload)
        freshness_payload.setdefault("freshness_check", True)
        freshness_payload.setdefault("freshness_target", "issue")
        try:
            self._require_write_freshness(
                replace(request, payload=freshness_payload),
                issue_number,
                default_target="issue",
            )
        except ProviderFreshnessError as exc:
            return self._conflict_payload(
                request=request,
                repo=repo,
                cache=cache,
                issue_number=issue_number,
                operation="close_issue",
                target="issue",
                error=exc,
            )
        closed = close_issue(
            issue_number,
            project=request.context.project,
            reason=reason,
            comment=str(comment) if comment is not None else None,
            runner=self.runner,
        )
        write_result = self._refresh_issue_bundle(request, repo, cache, issue_number)
        return {
            **dict(closed),
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def reopen(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        issue_number = normalize_issue_number(issue)
        comment = request.payload.get("comment")
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        freshness_payload = dict(request.payload)
        freshness_payload.setdefault("freshness_check", True)
        freshness_payload.setdefault("freshness_target", "issue")
        try:
            self._require_write_freshness(
                replace(request, payload=freshness_payload),
                issue_number,
                default_target="issue",
            )
        except ProviderFreshnessError as exc:
            return self._conflict_payload(
                request=request,
                repo=repo,
                cache=cache,
                issue_number=issue_number,
                operation="reopen_issue",
                target="issue",
                error=exc,
            )
        reopened = reopen_issue(
            issue_number,
            project=request.context.project,
            comment=str(comment) if comment is not None else None,
            runner=self.runner,
        )
        write_result = self._refresh_issue_bundle(request, repo, cache, issue_number)
        return {
            **dict(reopened),
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def logs(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        include = request.payload.get("include") or ("timeline", "events", "body_edits")
        if isinstance(include, str):
            include = (include,)
        if not isinstance(include, (list, tuple)):
            raise ProviderOperationError("logs include must be a string or list")

        payload: dict[str, Any] = {}
        for item in include:
            normalized = str(item).replace("-", "_")
            if normalized == "timeline":
                payload["timeline"] = issue_timeline(
                    issue,
                    project=request.context.project,
                runner=self.runner,
                )
            elif normalized == "events":
                payload["events"] = issue_events(
                    issue,
                    project=request.context.project,
                runner=self.runner,
                )
            elif normalized in {"body_edits", "body_edit_history"}:
                payload["body_edit_history"] = issue_body_edit_history(
                    issue,
                    project=request.context.project,
                runner=self.runner,
                )
            else:
                raise ProviderOperationError(f"unsupported GitHub issue log stream: {item}")
        return payload

    def comments(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = self.get(request)
        return {"comments": issue.get("comments", [])}

    def _require_write_freshness(
        self,
        request: ProviderRequest,
        issue: Any,
        *,
        default_target: str,
    ) -> None:
        if _truthy(request.payload.get("overwrite")):
            return
        spec = _freshness_spec(request.payload, default_target=default_target)
        if spec is None:
            return

        issue_number = normalize_issue_number(issue)
        artifact = f"GitHub issue #{issue_number} {spec['target']}"
        if spec["pending_new"]:
            require_provider_freshness(
                None,
                provider_fingerprint=None,
                artifact=artifact,
                pending_new=True,
            )
            return

        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        metadata: FreshnessMetadata | None
        try:
            metadata = cache.read_freshness_metadata(repo, issue_number, target=spec["target"])
        except WorkflowCacheError:
            metadata = FreshnessMetadata(
                fingerprint=None,
                path=cache.freshness_file(repo, issue_number, spec["target"]),
                target=spec["target"],
            )

        provider_fingerprint = self._provider_fingerprint(
            issue_number,
            request=request,
            target=spec["target"],
        )
        try:
            require_provider_freshness(
                metadata,
                provider_fingerprint=provider_fingerprint,
                artifact=artifact,
            )
        except WorkflowFreshnessConflict as exc:
            raise ProviderFreshnessError(str(exc), result=exc.result) from exc

    def _provider_fingerprint(
        self,
        issue: str,
        *,
        request: ProviderRequest,
        target: str,
    ) -> str | None:
        """Recompute the provider's current fingerprint for one freshness target.

        Routes through the same cache builders used at write time, so an
        unchanged artifact always produces an identical fingerprint.
        """

        if target == "comments":
            payload = view_issue(
                issue,
                project=request.context.project,
                fields=("number", "comments"),
                runner=self.runner,
            )
            return comments_fingerprint(_comment_fingerprint_items(payload))
        if target == "relationships":
            # Derived reference kinds are excluded from the fingerprint, so
            # skip their extra API reads when only the fingerprint is needed.
            relationships = issue_relationships(
                issue,
                project=request.context.project,
                runner=self.runner,
                include_derived=False,
            )
            compact = _compact_relationships_for_frontmatter(
                _relationships_from_issue(relationships)
            )
            return relationships_fingerprint(compact)
        payload = view_issue(
            issue,
            project=request.context.project,
            fields=("number", "title", "body"),
            runner=self.runner,
        )
        return content_fingerprint(payload.get("title"), payload.get("body"))
