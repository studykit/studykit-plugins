# SketchDistanceBetweenPointAndSurfaceDimension.entityToken Property

Parent Object: [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var.entityToken ``` ```` |

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>  // Get the value of the property. string propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |