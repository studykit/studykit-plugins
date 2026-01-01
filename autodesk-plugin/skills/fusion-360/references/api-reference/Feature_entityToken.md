# Feature.entityToken Property

Parent Object: [Feature](Feature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Feature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"feature\_var" is a variable referencing a Feature object.  ```` ``` # Get the value of the property. propertyValue = feature_var.entityToken ``` ```` |

"feature\_var" is a variable referencing a Feature object. ```` ``` #include <Fusion/Features/Feature.h>  // Get the value of the property. string propertyValue = feature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |