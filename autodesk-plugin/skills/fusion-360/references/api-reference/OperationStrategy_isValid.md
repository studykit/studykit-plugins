# OperationStrategy.isValid Property

Parent Object: [OperationStrategy](OperationStrategy.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationStrategy.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationStrategy\_var" is a variable referencing an OperationStrategy object. |

"operationStrategy\_var" is a variable referencing an OperationStrategy object. ```` ``` #include <Cam/Operations/OperationStrategy.h>  // Get the value of the property. boolean propertyValue = operationStrategy_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |