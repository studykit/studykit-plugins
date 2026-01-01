# SketchAngularDimension.value Property

Parent Object: [SketchAngularDimension](SketchAngularDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchAngularDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchAngularDimension_var.value  # Set the value of the property. sketchAngularDimension_var.value = propertyValue ``` ```` |

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object. ```` ``` #include <Fusion/Sketch/SketchAngularDimension.h>  // Get the value of the property. double propertyValue = sketchAngularDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchAngularDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |