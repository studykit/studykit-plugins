# SphereFeature.entityToken Property

Parent Object: [SphereFeature](SphereFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeature\_var" is a variable referencing a SphereFeature object.  ```` ``` # Get the value of the property. propertyValue = sphereFeature_var.entityToken ``` ```` |

"sphereFeature\_var" is a variable referencing a SphereFeature object. ```` ``` #include <Fusion/Features/SphereFeature.h>  // Get the value of the property. string propertyValue = sphereFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |