# Cone.objectType Property

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cone\_var" is a variable referencing a Cone object.  ```` ``` # Get the value of the property. propertyValue = cone_var.objectType ``` ```` |

"cone\_var" is a variable referencing a Cone object. ```` ``` #include <Core/Geometry/Cone.h>  // Get the value of the property. string propertyValue = cone_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |