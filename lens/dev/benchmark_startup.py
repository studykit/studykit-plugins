"""Measure fresh-process startup without writing project or navigator state."""
from __future__ import annotations

import argparse
import inspect
import json
from pathlib import Path
import statistics
import subprocess
import sys
import time


def worker(args):
    started = time.perf_counter()
    sys.path.insert(0, str(args.plugin_dir.resolve()))
    from ui import Navigator

    imported = time.perf_counter()
    root = args.root.resolve(strict=True)
    state = {"root": str(root), "include_ignored": args.ignored, "active": args.preview}
    # Allow the same harness to compare checkouts predating initial_state.
    parameters = inspect.signature(Navigator).parameters
    options = {"defer_status": True} if "defer_status" in parameters else {}
    if "initial_state" in parameters:
        nav = Navigator(root, "benchmark", False, "", initial_state=state, **options)
    else:
        nav = Navigator(root, "benchmark", False, "")
        nav.restore_state(state)
    restored = time.perf_counter()
    nav.prepare_preview(args.width)
    rendered = time.perf_counter()
    if nav.index is None:
        raise RuntimeError(nav.message)
    if nav.include_ignored != args.ignored or (args.preview and not nav.previewable):
        raise RuntimeError(f"Could not restore requested benchmark view: {nav.message}")
    return {"import_ms": (imported - started) * 1000,
            "scan_restore_ms": (restored - imported) * 1000,
            "preview_ms": (rendered - restored) * 1000,
            "files": len(nav.index.files), "directories": len(nav.index.directories),
            "status_pending": getattr(nav.index, "status_pending", False)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--plugin-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ignored", action="store_true")
    parser.add_argument("--preview", default="", help="File path relative to root")
    parser.add_argument("--width", type=int, default=110)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.repeat < 1 or args.width < 1:
        parser.error("repeat and width must be positive")
    if args.worker:
        print(json.dumps(worker(args)))
        return
    samples = []
    for _ in range(args.repeat):
        started = time.perf_counter()
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                                 *sys.argv[1:], "--worker"],
                                capture_output=True, text=True, check=True)
        elapsed = (time.perf_counter() - started) * 1000
        sample = json.loads(result.stdout)
        sample["process_ms"] = elapsed
        samples.append(sample)
    medians = {key: round(statistics.median(row[key] for row in samples), 1)
               for key in samples[0] if key != "status_pending"}
    print(json.dumps({"median": medians, "samples": samples}, indent=2))


if __name__ == "__main__":
    main()
