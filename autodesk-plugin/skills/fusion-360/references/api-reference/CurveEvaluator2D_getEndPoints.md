# CurveEvaluator2D.getEndPoints Method

Parent Object: [CurveEvaluator2D](CurveEvaluator2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

Get the end points of the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator2D\_var" is a variable referencing a [CurveEvaluator2D](CurveEvaluator2D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the end points were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Point2D](Point2D.htm) | The output start point of the curve. If the curve is unbounded at the start, this value will be null. |
| endPoint | [Point2D](Point2D.htm) | The output end point of the curve. If the curve is unbounded at the end, this value will be null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |