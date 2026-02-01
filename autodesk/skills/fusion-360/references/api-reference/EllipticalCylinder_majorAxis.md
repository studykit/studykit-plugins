# EllipticalCylinder.majorAxis Property

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Gets and sets the direction of the major axis of the ellipse that defines the cylinder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. |

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. ```` ``` #include <Core/Geometry/EllipticalCylinder.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ellipticalCylinder_var->majorAxis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = ellipticalCylinder_var->majorAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |