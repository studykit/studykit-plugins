# SketchEllipticalArc.sketchDimensions Property

Parent Object: [SketchEllipticalArc](SketchEllipticalArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

Returns the sketch dimensions that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. |

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. ```` ``` #include <Fusion/Sketch/SketchEllipticalArc.h>  // Get the value of the property. Ptr<SketchDimensionList> propertyValue = sketchEllipticalArc_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensionList](SketchDimensionList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |