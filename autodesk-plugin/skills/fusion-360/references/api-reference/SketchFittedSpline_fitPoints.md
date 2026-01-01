# SketchFittedSpline.fitPoints Property

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns the set of sketch points that the spline fits through. The points include the start and end points and are returned in the same order as the spline fits through them where the first point in the list is the start point and the last point is the end point. Editing the position of these sketch points will result in editing the spline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. |

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  // Get the value of the property. Ptr<SketchPointList> propertyValue = sketchFittedSpline_var->fitPoints(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPointList](SketchPointList.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch spline through points creation and relative functions API Sample](SketchSplineThroughPoints_Sample.htm) | Create a sketch spline with points and use some operations for spline tangent handle & curvature handle. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |