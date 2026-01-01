# Sphere.origin Property

Parent Object: [Sphere](Sphere.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Sphere.h>

## Description

Gets and sets the origin point (center) of the sphere.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphere\_var" is a variable referencing a Sphere object. |

"sphere\_var" is a variable referencing a Sphere object. ```` ``` #include <Core/Geometry/Sphere.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sphere_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sphere_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |