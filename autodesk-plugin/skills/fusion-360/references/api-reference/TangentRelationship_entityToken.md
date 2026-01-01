# TangentRelationship.entityToken Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Returns a token for the TangentRelationship object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same tangent relationship.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationship_var.entityToken ``` ```` |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. string propertyValue = tangentRelationship_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |