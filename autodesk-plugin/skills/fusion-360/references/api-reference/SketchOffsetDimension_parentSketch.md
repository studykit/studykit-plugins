# SketchOffsetDimension.parentSketch Property

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. |

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetDimension.h>  // Get the value of the property. Ptr<Sketch> propertyValue = sketchOffsetDimension_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |