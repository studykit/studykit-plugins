# SketchOffsetCurvesDimension.offsetConstraint Property

Parent Object: [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetCurvesDimension.h>

## Description

Returns the OffsetConstraint object that defines the curve offset. From the constraint you can get the original curves, the offset curves, and the dimension controlling the offset distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. |

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetCurvesDimension.h>  // Get the value of the property. Ptr<OffsetConstraint> propertyValue = sketchOffsetCurvesDimension_var->offsetConstraint(); ``` ```` |

## Property Value

This is a read only property whose value is an [OffsetConstraint](OffsetConstraint.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |