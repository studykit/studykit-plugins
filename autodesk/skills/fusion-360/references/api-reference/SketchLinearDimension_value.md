# SketchLinearDimension.value Property

Parent Object: [SketchLinearDimension](SketchLinearDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchLinearDimension_var.value  # Set the value of the property. sketchLinearDimension_var.value = propertyValue ``` ```` |

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDimension.h>  // Get the value of the property. double propertyValue = sketchLinearDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchLinearDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |