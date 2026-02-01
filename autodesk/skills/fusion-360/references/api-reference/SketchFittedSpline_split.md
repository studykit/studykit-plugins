# SketchFittedSpline.split Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Split a curve at a position specified along the curve

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.  ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  // Uses no optional arguments. returnValue = sketchFittedSpline_var->split(splitPoint);  // Uses optional arguments. returnValue = sketchFittedSpline_var->split(splitPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns the resulting 2 curves; the orginal curve + the newly created curve When split spline the original is deleted and two new curves returned. Empty collection returned if curve is closed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splitPoint | [Point3D](Point3D.htm) | A position (transient Point3D) on the curve that defines the point at which to split the curve |
| createConstraints | boolean | Constraints are created by default. Specify false to create no constraints.   This is an optional argument whose default value is True. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |