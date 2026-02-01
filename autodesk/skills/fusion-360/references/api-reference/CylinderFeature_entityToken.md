# CylinderFeature.entityToken Property

Parent Object: [CylinderFeature](CylinderFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeature\_var" is a variable referencing a CylinderFeature object.  ```` ``` # Get the value of the property. propertyValue = cylinderFeature_var.entityToken ``` ```` |

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. ```` ``` #include <Fusion/Features/CylinderFeature.h>  // Get the value of the property. string propertyValue = cylinderFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |