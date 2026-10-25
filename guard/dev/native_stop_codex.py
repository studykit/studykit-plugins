#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Exercise Guard's working-tree plugin with real Codex CLI and native reviewer.

Runs real gpt-6-luna requests. A PTY test driver supplies form choices. All
configuration, plugins, auth copies and generated projects live in a temporary
directory; only selected, sanitized evidence is copied to --output.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import pty
import re
import select
import shutil
import signal
import struct
import subprocess
import sys
import tempfile
import termios
import time


ANSI = re.compile(rb'\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)|\x1b\[[0-?]*[ -/]*[@-~]|\x1b[^\[\]]')


def run(command: list[str], *, env: dict[str, str], cwd: Path | None = None) -> str:
    completed = subprocess.run(command, env=env, cwd=cwd, text=True, capture_output=True, timeout=40)
    if completed.returncode:
        raise RuntimeError(f'{command[:3]} failed: {completed.stderr[:2000]}')
    return completed.stdout


def read_jsons(directory: Path) -> dict[str, object]:
    if not directory.exists():
        return {}
    result = {}
    for path in directory.rglob('*.json'):
        try:
            result[str(path.relative_to(directory))] = json.loads(path.read_text())
        except (OSError, ValueError):
            pass
    return result


def server_processes(root_pid: int) -> str:
    processes = subprocess.run(['ps', '-o', 'pid=,ppid=,command=', '-ax'], text=True, capture_output=True).stdout
    rows = [line.strip().split(None, 2) for line in processes.splitlines()]
    descendants = {str(root_pid)}
    for _ in range(8):
        descendants.update(row[0] for row in rows if len(row) == 3 and row[1] in descendants)
    evidence = []
    for row in rows:
        if len(row) == 3 and row[0] in descendants and 'mcp/server.py' in row[2]:
            evidence.append(' '.join(row))
            evidence.append(subprocess.run(['lsof', '-a', '-p', row[0], '-d', 'cwd', '-Fn'], text=True, capture_output=True).stdout)
    return '\n'.join(evidence)


def function_evidence(home: Path, root_sessions: set[str]) -> list[dict[str, object]]:
    sessions = []
    for path in (home / 'sessions').rglob('*.jsonl'):
        records = []
        metadata = {}
        for line in path.read_text(errors='replace').splitlines():
            try:
                record = json.loads(line)
            except ValueError:
                continue
            records.append(record)
            if record.get('type') == 'session_meta':
                metadata = record.get('payload', {})
        sessions.append((path, metadata, records))
    allowed = set(root_sessions)
    for _ in sessions:
        for _, metadata, _ in sessions:
            source = metadata.get('source', {})
            spawn = source.get('subagent', {}).get('thread_spawn', {}) if isinstance(source, dict) else {}
            if spawn.get('parent_thread_id') in allowed:
                allowed.add(metadata.get('id'))
    evidence = []
    for path, metadata, records in sessions:
        if metadata.get('id') not in allowed:
            continue
        for record in records:
            payload = record.get('payload', {})
            if not isinstance(payload, dict):
                continue
            if payload.get('type') == 'function_call' and payload.get('name') in {'spawn_agent', 'wait_agent', 'close_agent'}:
                kept = dict(payload)
                if kept.get('name') == 'spawn_agent':
                    arguments = json.loads(kept.get('arguments', '{}'))
                    arguments.pop('message', None)
                    kept['arguments'] = arguments
                    kept['message_omitted'] = 'Host-encrypted task text is unnecessary for named-agent invocation evidence.'
                evidence.append({'session_file': path.name, **kept})
            elif payload.get('type') == 'agent_message' and 'GUARD_REVIEW_FIXTURE_OK' in str(payload):
                evidence.append({'session_file': path.name, **payload})
            elif record.get('type') == 'session_meta' and isinstance(payload.get('source'), dict):
                evidence.append({'session_file': path.name, 'type': 'session_meta', 'id': payload.get('id'),
                                 'source': payload['source']})
    return evidence


def case(base: Path, home: Path, action: str, output: Path, env: dict[str, str], timeout: int) -> dict[str, object]:
    project = base / ('project-' + action)
    (project / '.codex' / 'agents').mkdir(parents=True)
    (project / 'target.txt').write_text('before\n')
    run(['git', 'init', '-q', str(project)], env=env)
    run(['git', 'add', 'target.txt'], env=env, cwd=project)
    (project / '.codex' / 'guard.local.json').write_text(json.dumps({'file_review_rules': [
        {'glob': 'target.txt', 'action': {'kind': 'agent', 'name': 'fixture_reviewer'}, 'on_stop': 'ask'}]}))
    agent = {'name': 'fixture_reviewer', 'description': 'Fixture-only native file reviewer used after Guard consent.',
             'model': 'gpt-6-luna', 'model_reasoning_effort': 'low',
             'developer_instructions': 'You are the fixture reviewer. Read only the absolute file paths supplied in your task. Do not edit any file, create agents, or complete checkpoints. If every listed file contains exactly after followed by a newline, return exactly GUARD_REVIEW_FIXTURE_OK. Otherwise report the mismatch.'}
    (project / '.codex' / 'agents' / 'fixture_reviewer.toml').write_text(''.join(f'{key} = {json.dumps(value)}\n' for key, value in agent.items()))
    config = home / 'config.toml'
    with config.open('a') as stream:
        stream.write(f'\n[projects.{json.dumps(str(project))}]\ntrust_level = "trusted"\n')
    prompt = ('Call the apply_patch tool directly, not a shell command named apply_patch, to replace target.txt contents with exactly after followed by a newline. '
              'Then respond READY. Do not invoke MCP tools yourself. Guard will ask its native Stop form. '
              'Only after that form is accepted, follow the approved frozen checkpoint instructions and invoke the exact native '
              'agent type fixture_reviewer with the listed absolute paths only. The user explicitly authorizes that native '
              'subagent after accepting Guard consent. Wait for its actual result, then run the supplied checkpoint completion '
              'command. Never impersonate a reviewer, substitute a generic agent, or complete before the reviewer finishes. '
              'Report the actual checkpoint completion JSON and reviewer result. Do not perform any other implementation.')
    command = ['codex', '--no-daemon', '--dangerously-bypass-hook-trust', '-C', str(project), '-m', 'gpt-6-luna',
               '-s', 'danger-full-access', '-a', 'on-request', '--no-alt-screen', prompt]
    pid, fd = pty.fork()
    if pid == 0:
        os.environ.clear()
        os.environ.update(env)
        os.environ.update({'TERM': 'xterm-256color', 'COLUMNS': '140', 'LINES': '45', 'GUARD_TRACE': '1'})
        os.execvp(command[0], command)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack('HHHH', 45, 140, 0, 0))
    raw = b''
    asked_at = None
    answered_at = None
    done_at = None
    pending_before: dict[str, object] = {}
    started = time.monotonic()
    timed_out = False
    diagnostic_at = None
    output.mkdir(parents=True, exist_ok=True)
    try:
        while time.monotonic() - started < timeout:
            ready, _, _ = select.select([fd], [], [], .1)
            if ready:
                try:
                    chunk = os.read(fd, 65536)
                except OSError:
                    break
                if not chunk:
                    break
                raw += chunk
            text = ANSI.sub(b'', raw).decode(errors='replace')
            if asked_at is None and 'Run the configured reviewers' in text:
                asked_at = time.monotonic()
                pending_before = read_jsons(project / '.codex' / 'guard')
                (output / 'question-screen.txt').write_text(text[-7000:])
                (output / 'server-process.txt').write_text(server_processes(pid))
                print(f'{action}: native Guard consent form visible', flush=True)
            if asked_at is not None and answered_at is None and time.monotonic() - asked_at > .5:
                # The required enum lists review first and keep-pending second.
                os.write(fd, {'accept': b'\r', 'decline': b'\x1b[B\r', 'cancel': b'\x1b'}[action])
                answered_at = time.monotonic()
            state = read_jsons(project / '.codex' / 'guard')
            states = [value for name, value in state.items() if name.startswith('state/') and isinstance(value, dict)]
            queued = sum(len(value.get('edited_files', [])) + len(value.get('edited_docs', [])) + len(value.get('edited_agent_docs', [])) for value in states)
            terminal_done = b'state=done' in raw and answered_at is not None and time.monotonic() - answered_at > 1
            marker = 'GUARD_REVIEW_FIXTURE_OK' in text
            if asked_at is None and 'Hook failed' in text and diagnostic_at is None:
                os.write(fd, b'\x1bOQ')
                diagnostic_at = time.monotonic()
            if diagnostic_at is not None and time.monotonic() - diagnostic_at > 2:
                break
            if terminal_done and (action != 'accept' or (marker and queued == 0)):
                if done_at is None:
                    done_at = time.monotonic()
                if time.monotonic() - done_at > 1:
                    break
            if asked_at is None and b'state=done' in raw and 'READY' in text and time.monotonic() - started > 25:
                # Report an actually missing consent form rather than fabricate a queue.
                break
        else:
            timed_out = True
    finally:
        try:
            os.kill(pid, signal.SIGTERM)
            for _ in range(20):
                ended, _ = os.waitpid(pid, os.WNOHANG)
                if ended:
                    break
                time.sleep(.1)
            else:
                os.kill(pid, signal.SIGKILL)
        except (ProcessLookupError, ChildProcessError, PermissionError):
            pass
        os.close(fd)
        try:
            os.waitpid(pid, 0)
        except ChildProcessError:
            pass
    text = ANSI.sub(b'', raw).decode(errors='replace')
    state = read_jsons(project / '.codex' / 'guard')
    root_sessions = {Path(name).stem for name in pending_before if name.startswith('state/')}
    calls = function_evidence(home, root_sessions)
    (output / 'terminal.raw').write_bytes(raw)
    (output / 'terminal.txt').write_text(text)
    (output / 'state-before.json').write_text(json.dumps(pending_before, indent=2))
    (output / 'state-after.json').write_text(json.dumps(state, indent=2))
    (output / 'native-agent-events.json').write_text(json.dumps(calls, indent=2))
    trace = project / '.codex' / 'guard' / 'trace.log'
    if trace.exists():
        shutil.copy2(trace, output / 'trace.log')
    report = {'case': action, 'timed_out': timed_out, 'form_visible': asked_at is not None,
              'target_contents': (project / 'target.txt').read_text(),
              'reviewer_marker': 'GUARD_REVIEW_FIXTURE_OK' in text,
              'native_fixture_spawn': any(item.get('name') == 'spawn_agent' and 'fixture_reviewer' in str(item.get('arguments')) for item in calls),
              'queued_before': sum(len(value.get('edited_files', [])) for name, value in pending_before.items() if name.startswith('state/') and isinstance(value, dict)),
              'queued_after': sum(len(value.get('edited_files', [])) for name, value in state.items() if name.startswith('state/') and isinstance(value, dict)),
              'checkpoints_after': sum(len(value.get('file_checkpoints', {})) for name, value in state.items() if name.startswith('state/') and isinstance(value, dict)),
              'consent_outcomes': sorted({value.get('last_answer', {}).get('outcome') for name, value in state.items()
                  if name.startswith('stop-consent/') and isinstance(value, dict) and value.get('last_answer', {}).get('outcome')}),
              'elapsed_seconds': round(time.monotonic() - started, 2)}
    (output / 'summary.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report), flush=True)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--auth-source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cases', nargs='+', choices=['accept', 'decline', 'cancel'], default=['accept', 'cancel'])
    parser.add_argument('--timeout', type=int, default=180)
    args = parser.parse_args()
    base = Path(tempfile.mkdtemp(prefix='guard-stop-integration-codex-')).resolve()
    home = base / 'home'
    home.mkdir(mode=0o700)
    env = {key: value for key, value in os.environ.items() if not key.startswith(('GUARD_', 'CLAUDE_', 'CODEX_', 'HERDR_'))}
    env['CODEX_HOME'] = str(home)
    try:
        shutil.copy2(args.auth_source, home / 'auth.json')
        os.chmod(home / 'auth.json', 0o600)
        plugin = base / 'market' / 'guard'
        shutil.copytree(args.plugin, plugin, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        market = base / 'market' / '.agents' / 'plugins'
        market.mkdir(parents=True)
        (market / 'marketplace.json').write_text(json.dumps({'name': 'guard-native-integration', 'interface': {'displayName': 'Guard Native Integration'},
            'plugins': [{'name': 'guard', 'source': {'source': 'local', 'path': './guard'}, 'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, 'category': 'Coding'}]}))
        for command in [['plugin', 'marketplace', 'add', str(base / 'market'), '--json'], ['plugin', 'add', 'guard@guard-native-integration', '--json']]:
            run(['codex', *command], env=env)
        args.output.mkdir(parents=True, exist_ok=True)
        hashes = {str(path.relative_to(plugin)): hashlib.sha256(path.read_bytes()).hexdigest() for path in plugin.rglob('*') if path.is_file()}
        (args.output / 'plugin-sha256.json').write_text(json.dumps(hashes, indent=2))
        reports = [case(base, home, action, args.output / action, env, args.timeout) for action in args.cases]
        return 0 if all(report['form_visible'] and not report['timed_out'] and report['queued_before'] > 0 and
            report['consent_outcomes'] == [{'accept': 'approved', 'decline': 'declined', 'cancel': 'cancelled'}[report['case']]] and
            (report['native_fixture_spawn'] and report['reviewer_marker'] and report['queued_after'] == 0 and report['checkpoints_after'] == 0
             if report['case'] == 'accept' else not report['native_fixture_spawn'] and report['queued_after'] > 0) for report in reports) else 1
    finally:
        (home / 'auth.json').unlink(missing_ok=True)
        shutil.rmtree(home, ignore_errors=True)
        print(f'Temporary auth and Codex home removed; fixture source retained at {base}', flush=True)


if __name__ == '__main__':
    raise SystemExit(main())
