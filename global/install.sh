#!/bin/sh
# Link this directory's definitions into the user's global Claude directory.
#
# `global/` mirrors the layout of ~/.claude, so global/agents/ lands in
# ~/.claude/agents. These are standalone definitions, not plugins: `claude --agent
# <name>` and @-mention resolve names from that directory, which is outside any
# repository. Linking rather than copying keeps this checkout the single source of
# truth — an edit here is live in the next session, with no reinstall step.
set -eu

root_dir=$(cd "$(dirname "$0")" && pwd)
src_dir=$root_dir/agents
dest_dir=${CLAUDE_AGENTS_DIR:-$HOME/.claude/agents}
force=0
uninstall=0
dry=0

usage() {
	cat <<'USAGE'
usage: install.sh [--uninstall] [--force] [--dry-run]

  --uninstall  remove links this script created (leaves anything else alone)
  --force      replace a destination that is not our link; a regular file is
               moved aside to <name>.bak-<timestamp> rather than deleted
  --dry-run    print what would happen and change nothing

Links global/agents/*.md into ~/.claude/agents; override the destination
with CLAUDE_AGENTS_DIR.
USAGE
}

for arg in "$@"; do
	case $arg in
	--uninstall) uninstall=1 ;;
	--force) force=1 ;;
	--dry-run) dry=1 ;;
	-h | --help)
		usage
		exit 0
		;;
	*)
		printf 'install.sh: unknown option %s\n\n' "$arg" >&2
		usage >&2
		exit 2
		;;
	esac
done

run() {
	if [ "$dry" -eq 1 ]; then
		printf '  would: %s\n' "$*"
	else
		"$@"
	fi
}

[ "$dry" -eq 1 ] || [ "$uninstall" -eq 1 ] || mkdir -p "$dest_dir"

status=0
found=0

for src in "$src_dir"/*.md; do
	[ -e "$src" ] || continue
	# An agent definition is a file with a `name:` in its YAML frontmatter. Anything
	# else here is documentation, and linking it would put a non-agent in the roster.
	[ "$(head -n 1 "$src")" = "---" ] || continue
	sed -n '2,/^---$/p' "$src" | grep -q '^name:' || continue
	name=${src##*/}
	found=$((found + 1))
	dest=$dest_dir/$name

	# -L rather than -e: a link to a deleted target is still ours to manage.
	if [ -L "$dest" ]; then
		target=$(readlink "$dest")
		ours=0
		case $target in
		"$src") ours=1 ;;
		esac
	else
		target=
		ours=0
	fi

	if [ "$uninstall" -eq 1 ]; then
		if [ "$ours" -eq 1 ]; then
			run rm "$dest"
			printf 'unlinked  %s\n' "$dest"
		elif [ -L "$dest" ] || [ -e "$dest" ]; then
			printf 'skipped   %s (not a link this script made)\n' "$dest"
		fi
		continue
	fi

	if [ "$ours" -eq 1 ]; then
		printf 'ok        %s\n' "$dest"
		continue
	fi

	if [ -L "$dest" ]; then
		if [ "$force" -eq 1 ]; then
			run rm "$dest"
		else
			printf 'CONFLICT  %s -> %s (use --force to replace)\n' "$dest" "$target" >&2
			status=1
			continue
		fi
	elif [ -e "$dest" ]; then
		if [ "$force" -eq 1 ]; then
			backup=$dest.bak-$(date +%Y%m%d%H%M%S)
			run mv "$dest" "$backup"
			printf 'moved     %s -> %s\n' "$dest" "$backup"
		else
			printf 'CONFLICT  %s exists and is not a link (use --force)\n' "$dest" >&2
			status=1
			continue
		fi
	fi

	run ln -s "$src" "$dest"
	printf 'linked    %s -> %s\n' "$dest" "$src"
done

if [ "$found" -eq 0 ]; then
	printf 'install.sh: no agent definitions in %s\n' "$src_dir" >&2
	exit 1
fi

exit "$status"
