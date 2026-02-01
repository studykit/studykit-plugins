# Cylinder.objectType Property

Parent Object: [Cylinder](Cylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinder\_var" is a variable referencing a Cylinder object.  ```` ``` # Get the value of the property. propertyValue = cylinder_var.objectType ``` ```` |

"cylinder\_var" is a variable referencing a Cylinder object. ```` ``` #include <Core/Geometry/Cylinder.h>  // Get the value of the property. string propertyValue = cylinder_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |