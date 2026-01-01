# SketchDimension.value Property

Parent Object: [SketchDimension](SketchDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimension\_var" is a variable referencing a SketchDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDimension_var.value  # Set the value of the property. sketchDimension_var.value = propertyValue ``` ```` |

"sketchDimension\_var" is a variable referencing a SketchDimension object. ```` ``` #include <Fusion/Sketch/SketchDimension.h>  // Get the value of the property. double propertyValue = sketchDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |