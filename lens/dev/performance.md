# Startup performance

## Finding

The September 2026 investigation found redundant filesystem work on opening and
reopening, especially with ignored files visible. The measured bottleneck did
not justify replacing Python with Go or Rust.

The previous filesystem scan constructed a `Path` and called `relative_to` for
every file and directory. On a 50,000-entry local view, profiling attributed
about two thirds of scan time to that repeated ancestry calculation. Restoring
an ignored-files view also performed a default Git scan before rescanning with
the saved visibility setting.

Version 0.16.1 computes relative prefixes once per directory, uses string paths
in the breadth-first queue, and reuses the walker's existing directory-symlink
filtering. Startup applies the saved visibility setting before its first scan.
It still reads the current filesystem and preview content on every open; there
is no persistent file-index or content cache to become stale.

## Measurements

Measured on macOS arm64 with Herdr 0.9.1, uv-managed CPython 3.13.15, Rich 15.0.0,
and cached dependencies. These are local measurements, not cross-platform
latency guarantees. Baseline: 0.16.0; changed version: 0.16.1.

The controlled fixture contained 36,002 files and 12,001 directories in a Git
repository. Almost all entries were under an ignored `cache/` directory.
The saved view enabled ignored files and previewed a small `README.md`.

| Measurement | Before | After |
| --- | ---: | ---: |
| Real shortcut to first rendered focus badge, median of five opens | 1,220.8 ms | 654.8 ms |
| Scan and saved-view restoration, median of five fresh processes | 1,003.1 ms | 408.1 ms |
| Markdown preview preparation, median of five fresh processes | 23.0 ms | 23.1 ms |
| Full component benchmark process, including harness/interpreter startup | 1,072.9 ms | 481.5 ms |

The real shortcut test used separate named Herdr sessions, isolated XDG
directories, the linked working tree or an untouched baseline copy, a 180×50
PTY client, and `prefix+t`. Each open was followed by Ctrl+C before reopening.
The baseline's dependency bootstrap was warmed before the final comparison.
The before and after host runs were sequential. Timing began when the prefix
and shortcut bytes were written to the client and stopped when its output
contained `FOCUS: FILES` (the header badge of that version; the focus now shows in the mode line as ` FILES `); it includes host dispatch, action/panel launches,
filesystem scanning, restoration, preview rendering, and client delivery.
It does not measure physical monitor presentation latency.

Final host samples, in milliseconds:

- Before: 1210.6, 1216.6, 1220.8, 1230.9, 1252.8.
- After: 648.1, 657.7, 640.9, 668.1, 654.8.

The saved ignored-files setting and Markdown preview survived all reopenings.
A separate small one-file project opened in 157–182 ms after the change.
Component timing on this checkout put Python startup at about 30 ms, the uv
script launch at about 53 ms, and the three Git probes together at about 35 ms.
Those costs remain, but were much smaller than the large-view scan.

## Reproduce component measurements

From the repository root:

```sh
uv run --no-config --no-project --with rich==15.0.0 python \
  lens/dev/benchmark_startup.py /absolute/path/to/project \
  --ignored --preview README.md
```

Omit `--ignored` or `--preview` to measure other views. `--plugin-dir` selects a
separate plugin checkout for comparisons. The harness starts a fresh process
for each sample and prints phase timings and entry counts as JSON. It does not
save navigator state. Its process timing includes harness overhead and does
not include Herdr or terminal drawing; it cannot replace the live-host test.

To construct the controlled fixture, run this outside the repository and use
the printed directory as the benchmark root:

```python
from pathlib import Path
import subprocess
import tempfile

root = Path(tempfile.mkdtemp(prefix="lens-benchmark-"))
subprocess.run(["git", "init", "-q", str(root)], check=True)
(root / ".gitignore").write_text("cache/\n")
(root / "README.md").write_text("# Preview fixture\n\nHello navigator.\n")
for package in range(3000):
    directory = root / "cache" / f"pkg{package:04d}" / "lib" / "nested" / "sources"
    directory.mkdir(parents=True)
    for number in range(12):
        (directory / f"file{number:02d}.txt").touch()
print(root)
```

For a live comparison, follow [the host test setup](testing.md), use a clean
named session and a PTY client, dismiss first-run onboarding, and register the
checkout under test. Enable ignored files and preview the fixture README, then
close with Ctrl+Q to save the view before measuring repeated shortcut opens.
Keep the same terminal dimensions and fixture for both versions. Do not run
other benchmarks concurrently with a timed host run.

## Scope and validation

All 187 automated tests passed, including new coverage for a single startup
scan with saved ignored-file visibility, fresh files appearing on reopening,
and invalid saved roots falling back to the default view. Existing checks cover
traversal limits, breadth-first ordering, symlinks, nested repositories, root
changes, and resume-state precedence. Live verification covered Popup opens
and reopenings on macOS. Linux and overlay timing were not measured.

Large Git repositories, network filesystems, and large Markdown previews can
have different bottlenecks. Measure the affected root before considering a
language rewrite; changing language alone would not remove Git subprocess
latency or unnecessary scans.

Official references checked during the investigation:

- [Herdr CLI reference](https://herdr.dev/docs/cli-reference/#plugins)
- [Herdr 0.9.1 pane launch implementation](https://github.com/herdrdev/herdr/blob/v0.9.1/src/app/api/plugins/panes.rs)
- [uv script execution](https://docs.astral.sh/uv/guides/scripts/)
- [Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference)
- [Codex plugins](https://developers.openai.com/codex/plugins)

Herdr continues to own the UI; no Claude Code or Codex registration changed.

## Deferred Git status in 0.17.0

The interactive adapter now requests file listing without `git status`.
Repository detection and `git ls-files` still run before the first frame so
tracked, untracked, and ignored-file listing semantics remain consistent.
After the first complete curses draw, the UI starts one daemon worker for Git
status. The UI thread checks completion without waiting, then applies change
indicators and any staged deletions missing from `ls-files`. The input timeout
is 50 ms while a query is in flight, returning to 250 ms afterward.

The changes-only view shows a loading state before its filtered list is ready.
Pending saved selections survive checkpoints and immediate closure; after
completion, selection and scroll are restored unless navigation has superseded
them. Status errors are distinct from a clean repository and leave browsing
usable. Ctrl+R retries. Root changes and refreshes invalidate results by index
identity, including refreshes of the same root. At most one status worker runs
at once; it never calls curses, and closing the navigator does not join it.
The existing Git subprocess timeout continues to bound queries.

A separate macOS Herdr 0.9.1 session with isolated configuration and a small
throwaway Git project injected a **1.5-second delay only into `git status`**.
Real client key input verified:

- Browse displayed its first focus badge at 687 ms, accepted file selection and
  displayed the preview before status completed, and showed change indicators
  at 2,234 ms. This first open included startup overhead.
- The changes action displayed its first frame at 268 ms and populated status
  at 1,859 ms.
- Closing while a later query was pending returned without waiting for status.

These delayed-command checks demonstrate ordering and responsiveness, not an
ordinary-repository speedup estimate. The earlier 0.16.0/0.16.1 timing table is
unchanged. The current component benchmark requests deferred status when the
selected checkout supports it; `status_pending` in each sample makes clear
that its process timing excludes the later background query. It does not
start a worker because there is no terminal frame in the component benchmark.

Final automated validation: 199 tests passed. Added coverage exercises first-draw
ordering, interactive input and closure during a blocked query, stale results
after refresh/root changes, error recovery, staged deletions, pending saved
selection, and the entry limit when merging late status results.
