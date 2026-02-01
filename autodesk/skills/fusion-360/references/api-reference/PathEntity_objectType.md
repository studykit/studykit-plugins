# PathEntity.objectType Property

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a PathEntity object.  ```` ``` # Get the value of the property. propertyValue = pathEntity_var.objectType ``` ```` |

"pathEntity\_var" is a variable referencing a PathEntity object. ```` ``` #include <Fusion/Features/PathEntity.h>  // Get the value of the property. string propertyValue = pathEntity_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |