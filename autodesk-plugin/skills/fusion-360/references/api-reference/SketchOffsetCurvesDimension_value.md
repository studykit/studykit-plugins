# SketchOffsetCurvesDimension.value Property

Parent Object: [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetCurvesDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchOffsetCurvesDimension_var.value  # Set the value of the property. sketchOffsetCurvesDimension_var.value = propertyValue ``` ```` |

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetCurvesDimension.h>  // Get the value of the property. double propertyValue = sketchOffsetCurvesDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchOffsetCurvesDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |