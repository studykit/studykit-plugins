# OffsetFacesFeature.entityToken Property

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object.  ```` ``` # Get the value of the property. propertyValue = offsetFacesFeature_var.entityToken ``` ```` |

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. ```` ``` #include <Fusion/Features/OffsetFacesFeature.h>  // Get the value of the property. string propertyValue = offsetFacesFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |