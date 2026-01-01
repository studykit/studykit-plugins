# EllipticalArc2D.asNurbsCurve Property

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Returns a NURBS curve that is geometrically identical to the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. |

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. ```` ``` #include <Core/Geometry/EllipticalArc2D.h>  // Get the value of the property. Ptr<NurbsCurve2D> propertyValue = ellipticalArc2D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve2D](NurbsCurve2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |