#!/bin/sh
# guard's status-line wrapper — installed by `/guard:statusline`, run by Claude Code.
#
#   statusLine.command  →  ~/.claude/guard-statusline.sh ['<the command it replaced>']
#
# guard cannot own the main status line: a plugin's settings.json honors only `agent` and
# `subagentStatusLine`. So this file is COPIED out of the plugin into the user's own
# ~/.claude, and the setting points there. That indirection is the point — the plugin lives
# in a versioned cache directory that every update relocates, and a settings value naming
# that path would break on the next `/plugin update` with no error anywhere. This copy
# resolves the installed plugin at RUN time instead.
#
# With an argument, that argument is the status line this one replaced: it is run with the
# same JSON on stdin and its output printed after guard's segment, so installing guard's
# indicator never costs the user the line they already had. With no argument, the modest
# default below is used.
#
# Two rules, both from the host's own documentation. It runs on every assistant message,
# debounced at 300ms, and a newer update cancels the one in flight — so it reads stdin once
# and spawns as little as it can. And its stdout is a terminal row: every failure prints
# nothing, because a status line is the wrong place to report one.

# --- locate the installed plugin --------------------------------------------------------
# $GUARD_STATUSLINE_HOOK wins when set: a status line has no `--plugin-dir`, so an env
# override is the only way to point this at a working tree. Otherwise the newest version
# under any marketplace that shipped guard. Version dirs are sorted per component, so 0.79.0
# beats 0.9.0 — a plain lexical sort gets that backwards and silently freezes the segment at
# an old version.
_guard_hook() {
  if [ -n "${GUARD_STATUSLINE_HOOK:-}" ] && [ -x "${GUARD_STATUSLINE_HOOK}" ]; then
    printf '%s' "$GUARD_STATUSLINE_HOOK"
    return 0
  fi
  for base in "$HOME"/.claude/plugins/cache/*/guard; do
    [ -d "$base" ] || continue
    ver=$(cd "$base" 2>/dev/null && ls -d */ 2>/dev/null | tr -d / \
          | sort -t. -k1,1n -k2,2n -k3,3n | tail -1)
    [ -n "$ver" ] || continue
    if [ -x "$base/$ver/scripts/guard_hook.py" ]; then
      printf '%s' "$base/$ver/scripts/guard_hook.py"
      return 0
    fi
  done
  return 1
}

# Defined here, not inside the default-line branch below: the separator between guard's
# segment and a CHAINED line needs them too, and an undefined colour there printed a bare
# `|` that did not match the rest of the row.
R='\033[0m'; DIM='\033[2m'; CYAN='\033[36m'
GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'

# stdin can be read only once, and both halves of the line need it.
JSON=$(cat)

GUARD=""
HOOK=$(_guard_hook) && [ -n "$HOOK" ] && \
  GUARD=$(printf '%s' "$JSON" | "$HOOK" status 2>/dev/null)

# --- the rest of the line ---------------------------------------------------------------
REST=""
if [ -n "${1:-}" ]; then
  # The command this one replaced. Run through `sh -c` because a status-line setting is a
  # shell command string, not an argv — which is how the user wrote it and how the host would
  # have run it.
  REST=$(printf '%s' "$JSON" | sh -c "$1" 2>/dev/null)
elif command -v jq >/dev/null 2>&1; then
  # A deliberately plain default: no icons and no 24-bit colour, because this file is
  # installed on machines whose font and terminal are unknown. Anyone who wants a richer
  # line already has one, and it arrives here as the argument above.
  {
    read -r PROJ; read -r CUR; read -r CTX; read -r MODEL
  } <<EOF
$(printf '%s' "$JSON" | jq -r '
  [ (.workspace.project_dir // .cwd // ""),
    (.workspace.current_dir // .cwd // ""),
    (if (.context_window.remaining_percentage // null) == null then ""
     else (.context_window.remaining_percentage | floor | tostring) end),
    (.model.display_name // "") ] | .[]' 2>/dev/null)
EOF
  [ -z "$CUR" ] && CUR="$PROJ"

  # Where you are, stated against the project rather than against the filesystem: a bare
  # basename cannot tell a repo root from a directory of the same name three levels down.
  DIR=""
  case "$CUR" in
    "") ;;
    "$PROJ") DIR=$(basename "$PROJ") ;;
    "$PROJ"/*) DIR="$(basename "$PROJ")/${CUR#"$PROJ"/}" ;;
    *) DIR=$(printf '%s' "$CUR" | sed "s#^$HOME#~#") ;;
  esac

  # `*` is any difference from HEAD, staged or not: at this altitude the question is whether
  # the tree still matches the commit, not which index a change sits in.
  GIT=""
  if [ -n "$CUR" ] && git -C "$CUR" rev-parse --git-dir >/dev/null 2>&1; then
    BRANCH=$(git -C "$CUR" -c core.filesRefLockTimeout=0 branch --show-current 2>/dev/null)
    [ -z "$BRANCH" ] && BRANCH="detached"
    git -C "$CUR" -c core.filesRefLockTimeout=0 diff-index --quiet HEAD -- 2>/dev/null \
      || BRANCH="$BRANCH*"
    GIT="${CYAN}${BRANCH}${R}"
  fi

  # Remaining, not used, and it changes colour as it drains: the number is only ever read to
  # answer "how much room is left", and the colour answers that before the digits are.
  CTXF=""
  if [ -n "$CTX" ]; then
    if [ "$CTX" -gt 50 ] 2>/dev/null; then C="$GREEN"
    elif [ "$CTX" -gt 20 ] 2>/dev/null; then C="$YELLOW"
    else C="$RED"; fi
    CTXF="${C}${CTX}%${R}"
  fi

  [ -n "$MODEL" ] && MODEL="${DIM}${MODEL}${R}"

  # An absent field takes its separator with it, so a directory outside any repo or a session
  # before its first API response leaves no gap behind.
  for F in "$DIR" "$GIT" "$CTXF" "$MODEL"; do
    [ -z "$F" ] && continue
    if [ -z "$REST" ]; then REST="$F"; else REST="$REST ${DIM}·${R} $F"; fi
  done
fi

# Nothing at all rather than an empty row: with no session id and no payload there is nothing
# to say, and a blank line still occupies a row of the user's terminal.
if [ -n "$GUARD" ] && [ -n "$REST" ]; then
  printf '%b\n' "$GUARD ${DIM}|${R} $REST"
elif [ -n "$GUARD" ]; then
  printf '%b\n' "$GUARD"
elif [ -n "$REST" ]; then
  printf '%b\n' "$REST"
fi
