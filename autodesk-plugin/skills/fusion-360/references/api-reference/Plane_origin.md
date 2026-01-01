# Plane.origin Property

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Gets and sets the origin point of the plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a Plane object. |

"plane\_var" is a variable referencing a Plane object. ```` ``` #include <Core/Geometry/Plane.h>  // Get the value of the property. Ptr<Point3D> propertyValue = plane_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = plane_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |