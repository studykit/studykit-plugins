# DataObjectFuture.state Property

Parent Object: [DataObjectFuture](DataObjectFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObjectFuture.h>

## Description

Returns the current state of the process associated with this future.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. |

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. ```` ``` #include <Core/Dashboard/DataObjectFuture.h>  // Get the value of the property. FutureStates propertyValue = dataObjectFuture_var->state(); ``` ```` |

## Property Value

This is a read only property whose value is a [FutureStates](FutureStates.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |