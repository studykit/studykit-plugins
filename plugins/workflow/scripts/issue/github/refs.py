#!/usr/bin/env python3
"""GitHub issue reference parsing helpers."""

from __future__ import annotations

import re
from collections.abc import Sequence

from workflow_github import GitHubRepository, normalize_issue_number

MAX_ISSUE_REFS = 20

ISSUE_HASH_RE = re.compile(r"(?<![\w#])#([1-9]\d*)\b")
ISSUE_REPO_RE = re.compile(
    r"(?<![\w/.-])(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)#(?P<num>[1-9]\d*)\b",
    re.IGNORECASE,
)
ISSUE_URL_RE = re.compile(
    r"https?://(?P<host>[^/\s]+)/(?P<owner>[^/\s]+)/(?P<repo>[^/\s]+)/issues/(?P<num>[1-9]\d*)\b",
    re.IGNORECASE,
)


def issue_numbers_from_references(
    references: Sequence[str],
    *,
    repo: GitHubRepository | None = None,
    allow_bare_numbers: bool = True,
    max_refs: int = MAX_ISSUE_REFS,
) -> list[str]:
    """Extract unique GitHub issue numbers from explicit shell-tool references."""

    numbers: list[str] = []
    seen: set[str] = set()

    def add(raw: str) -> None:
        if len(numbers) >= max_refs:
            return
        try:
            normalized = normalize_issue_number(raw)
        except Exception:
            return
        if normalized in seen:
            return
        seen.add(normalized)
        numbers.append(normalized)

    for reference in references:
        if allow_bare_numbers:
            before = len(numbers)
            add(reference)
            if len(numbers) > before:
                continue
        for number in extract_issue_numbers(
            reference,
            repo=repo,
            max_refs=max_refs - len(numbers),
        ):
            add(number)

    return numbers


def extract_issue_numbers(
    text: str,
    *,
    repo: GitHubRepository | None = None,
    max_refs: int = MAX_ISSUE_REFS,
) -> list[str]:
    """Extract same-repository GitHub issue references in first-seen order."""

    numbers: list[str] = []
    seen: set[str] = set()
    candidates: list[tuple[int, str]] = []

    def add(raw: str) -> None:
        if len(numbers) >= max_refs:
            return
        try:
            normalized = normalize_issue_number(raw)
        except Exception:
            return
        if normalized in seen:
            return
        seen.add(normalized)
        numbers.append(normalized)

    for match in ISSUE_URL_RE.finditer(text):
        if repo is not None and not same_github_repo(
            repo,
            host=match.group("host"),
            owner=match.group("owner"),
            repo_name=match.group("repo"),
        ):
            continue
        candidates.append((match.start(), match.group("num")))

    for match in ISSUE_REPO_RE.finditer(text):
        if repo is not None and not same_github_repo(
            repo,
            host=repo.host,
            owner=match.group("owner"),
            repo_name=match.group("repo"),
        ):
            continue
        candidates.append((match.start(), match.group("num")))

    for match in ISSUE_HASH_RE.finditer(text):
        candidates.append((match.start(), match.group(1)))

    for _, raw in sorted(candidates, key=lambda item: item[0]):
        add(raw)

    return numbers


def same_github_repo(
    repo: GitHubRepository,
    *,
    host: str,
    owner: str,
    repo_name: str,
) -> bool:
    return (
        host.lower(),
        owner.lower(),
        repo_name.removesuffix(".git").lower(),
    ) == (
        repo.host.lower(),
        repo.owner.lower(),
        repo.name.lower(),
    )
