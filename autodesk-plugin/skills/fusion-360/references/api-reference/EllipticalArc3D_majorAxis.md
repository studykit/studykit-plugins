# EllipticalArc3D.majorAxis Property

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Gets and sets the major axis of the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. |

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. ```` ``` #include <Core/Geometry/EllipticalArc3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ellipticalArc3D_var->majorAxis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = ellipticalArc3D_var->majorAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |