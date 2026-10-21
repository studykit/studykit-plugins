# Delegate development

The plugin ships a Codex and a Claude Code edition from one package; `dev/design.md`
§ Layout explains why each host's entry points live where they do. Keep the plugin self-contained: installed packages must not depend on files elsewhere in this
checkout. Sizing belongs to the sizer agent. In the Claude Code edition, checking results and
proposing verdicts belongs to the verifier agent, and recording them to the main session;
the Codex edition still verifies in the main session. Preserve user configuration and delegation history across setup, updates, and removal.

See `dev/design.md` for runtime boundaries and validation. Run tests with
`python3 -m unittest discover -s delegate/tests -v` from the repository root.
