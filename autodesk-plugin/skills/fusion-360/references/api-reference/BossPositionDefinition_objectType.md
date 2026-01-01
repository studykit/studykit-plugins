# BossPositionDefinition.objectType Property

Parent Object: [BossPositionDefinition](BossPositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossPositionDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossPositionDefinition\_var" is a variable referencing a BossPositionDefinition object.  ```` ``` # Get the value of the property. propertyValue = bossPositionDefinition_var.objectType ``` ```` |

"bossPositionDefinition\_var" is a variable referencing a BossPositionDefinition object. ```` ``` #include <Fusion/Plastic/BossPositionDefinition.h>  // Get the value of the property. string propertyValue = bossPositionDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |