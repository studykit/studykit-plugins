# OperationInput.objectType Property

Parent Object: [OperationInput](OperationInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationInput\_var" is a variable referencing an OperationInput object.  ```` ``` # Get the value of the property. propertyValue = operationInput_var.objectType ``` ```` |

"operationInput\_var" is a variable referencing an OperationInput object. ```` ``` #include <Cam/Operations/OperationInput.h>  // Get the value of the property. string propertyValue = operationInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |