# BossFeatures.itemByName Method

Parent Object: [BossFeatures](BossFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatures.h>

## Description

Function that returns the specified boss feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatures\_var" is a variable referencing a [BossFeatures](BossFeatures.htm) object.```` ``` returnValue = bossFeatures_var.itemByName(name) ``` ```` |

"bossFeatures\_var" is a variable referencing a [BossFeatures](BossFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BossFeature](BossFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |