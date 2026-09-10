#!/usr/bin/env bash
# Everything the handover skill needs to name its file, in one call.
#
# One script rather than three injected commands because only one runtime substitutes and
# runs them: a host without dynamic injection can run this by hand and get the same fields.
#
# The directory is created here so the skill never has to, and so the path printed below is
# always one that exists.
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
handover_dir="$repo_root/.handover"
mkdir -p "$handover_dir"

# Filename timestamp and human timestamp are separate fields. The filename needs no spaces;
# the handover's own text is better for a zone-qualified time, and joining the two would
# force one of them to be wrong. The timestamp is also what orders the directory, which is
# why the filename carries no sequence number: a counter has to be read from the directory
# to be written, and reading it wrong — a rename, a second checkout — numbers two handovers
# the same without failing.
printf 'repo-root: %s\n' "$repo_root"
printf 'handover-dir: %s\n' "$handover_dir"
printf 'filename-timestamp: %s\n' "$(date +'%Y%m%d-%H%M')"
printf 'now: %s\n' "$(date +'%Y-%m-%d %H:%M %Z %z')"
printf 'git-status (first 20):\n'
git status --short | head -20
