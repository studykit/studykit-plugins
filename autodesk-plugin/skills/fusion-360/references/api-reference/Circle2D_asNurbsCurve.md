# Circle2D.asNurbsCurve Property

Parent Object: [Circle2D](Circle2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle2D.h>

## Description

Returns a NURBS curve that is geometrically identical to the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle2D\_var" is a variable referencing a Circle2D object. |

"circle2D\_var" is a variable referencing a Circle2D object. ```` ``` #include <Core/Geometry/Circle2D.h>  // Get the value of the property. Ptr<NurbsCurve2D> propertyValue = circle2D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve2D](NurbsCurve2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |