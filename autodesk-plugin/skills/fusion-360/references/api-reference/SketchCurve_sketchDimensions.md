# SketchCurve.sketchDimensions Property

Parent Object: [SketchCurve](SketchCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

Returns the sketch dimensions that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurve\_var" is a variable referencing a SketchCurve object. |

"sketchCurve\_var" is a variable referencing a SketchCurve object. ```` ``` #include <Fusion/Sketch/SketchCurve.h>  // Get the value of the property. Ptr<SketchDimensionList> propertyValue = sketchCurve_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensionList](SketchDimensionList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |