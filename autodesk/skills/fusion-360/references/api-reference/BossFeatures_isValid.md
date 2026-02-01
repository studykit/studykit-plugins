# BossFeatures.isValid Property

Parent Object: [BossFeatures](BossFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatures\_var" is a variable referencing a BossFeatures object. |

"bossFeatures\_var" is a variable referencing a BossFeatures object. ```` ``` #include <Fusion/Plastic/BossFeatures.h>  // Get the value of the property. boolean propertyValue = bossFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |