# BossFeatures.objectType Property

Parent Object: [BossFeatures](BossFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatures\_var" is a variable referencing a BossFeatures object.  ```` ``` # Get the value of the property. propertyValue = bossFeatures_var.objectType ``` ```` |

"bossFeatures\_var" is a variable referencing a BossFeatures object. ```` ``` #include <Fusion/Plastic/BossFeatures.h>  // Get the value of the property. string propertyValue = bossFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |