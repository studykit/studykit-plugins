# SketchFixedSpline.trim Method

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Trim a curve by specifying a point that determines the segment of the curve to trim away

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchFixedSpline.h>  // Uses no optional arguments. returnValue = sketchFixedSpline_var->trim(segmentPoint);  // Uses optional arguments. returnValue = sketchFixedSpline_var->trim(segmentPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | When trimming the start or end side of a line, unclosed circular or elliptical arc, the original entity is modified and returned When trimming the middle of a line, unclosed circular or elliptical arc the original entity is deleted and two new entities are returned When trimming the start or end of any type of closed curve, the original is deleted and a new curve is returned Any trimming of a spline (open or closed) deletes the original and new spline/s are returned Trimming a curve having no intersections deletes the original and returns an empty collection |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| segmentPoint | [Point3D](Point3D.htm) | A point (transient Point3D) on or closest to the segment of the curve to remove. (start, end or middle) The segment of the curve closest to the segmentPoint gets removed |
| createConstraints | boolean | Constraints are created by default. Specify false to not create constraints.   This is an optional argument whose default value is True. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |