# Polyline2D.objectType Property

Parent Object: [Polyline2D](Polyline2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline2D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline2D\_var" is a variable referencing a Polyline2D object.  ```` ``` # Get the value of the property. propertyValue = polyline2D_var.objectType ``` ```` |

"polyline2D\_var" is a variable referencing a Polyline2D object. ```` ``` #include <Core/Geometry/Polyline2D.h>  // Get the value of the property. string propertyValue = polyline2D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |