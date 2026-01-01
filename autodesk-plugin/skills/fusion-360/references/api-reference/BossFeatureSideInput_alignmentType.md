# BossFeatureSideInput.alignmentType Property

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Get or set boss alignment shape. This usually corresponds to the alignment shape of the boss counterpart.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. |

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Get the value of the property. BossAlignmentTypes propertyValue = bossFeatureSideInput_var->alignmentType();  // Set the value of the property, where value_var is a BossAlignmentTypes. bool returnValue = bossFeatureSideInput_var->alignmentType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BossAlignmentTypes](BossAlignmentTypes.htm).

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