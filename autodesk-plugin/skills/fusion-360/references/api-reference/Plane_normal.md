# Plane.normal Property

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Gets and sets the normal of the plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a Plane object. |

"plane\_var" is a variable referencing a Plane object. ```` ``` #include <Core/Geometry/Plane.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = plane_var->normal();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = plane_var->normal(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |