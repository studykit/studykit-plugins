# NurbsCurve2D.objectType Property

Parent Object: [NurbsCurve2D](NurbsCurve2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve2D\_var" is a variable referencing a NurbsCurve2D object.  ```` ``` # Get the value of the property. propertyValue = nurbsCurve2D_var.objectType ``` ```` |

"nurbsCurve2D\_var" is a variable referencing a NurbsCurve2D object. ```` ``` #include <Core/Geometry/NurbsCurve2D.h>  // Get the value of the property. string propertyValue = nurbsCurve2D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |