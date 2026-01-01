# SketchLinearDiameterDimension.entityToken Property

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchLinearDiameterDimension_var.entityToken ``` ```` |

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDiameterDimension.h>  // Get the value of the property. string propertyValue = sketchLinearDiameterDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |