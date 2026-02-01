# MoveFeature.entityToken Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object.  ```` ``` # Get the value of the property. propertyValue = moveFeature_var.entityToken ``` ```` |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. string propertyValue = moveFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |