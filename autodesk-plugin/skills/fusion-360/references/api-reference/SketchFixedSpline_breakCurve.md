# SketchFixedSpline.breakCurve Method

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchFixedSpline.h>  // Uses no optional arguments. returnValue = sketchFixedSpline_var->breakCurve(segmentPoint);  // Uses optional arguments. returnValue = sketchFixedSpline_var->breakCurve(segmentPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | All of the curves resulting from the break are returned in an ObjectCollection. In the case where no intersections are found and as a result the curve is not broken, an empty ObjectCollection is returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| segmentPoint | [Point3D](Point3D.htm) | A point that specifies the segment of the curve that is to be split from the rest of the curve. The nearest intersection(s) to this point define the break location(s). |
| createConstraints | boolean | Optional argument that specifies if constraints should be created between the new curve segments. A value of true indicates constraints will be created.   This is an optional argument whose default value is True. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |