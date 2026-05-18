#!/usr/bin/env python3
"""GitHub Issues native provider implementation."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, replace
from typing import Any

from pathlib import Path

from workflow_cache import (
    FreshnessMetadata,
    PendingIssueRelationshipOperation,
    WorkflowCacheError,
    WorkflowFreshnessConflict,
    require_provider_freshness,
)
from workflow_command import CommandRunner
from workflow_config import WorkflowConfigError, load_workflow_config
from workflow_github import (
    DEFAULT_ISSUE_FIELDS,
    add_issue_dependency,
    add_sub_issue,
    close_issue,
    comment_issue,
    create_issue,
    edit_issue,
    issue_relationships,
    issue_body_edit_history,
    issue_events,
    issue_timeline,
    normalize_issue_number,
    remove_issue_dependency,
    remove_sub_issue,
    reopen_issue,
    resolve_github_repository,
    view_issue,
)
from workflow_github_issue_cache import GitHubIssueCache
from workflow_providers import (
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_DEFAULT,
    TRANSPORT_NATIVE,
    IssueProvider,
    ProviderFreshnessError,
    ProviderOperationError,
    ProviderRequest,
    _close_reason_from_state_reason,
    _freshness_spec,
    _latest_provider_comment_timestamp,
    _optional_string,
    _optional_workflow_config,
    _payload_has_relationship_projection,
    _relationship_action,
    _relationship_values,
    _required_payload_value,
    _string_list,
    _truthy,
)
from workflow_refs import ProviderReferenceError, normalize_provider_reference

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


class GitHubIssueNativeProvider(IssueProvider):
    """Native GitHub Issues provider backed by ``workflow_github.py``."""

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

        created = create_issue(
            title=title,
            body=body,
            labels=labels,
            state=state,
            state_reason=state_reason,
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
        if _truthy(request.payload.get("from_cache")) or _truthy(request.payload.get("cache_write_back")):
            return self._update_from_cache(request, issue)

        title = request.payload.get("title")
        body = request.payload.get("body")
        labels = request.payload.get("labels")
        if title is None and body is None and labels is None:
            raise ProviderOperationError("GitHub issue update requires from_cache or at least one of title, body, labels")
        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        try:
            self._require_write_freshness(request, issue_number, default_target="issue")
        except ProviderFreshnessError as exc:
            return self._stale_cache_block_payload(
                request=request,
                repo=repo,
                cache=cache,
                issue_number=issue_number,
                operation="update_issue",
                target="issue",
                error=exc,
            )
        current_labels: tuple[str, ...] | None = None
        if labels is not None:
            current = view_issue(
                issue_number,
                project=request.context.project,
                fields=("number", "labels"),
                runner=self.runner,
            )
            current_labels = tuple(_string_list(current.get("labels")))
        edited = edit_issue(
            issue_number,
            title=str(title) if title is not None else None,
            body=str(body) if body is not None else None,
            labels=tuple(_string_list(labels)) if labels is not None else None,
            current_labels=current_labels,
            project=request.context.project,
            runner=self.runner,
        )
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
            "verified": bool(edited.get("verified")),
            "edit": dict(edited),
            "cache_refreshed": True,
            "cache": write_result.to_json(),
        }

    def _update_from_cache(self, request: ProviderRequest, issue: Any) -> Mapping[str, Any]:
        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        projection = cache.read_issue(
            repo,
            issue_number,
            include_body=True,
            include_comments=False,
            include_relationships=False,
        )
        try:
            provider_current = self._require_cached_issue_write_freshness(request, repo, cache, issue_number)
        except ProviderFreshnessError as exc:
            return self._stale_cache_block_payload(
                request=request,
                repo=repo,
                cache=cache,
                issue_number=issue_number,
                operation="update_issue_from_cache",
                target="issue",
                error=exc,
            )
        current_labels = tuple(_string_list(provider_current.get("labels")))

        edited = edit_issue(
            issue_number,
            title=str(projection.get("title") or ""),
            body=str(projection.get("body") or ""),
            labels=tuple(_string_list(projection.get("labels"))),
            current_labels=current_labels,
            project=request.context.project,
            runner=self.runner,
        )

        state_result: Mapping[str, Any] | None = None
        desired_state = str(projection.get("state") or "").upper()
        current_state = str(provider_current.get("state") or "").upper()
        if desired_state == "CLOSED" and current_state != "CLOSED":
            state_result = close_issue(
                issue_number,
                project=request.context.project,
                reason=_close_reason_from_state_reason(projection.get("stateReason")),
                runner=self.runner,
            )
        elif desired_state == "OPEN" and current_state != "OPEN":
            state_result = reopen_issue(
                issue_number,
                project=request.context.project,
                runner=self.runner,
            )

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
            "operation": "update_issue_from_cache",
            "issue": issue_number,
            "verified": bool(edited.get("verified")) and (state_result is None or bool(state_result.get("verified"))),
            "edit": dict(edited),
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
                return self._stale_cache_block_payload(
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

    def apply_relationships(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = _required_payload_value(request, "issue")
        if _truthy(request.payload.get("from_pending")) or _truthy(request.payload.get("pending_relationships")):
            return self._apply_pending_relationships(request, issue)
        raise ProviderOperationError("GitHub issue apply_relationships currently requires pending_relationships")

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
        return self._apply_relationship_operations(request, issue, operations, pending_operations=None)

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
        return self._apply_relationship_operations(request, issue, operations, pending_operations=None)

    def _apply_pending_relationships(self, request: ProviderRequest, issue: Any) -> Mapping[str, Any]:
        issue_number = normalize_issue_number(issue)
        repo = resolve_github_repository(request.context.project, runner=self.runner)
        cache = GitHubIssueCache.for_project(request.context.project, configured_repo=repo)
        pending_operations = cache.read_pending_issue_relationships(repo, issue_number)
        if not pending_operations:
            raise ProviderOperationError(f"no pending relationship frontmatter found for GitHub issue #{issue_number}")

        operations = [
            _ResolvedRelationshipOperation(
                action=operation.action,
                relationship=operation.relationship,
                target_issue=self._resolve_github_issue_reference(request, operation.target_ref),
                replace_parent=operation.replace_parent,
            )
            for operation in pending_operations
        ]
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
        consumed_pending: list[PendingIssueRelationshipOperation] = []
        consumed_resolved: list[_ResolvedRelationshipOperation] = []
        try:
            for resolved, pending in zip(operations, pending_operations):
                applied.append(self._dispatch_relationship_operation(issue_number, resolved, request=request))
                consumed_pending.append(pending)
                consumed_resolved.append(resolved)
        except Exception as exc:
            removed = self._remove_consumed_pending_relationships(
                cache,
                repo,
                issue_number,
                consumed_pending=consumed_pending,
            )
            refresh_error: str | None = None
            relationship_location: Path | None = None
            try:
                relationship_location = self._refresh_relationship_projection(request, issue_number)
            except Exception as refresh_exc:  # pragma: no cover - defensive reporting path
                refresh_error = str(refresh_exc)
            details = (
                f"GitHub relationship apply failed after {len(applied)} provider operation(s); "
                "provider state may have partially changed. Refresh relationships and re-stage before retry."
            )
            if refresh_error:
                details += f" Relationship refresh also failed: {refresh_error}"
            raise ProviderOperationError(details) from exc

        relationship_location = self._refresh_relationship_projection(request, issue_number)
        removed = self._remove_consumed_pending_relationships(
            cache,
            repo,
            issue_number,
            consumed_pending=consumed_pending,
        )
        return {
            "operation": "apply_relationships",
            "issue": issue_number,
            "applied": len(applied),
            "operations": [operation.to_json() for operation in operations],
            "provider_results": [dict(item) for item in applied],
            "pending_operations": [operation.to_json() for operation in pending_operations],
            "consumed_operations": [operation.to_json() for operation in consumed_resolved],
            "cache_refreshed": True,
            "relationship_location": str(relationship_location),
            "pending_source": "issue",
            "pending_file": pending_operations[0].file_name,
            "removed_pending_files": [str(path) for path in removed],
        }

    def _remove_consumed_pending_relationships(
        self,
        cache: GitHubIssueCache,
        repo: Any,
        issue_number: str,
        *,
        consumed_pending: list[PendingIssueRelationshipOperation],
    ) -> list[Path]:
        if not consumed_pending:
            return []
        return cache.remove_pending_issue_relationships(repo, issue_number, consumed_pending)

    def _apply_relationship_operations(
        self,
        request: ProviderRequest,
        issue_number: str,
        operations: list[_ResolvedRelationshipOperation],
        *,
        pending_operations: list[PendingIssueRelationshipOperation] | None,
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
        return {
            "operation": "apply_relationships",
            "issue": issue_number,
            "applied": len(applied),
            "operations": [operation.to_json() for operation in operations],
            "provider_results": [dict(item) for item in applied],
            "pending_operations": [operation.to_json() for operation in pending_operations or []],
            "cache_refreshed": True,
            "relationship_location": str(relationship_location),
        }

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

    def _stale_cache_block_payload(
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
            "status": "blocked",
            "reason": "stale_cache",
            "message": (
                f"{operation} blocked because GitHub issue #{issue_number} {target} changed on the provider. "
                "The cache was refreshed; reread the listed paths before retrying."
            ),
            "target": target,
            "freshness": error.to_json(),
            "reread_required": True,
            "reread_paths": self._reread_paths(cache, repo, issue_number, target=target),
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
        paths: list[Path] = [cache.issue_file(repo, issue_number)]
        if target == "comments":
            paths.extend(cache.comment_files(repo, issue_number))
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
            return self._stale_cache_block_payload(
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
            return self._stale_cache_block_payload(
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
        spec = _freshness_spec(request.payload, default_target=default_target)
        if spec is None:
            return

        issue_number = normalize_issue_number(issue)
        artifact = f"GitHub issue #{issue_number} {spec['target']}"
        if spec["pending_new"]:
            require_provider_freshness(
                None,
                provider_updated_at=None,
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
                source_updated_at=None,
                fetched_at=None,
                path=cache.freshness_file(repo, issue_number, spec["target"]),
                target=spec["target"],
            )

        provider_updated_at = self._provider_freshness_timestamp(
            issue_number,
            request=request,
            target=spec["target"],
        )
        try:
            require_provider_freshness(
                metadata,
                provider_updated_at=provider_updated_at,
                artifact=artifact,
            )
        except WorkflowFreshnessConflict as exc:
            raise ProviderFreshnessError(str(exc), result=exc.result) from exc

    def _require_cached_issue_write_freshness(
        self,
        request: ProviderRequest,
        repo: GitHubRepository,
        cache: GitHubIssueCache,
        issue_number: str,
    ) -> Mapping[str, Any]:
        artifact = f"GitHub issue #{issue_number} issue"
        try:
            metadata = cache.read_freshness_metadata(repo, issue_number, target="issue")
        except WorkflowCacheError:
            metadata = FreshnessMetadata(
                source_updated_at=None,
                fetched_at=None,
                path=cache.freshness_file(repo, issue_number, "issue"),
                target="issue",
            )

        provider_current = view_issue(
            issue_number,
            project=request.context.project,
            fields=("number", "updatedAt", "labels", "state", "stateReason"),
            runner=self.runner,
        )
        try:
            require_provider_freshness(
                metadata,
                provider_updated_at=_optional_string(provider_current.get("updatedAt")),
                artifact=artifact,
            )
        except WorkflowFreshnessConflict as exc:
            raise ProviderFreshnessError(str(exc), result=exc.result) from exc
        return provider_current

    def _provider_freshness_timestamp(
        self,
        issue: str,
        *,
        request: ProviderRequest,
        target: str,
    ) -> str | None:
        fields = ("number", "updatedAt")
        if target == "comments":
            fields = ("number", "updatedAt", "comments")

        payload = view_issue(
            issue,
            project=request.context.project,
            fields=fields,
            runner=self.runner,
        )
        if target == "comments":
            return _latest_provider_comment_timestamp(payload.get("comments")) or _optional_string(
                payload.get("updatedAt")
            )
        return _optional_string(payload.get("updatedAt"))
