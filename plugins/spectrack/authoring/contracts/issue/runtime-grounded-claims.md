# Runtime-Grounded Claims

The grounding rule for assertions about runtime behavior in an issue body.
It applies to implementation-bearing types — `task`, `bug`, and `spike` — where
a downstream decision rests on what the running system actually does. Read with
`./common.md` (issue rules, body conventions).

A *runtime-grounded claim* is an assertion about runtime behavior that a
downstream decision rests on — a measurement, the output of a command, an
observed trace or render, or a fact about a compiled artifact (e.g. a
bytecode/line attribution). These are the claims most often wrong in practice,
because they are easy to assert from reasoning and easy to get wrong.

- Record the exact command or observation that produced the claim, together with
  its captured result — not an asserted expectation. "`gradlew test` fails with
  X" backed by the actual output, not "this should fail".
- A runtime-grounded claim that was never actually run is missing evidence, not
  weak evidence. Reasoning about the code is not a substitute for running the
  premise.
- Before building on a runtime-grounded claim — **including in the same session
  that recorded it** — confirm it empirically. Re-run the command and check the
  result still holds; when no existing command exposes the fact, add temporary
  logging or instrumentation at the decisive point, run, observe the actual
  value, then remove the instrumentation. The wrong-assumption failure mode is
  epistemic, not informational: a premise nobody executed stays unverified no
  matter how much context the implementer carries, so re-grounding is required
  even when the author and the implementer are the same session.
