# SketchPoint.geometricConstraints Property

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

Returns the sketch constraints that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a SketchPoint object. |

"sketchPoint\_var" is a variable referencing a SketchPoint object. ```` ``` #include <Fusion/Sketch/SketchPoint.h>  // Get the value of the property. Ptr<GeometricConstraintList> propertyValue = sketchPoint_var->geometricConstraints(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricConstraintList](GeometricConstraintList.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |