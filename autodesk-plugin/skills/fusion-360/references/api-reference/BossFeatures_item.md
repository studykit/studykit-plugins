# BossFeatures.item Method

Parent Object: [BossFeatures](BossFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatures.h>

## Description

Function that returns the specified boss feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatures\_var" is a variable referencing a [BossFeatures](BossFeatures.htm) object.```` ``` returnValue = bossFeatures_var.item(index) ``` ```` |

"bossFeatures\_var" is a variable referencing a [BossFeatures](BossFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BossFeature](BossFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |