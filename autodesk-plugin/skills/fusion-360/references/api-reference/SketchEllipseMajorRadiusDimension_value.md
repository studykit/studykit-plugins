# SketchEllipseMajorRadiusDimension.value Property

Parent Object: [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchEllipseMajorRadiusDimension_var.value  # Set the value of the property. sketchEllipseMajorRadiusDimension_var.value = propertyValue ``` ```` |

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>  // Get the value of the property. double propertyValue = sketchEllipseMajorRadiusDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchEllipseMajorRadiusDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |