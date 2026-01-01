# CurveEvaluator2D.getCurvature Method

Parent Object: [CurveEvaluator2D](CurveEvaluator2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

Get the curvature value at a parameter position on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator2D\_var" is a variable referencing a [CurveEvaluator2D](CurveEvaluator2D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the curvature was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter position to return the curvature information at. This value must be within the range of the parameter extents as provided by getParameterExtents. |
| direction | [Vector2D](Vector2D.htm) | The output direction of the curvature at the position on the curve. |
| curvature | double | The output magnitude of the curvature at the position on the curve. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |