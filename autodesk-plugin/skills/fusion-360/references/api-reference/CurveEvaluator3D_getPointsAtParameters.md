# CurveEvaluator3D.getPointsAtParameters Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get the points on the curve that correspond to evaluating a set of parameter positions on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the points were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameters | double[] | The array of parameter positions to evaluate the curve position at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents. |
| points | Point3D[] | The output array of curve positions corresponding to evaluating the curve at that parameter position. The length of this array will be equal to the length of the parameters array specified. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |