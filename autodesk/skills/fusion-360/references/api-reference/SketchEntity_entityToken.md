# SketchEntity.entityToken Property

Parent Object: [SketchEntity](SketchEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntity.h>

## Description

Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntity\_var" is a variable referencing a SketchEntity object.  ```` ``` # Get the value of the property. propertyValue = sketchEntity_var.entityToken ``` ```` |

"sketchEntity\_var" is a variable referencing a SketchEntity object. ```` ``` #include <Fusion/Sketch/SketchEntity.h>  // Get the value of the property. string propertyValue = sketchEntity_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |