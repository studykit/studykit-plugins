# SketchOffsetDimension.parameter Property

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. |

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchOffsetDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |