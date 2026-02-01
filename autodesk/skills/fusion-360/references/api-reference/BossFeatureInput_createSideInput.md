# BossFeatureInput.createSideInput Method

Parent Object: [BossFeatureInput](BossFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureInput.h>

## Description

Creates a new BossFeatureSideInput object that is used to specify the input for boss feature side. This object can be set to side1 or side2. Side1 is meant to be side where screw head engages with the boss and Side2 is meant to be a side where screw thread engages with the part or metal inserts.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureInput\_var" is a variable referencing a [BossFeatureInput](BossFeatureInput.htm) object.```` ``` returnValue = bossFeatureInput_var.createSideInput() ``` ```` |

"bossFeatureInput\_var" is a variable referencing a [BossFeatureInput](BossFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BossFeatureSideInput](BossFeatureSideInput.htm) | Returns BossFeatureSideInput if successful. |

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