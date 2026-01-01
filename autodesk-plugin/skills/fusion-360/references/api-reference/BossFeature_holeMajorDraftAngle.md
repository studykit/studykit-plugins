# BossFeature.holeMajorDraftAngle Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Returns the model parameter controlling major hole draft angle for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = bossFeature_var->holeMajorDraftAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |