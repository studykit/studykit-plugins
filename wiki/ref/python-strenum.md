# Python `enum.StrEnum` — version added & string behavior

Source: https://docs.python.org/3/library/enum.html (fetched 2026-07-11)

## Version added

> **class enum.StrEnum**
> _StrEnum_ is the same as _Enum_, but its members are also strings and can be used
> in most of the same places that a string can be used.
>
> Added in version 3.11.

This is why guard requires **Python 3.11+**: `scripts/guard_hook.py` defines its
`EditGate` / `JudgeGate` config values as `enum.StrEnum`, which does not exist before
3.11 (importing it there raises `ImportError`).

## String behavior (why StrEnum, not `class X(str, Enum)`)

`StrEnum` sets `__str__`/`__format__` to `str`'s, so a member renders as its **value**:

> `__str__()` is `str.__str__()` to better support the _replacement of existing
> constants_ use-case. `__format__()` is likewise `str.__format__()` for that same
> reason.

Consequences guard relies on:

- `f"{JudgeGate.HEADLESS}"` == `"headless"` (the value, not `"JudgeGate.HEADLESS"`).
- `json.dumps(EditGate.ASK)` == `'"ask"'` (StrEnum is a `str` subclass).
- `EditGate.ASK == "ask"` is `True`.

A plain `class X(str, Enum)` mixin compares equal to its value too, but its `__str__`
yields `"X.ASK"` (the member name), which would require `.value` at every f-string /
`json.dumps` site. StrEnum avoids that.
