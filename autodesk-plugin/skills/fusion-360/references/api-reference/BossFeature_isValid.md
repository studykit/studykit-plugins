# BossFeature.isValid Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object. |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. boolean propertyValue = bossFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |