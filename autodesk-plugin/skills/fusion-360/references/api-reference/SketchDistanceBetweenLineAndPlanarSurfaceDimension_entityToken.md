# SketchDistanceBetweenLineAndPlanarSurfaceDimension.entityToken Property

Parent Object: [SketchDistanceBetweenLineAndPlanarSurfaceDimension](SketchDistanceBetweenLineAndPlanarSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var.entityToken ``` ```` |

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>  // Get the value of the property. string propertyValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |