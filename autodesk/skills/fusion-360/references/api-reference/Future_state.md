# Future.state Property

Parent Object: [Future](Future.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Future.h>

## Description

Returns the current state of the process associated with this future.

## Syntax

* [Python](#Python)
* [C++](#C++)

"future\_var" is a variable referencing a Future object. |

"future\_var" is a variable referencing a Future object. ```` ``` #include <Core/Application/Future.h>  // Get the value of the property. FutureStates propertyValue = future_var->state(); ``` ```` |

## Property Value

This is a read only property whose value is a [FutureStates](FutureStates.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |