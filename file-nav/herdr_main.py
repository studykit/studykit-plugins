#!/usr/bin/env -S uv run --no-config --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["rich==15.0.0", "pygments>=2.19,<3"]
# ///
"""Translate Herdr invocation context into explicit navigator inputs."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import tomllib

from popup_size import PopupSize, load_size, save_size
from layout_mode import MODES, load_layout, save_layout
from ls_colors import directory_style
from view_state import load_view, save_view


def theme_config(env):
    directory = Path(env.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "herdr"
    path = Path(env.get("HERDR_CONFIG_PATH") or directory / "config.toml")
    try:
        with path.open("rb") as stream:
            config = tomllib.load(stream)
        return {key: config[key] for key in ("theme", "ui") if key in config}
    except (OSError, ValueError):
        return {}


def call(binary: str, *args: str) -> dict:
    result = subprocess.run([binary, *args], capture_output=True, text=True, timeout=15)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Herdr command failed")
    value = json.loads(result.stdout)
    if value.get("error"):
        raise RuntimeError(str(value["error"]))
    return value["result"]


def source(env: dict, binary: str) -> tuple[str, Path]:
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    if not isinstance(context, dict):
        raise ValueError("Herdr plugin context must be an object")
    pane_id = env.get("FILE_NAV_SOURCE_PANE") or context.get("focused_pane_id") or env.get("HERDR_PANE_ID")
    if not pane_id:
        raise ValueError("No focused pane was provided by Herdr")
    pane = call(binary, "pane", "get", pane_id)["pane"]
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not cwd or not Path(cwd).is_absolute() or not Path(cwd).is_dir():
        raise ValueError("The source pane's working directory is unavailable")
    return pane_id, Path(cwd).resolve()


def open_panel(env, binary, pane_id, root, changes, size, resume=None, placement="popup"):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    # Herdr 0.9.1 needs a manifest entrypoint for popup placement.
    args = ["plugin", "pane", "open", "--plugin", env["HERDR_PLUGIN_ID"],
            "--entrypoint", "popup" if placement == "popup" else "navigator", "--cwd", str(root),
            "--env", f"FILE_NAV_SOURCE_PANE={pane_id}",
            "--env", f"FILE_NAV_CHANGES={int(changes)}",
            "--env", f"FILE_NAV_WIDTH={size.width}",
            "--env", f"FILE_NAV_HEIGHT={size.height}", "--focus"]
    if placement == "popup":
        args.extend(["--width", f"{size.width}%", "--height", f"{size.height}%"])
    if resume:
        args.extend(["--env", f"FILE_NAV_RESUME={resume}"])
    return call(binary, *args)


def resume_path(env, raw):
    path = Path(raw).resolve()
    directory = Path(env["HERDR_PLUGIN_STATE_DIR"]).resolve()
    if path.parent != directory or not path.name.startswith("resize-") or path.suffix != ".json":
        raise ValueError("Invalid navigator resume file")
    return path


def current_layout(env):
    return "overlay" if env.get("HERDR_PANE_ID") else "popup"


def change_layout(env, pane_id, placement, size, view):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    prepare_resize(env, pane_id, size, view, placement)
    return True


def prepare_resize(env, pane_id, size, view, placement="popup"):
    directory = Path(env["HERDR_PLUGIN_STATE_DIR"])
    directory.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="resize-", suffix=".json", dir=directory)
    path = Path(name)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump({"pane_id": pane_id, "size": size.as_dict(), "view": view,
                       "placement": placement, "previous_pane": env.get("HERDR_PANE_ID"),
                       "previous_pid": os.getpid()}, stream)
        # The navigator exits after this returns. The helper waits for its surface
        # to close before opening the replacement with the saved view.
        helper_env = dict(env)
        # `pane current` otherwise resolves the now-closed navigator from its env.
        helper_env.pop("HERDR_PANE_ID", None)
        with (directory / "resize.log").open("ab") as log:
            subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "reopen", str(path)],
                             env=helper_env, stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                             start_new_session=True, close_fds=True)
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def reopen(env, raw):
    path = resume_path(env, raw)
    payload = json.loads(path.read_text())
    size = PopupSize(**payload["size"])
    view, pane_id = payload["view"], payload["pane_id"]
    placement = payload.get("placement", "popup")
    previous_pane = payload.get("previous_pane")
    binary = env.get("HERDR_BIN_PATH") or "herdr"
    deadline = time.monotonic() + 5
    try:
        previous_pid = payload.get("previous_pid")
        while previous_pid:
            try:
                os.kill(previous_pid, 0)
            except ProcessLookupError:
                break
            if time.monotonic() >= deadline:
                raise RuntimeError("The previous navigator process did not exit")
            time.sleep(0.05)
        while True:
            if previous_pane:
                try:
                    call(binary, "pane", "get", previous_pane)
                except RuntimeError as error:
                    if "pane_not_found" not in str(error):
                        raise
                    previous_pane = None
                else:
                    if time.monotonic() >= deadline:
                        raise RuntimeError("The previous navigator pane did not close")
                    time.sleep(0.05)
                    continue
            current = call(binary, "pane", "current")["pane"]
            if current["pane_id"] != pane_id:
                raise RuntimeError("Layout change cancelled because focus moved to another source pane")
            try:
                open_panel(env, binary, pane_id, Path(view["root"]), view["changes"], size, path,
                           placement=placement)
                break
            except RuntimeError as error:
                if "ui_busy" not in str(error) or time.monotonic() >= deadline:
                    raise
                time.sleep(0.05)
        if env.get("HERDR_PLUGIN_CONFIG_DIR"):
            save_size(Path(env["HERDR_PLUGIN_CONFIG_DIR"]), size)
            save_layout(Path(env["HERDR_PLUGIN_CONFIG_DIR"]), placement)
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    return 0


def main(env: dict, operation: str) -> int:
    if env.get("HERDR_ENV") != "1":
        raise ValueError("Run File Navigator from inside Herdr")
    binary = env.get("HERDR_BIN_PATH") or "herdr"
    pane_id, root = source(env, binary)
    if operation in ("browse", "changes"):
        config_dir = Path(env["HERDR_PLUGIN_CONFIG_DIR"]) if env.get("HERDR_PLUGIN_CONFIG_DIR") else None
        open_panel(env, binary, pane_id, root, operation == "changes", load_size(config_dir),
                   placement=load_layout(config_dir))
    elif operation == "panel":
        import curses
        from ui import Navigator
        state_dir = Path(env["HERDR_PLUGIN_STATE_DIR"]) if env.get("HERDR_PLUGIN_STATE_DIR") else None
        restored = None
        if env.get("FILE_NAV_RESUME"):
            path = resume_path(env, env["FILE_NAV_RESUME"])
            restored = json.loads(path.read_text())["view"]
            root = Path(restored["root"]).resolve(strict=True)
            path.unlink()
        else:
            restored = load_view(state_dir, root)
            # An explicit changes action must still open the changes view.
            if restored is not None and env.get("FILE_NAV_CHANGES") == "1":
                restored["changes"] = True
        size = PopupSize(int(env.get("FILE_NAV_WIDTH", 96)), int(env.get("FILE_NAV_HEIGHT", 92)))
        on_resize = None
        if env.get("HERDR_PLUGIN_STATE_DIR") and env.get("HERDR_PLUGIN_CONFIG_DIR"):
            on_resize = lambda chosen, view: prepare_resize(env, pane_id, chosen, view)
        navigator = Navigator(root, pane_id, env.get("FILE_NAV_CHANGES") == "1",
                              env.get("VISUAL") or env.get("EDITOR") or "", size, on_resize,
                              theme_loader=lambda: theme_config(env),
                              folder_style=directory_style(env, sys.platform),
                              on_state=(lambda view: save_view(state_dir, view)) if state_dir else None,
                              layout_loader=lambda: current_layout(env),
                              on_layout=lambda placement, chosen, view:
                                  change_layout(env, pane_id, placement, chosen, view))
        if restored is not None:
            navigator.restore_state(restored)
            if env.get("FILE_NAV_RESUME"):
                navigator.message = "Restored view after layout change"
        try:
            curses.wrapper(navigator.run)
        finally:
            navigator.checkpoint()
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return 0


if __name__ == "__main__":
    try:
        operation = sys.argv[1] if len(sys.argv) > 1 else "browse"
        env = dict(os.environ)
        if operation == "reopen" and env.get("HERDR_ENV") == "1":
            sys.exit(reopen(env, sys.argv[2]))
        sys.exit(main(env, operation))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"File Navigator: {error}", file=sys.stderr)
        sys.exit(1)
