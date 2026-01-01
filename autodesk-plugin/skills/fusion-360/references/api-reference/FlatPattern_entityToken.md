# FlatPattern.entityToken Property

Parent Object: [FlatPattern](FlatPattern.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPattern\_var" is a variable referencing a FlatPattern object.  ```` ``` # Get the value of the property. propertyValue = flatPattern_var.entityToken ``` ```` |

"flatPattern\_var" is a variable referencing a FlatPattern object. ```` ``` #include <Fusion/SheetMetal/FlatPattern.h>  // Get the value of the property. string propertyValue = flatPattern_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |