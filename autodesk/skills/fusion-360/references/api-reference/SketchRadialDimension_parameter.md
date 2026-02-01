# SketchRadialDimension.parameter Property

Parent Object: [SketchRadialDimension](SketchRadialDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchRadialDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. |

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. ```` ``` #include <Fusion/Sketch/SketchRadialDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchRadialDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |