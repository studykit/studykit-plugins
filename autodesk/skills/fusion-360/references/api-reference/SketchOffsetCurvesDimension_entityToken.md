# SketchOffsetCurvesDimension.entityToken Property

Parent Object: [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetCurvesDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchOffsetCurvesDimension_var.entityToken ``` ```` |

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetCurvesDimension.h>  // Get the value of the property. string propertyValue = sketchOffsetCurvesDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |