# BossFeatureSideInput.holeExtentType Property

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Get or set hole extent this feature represents. For top side only through hole extent is accepted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. |

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Get the value of the property. BossHoleExtentTypes propertyValue = bossFeatureSideInput_var->holeExtentType();  // Set the value of the property, where value_var is a BossHoleExtentTypes. bool returnValue = bossFeatureSideInput_var->holeExtentType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BossHoleExtentTypes](BossHoleExtentTypes.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boss Feature Sample](BossFeatureSample_Sample.htm) | Demonstrates creating a new boss feature |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |