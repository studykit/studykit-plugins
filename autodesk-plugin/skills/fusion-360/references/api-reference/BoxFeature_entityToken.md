# BoxFeature.entityToken Property

Parent Object: [BoxFeature](BoxFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeature\_var" is a variable referencing a BoxFeature object.  ```` ``` # Get the value of the property. propertyValue = boxFeature_var.entityToken ``` ```` |

"boxFeature\_var" is a variable referencing a BoxFeature object. ```` ``` #include <Fusion/Features/BoxFeature.h>  // Get the value of the property. string propertyValue = boxFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |