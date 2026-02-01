# OperationBase.hasError Property

Parent Object: [OperationBase](OperationBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

Gets if errors were encountered when generating the operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationBase\_var" is a variable referencing an OperationBase object. |

"operationBase\_var" is a variable referencing an OperationBase object. ```` ``` #include <Cam/Operations/OperationBase.h>  // Get the value of the property. boolean propertyValue = operationBase_var->hasError(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |