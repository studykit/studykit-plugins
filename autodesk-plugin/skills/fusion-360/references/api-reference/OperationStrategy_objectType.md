# OperationStrategy.objectType Property

Parent Object: [OperationStrategy](OperationStrategy.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationStrategy.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationStrategy\_var" is a variable referencing an OperationStrategy object.  ```` ``` # Get the value of the property. propertyValue = operationStrategy_var.objectType ``` ```` |

"operationStrategy\_var" is a variable referencing an OperationStrategy object. ```` ``` #include <Cam/Operations/OperationStrategy.h>  // Get the value of the property. string propertyValue = operationStrategy_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |