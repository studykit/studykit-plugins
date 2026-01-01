# SketchFittedSpline.geometricConstraints Property

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns the sketch constraints that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. |

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  // Get the value of the property. Ptr<GeometricConstraintList> propertyValue = sketchFittedSpline_var->geometricConstraints(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricConstraintList](GeometricConstraintList.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |