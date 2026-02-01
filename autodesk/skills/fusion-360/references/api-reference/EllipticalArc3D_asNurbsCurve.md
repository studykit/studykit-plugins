# EllipticalArc3D.asNurbsCurve Property

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Returns a NURBS curve that is geometrically identical to the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. |

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. ```` ``` #include <Core/Geometry/EllipticalArc3D.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = ellipticalArc3D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |