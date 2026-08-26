"""guard's implementation, split by layer.

The entry point stays ``scripts/guard_hook.py``: that path is in ``hooks/hooks.json``, in
every command and agent definition that shells out to the CLI, and in the Codex adapter's
import. This package is what it dispatches into.

Imports run one way only, and a cycle here is a design error rather than a technical one::

    config -> paths -> turnrec / payload / emit -> transcript
                    -> agents -> state -> dispatch -> cmd_* -> guard_hook

- ``config``     the host split, ``AgentMode``, the config schema and its file I/O
- ``paths``      project root resolution, the state tree's paths, the debug trace
- ``turnrec``    the answer file and the request file beside it
- ``payload``    hook payload on stdin, and the session id in it
- ``emit``       the three hook-output shapes guard writes to stdout
- ``transcript`` reading the host's transcript, and the ``transcript`` CLI over it
- ``agents``     the roster guard can recommend, and mechanical eligibility
- ``state``      the per-session state file
- ``dispatch``   the text handed to the main agent
- ``cmd_search`` ``pre-search``: the one hook that denies rather than reports
- ``cmd_*``      one module per hook event, plus the CLI verbs (``cmd_candidates``
                 is the router's roster lookup, not an event)

``config`` is the only module that may read ``GUARD_HOST``, and it reads it once at import.
The Codex adapter sets that variable before importing anything here, so a second reader
would be a second answer to "which host am I".
"""
