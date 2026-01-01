# SketchDistanceBetweenLineAndPlanarSurfaceDimension.value Property

Parent Object: [SketchDistanceBetweenLineAndPlanarSurfaceDimension](SketchDistanceBetweenLineAndPlanarSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>

## Description

Gets and sets the current value of the sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var.value  # Set the value of the property. sketchDistanceBetweenLineAndPlanarSurfaceDimension_var.value = propertyValue ``` ```` |

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>  // Get the value of the property. double propertyValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |