# RigidGroup.entityToken Property

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Returns a token for the RigidGroup object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same rigid group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a RigidGroup object.  ```` ``` # Get the value of the property. propertyValue = rigidGroup_var.entityToken ``` ```` |

"rigidGroup\_var" is a variable referencing a RigidGroup object. ```` ``` #include <Fusion/Components/RigidGroup.h>  // Get the value of the property. string propertyValue = rigidGroup_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |