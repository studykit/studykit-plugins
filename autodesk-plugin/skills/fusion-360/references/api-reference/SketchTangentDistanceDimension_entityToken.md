# SketchTangentDistanceDimension.entityToken Property

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchTangentDistanceDimension_var.entityToken ``` ```` |

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. ```` ``` #include <Fusion/Sketch/SketchTangentDistanceDimension.h>  // Get the value of the property. string propertyValue = sketchTangentDistanceDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |