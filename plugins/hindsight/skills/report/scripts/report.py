#!/usr/bin/env python3
"""hindsight report — deterministic, no LLM.

Claude Code-specific: reads the accumulated hindsight state from
`~/.claude/hindsight/` and prints a single, ranked Markdown report. It does
NOT analyze transcripts — that is the job of the `review` skill, which fills
`findings/` and `profile/`. This script only aggregates and presents what is
already there, so it is cheap, deterministic, and runs on demand without
re-scanning history.

Two tracks, mirroring the `review` skill:
  findings/<slug>.md  — recurring agent mistakes (track 1)
  profile/<slug>.md   — how the user works and communicates (track 2)

Layout it reads:
  ~/.claude/hindsight/findings/<slug>.md
  ~/.claude/hindsight/profile/<slug>.md
  ~/.claude/hindsight/runs/run-<stamp>.md   # counted for context only

Output is Markdown on stdout (optionally also written to --out). The skill
relays it to the user verbatim.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
STATE_ROOT = HOME / ".claude" / "hindsight"
FINDINGS_DIR = STATE_ROOT / "findings"
PROFILE_DIR = STATE_ROOT / "profile"
RUNS_DIR = STATE_ROOT / "runs"

# Body sections surfaced per track (heading -> label in the report).
FINDING_SECTIONS = [("What goes wrong", "What goes wrong"),
                    ("Prevention hypothesis", "Prevent")]
PROFILE_SECTIONS = [("Observation", "Observation"),
                    ("How the LLM should adapt", "Adapt")]

TRIM_CAP = 420  # chars per surfaced section in default mode


def now_iso() -> str:
  return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_doc(path: Path) -> tuple[dict[str, str], str]:
  """Split a `--- frontmatter ---` Markdown file into (meta, body)."""
  text = path.read_text(encoding="utf-8")
  meta: dict[str, str] = {}
  body = text
  if text.lstrip().startswith("---"):
    parts = text.split("---", 2)
    if len(parts) >= 3:
      front, body = parts[1], parts[2]
      for line in front.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
          continue
        key, _, value = line.partition(":")
        value = value.strip()
        # Drop a trailing inline comment (" # ..."), keep mid-value '#'.
        if " #" in value:
          value = value.split(" #", 1)[0].strip()
        meta[key.strip()] = value.strip().strip("'\"")
  return meta, body


def sections(body: str) -> dict[str, str]:
  """Map each `## Heading` to its text block."""
  out: dict[str, str] = {}
  current: str | None = None
  buf: list[str] = []
  for line in body.splitlines():
    if line.startswith("## "):
      if current is not None:
        out[current] = "\n".join(buf).strip()
      current = line[3:].strip()
      buf = []
    elif current is not None:
      buf.append(line)
  if current is not None:
    out[current] = "\n".join(buf).strip()
  return out


def first_para(text: str, cap: int) -> str:
  """First paragraph, whitespace-collapsed, capped with an ellipsis."""
  para = text.split("\n\n", 1)[0].strip()
  para = " ".join(para.split())
  if len(para) > cap:
    para = para[:cap].rstrip() + "…"
  return para


def to_int(value: str) -> int:
  try:
    return int(value)
  except (TypeError, ValueError):
    return 0


def load(directory: Path) -> list[tuple[dict[str, str], str]]:
  if not directory.is_dir():
    return []
  docs = []
  for path in sorted(directory.glob("*.md")):
    meta, body = parse_doc(path)
    meta.setdefault("slug", path.stem)
    docs.append((meta, body))
  return docs


def span(meta: dict[str, str]) -> str:
  first, last = meta.get("first_seen", ""), meta.get("last_seen", "")
  if first and last and first != last:
    return f"{first}→{last}"
  return last or first or ""


def occ_label(n: int) -> str:
  return f"{n} occurrence" + ("" if n == 1 else "s")


def render_finding(meta: dict[str, str], body: str, mode: str) -> list[str]:
  status = meta.get("status", "open")
  occ = to_int(meta.get("occurrences", "0"))
  lines = [f"### [{status}] {meta.get('pattern', meta['slug'])}"]
  bits = [f"`{meta['slug']}`", meta.get("category", "?"), occ_label(occ)]
  if span(meta):
    bits.append(span(meta))
  lines.append(" · ".join(bits))
  if mode == "brief":
    return lines
  if mode == "full":
    lines.append("")
    lines.append(body.strip())
    return lines
  secs = sections(body)
  for heading, label in FINDING_SECTIONS:
    if secs.get(heading):
      lines.append(f"- **{label}:** {first_para(secs[heading], TRIM_CAP)}")
  return lines


def render_profile(meta: dict[str, str], body: str, mode: str) -> list[str]:
  occ = to_int(meta.get("occurrences", "0"))
  lines = [f"### {meta.get('pattern', meta['slug'])}"]
  bits = [f"`{meta['slug']}`", meta.get("kind", "?"), occ_label(occ)]
  if span(meta):
    bits.append(span(meta))
  lines.append(" · ".join(bits))
  if mode == "brief":
    return lines
  if mode == "full":
    lines.append("")
    lines.append(body.strip())
    return lines
  secs = sections(body)
  for heading, label in PROFILE_SECTIONS:
    if secs.get(heading):
      lines.append(f"- **{label}:** {first_para(secs[heading], TRIM_CAP)}")
  return lines


def build_report(track: str, status_filter: str, mode: str) -> str:
  findings = load(FINDINGS_DIR) if track in ("findings", "both") else []
  profile = load(PROFILE_DIR) if track in ("profile", "both") else []
  runs = sorted(p.name for p in RUNS_DIR.glob("run-*.md")) if RUNS_DIR.is_dir() else []

  if status_filter != "all":
    findings = [(m, b) for m, b in findings
                if m.get("status", "open") == status_filter]

  # Findings: open first, then by occurrences desc, then slug.
  findings.sort(key=lambda d: (d[0].get("status", "open") != "open",
                               -to_int(d[0].get("occurrences", "0")),
                               d[0]["slug"]))
  # Profile: by occurrences desc, then slug.
  profile.sort(key=lambda d: (-to_int(d[0].get("occurrences", "0")), d[0]["slug"]))

  out: list[str] = ["# Hindsight Report",
                    f"_generated {now_iso()} · source: {STATE_ROOT}_", ""]

  summary = []
  if track in ("findings", "both"):
    n_open = sum(1 for m, _ in findings if m.get("status", "open") == "open")
    n_other = len(findings) - n_open
    summary.append(f"**Agent mistakes:** {len(findings)} "
                   f"({n_open} open, {n_other} mitigated/other)")
  if track in ("profile", "both"):
    summary.append(f"**Profile:** {len(profile)} patterns")
  latest = runs[-1].removeprefix("run-").removesuffix(".md") if runs else "none"
  summary.append(f"**Runs:** {len(runs)} (latest {latest})")
  out.append(" · ".join(summary))

  if track in ("findings", "both"):
    out += ["", "---", "", "## Agent mistakes — what to keep preventing"]
    if findings:
      for meta, body in findings:
        out.append("")
        out += render_finding(meta, body, mode)
    else:
      out.append("")
      out.append("_No findings recorded yet._")

  if track in ("profile", "both"):
    out += ["", "---", "", "## How you work — profile"]
    if profile:
      for meta, body in profile:
        out.append("")
        out += render_profile(meta, body, mode)
    else:
      out.append("")
      out.append("_No profile patterns recorded yet._")

  return "\n".join(out).rstrip() + "\n"


def main() -> int:
  ap = argparse.ArgumentParser(description="Render the accumulated hindsight "
                               "findings and profile as a Markdown report.")
  ap.add_argument("--track", choices=["findings", "profile", "both"],
                  default="both", help="which track(s) to include")
  ap.add_argument("--status", choices=["open", "mitigated", "all"],
                  default="all", help="filter findings by status")
  group = ap.add_mutually_exclusive_group()
  group.add_argument("--brief", action="store_true",
                     help="ranked headings only, no body excerpts")
  group.add_argument("--full", action="store_true",
                     help="include the full body of every pattern")
  ap.add_argument("--out", type=Path, default=None,
                  help="also write the report to this file")
  args = ap.parse_args()

  if not STATE_ROOT.is_dir():
    print(f"No hindsight state at {STATE_ROOT}. "
          "Run /hindsight:review first to populate it.", file=sys.stderr)
    return 1

  mode = "brief" if args.brief else "full" if args.full else "default"
  report = build_report(args.track, args.status, mode)

  if args.out is not None:
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report, encoding="utf-8")

  sys.stdout.write(report)
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
