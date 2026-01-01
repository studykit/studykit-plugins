# BossFeatureSideInput.ribType Property

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Type of boss ribs this feature represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. |

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Get the value of the property. BossRibShapeTypes propertyValue = bossFeatureSideInput_var->ribType();  // Set the value of the property, where value_var is a BossRibShapeTypes. bool returnValue = bossFeatureSideInput_var->ribType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BossRibShapeTypes](BossRibShapeTypes.htm).

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