# BossFeatureSideInput.setRibExtent Method

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Set rib extent type for particular rib for position point provided.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a [BossFeatureSideInput](BossFeatureSideInput.htm) object.```` ``` returnValue = bossFeatureSideInput_var.setRibExtent(position, ribExtentTypes) ``` ```` |

"bossFeatureSideInput\_var" is a variable referencing a [BossFeatureSideInput](BossFeatureSideInput.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| position | [Base](Base.htm) | Position point object for the rib extent types provided |
| ribExtentTypes | integer[] | Vector of BossRibExtentTypes for individual rib based on rib count input. |

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