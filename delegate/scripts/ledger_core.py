"""Host-neutral append-only delegation history and verdict summaries."""

from __future__ import annotations

import argparse
import json
import secrets
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CATEGORIES = (
    "lookup",
    "mechanical-edit",
    "implement",
    "debug",
    "review",
    "research",
    "write",
    "plan",
)
EFFORTS = ("low", "medium", "high", "xhigh", "max")
VERDICTS = ("pass", "partial", "fail")
CAUSES = ("capability", "instruction", "environment")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def append(entry: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load(path: Path) -> list[dict[str, Any]]:
    """Runs in recording order, each with its latest amendment applied."""
    if not path.exists():
        return []
    runs: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("kind") == "run":
                runs[entry["id"]] = entry
            elif entry.get("kind") == "amend" and entry.get("id") in runs:
                run = runs[entry["id"]]
                for key in ("verdict", "cause", "reason"):
                    run[key] = entry.get(key)
                run["amended_by"] = entry.get("by")
    return list(runs.values())


def check_cause(verdict: str, cause: str | None) -> None:
    if verdict != "pass" and cause is None:
        sys.exit(f"ledger: --cause is required for a {verdict} verdict")
    if verdict == "pass" and cause is not None:
        sys.exit("ledger: a pass verdict takes no --cause")


def cmd_add(args: argparse.Namespace) -> None:
    check_cause(args.verdict, args.cause)
    run_id = f"{datetime.now():%Y%m%d-%H%M%S}-{secrets.token_hex(2)}"
    append(
        {
            "kind": "run",
            "id": run_id,
            "ts": now(),
            "project": Path.cwd().name,
            "category": args.category,
            "task": args.task,
            "agent_type": args.agent_type,
            "model": args.model,
            "effort": args.effort,
            "verdict": args.verdict,
            "cause": args.cause,
            "reason": args.reason,
            "tokens": args.tokens,
            "duration_ms": args.duration_ms,
            "retry_of": args.retry_of,
        },
        args.ledger_path,
    )
    print(run_id)


def cmd_amend(args: argparse.Namespace) -> None:
    check_cause(args.verdict, args.cause)
    if not any(run["id"] == args.id for run in load(args.ledger_path)):
        sys.exit(f"ledger: no run with id {args.id}")
    append(
        {
            "kind": "amend",
            "id": args.id,
            "ts": now(),
            "by": args.by,
            "verdict": args.verdict,
            "cause": args.cause,
            "reason": args.reason,
        },
        args.ledger_path,
    )
    print(f"amended {args.id}")


def tier_key(run: dict[str, Any], models: tuple[str, ...]) -> tuple[int, int]:
    model, effort = run.get("model"), run.get("effort")
    return (
        models.index(model) if model in models else len(models),
        EFFORTS.index(effort) if effort in EFFORTS else len(EFFORTS),
    )


def cmd_recall(args: argparse.Namespace) -> None:
    runs = [
        r for r in load(args.ledger_path) if args.category is None or r.get("category") == args.category
    ]
    if not runs:
        scope = f"category {args.category}" if args.category else "any category"
        print(f"No recorded runs for {scope}.")
        return

    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for run in runs:
        by_category[run.get("category", "?")].append(run)

    for category, cat_runs in sorted(by_category.items()):
        print(f"## {category}")
        by_tier: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for run in cat_runs:
            by_tier[(run.get("model", "?"), run.get("effort", "?"))].append(run)
        for (model, effort), tier_runs in sorted(
            by_tier.items(), key=lambda item: tier_key(item[1][0], args.models)
        ):
            recent = tier_runs[-args.window :]
            counts = {v: sum(r.get("verdict") == v for r in tier_runs) for v in VERDICTS}
            cap_recent = sum(
                r.get("verdict") != "pass" and r.get("cause") == "capability"
                for r in recent
            )
            streak = 0
            for run in reversed(tier_runs):
                if run.get("verdict") != "pass":
                    break
                streak += 1
            tokens = [r["tokens"] for r in tier_runs if r.get("tokens")]
            avg = f", avg {sum(tokens) // len(tokens)} tokens" if tokens else ""
            print(
                f"- {model}/{effort}: {len(tier_runs)} runs — "
                f"{counts['pass']} pass, {counts['partial']} partial, {counts['fail']} fail; "
                f"capability failures in last {len(recent)}: {cap_recent}; "
                f"current pass streak: {streak}{avg}"
            )
        misses = [r for r in cat_runs if r.get("verdict") != "pass"][-args.notes :]
        for run in misses:
            amended = f" (amended by {run['amended_by']})" if run.get("amended_by") else ""
            print(
                f"  - {run['id']} {run.get('model')}/{run.get('effort')} "
                f"{run.get('verdict')}/{run.get('cause')}{amended}: "
                f"{run.get('task')} — {run.get('reason')}"
            )
        print()


def main(path: Path, models: tuple[str, ...]) -> None:
    parser = argparse.ArgumentParser(prog="ledger", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="record one delegated run")
    add.add_argument("--category", required=True, choices=CATEGORIES)
    add.add_argument("--task", required=True, help="one line: what was asked")
    add.add_argument("--agent-type", required=True)
    add.add_argument("--model", required=True, choices=models)
    add.add_argument("--effort", required=True, choices=EFFORTS)
    add.add_argument("--verdict", required=True, choices=VERDICTS)
    add.add_argument("--cause", choices=CAUSES, help="required unless the verdict is pass")
    add.add_argument("--reason", required=True, help="one line: why this verdict")
    add.add_argument("--tokens", type=int)
    add.add_argument("--duration-ms", type=int)
    add.add_argument("--retry-of", help="id of the run this one retries")
    add.set_defaults(func=cmd_add)

    amend = sub.add_parser("amend", help="replace a run's verdict")
    amend.add_argument("id")
    amend.add_argument("--verdict", required=True, choices=VERDICTS)
    amend.add_argument("--cause", choices=CAUSES)
    amend.add_argument("--reason", required=True)
    amend.add_argument("--by", default="user")
    amend.set_defaults(func=cmd_amend)

    recall = sub.add_parser("recall", help="summarize past runs per category and tier")
    recall.add_argument("--category", choices=CATEGORIES)
    recall.add_argument("--window", type=int, default=5, help="recent runs per tier (default 5)")
    recall.add_argument("--notes", type=int, default=5, help="recent misses to list (default 5)")
    recall.set_defaults(func=cmd_recall)

    args = parser.parse_args()
    args.ledger_path = path
    args.models = models
    args.func(args)

