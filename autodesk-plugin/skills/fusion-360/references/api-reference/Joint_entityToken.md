# Joint.entityToken Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Returns a token for the Joint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.entityToken ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. string propertyValue = joint_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |