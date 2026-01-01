# BossFeatureSideInput.setCountersink Method

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Set boss shape into constant diameter shank with countersink hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a [BossFeatureSideInput](BossFeatureSideInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"bossFeatureSideInput\_var" is a variable referencing a [BossFeatureSideInput](BossFeatureSideInput.htm) object.  ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Uses no optional arguments. returnValue = bossFeatureSideInput_var->setCountersink(diameter, holeDiameter, holeMajorDiameter, depth);  // Uses optional arguments. returnValue = bossFeatureSideInput_var->setCountersink(diameter, holeDiameter, holeMajorDiameter, depth, countersinkAngle); ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| diameter | [ValueInput](ValueInput.htm) | The outside diameter for the boss feature shank. |
| holeDiameter | [ValueInput](ValueInput.htm) | The hole diameter. |
| holeMajorDiameter | [ValueInput](ValueInput.htm) | The hole major (or countersink) diameter. |
| depth | [ValueInput](ValueInput.htm) | With respect to hole orientation in the boss feature the parameter is either the counterbore depth or thickness of the material under the screw head. |
| countersinkAngle | [ValueInput](ValueInput.htm) | Optional parameter for hole countersink angle. If not specified it is set to 90 deg.   This is an optional argument whose default value is null. |

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