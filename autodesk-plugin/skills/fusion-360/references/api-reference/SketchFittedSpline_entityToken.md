# SketchFittedSpline.entityToken Property

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object.  ```` ``` # Get the value of the property. propertyValue = sketchFittedSpline_var.entityToken ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  // Get the value of the property. string propertyValue = sketchFittedSpline_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |