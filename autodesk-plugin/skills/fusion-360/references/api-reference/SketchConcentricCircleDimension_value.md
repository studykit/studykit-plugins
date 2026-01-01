# SketchConcentricCircleDimension.value Property

Parent Object: [SketchConcentricCircleDimension](SketchConcentricCircleDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConcentricCircleDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchConcentricCircleDimension_var.value  # Set the value of the property. sketchConcentricCircleDimension_var.value = propertyValue ``` ```` |

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. ```` ``` #include <Fusion/Sketch/SketchConcentricCircleDimension.h>  // Get the value of the property. double propertyValue = sketchConcentricCircleDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchConcentricCircleDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |