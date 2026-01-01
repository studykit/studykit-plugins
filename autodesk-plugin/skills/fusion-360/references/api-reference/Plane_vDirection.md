# Plane.vDirection Property

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Gets the V Direction of the plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a Plane object. |

"plane\_var" is a variable referencing a Plane object. ```` ``` #include <Core/Geometry/Plane.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = plane_var->vDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |