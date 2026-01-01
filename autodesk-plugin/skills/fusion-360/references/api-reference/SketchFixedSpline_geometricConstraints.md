# SketchFixedSpline.geometricConstraints Property

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Returns the sketch constraints that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object. |

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object. ```` ``` #include <Fusion/Sketch/SketchFixedSpline.h>  // Get the value of the property. Ptr<GeometricConstraintList> propertyValue = sketchFixedSpline_var->geometricConstraints(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricConstraintList](GeometricConstraintList.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |