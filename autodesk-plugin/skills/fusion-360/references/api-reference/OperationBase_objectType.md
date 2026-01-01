# OperationBase.objectType Property

Parent Object: [OperationBase](OperationBase.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationBase\_var" is a variable referencing an OperationBase object.  ```` ``` # Get the value of the property. propertyValue = operationBase_var.objectType ``` ```` |

"operationBase\_var" is a variable referencing an OperationBase object. ```` ``` #include <Cam/Operations/OperationBase.h>  // Get the value of the property. string propertyValue = operationBase_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |