# SketchFittedSpline.getCurvatureHandle Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns the sketch arc that acts as the handle to control the curvature at the specified fit point. Returns null in the case where the curvature handle has not been activated at that sketch point. Deleting the returned arc will deactivate the curvature handle. Use the activateCurvatureHandle method to activate the curvature handle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` returnValue = sketchFittedSpline_var.getCurvatureHandle(fitPoint) ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchArc](SketchArc.htm) | Returns the sketch arc that acts as the handle to control the curvature at the specified point or returns null in the case where the curvature handle has not been activated at the specified sketch point. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fitPoint | [SketchPoint](SketchPoint.htm) | The fit point on the curve where you want to get the curvature handle. The fit points can be obtained by using the fitPoints property of the SketchFittedSpline object. |

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