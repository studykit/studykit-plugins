# JointOrigin.entityToken Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Returns a token for the JointOrigin object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same joint origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object.  ```` ``` # Get the value of the property. propertyValue = jointOrigin_var.entityToken ``` ```` |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. string propertyValue = jointOrigin_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |