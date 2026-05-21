"""Legacy per-intent dispatcher modules.

These modules originally lived at ``scripts/issue_*.py`` as standalone CLI
entry points. They have been moved here so the unified ``issue.py``
dispatcher can import their ``main(argv)`` and route subcommand calls to
the matching legacy intent without duplicating logic.

The files retain their PEP 723 inline metadata, so they remain runnable
in isolation via ``uv run --script`` for debugging, but the public
``$WORKFLOW`` surface is ``issue.py <verb>``.
"""
