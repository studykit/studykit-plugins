# SketchText.entityToken Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object.  ```` ``` # Get the value of the property. propertyValue = sketchText_var.entityToken ``` ```` |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. string propertyValue = sketchText_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |