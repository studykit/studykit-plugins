# OperationBase.isProtected Property

Parent Object: [OperationBase](OperationBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationBase\_var" is a variable referencing an OperationBase object. |

"operationBase\_var" is a variable referencing an OperationBase object. ```` ``` #include <Cam/Operations/OperationBase.h>  // Get the value of the property. boolean propertyValue = operationBase_var->isProtected();  // Set the value of the property, where value_var is a boolean. bool returnValue = operationBase_var->isProtected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |