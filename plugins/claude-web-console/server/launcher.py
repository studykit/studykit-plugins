#!/usr/bin/env python3
"""Start the claude-web-console: optional local PlantUML engine + web server,
then open the viewer in a browser.

PlantUML is optional. When java or a plantuml.jar is missing, the launcher
skips it and the viewer shows an "engine unavailable" placeholder for diagrams;
Markdown and math still render.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import threading
import webbrowser
from pathlib import Path

import server  # sibling module (same directory is on sys.path[0])

REPO_JAR_GLOB = "plugins/plantuml/skills/compose/scripts/plantuml*.jar"


def _plantuml_port() -> int:
    try:
        return int(os.environ.get("CLAUDE_WEB_CONSOLE_PLANTUML_PORT", ""))
    except ValueError:
        return 8478


def _find_jar() -> Path | None:
    env = os.environ.get("CLAUDE_WEB_CONSOLE_PLANTUML_JAR", "")
    if env and Path(env).is_file():
        return Path(env)
    here = Path(__file__).resolve()
    for base in [here.parent, *here.parents]:
        matches = sorted(base.glob(REPO_JAR_GLOB))
        if matches:
            return matches[0]
    return None


def _start_plantuml() -> subprocess.Popen | None:
    if shutil.which("java") is None:
        print("[claude-web-console] java not found; PlantUML rendering disabled.")
        return None
    jar = _find_jar()
    if jar is None:
        print("[claude-web-console] plantuml.jar not found; PlantUML rendering disabled.")
        return None
    port = _plantuml_port()
    cmd = ["java", "-jar", str(jar), f"-picoweb:{port}:127.0.0.1"]
    print(f"[claude-web-console] starting PlantUML PicoWeb on 127.0.0.1:{port} ({jar.name})")
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    web_port = server._default_port()
    plantuml = _start_plantuml()
    url = f"http://127.0.0.1:{web_port}/"
    print(f"[claude-web-console] viewer at {url}  (Ctrl-C to stop)")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve(web_port)
    except KeyboardInterrupt:
        pass
    finally:
        if plantuml is not None:
            plantuml.terminate()


if __name__ == "__main__":
    main()
