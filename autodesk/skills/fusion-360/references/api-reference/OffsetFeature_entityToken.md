# OffsetFeature.entityToken Property

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an OffsetFeature object.  ```` ``` # Get the value of the property. propertyValue = offsetFeature_var.entityToken ``` ```` |

"offsetFeature\_var" is a variable referencing an OffsetFeature object. ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Get the value of the property. string propertyValue = offsetFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |