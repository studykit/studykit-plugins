# SketchFittedSpline.getTangentHandle Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns the sketch line that acts as the handle to control the tangency at the specified fit point. Returns null in the case where the tangent handle has not been activated at that sketch point. Deleting the returned line will deactivate the tangent handle. Use the activateTangentHandle method to activate the tangent handle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` returnValue = sketchFittedSpline_var.getTangentHandle(fitPoint) ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLine](SketchLine.htm) | Returns the sketch line that acts as the handle to control the tangency at the specified point or returns null in the case where the tangency handle has not been activated at the specified sketch point. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fitPoint | [SketchPoint](SketchPoint.htm) | The fit point on the curve where you want to get the tangent handle. The fit points can be obtained by using the fitPoints property of the SketchFittedSpline object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch spline through points creation and relative functions API Sample](SketchSplineThroughPoints_Sample.htm) | Create a sketch spline with points and use some operations for spline tangent handle & curvature handle. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |