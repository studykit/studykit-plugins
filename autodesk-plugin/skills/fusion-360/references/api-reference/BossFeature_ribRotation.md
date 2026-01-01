# BossFeature.ribRotation Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Returns the model parameter controlling rotation angle of the first rib from the reference vector. For selected sketch point(s) the direction of reference vector is X-axis of the parent sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = bossFeature_var->ribRotation(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |