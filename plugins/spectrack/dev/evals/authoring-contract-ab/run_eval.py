#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML"]
# ///
"""Run SpecTrack issue-authoring A/B evals with Codex.

This harness is intentionally ad-hoc and dev-facing. It creates prompts and,
when requested, calls Codex to draft GitHub issue bodies. It never publishes
issues and tells Codex not to modify files or run commands.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

SCRIPT = Path(__file__).resolve()
EVAL_DIR = SCRIPT.parent
PLUGIN_ROOT = EVAL_DIR.parents[2]
REPO_ROOT = PLUGIN_ROOT.parents[1]
CASES_PATH = EVAL_DIR / "cases.yml"
RUBRIC_PATH = EVAL_DIR / "judge-rubric.md"
RESULTS_DIR = EVAL_DIR / "results"
SPECTRACK = PLUGIN_ROOT / "scripts" / "spectrack"

CONDITIONS = ("with_contract", "no_contract")


def load_cases(path: Path = CASES_PATH) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    cases = data.get("cases") if isinstance(data, dict) else None
    if not isinstance(cases, list):
        raise SystemExit(f"expected cases list in {path}")
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("type"):
            raise SystemExit(f"invalid case entry in {path}: {case!r}")
    return cases


def slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")


def mustread_args(case: dict[str, Any]) -> list[str]:
    args = [str(SPECTRACK), "mustread", "--type", str(case["type"]), "--provider", "github"]
    side = case.get("side")
    if side:
        args += ["--side", str(side)]
    target = case.get("target")
    if target:
        args += ["--target", str(target)]
    mode = case.get("mode")
    if mode:
        args += ["--mode", str(mode)]
    return args


def resolve_contract_bundle(case: dict[str, Any]) -> tuple[str, list[Path], str]:
    """Return rendered mustread output, file paths, and concatenated contents."""
    result = subprocess.run(
        mustread_args(case),
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"mustread failed for {case['id']}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    reading_match = re.search(r"<reading[^>]*>\s*(.*?)\s*</reading>", result.stdout, flags=re.DOTALL)
    if reading_match is None:
        raise RuntimeError(f"mustread output missing <reading> block for {case['id']}:\n{result.stdout}")
    rels = re.findall(r"^- (.+)$", reading_match.group(1), flags=re.MULTILINE)
    paths = [PLUGIN_ROOT / "authoring" / rel for rel in rels]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise RuntimeError(f"mustread returned missing paths for {case['id']}: {missing}")
    parts: list[str] = []
    for path in paths:
        rel = path.relative_to(PLUGIN_ROOT / "authoring")
        parts.append(f"## {rel}\n\n{path.read_text(encoding='utf-8').strip()}\n")
    return result.stdout.strip(), paths, "\n".join(parts).strip()


def case_header(case: dict[str, Any]) -> str:
    fields = [
        f"type: {case['type']}",
        "provider: github",
    ]
    for key in ("side", "target", "mode"):
        if case.get(key):
            fields.append(f"{key}: {case[key]}")
    return "\n".join(fields)


def build_prompt(case: dict[str, Any], condition: str) -> str:
    base = f"""You are drafting a GitHub issue body for a SpecTrack workflow artifact.

Rules for this run:
- Output only the issue body Markdown, with no title, no preface, and no fenced wrapper.
- Do not publish the issue.
- Do not modify files.
- Do not run shell commands.
- Required/recommended sections are minimum shape, not a closed schema. If the case needs a precise purpose-specific section, add it.
- Be concrete and use the request details. Avoid generic filler.

Artifact metadata:
{case_header(case)}

User request:
{case['input'].strip()}
""".strip()

    if condition == "no_contract":
        return base + "\n\nDraft the best publish-ready GitHub issue body you can from the information above."

    if condition != "with_contract":
        raise ValueError(f"unknown condition: {condition}")

    mustread_output, _paths, contract_text = resolve_contract_bundle(case)
    return (
        base
        + "\n\nApply these SpecTrack authoring contracts before drafting. They are binding for this run.\n\n"
        + "# Resolver output\n\n"
        + mustread_output
        + "\n\n# Contract files\n\n"
        + contract_text
        + "\n\nDraft the GitHub issue body now."
    )


def run_codex(prompt: str, output_file: Path, *, model: str | None, timeout: int) -> None:
    cmd = [
        "codex",
        "exec",
        "--sandbox",
        "read-only",
        "--output-last-message",
        str(output_file),
    ]
    if model:
        cmd += ["--model", model]
    cmd.append("-")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    log_file = output_file.with_suffix(".codex.log")
    result = subprocess.run(
        cmd,
        input=prompt,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    log_file.write_text(result.stdout, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"codex failed for {output_file} (exit {result.returncode}); see {log_file}")
    if not output_file.is_file() or not output_file.read_text(encoding="utf-8").strip():
        raise RuntimeError(f"codex did not write a draft to {output_file}; see {log_file}")


def timestamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def write_generation_plan(args: argparse.Namespace) -> Path:
    cases = load_cases(args.cases)
    run_dir = RESULTS_DIR / timestamp()
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "cases.yml").write_text(args.cases.read_text(encoding="utf-8"), encoding="utf-8")

    for repeat in range(1, args.repeats + 1):
        for case in cases:
            case_dir = run_dir / f"run-{repeat}" / slug(str(case["id"]))
            case_dir.mkdir(parents=True, exist_ok=True)
            for condition in CONDITIONS:
                prompt = build_prompt(case, condition)
                prompt_file = case_dir / f"{condition}.prompt.md"
                draft_file = case_dir / f"{condition}.draft.md"
                prompt_file.write_text(prompt + "\n", encoding="utf-8")
                if args.run:
                    run_codex(prompt, draft_file, model=args.model, timeout=args.timeout)

    return run_dir


def paired_case_dirs(results: Path) -> list[Path]:
    dirs: list[Path] = []
    for path in sorted(results.glob("run-*/*")):
        if path.is_dir() and all((path / f"{cond}.draft.md").is_file() for cond in CONDITIONS):
            dirs.append(path)
    return dirs


def build_judge_prompt(case_dir: Path, *, seed: int) -> str:
    rng = random.Random(seed + sum(ord(ch) for ch in str(case_dir)))
    order = list(CONDITIONS)
    rng.shuffle(order)
    label_for = {"A": order[0], "B": order[1]}
    rubric = RUBRIC_PATH.read_text(encoding="utf-8").strip()
    draft_a = (case_dir / f"{label_for['A']}.draft.md").read_text(encoding="utf-8").strip()
    draft_b = (case_dir / f"{label_for['B']}.draft.md").read_text(encoding="utf-8").strip()
    key = "\n".join(f"{label}: {cond}" for label, cond in label_for.items())
    (case_dir / "judge-key.txt").write_text(key + "\n", encoding="utf-8")
    return f"""{rubric}

# Case

{case_dir.name}

# Draft A

{draft_a}

# Draft B

{draft_b}
""".strip()


def run_judges(args: argparse.Namespace) -> None:
    case_dirs = paired_case_dirs(args.judge)
    if not case_dirs:
        raise SystemExit(f"no paired drafts found under {args.judge}")
    for case_dir in case_dirs:
        prompt = build_judge_prompt(case_dir, seed=args.seed)
        (case_dir / "judge.prompt.md").write_text(prompt + "\n", encoding="utf-8")
        run_codex(prompt, case_dir / "judge.md", model=args.model, timeout=args.timeout)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--repeats", type=int, default=1)
    parser.add_argument("--model", help="Codex model override; omit to use Codex CLI default")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--run", action="store_true", help="call codex to create drafts")
    parser.add_argument("--prompts-only", action="store_true", help="write prompts without calling codex")
    parser.add_argument("--judge", type=Path, help="judge an existing results directory")
    parser.add_argument("--seed", type=int, default=1729, help="A/B randomization seed for judging")
    args = parser.parse_args(argv)
    if args.repeats < 1:
        parser.error("--repeats must be >= 1")
    if args.judge and (args.run or args.prompts_only):
        parser.error("--judge cannot be combined with --run/--prompts-only")
    if not args.judge and not (args.run or args.prompts_only):
        parser.error("choose --prompts-only, --run, or --judge RESULTS_DIR")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.judge:
        run_judges(args)
        print(f"judged drafts under {args.judge}")
        return 0
    run_dir = write_generation_plan(args)
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
