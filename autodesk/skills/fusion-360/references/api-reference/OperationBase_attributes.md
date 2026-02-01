# OperationBase.attributes Property

Parent Object: [OperationBase](OperationBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

Returns the collection of attributes associated with this object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationBase\_var" is a variable referencing an OperationBase object. |

"operationBase\_var" is a variable referencing an OperationBase object. ```` ``` #include <Cam/Operations/OperationBase.h>  // Get the value of the property. Ptr<Attributes> propertyValue = operationBase_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version August 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |