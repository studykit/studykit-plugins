#!/usr/bin/env python3
"""claude-web-console local server: HTTP + Server-Sent Events.

Receives conversation events from the plugin hooks (POST /event), replays and
streams them to browser viewers (GET /events), and serves the static viewer.
Standard library only.
"""
from __future__ import annotations

import json
import os
import queue
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

STATIC_DIR = Path(__file__).resolve().parent / "static"
HISTORY_LIMIT = 5000

_lock = threading.Lock()
_history: list[dict] = []
_clients: "list[queue.Queue[dict]]" = []

# Static assets fall back to application/octet-stream (see the GET handler). A
# browser refuses to execute an ES module served as octet-stream, so a missing
# ".mjs" mapping silently breaks the whole viewer — the vendored module never
# evaluates. ".woff2" must stay mapped for the KaTeX fonts for the same reason.
CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".svg": "image/svg+xml",
    ".json": "application/json; charset=utf-8",
    ".ico": "image/x-icon",
    ".woff2": "font/woff2",
}


def _default_port() -> int:
    try:
        return int(os.environ.get("CLAUDE_WEB_CONSOLE_PORT", ""))
    except ValueError:
        return 8477


def _plantuml_server() -> str:
    try:
        port = int(os.environ.get("CLAUDE_WEB_CONSOLE_PLANTUML_PORT", ""))
    except ValueError:
        port = 8478
    return f"http://127.0.0.1:{port}/plantuml"


def _broadcast(event: dict) -> None:
    with _lock:
        _history.append(event)
        overflow = len(_history) - HISTORY_LIMIT
        if overflow > 0:
            del _history[:overflow]
        for client in _clients:
            client.put(event)


def _register_client() -> "tuple[queue.Queue[dict], list[dict]]":
    client: "queue.Queue[dict]" = queue.Queue()
    with _lock:
        snapshot = list(_history)
        _clients.append(client)
    return client, snapshot


def _unregister_client(client: "queue.Queue[dict]") -> None:
    with _lock:
        if client in _clients:
            _clients.remove(client)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args: object) -> None:  # keep the console quiet
        pass

    def do_POST(self) -> None:
        if self.path.split("?", 1)[0] != "/event":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b""
        try:
            event = json.loads(raw or b"{}")
        except (json.JSONDecodeError, ValueError):
            self.send_error(400)
            return
        if isinstance(event, dict):
            _broadcast(event)
        self.send_response(204)
        self.end_headers()

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/events":
            self._serve_events()
        elif path == "/config.json":
            self._serve_json({"plantumlServer": _plantuml_server()})
        else:
            self._serve_static(path)

    def _serve_json(self, obj: dict) -> None:
        body = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_static(self, path: str) -> None:
        rel = "index.html" if path in ("/", "") else path.lstrip("/")
        target = (STATIC_DIR / rel).resolve()
        try:
            target.relative_to(STATIC_DIR)
        except ValueError:
            self.send_error(404)
            return
        if not target.is_file():
            self.send_error(404)
            return
        data = target.read_bytes()
        ctype = CONTENT_TYPES.get(target.suffix, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _serve_events(self) -> None:
        client, snapshot = _register_client()
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()
        self.close_connection = True
        try:
            for event in snapshot:
                self._sse_send(event)
            while True:
                try:
                    self._sse_send(client.get(timeout=15))
                except queue.Empty:
                    self.wfile.write(b": ping\n\n")
                    self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            _unregister_client(client)

    def _sse_send(self, event: dict) -> None:
        self.wfile.write(f"data: {json.dumps(event)}\n\n".encode("utf-8"))
        self.wfile.flush()


def serve(port: int | None = None) -> None:
    port = port or _default_port()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    httpd.daemon_threads = True
    httpd.serve_forever()


if __name__ == "__main__":
    serve()
