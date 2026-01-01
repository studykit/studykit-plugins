# SketchControlPointSpline.evaluator Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Returns an evaluator object that lets you perform evaluations on the precise geometry of the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. Ptr<CurveEvaluator3D> propertyValue = sketchControlPointSpline_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [CurveEvaluator3D](CurveEvaluator3D.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |