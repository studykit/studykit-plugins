# OperationBase.error Property

Parent Object: [OperationBase](OperationBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

Returns a message corresponding to any active error associated with the value of this parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationBase\_var" is a variable referencing an OperationBase object. |

"operationBase\_var" is a variable referencing an OperationBase object. ```` ``` #include <Cam/Operations/OperationBase.h>  // Get the value of the property. string propertyValue = operationBase_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |