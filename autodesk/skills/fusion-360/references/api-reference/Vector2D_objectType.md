# Vector2D.objectType Property

Parent Object: [Vector2D](Vector2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector2D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"vector2D\_var" is a variable referencing a Vector2D object.  ```` ``` # Get the value of the property. propertyValue = vector2D_var.objectType ``` ```` |

"vector2D\_var" is a variable referencing a Vector2D object. ```` ``` #include <Core/Geometry/Vector2D.h>  // Get the value of the property. string propertyValue = vector2D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |