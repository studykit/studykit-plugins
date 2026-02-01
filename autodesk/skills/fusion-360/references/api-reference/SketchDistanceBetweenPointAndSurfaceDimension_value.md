# SketchDistanceBetweenPointAndSurfaceDimension.value Property

Parent Object: [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var.value  # Set the value of the property. sketchDistanceBetweenPointAndSurfaceDimension_var.value = propertyValue ``` ```` |

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>  // Get the value of the property. double propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchDistanceBetweenPointAndSurfaceDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |