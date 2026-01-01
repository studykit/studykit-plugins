# TrimFeature.entityToken Property

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a TrimFeature object.  ```` ``` # Get the value of the property. propertyValue = trimFeature_var.entityToken ``` ```` |

"trimFeature\_var" is a variable referencing a TrimFeature object. ```` ``` #include <Fusion/Features/TrimFeature.h>  // Get the value of the property. string propertyValue = trimFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |