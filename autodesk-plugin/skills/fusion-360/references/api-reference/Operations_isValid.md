# Operations.isValid Property

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an Operations object. |

"operations\_var" is a variable referencing an Operations object. ```` ``` #include <Cam/Operations/Operations.h>  // Get the value of the property. boolean propertyValue = operations_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |