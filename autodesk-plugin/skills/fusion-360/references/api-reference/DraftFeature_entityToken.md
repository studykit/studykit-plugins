# DraftFeature.entityToken Property

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a DraftFeature object.  ```` ``` # Get the value of the property. propertyValue = draftFeature_var.entityToken ``` ```` |

"draftFeature\_var" is a variable referencing a DraftFeature object. ```` ``` #include <Fusion/Features/DraftFeature.h>  // Get the value of the property. string propertyValue = draftFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |