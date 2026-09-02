# Runtime-Grounded Claims

The grounding rule for runtime-behavior assertions in implementation-bearing
issue bodies (`task`, `bug`, `spike`).

A *runtime-grounded claim* is an assertion about runtime behavior that a
downstream decision rests on: a command output, measurement, observed trace or
render, or fact about a compiled artifact.

- Record the exact command or observation and captured result. Do not replace it
  with an expected outcome.
- If it was not run or observed, it is missing evidence; reasoning about code is
  not a substitute.
- Before building on the claim, confirm it still holds. Re-run the command or
  instrument the decisive point, observe the value, then remove instrumentation.
