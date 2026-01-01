# SketchDiameterDimension.value Property

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDiameterDimension_var.value  # Set the value of the property. sketchDiameterDimension_var.value = propertyValue ``` ```` |

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchDiameterDimension.h>  // Get the value of the property. double propertyValue = sketchDiameterDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchDiameterDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |