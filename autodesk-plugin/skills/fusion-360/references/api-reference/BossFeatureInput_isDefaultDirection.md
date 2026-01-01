# BossFeatureInput.isDefaultDirection Property

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

Get or set if the boss feature (or boss connection) goes in the default direction or is reversed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. |

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. ```` ``` #include <Fusion/Plastic/BossFeatureInput.h>  // Get the value of the property. boolean propertyValue = bossFeatureInput_var->isDefaultDirection();  // Set the value of the property, where value_var is a boolean. bool returnValue = bossFeatureInput_var->isDefaultDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |