# EllipticalCylinder.origin Property

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Gets and sets the origin point (center) of the base of the cylinder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. |

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. ```` ``` #include <Core/Geometry/EllipticalCylinder.h>  // Get the value of the property. Ptr<Point3D> propertyValue = ellipticalCylinder_var->origin();  // Set the value of the property, where value_var is a Point3D. bool returnValue = ellipticalCylinder_var->origin(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |