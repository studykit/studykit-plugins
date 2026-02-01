# SketchOffsetDimension.entityToken Property

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchOffsetDimension_var.entityToken ``` ```` |

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetDimension.h>  // Get the value of the property. string propertyValue = sketchOffsetDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |