# SketchLinearDiameterDimension.value Property

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchLinearDiameterDimension_var.value  # Set the value of the property. sketchLinearDiameterDimension_var.value = propertyValue ``` ```` |

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDiameterDimension.h>  // Get the value of the property. double propertyValue = sketchLinearDiameterDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchLinearDiameterDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |