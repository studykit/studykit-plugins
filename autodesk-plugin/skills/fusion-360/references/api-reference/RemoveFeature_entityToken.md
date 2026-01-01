# RemoveFeature.entityToken Property

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a RemoveFeature object.  ```` ``` # Get the value of the property. propertyValue = removeFeature_var.entityToken ``` ```` |

"removeFeature\_var" is a variable referencing a RemoveFeature object. ```` ``` #include <Fusion/Features/RemoveFeature.h>  // Get the value of the property. string propertyValue = removeFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |