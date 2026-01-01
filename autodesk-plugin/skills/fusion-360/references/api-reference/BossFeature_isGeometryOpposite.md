# BossFeature.isGeometryOpposite Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Gets if this boss feature instance represents a bottom side where screw thread engages with the part. If this feature instance represents a geometry where screw head engages it returns false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. boolean propertyValue = bossFeature_var->isGeometryOpposite(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |