# Operation.objectType Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object.  ```` ``` # Get the value of the property. propertyValue = operation_var.objectType ``` ```` |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. string propertyValue = operation_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |