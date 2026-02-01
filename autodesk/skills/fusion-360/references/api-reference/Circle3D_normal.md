# Circle3D.normal Property

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Gets and sets the normal of the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle3D\_var" is a variable referencing a Circle3D object. |

"circle3D\_var" is a variable referencing a Circle3D object. ```` ``` #include <Core/Geometry/Circle3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = circle3D_var->normal();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = circle3D_var->normal(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |