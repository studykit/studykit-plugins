# BossFeatureSideInput.holeMajorDraftAngle Property

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Get or set major hole draft angle for counterbore and countersink hole. This input is ignored for blank boss or boss with simple hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. |

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = bossFeatureSideInput_var->holeMajorDraftAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = bossFeatureSideInput_var->holeMajorDraftAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

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