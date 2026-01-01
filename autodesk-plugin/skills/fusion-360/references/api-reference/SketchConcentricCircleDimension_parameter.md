# SketchConcentricCircleDimension.parameter Property

Parent Object: [SketchConcentricCircleDimension](SketchConcentricCircleDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConcentricCircleDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. |

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. ```` ``` #include <Fusion/Sketch/SketchConcentricCircleDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchConcentricCircleDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |