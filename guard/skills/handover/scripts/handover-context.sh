#!/usr/bin/env bash
# Everything the handover skill needs to name its file, in one call.
#
# One script rather than four injected commands because only one runtime substitutes and
# runs them: a host without dynamic injection can run this by hand and get the same fields.
#
# Creating the directory is part of the same call as counting it, so the number below is
# always counted against a directory that exists.
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
handover_dir="$repo_root/.handover"
mkdir -p "$handover_dir"

# Counted in the directory the skill actually writes to. The version this was ported from
# counted a differently-named directory after the skill's was renamed: every handover came
# out numbered 1, and nothing failed.
largest="$(
  find "$handover_dir" -maxdepth 1 -type f -name '[0-9]*-*.md' -exec basename {} \; |
    sed -n 's/^\([0-9][0-9]*\)-.*\.md$/\1/p' |
    sort -n |
    tail -1
)"

# Filename timestamp and human timestamp are separate fields. The filename needs no spaces;
# the handover's own text is better for a zone-qualified time, and joining the two would
# force one of them to be wrong.
printf 'repo-root: %s\n' "$repo_root"
printf 'handover-dir: %s\n' "$handover_dir"
printf 'filename-timestamp: %s\n' "$(date +'%Y%m%d-%H%M')"
printf 'now: %s\n' "$(date +'%Y-%m-%d %H:%M %Z %z')"
printf 'next-number: %s\n' "$(( ${largest:-0} + 1 ))"
printf 'git-status (first 20):\n'
git status --short | head -20
