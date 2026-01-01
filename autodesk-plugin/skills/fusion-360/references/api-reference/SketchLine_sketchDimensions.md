# SketchLine.sketchDimensions Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

Returns the sketch dimensions that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object. |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. Ptr<SketchDimensionList> propertyValue = sketchLine_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensionList](SketchDimensionList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |