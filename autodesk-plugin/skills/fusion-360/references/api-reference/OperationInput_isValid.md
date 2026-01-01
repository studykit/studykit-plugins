# OperationInput.isValid Property

Parent Object: [OperationInput](OperationInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationInput\_var" is a variable referencing an OperationInput object. |

"operationInput\_var" is a variable referencing an OperationInput object. ```` ``` #include <Cam/Operations/OperationInput.h>  // Get the value of the property. boolean propertyValue = operationInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |