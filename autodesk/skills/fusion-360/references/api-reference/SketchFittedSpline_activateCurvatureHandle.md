# SketchFittedSpline.activateCurvatureHandle Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Activates the curvature handle for the specified fit point and returns the sketch arc that acts as the handle to control the curvature. You can use the getCurvatureHandle property to determine if the curvature handle has already been activated. If this method is called for a handle that already exists, nothing changes and the existing sketch arc that acts as the curvature handle is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` returnValue = sketchFittedSpline_var.activateCurvatureHandle(fitPoint) ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  returnValue = sketchFittedSpline_var->activateCurvatureHandle(fitPoint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchArc](SketchArc.htm) | Returns the sketch arc that acts as the curvature handle at the specified fit point. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fitPoint | [SketchPoint](SketchPoint.htm) | The fit point on the curve where you want to activate the curvature handle. The fit points can be obtained by using the fitPoints property of the SketchFittedSpline object. |

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