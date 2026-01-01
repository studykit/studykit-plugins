# NurbsCurve2D.evaluator Property

Parent Object: [NurbsCurve2D](NurbsCurve2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

Returns an evaluator object that lets you perform additional evaluations on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve2D\_var" is a variable referencing a NurbsCurve2D object. |

"nurbsCurve2D\_var" is a variable referencing a NurbsCurve2D object. ```` ``` #include <Core/Geometry/NurbsCurve2D.h>  // Get the value of the property. Ptr<CurveEvaluator2D> propertyValue = nurbsCurve2D_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [CurveEvaluator2D](CurveEvaluator2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |