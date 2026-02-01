# SketchTangentDistanceDimension.parameter Property

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. |

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. ```` ``` #include <Fusion/Sketch/SketchTangentDistanceDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchTangentDistanceDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |