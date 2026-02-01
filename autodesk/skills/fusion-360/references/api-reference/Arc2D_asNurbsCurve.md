# Arc2D.asNurbsCurve Property

Parent Object: [Arc2D](Arc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc2D.h>

## Description

Returns a NURBS curve that is geometrically identical to the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc2D\_var" is a variable referencing an Arc2D object. |

"arc2D\_var" is a variable referencing an Arc2D object. ```` ``` #include <Core/Geometry/Arc2D.h>  // Get the value of the property. Ptr<NurbsCurve2D> propertyValue = arc2D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve2D](NurbsCurve2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |