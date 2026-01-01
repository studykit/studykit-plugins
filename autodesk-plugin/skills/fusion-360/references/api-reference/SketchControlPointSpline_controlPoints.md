# SketchControlPointSpline.controlPoints Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Returns the set of sketch points that the control frame of the spline fits through. The points include the start and end points and are returned in the same order as the spline fits through them where the first point in the list is the start point and the last point is the end point. Editing the position of these sketch points will result in editing the spline.

## Remarks

There are cases, like when a curve is offset, where a control point spline is created but the control frame is not displayed and the curve is not editable. You can check for this case by checking the value of the isControlFrameDisplayed property. If it is true, this property will return an empty array of control points since they do not currently exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object.  ```` ``` # Get the value of the property. propertyValue = sketchControlPointSpline_var.controlPoints ``` ```` |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. std::vector<Ptr<SketchPoint>> propertyValue = sketchControlPointSpline_var->controlPoints(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchPoint](SketchPoint.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |