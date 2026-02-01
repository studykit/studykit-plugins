# BossFeature.update Method

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Changes the boss feature (or boss connection) to the input provided. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object.```` ``` returnValue = bossFeature_var.update(input) ``` ```` |

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [BossFeatureInput](BossFeatureInput.htm) | The object defines inputs the feature will be set to. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |