# EllipticalArc3D.normal Property

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Gets the normal of the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. |

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. ```` ``` #include <Core/Geometry/EllipticalArc3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ellipticalArc3D_var->normal(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |