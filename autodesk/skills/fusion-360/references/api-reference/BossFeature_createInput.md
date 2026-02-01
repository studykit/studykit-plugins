# BossFeature.createInput Method

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Creates object with inputs this feature represents. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object.```` ``` returnValue = bossFeature_var.createInput() ``` ```` |

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BossFeatureInput](BossFeatureInput.htm) | Returns BossFeatureInput this feature represent if successful. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |