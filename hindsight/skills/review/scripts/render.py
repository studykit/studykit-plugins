#!/usr/bin/env python3
"""hindsight renderer — deterministic, no LLM.

Claude Code-specific: reads Claude Code session transcripts from
`~/.claude/projects/`. This script is a Claude-only adapter entrypoint — it
resolves host paths from `HOME` and writes to a user-level data directory
outside the plugin install dir.

Turns raw Claude Code transcripts into clean, LLM-readable conversation
chunks. It does NOT judge anything — that is the job of the two model
stages the skill drives, across two tracks (agent mistakes + how the user
uses the LLM):

  Stage 1 (cheap model) scans each chunk ONCE and returns both the
           *locations* of suspected agent mistakes and short *observations*
           about how the user works/communicates.
  Stage 2 (top model) re-reads the flagged spots in these same chunk files,
           confirms genuine mistakes → findings/, and clusters the
           observations into a user-communication profile → profile/.

Incremental via a ledger watermark: only turns appended since the last run
are rendered (with a little prior context for readability).

Layout:
  ~/.claude/projects/<encoded-cwd>/<session>.jsonl  # input transcripts
  ~/.claude/hindsight/ledger.json                   # per-transcript watermark
  ~/.claude/hindsight/render/<session>__cNN.md      # readable chunks (Stage 1 input)
  ~/.claude/hindsight/render/run-<stamp>.json        # manifest of this run's chunks
  ~/.claude/hindsight/findings/                      # Stage 2 output (mistake patterns)
  ~/.claude/hindsight/profile/                       # Stage 2 output (usage patterns)
  ~/.claude/hindsight/runs/                          # Stage 2 output (run reports)
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
PROJECTS_ROOT = HOME / ".claude" / "projects"
STATE_ROOT = HOME / ".claude" / "hindsight"
LEDGER_PATH = STATE_ROOT / "ledger.json"
RENDER_DIR = STATE_ROOT / "render"

CHUNK_CHARS = 24000   # ~6k tokens of readable text per Stage-1 subagent
LEAD_CONTEXT = 6      # prior turns kept for readability when a session resumes
TEXT_CAP = 600
TOOL_CAP = 400

INJECTED = ("<system-reminder", "<command-name>", "<command-message>",
            "<command-args", "<local-command", "<bash-input", "<bash-stdout",
            "<bash-stderr", "Caveat:")


def now_stamp() -> str:
  return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def truncate(s: str, cap: int) -> str:
  s = " ".join(s.split())
  return s if len(s) <= cap else s[: cap - 1] + "…"


def real_user_text(blocks) -> str:
  if isinstance(blocks, str):
    text = blocks
  else:
    parts = [b.get("text", "") for b in blocks
             if isinstance(b, dict) and b.get("type") == "text"]
    text = "\n".join(parts)
  text = text.strip()
  if not text or any(text.lstrip().startswith(m) for m in INJECTED):
    return ""
  return text


def tool_result_blocks(blocks):
  if not isinstance(blocks, list):
    return []
  out = []
  for b in blocks:
    if isinstance(b, dict) and b.get("type") == "tool_result":
      content = b.get("content", "")
      if isinstance(content, list):
        content = " ".join(c.get("text", "") for c in content
                           if isinstance(c, dict))
      out.append((bool(b.get("is_error")), str(content)))
  return out


def assistant_summary(blocks):
  texts, tools = [], []
  if isinstance(blocks, list):
    for b in blocks:
      if not isinstance(b, dict):
        continue
      if b.get("type") == "text":
        texts.append(b.get("text", ""))
      elif b.get("type") == "tool_use":
        inp = b.get("input", {})
        hint = inp.get("file_path") or inp.get("command") or inp.get("pattern") or ""
        tools.append(f"{b.get('name', '?')}({truncate(str(hint), 90)})")
  return "\n".join(texts).strip(), tools


def parse_events(path: Path):
  """Linear conversational events with source line index; noise stripped."""
  events = []
  total = 0
  with path.open(encoding="utf-8", errors="replace") as fh:
    for idx, line in enumerate(fh):
      total = idx + 1
      line = line.strip()
      if not line:
        continue
      try:
        rec = json.loads(line)
      except json.JSONDecodeError:
        continue
      if rec.get("isSidechain") or rec.get("isMeta"):
        continue
      typ = rec.get("type")
      msg = rec.get("message") or {}
      ts = rec.get("timestamp", "")
      if typ == "user":
        blocks = msg.get("content", "")
        for is_err, content in tool_result_blocks(blocks):
          events.append({"i": idx, "role": "tool", "ts": ts,
                         "is_error": is_err, "text": truncate(content, TOOL_CAP)})
        utext = real_user_text(blocks)
        if utext:
          events.append({"i": idx, "role": "user", "ts": ts,
                         "text": truncate(utext, TEXT_CAP)})
      elif typ == "assistant":
        text, tools = assistant_summary(msg.get("content", ""))
        if text or tools:
          events.append({"i": idx, "role": "assistant", "ts": ts,
                         "text": truncate(text, TEXT_CAP), "tools": tools})
  return events, total


def render_event(ev) -> str:
  ts = ev.get("ts", "")
  role = ev["role"]
  if role == "user":
    return f"[{ts}] USER: {ev['text']}"
  if role == "assistant":
    head = f"[{ts}] ASSISTANT: {ev['text']}".rstrip()
    lines = [head]
    for t in ev.get("tools", []):
      lines.append(f"    ⤷ {t}")
    return "\n".join(lines)
  tag = "RESULT(error)" if ev.get("is_error") else "RESULT"
  return f"[{ts}] {tag}: {ev['text']}"


def project_meta(path: Path):
  with path.open(encoding="utf-8", errors="replace") as fh:
    for line in fh:
      try:
        rec = json.loads(line)
      except json.JSONDecodeError:
        continue
      if rec.get("cwd"):
        return rec.get("cwd", ""), rec.get("gitBranch", ""), rec.get("sessionId", "")
  return "", "", ""


def chunk_session(seq):
  """Split a rendered event sequence into char-bounded chunks."""
  chunks, cur, size = [], [], 0
  for ev in seq:
    block = render_event(ev)
    if cur and size + len(block) > CHUNK_CHARS:
      chunks.append(cur)
      cur, size = [], 0
    cur.append((ev, block))
    size += len(block) + 1
  if cur:
    chunks.append(cur)
  return chunks


def main() -> None:
  ap = argparse.ArgumentParser(description="Render transcripts into readable chunks.")
  ap.add_argument("--project", help="only transcripts whose cwd/path contains this substring")
  ap.add_argument("--since", help="only transcript files modified on/after YYYY-MM-DD")
  args = ap.parse_args()

  since_ts = None
  if args.since:
    since_ts = datetime.strptime(args.since, "%Y-%m-%d").replace(
      tzinfo=timezone.utc).timestamp()

  RENDER_DIR.mkdir(parents=True, exist_ok=True)
  (STATE_ROOT / "findings").mkdir(parents=True, exist_ok=True)
  (STATE_ROOT / "profile").mkdir(parents=True, exist_ok=True)
  (STATE_ROOT / "skills-candidates").mkdir(parents=True, exist_ok=True)
  (STATE_ROOT / "runs").mkdir(parents=True, exist_ok=True)

  ledger = {}
  if LEDGER_PATH.exists():
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
  transcripts = ledger.setdefault("transcripts", {})

  files = sorted(PROJECTS_ROOT.glob("*/*.jsonl"))
  run_stamp = now_stamp()
  manifest = {"run": run_stamp, "chunks": []}
  scanned = new_lines = n_chunks = touched = 0

  for path in files:
    if since_ts and path.stat().st_mtime < since_ts:
      continue
    if args.project and args.project not in str(path):
      continue
    scanned += 1
    key = str(path)
    rec = transcripts.get(key, {})
    watermark = rec.get("lines", 0)

    events, total = parse_events(path)
    if total < watermark:           # file rewritten/compacted
      watermark = 0
    new = [n for n, e in enumerate(events) if e["i"] >= watermark]
    if not new:
      transcripts[key] = {"lines": total, "last_rendered": run_stamp}
      continue

    new_lines += max(0, total - watermark)
    start = new[0]
    ctx = events[max(0, start - LEAD_CONTEXT):start]
    seq = list(ctx)
    if ctx:
      seq.append({"role": "user", "ts": "", "text": "──── new since last run ────"})
    seq.extend(events[start:])

    cwd, branch, session = project_meta(path)
    if args.project and args.project not in cwd and args.project not in key:
      transcripts[key] = {"lines": total, "last_rendered": run_stamp}
      continue

    for ci, chunk in enumerate(chunk_session(seq)):
      body = "\n".join(block for _, block in chunk)
      ts_list = [ev.get("ts") for ev, _ in chunk if ev.get("ts")]
      header = (
        f"# transcript: {path.name}\n"
        f"# project: {cwd}\n# branch: {branch}\n# session: {session}\n"
        f"# chunk: {ci + 1}\n"
        f"# Locate mistakes by the [timestamp] prefix on each line.\n\n"
      )
      cfile = RENDER_DIR / f"{session}__c{ci:02d}.md"
      cfile.write_text(header + body + "\n", encoding="utf-8")
      manifest["chunks"].append({
        "file": str(cfile),
        "transcript": path.name,
        "transcript_path": key,
        "project": cwd,
        "branch": branch,
        "session": session,
        "ts_start": ts_list[0] if ts_list else "",
        "ts_end": ts_list[-1] if ts_list else "",
      })
      n_chunks += 1
    touched += 1
    transcripts[key] = {"lines": total, "last_rendered": run_stamp}

  LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2),
                         encoding="utf-8")

  if n_chunks == 0:
    print(f"scanned {scanned} transcripts, {new_lines} new lines — "
          f"nothing new to render.")
    print("MANIFEST: none")
    return

  manifest_path = RENDER_DIR / f"run-{run_stamp}.json"
  manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                           encoding="utf-8")
  print(f"scanned {scanned} transcripts, {new_lines} new lines.")
  print(f"rendered {n_chunks} chunk(s) across {touched} session(s).")
  print(f"MANIFEST: {manifest_path}")


if __name__ == "__main__":
  main()
