# SketchDiameterDimension.entityToken Property

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchDiameterDimension_var.entityToken ``` ```` |

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchDiameterDimension.h>  // Get the value of the property. string propertyValue = sketchDiameterDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |