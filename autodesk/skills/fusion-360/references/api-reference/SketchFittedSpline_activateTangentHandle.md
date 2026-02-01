# SketchFittedSpline.activateTangentHandle Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Activates the tangent handle for the specified fit point and returns the sketch line that acts as the handle to control the tangency. You can use the getTangentHandle property to determine if the tangent handle has already been activated. If this method is called for a handle that already exists, nothing changes and the existing sketch line that acts as the tangent handle is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` returnValue = sketchFittedSpline_var.activateTangentHandle(fitPoint) ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  returnValue = sketchFittedSpline_var->activateTangentHandle(fitPoint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLine](SketchLine.htm) | Returns the sketch line that acts as the tangent handle at the specified fit point. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fitPoint | [SketchPoint](SketchPoint.htm) | The fit point on the curve where you want to activate the tangent handle. The fit points can be obtained by using the fitPoints property of the SketchFittedSpline object. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |