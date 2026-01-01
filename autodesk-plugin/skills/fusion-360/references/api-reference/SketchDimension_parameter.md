# SketchDimension.parameter Property

Parent Object: [SketchDimension](SketchDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimension\_var" is a variable referencing a SketchDimension object. |

"sketchDimension\_var" is a variable referencing a SketchDimension object. ```` ``` #include <Fusion/Sketch/SketchDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |