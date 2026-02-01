# EllipticalArc3D.center Property

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Gets and sets the center point of the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. |

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. ```` ``` #include <Core/Geometry/EllipticalArc3D.h>  // Get the value of the property. Ptr<Point3D> propertyValue = ellipticalArc3D_var->center();  // Set the value of the property, where value_var is a Point3D. bool returnValue = ellipticalArc3D_var->center(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |