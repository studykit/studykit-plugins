# Polyline3D.evaluator Property

Parent Object: [Polyline3D](Polyline3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline3D.h>

## Description

Returns an evaluator object that lets you perform additional evaluations on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline3D\_var" is a variable referencing a Polyline3D object. |

"polyline3D\_var" is a variable referencing a Polyline3D object. ```` ``` #include <Core/Geometry/Polyline3D.h>  // Get the value of the property. Ptr<CurveEvaluator3D> propertyValue = polyline3D_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [CurveEvaluator3D](CurveEvaluator3D.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |