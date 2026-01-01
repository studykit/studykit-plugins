# RevolveFeature.entityToken Property

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a RevolveFeature object.  ```` ``` # Get the value of the property. propertyValue = revolveFeature_var.entityToken ``` ```` |

"revolveFeature\_var" is a variable referencing a RevolveFeature object. ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Get the value of the property. string propertyValue = revolveFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |