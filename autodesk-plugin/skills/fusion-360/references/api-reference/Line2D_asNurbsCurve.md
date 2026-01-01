# Line2D.asNurbsCurve Property

Parent Object: [Line2D](Line2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line2D.h>

## Description

Returns a NURBS curve that is geometrically identical to the line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line2D\_var" is a variable referencing a Line2D object. |

"line2D\_var" is a variable referencing a Line2D object. ```` ``` #include <Core/Geometry/Line2D.h>  // Get the value of the property. Ptr<NurbsCurve2D> propertyValue = line2D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve2D](NurbsCurve2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |