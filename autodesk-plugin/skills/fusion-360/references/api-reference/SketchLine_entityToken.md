# SketchLine.entityToken Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object.  ```` ``` # Get the value of the property. propertyValue = sketchLine_var.entityToken ``` ```` |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. string propertyValue = sketchLine_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |