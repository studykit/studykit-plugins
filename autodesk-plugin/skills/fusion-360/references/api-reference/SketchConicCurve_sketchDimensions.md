# SketchConicCurve.sketchDimensions Property

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Returns the sketch dimensions that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. |

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Get the value of the property. Ptr<SketchDimensionList> propertyValue = sketchConicCurve_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensionList](SketchDimensionList.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |