# BossFeature.holeDepth Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Returns the model parameter controlling the hole depth with respect to hole extent type. If hole extent type is set to BossHoleThrough parameter not used. If hole extent type is BossBlindFull the parameter is a distance from farthest face. If hole extent type is set to BossBlindDepth the parameter is a distance from start face of the hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = bossFeature_var->holeDepth(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |