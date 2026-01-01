# SketchControlPointSpline.addControlPoint Method

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Adds an additional control point to the control point spline. Inserting a new control point does not change the shape of the curve, but the control frame will be re-computed and the control points will be adjusted to maintain the current shape.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a [SketchControlPointSpline](SketchControlPointSpline.htm) object.```` ``` returnValue = sketchControlPointSpline_var.addControlPoint(parameter) ``` ```` |

"sketchControlPointSpline\_var" is a variable referencing a [SketchControlPointSpline](SketchControlPointSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  returnValue = sketchControlPointSpline_var->addControlPoint(parameter); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if adding the control point was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter position that defines where to insert the new control point. The parameter value must be within the parametric range of the curve. This can be determined by using the getParameterExtents method of the CurveEvaluator3D returned by the evaluator property. |

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |