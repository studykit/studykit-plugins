# Operations.objectType Property

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an Operations object.  ```` ``` # Get the value of the property. propertyValue = operations_var.objectType ``` ```` |

"operations\_var" is a variable referencing an Operations object. ```` ``` #include <Cam/Operations/Operations.h>  // Get the value of the property. string propertyValue = operations_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |