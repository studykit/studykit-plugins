# SketchEntity.sketchDimensions Property

Parent Object: [SketchEntity](SketchEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntity.h>

## Description

Returns the sketch dimensions that are attached to this curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntity\_var" is a variable referencing a SketchEntity object. |

"sketchEntity\_var" is a variable referencing a SketchEntity object. ```` ``` #include <Fusion/Sketch/SketchEntity.h>  // Get the value of the property. Ptr<SketchDimensionList> propertyValue = sketchEntity_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensionList](SketchDimensionList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |