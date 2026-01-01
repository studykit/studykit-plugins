# EllipticalCone.origin Property

Parent Object: [EllipticalCone](EllipticalCone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCone.h>

## Description

Gets and sets the origin point (center) of the base of the cone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. |

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. ```` ``` #include <Core/Geometry/EllipticalCone.h>  // Get the value of the property. Ptr<Point3D> propertyValue = ellipticalCone_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = ellipticalCone_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |