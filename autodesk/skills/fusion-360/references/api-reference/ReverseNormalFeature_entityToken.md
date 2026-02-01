# ReverseNormalFeature.entityToken Property

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object.  ```` ``` # Get the value of the property. propertyValue = reverseNormalFeature_var.entityToken ``` ```` |

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. ```` ``` #include <Fusion/Features/ReverseNormalFeature.h>  // Get the value of the property. string propertyValue = reverseNormalFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |