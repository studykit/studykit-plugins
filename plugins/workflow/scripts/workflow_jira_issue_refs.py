#!/usr/bin/env python3
"""Jira issue reference parsing helpers."""

from __future__ import annotations

import re
from collections.abc import Sequence
from typing import Any

JIRA_KEY_RE = re.compile(r"^(?P<project>[A-Z][A-Z0-9]+)-(?P<number>[1-9]\d*)$", re.IGNORECASE)

JIRA_REFERENCE_RE = re.compile(r"(?<![A-Z0-9])(?P<key>[A-Z][A-Z0-9]+-[1-9]\d*)\b", re.IGNORECASE)


class JiraProviderError(RuntimeError):
    """Raised when Jira provider data or configuration cannot be handled."""


def normalize_jira_issue_key(value: Any) -> str:
    """Normalize a Jira issue key such as ``test-1234`` to ``TEST-1234``."""

    text = str(value).strip()
    match = JIRA_KEY_RE.match(text)
    if not match:
        raise JiraProviderError(f"invalid Jira issue key: {value}")
    return f"{match.group('project').upper()}-{int(match.group('number'))}"


def jira_issue_keys_from_references(
    references: Sequence[str],
    *,
    max_refs: int = 20,
) -> list[str]:
    """Extract unique Jira issue keys from explicit references."""

    keys: list[str] = []
    seen: set[str] = set()

    def add(raw: str) -> None:
        if len(keys) >= max_refs:
            return
        try:
            normalized = normalize_jira_issue_key(raw)
        except Exception:
            return
        if normalized in seen:
            return
        seen.add(normalized)
        keys.append(normalized)

    for reference in references:
        for match in JIRA_REFERENCE_RE.finditer(reference):
            add(match.group("key"))
    return keys

