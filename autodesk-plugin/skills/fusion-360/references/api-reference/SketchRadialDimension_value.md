# SketchRadialDimension.value Property

Parent Object: [SketchRadialDimension](SketchRadialDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchRadialDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchRadialDimension_var.value  # Set the value of the property. sketchRadialDimension_var.value = propertyValue ``` ```` |

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. ```` ``` #include <Fusion/Sketch/SketchRadialDimension.h>  // Get the value of the property. double propertyValue = sketchRadialDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchRadialDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |