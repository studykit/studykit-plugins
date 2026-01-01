# CurveEvaluator2D.getPointAtParameter Method

Parent Object: [CurveEvaluator2D](CurveEvaluator2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

Get the point on the curve that corresponds to evaluating a parameter position on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator2D\_var" is a variable referencing a [CurveEvaluator2D](CurveEvaluator2D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the point was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter position to evaluate the curve position at. The parameter value must be within the range of the parameter extents as provided by getParameterExtents. |
| point | [Point2D](Point2D.htm) | The output curve position corresponding to evaluating the curve at that parameter position. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |