# ClearanceHoleInfo.objectType Property

Parent Object: [ClearanceHoleInfo](ClearanceHoleInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ClearanceHoleInfo.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"clearanceHoleInfo\_var" is a variable referencing a ClearanceHoleInfo object.  ```` ``` # Get the value of the property. propertyValue = clearanceHoleInfo_var.objectType ``` ```` |

"clearanceHoleInfo\_var" is a variable referencing a ClearanceHoleInfo object. ```` ``` #include <Fusion/Features/ClearanceHoleInfo.h>  // Get the value of the property. string propertyValue = clearanceHoleInfo_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |