# BossFeatureInput.side1 Property

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

Gets or sets inputs for top side of the boss feature connection. It is the side where screw head engages with the boss. Default Side1 direction is considered direction of Z-axis of the parent sketch for selected position point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. |

"bossFeatureInput\_var" is a variable referencing a BossFeatureInput object. ```` ``` #include <Fusion/Plastic/BossFeatureInput.h>  // Get the value of the property. Ptr<BossFeatureSideInput> propertyValue = bossFeatureInput_var->side1();  // Set the value of the property, where value_var is a BossFeatureSideInput. bool returnValue = bossFeatureInput_var->side1(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BossFeatureSideInput](BossFeatureSideInput.htm).

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