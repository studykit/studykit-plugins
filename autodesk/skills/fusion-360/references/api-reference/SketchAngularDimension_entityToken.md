# SketchAngularDimension.entityToken Property

Parent Object: [SketchAngularDimension](SketchAngularDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchAngularDimension.h>

## Description

Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchAngularDimension_var.entityToken ``` ```` |

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object. ```` ``` #include <Fusion/Sketch/SketchAngularDimension.h>  // Get the value of the property. string propertyValue = sketchAngularDimension_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |