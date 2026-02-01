# SketchEllipseMinorRadiusDimension.value Property

Parent Object: [SketchEllipseMinorRadiusDimension](SketchEllipseMinorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchEllipseMinorRadiusDimension_var.value  # Set the value of the property. sketchEllipseMinorRadiusDimension_var.value = propertyValue ``` ```` |

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>  // Get the value of the property. double propertyValue = sketchEllipseMinorRadiusDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchEllipseMinorRadiusDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |