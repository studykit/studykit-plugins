# SketchTangentDistanceDimension.value Property

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchTangentDistanceDimension_var.value  # Set the value of the property. sketchTangentDistanceDimension_var.value = propertyValue ``` ```` |

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. ```` ``` #include <Fusion/Sketch/SketchTangentDistanceDimension.h>  // Get the value of the property. double propertyValue = sketchTangentDistanceDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchTangentDistanceDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |