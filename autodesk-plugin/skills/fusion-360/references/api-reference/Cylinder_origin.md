# Cylinder.origin Property

Parent Object: [Cylinder](Cylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

The origin point (center) of the base of the cylinder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinder\_var" is a variable referencing a Cylinder object. |

"cylinder\_var" is a variable referencing a Cylinder object. ```` ``` #include <Core/Geometry/Cylinder.h>  // Get the value of the property. Ptr<Point3D> propertyValue = cylinder_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = cylinder_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |