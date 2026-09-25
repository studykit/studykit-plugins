#!/bin/sh
# guard's status-line wrapper — installed by `/guard:statusline`, run by Claude Code.
#
#   statusLine.command  →  ~/.claude/guard-statusline.sh ['<the command it replaced>']
#
#    3⚑    studykit-plugins › plugins › guard    main*    62%    Opus · xhigh ✻    3:41 PM
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
# indicator never costs the user the line they already had. With no argument, the default
# line below is used.
#
# Two rules, both from the host's own documentation. It runs on every assistant message,
# debounced at 300ms, and a newer update cancels the one in flight — so it parses stdin ONCE
# and spawns nothing but git. And its stdout is a terminal row, never a log: a missing field
# drops itself and the rest of the line still prints. Nothing here ever reports an error.
#
# The default line uses 24-bit colour and Nerd Font glyphs, so it assumes a terminal and font
# that render both. A glyph the font lacks shows as a replacement box, not as a failure.

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

# Palette. No background fills, so the row sits on whatever the terminal already shows.
R='\033[0m'
BRIGHT='\033[38;2;239;236;236m'
DIM='\033[38;2;122;118;126m'
# Icons are the only thing separating one field from the next — there are no bars, no
# background fills and no repeated separators on this row — so they are the row's brightest
# element and never carry state. A dim glyph in front of a dim value gave the eye nothing to
# land on, and the parts ran together.
ICON="$BRIGHT"
CYAN='\033[38;2;87;233;235m'
BLUE='\033[38;2;93;180;238m'
GREEN='\033[38;2;71;215;161m'
YELLOW='\033[38;2;232;229;98m'
PINK='\033[38;2;255;91;130m'

# Nerd Font glyphs, written as octal UTF-8 rather than pasted: a private-use codepoint
# does not survive every editor and copy path, and a silently emptied variable here
# turns each field's label into a stray space.
I_GUARD=$(printf '\357\204\262')   # U+F132 shield
I_DIR=$(printf '\357\201\273')     # U+F07B folder
I_GIT=$(printf '\356\202\240')     # U+E0A0 branch
I_CTX=$(printf '\357\203\244')     # U+F0E4 gauge
I_MODEL=$(printf '\357\222\274')   # U+F4BC cpu — Nerd Fonts have no robot/brain glyph
I_TIME=$(printf '\357\200\227')    # U+F017 clock
I_THINK=$(printf '\342\234\273')   # U+273B ✻ — the glyph Claude Code's own thinking
                                   # indicator spins. Not a Nerd Font glyph; the terminal
                                   # falls back for it, as it does for guard's own U+2691 flag.

# stdin can be read only once, and both halves of the line need it.
JSON=$(cat)

# --- guard ------------------------------------------------------------------------------
# guard prints its own coloured field (`guard 3 pending · ⚑` …); the shield stands in for the
# word so the field costs a few columns instead of nine.
#
# The shield takes ONE colour, like every other icon on this row, and the state colours guard
# chose are left to the values they belong to. It labels the field rather than reporting
# anything: guard's switches are independent, and a shield tinted by one of them says
# something about the other it has no business saying. So the substitution moves the glyph
# OUTSIDE guard's colour span and re-opens that span for the rest.
#
# Two fallbacks, in order: plain in-place substitution, then guard's own string untouched.
# Degrading to the word is fine; degrading to a blank field would hide a switch, which is the
# one thing this segment exists to prevent.
GUARD=""
HOOK=$(_guard_hook) && [ -n "$HOOK" ] && \
  GUARD=$(printf '%s' "$JSON" | "$HOOK" status 2>/dev/null)
if [ -n "$GUARD" ]; then
  # Real ESC bytes, not the `\033` strings used elsewhere: sed reads `\0` in a replacement
  # as a backreference and swallows the backslash, which left the escape codes printed as
  # literal `033[2m` text in the row.
  E=$(printf '\033')
  ICON_RAW=$(printf '%b' "$ICON"); R_RAW="${E}[0m"
  MOVED=$(printf '%s' "$GUARD" \
    | sed -E "s/(${E}\[[0-9;]*m)guard /${ICON_RAW}${I_GUARD}${R_RAW} \1/" 2>/dev/null)
  if [ -n "$MOVED" ] && [ "$MOVED" != "$GUARD" ]; then
    GUARD="$MOVED"
  else
    SHIELDED=$(printf '%s' "$GUARD" | sed "s/guard /$I_GUARD /" 2>/dev/null)
    [ -n "$SHIELDED" ] && GUARD="$SHIELDED"
  fi
fi

# --- a chained line ---------------------------------------------------------------------
if [ -n "${1:-}" ]; then
  # The command this one replaced. Run through `sh -c` because a status-line setting is a
  # shell command string, not an argv — which is how the user wrote it and how the host would
  # have run it.
  REST=$(printf '%s' "$JSON" | sh -c "$1" 2>/dev/null)
  OUT=""
  for F in "$GUARD" "$REST"; do
    [ -z "$F" ] && continue
    if [ -z "$OUT" ]; then OUT="$F"; else OUT="$OUT   $F"; fi
  done
  [ -n "$OUT" ] && printf '%b\n' "$OUT"
  exit 0
fi

# --- the default line, from one jq call -------------------------------------------------
# One field per line, empty when absent. A model with no effort parameter omits `effort`
# entirely rather than sending a null, so every read below has to tolerate an empty line.
# Without jq every field here is empty and only guard's segment and the clock print.
{
  read -r PROJ
  read -r CUR
  read -r CTX
  read -r MODEL
  read -r EFFORT
  read -r FAST
  read -r THINK
} <<EOF
$(printf '%s' "$JSON" | jq -r '
  [ (.workspace.project_dir // .cwd // ""),
    (.workspace.current_dir // .cwd // ""),
    (if (.context_window.remaining_percentage // null) == null then ""
     else (.context_window.remaining_percentage | floor | tostring) end),
    (.model.display_name // ""),
    (.effort.level // ""),
    (if .fast_mode then "1" else "" end),
    (if .thinking.enabled then "1" else "" end) ] | .[]' 2>/dev/null)
EOF

# --- path -------------------------------------------------------------------------------
# Relative to the project, because the project is the frame everything else in the session is
# in. Inside it: the repo's own name, then each level below it, joined with › — bright name,
# dim tail, so "which repo" and "where in it" never blur. Outside it: the ~-shortened path,
# dim throughout, since being outside the project is the thing worth noticing. Nothing is
# elided; if a deep tree ever crowds the row, that is a design decision to make on purpose.
DIRFIELD=""
[ -z "$CUR" ] && CUR="$PROJ"
if [ -n "$CUR" ]; then
  case "$CUR" in
    "$PROJ")
      DIRFIELD="${BRIGHT}$(basename "$PROJ")${R}" ;;
    "$PROJ"/*)
      TAIL=$(printf '%s' "${CUR#"$PROJ"/}" | sed 's#/# › #g')
      DIRFIELD="${BRIGHT}$(basename "$PROJ")${R}${DIM} › ${TAIL}${R}" ;;
    *)
      SHORT=$(printf '%s' "$CUR" | sed "s#^$HOME#~#" | sed 's#/# › #g')
      DIRFIELD="${DIM}${SHORT}${R}" ;;
  esac
  DIRFIELD="${ICON}${I_DIR}${R} ${DIRFIELD}"
fi

# --- git --------------------------------------------------------------------------------
# `*` is any difference from HEAD, staged or not: at status-line altitude the useful question
# is "does this tree still match the commit", not which index the change sits in.
GITFIELD=""
if [ -n "$CUR" ] && git -C "$CUR" rev-parse --git-dir >/dev/null 2>&1; then
  BRANCH=$(git -C "$CUR" -c core.filesRefLockTimeout=0 branch --show-current 2>/dev/null)
  [ -z "$BRANCH" ] && BRANCH="detached"
  DIRTY=""
  git -C "$CUR" -c core.filesRefLockTimeout=0 diff-index --quiet HEAD -- 2>/dev/null \
    || DIRTY="*"
  GITFIELD="${ICON}${I_GIT}${R} ${CYAN}${BRANCH}${DIRTY}${R}"
fi

# --- context ----------------------------------------------------------------------------
# Remaining, not used, and it changes colour as it drains: the number is only ever consulted
# to answer "how much room is left", and a colour answers that before the digits are read.
CTXFIELD=""
if [ -n "$CTX" ]; then
  if [ "$CTX" -gt 50 ] 2>/dev/null; then C="$GREEN"
  elif [ "$CTX" -gt 20 ] 2>/dev/null; then C="$YELLOW"
  else C="$PINK"; fi
  CTXFIELD="${ICON}${I_CTX}${R} ${C}${CTX}%${R}"
fi

# --- model, effort, and the two marks ---------------------------------------------------
# ✻ thinking, ⚡ fast mode. Both hang off the model because that is what they modify, and both
# appear only when on: they are the exceptions, and an always-printed "off" would say nothing
# most of the time while costing width every time.
MODELFIELD=""
if [ -n "$MODEL" ]; then
  MODELFIELD="${ICON}${I_MODEL}${R} ${BLUE}${MODEL}${R}"
  [ -n "$EFFORT" ] && MODELFIELD="${MODELFIELD}${DIM} · ${EFFORT}${R}"
  [ -n "$THINK" ] && MODELFIELD="${MODELFIELD}${DIM} ${I_THINK}${R}"
  [ -n "$FAST" ] && MODELFIELD="${MODELFIELD}${YELLOW} ⚡${R}"
fi

TIMEFIELD="${ICON}${I_TIME}${R} ${DIM}$(date '+%l:%M %p' | sed 's/^ //')${R}"

# --- assemble ---------------------------------------------------------------------------
# Fixed order, and an absent field takes its separator with it, so a missing git repo or a
# session before the first API response leaves no gap behind.
OUT=""
for F in "$GUARD" "$DIRFIELD" "$GITFIELD" "$CTXFIELD" "$MODELFIELD" "$TIMEFIELD"; do
  [ -z "$F" ] && continue
  if [ -z "$OUT" ]; then OUT="$F"; else OUT="$OUT   $F"; fi
done
printf '%b\n' "$OUT"
