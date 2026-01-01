# BossFeature.direction Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Returns the direction of the boss feature with respect to selected position point. For selected sketch point this direction represents a Z-axis of the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = bossFeature_var->direction(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |