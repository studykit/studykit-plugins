# OffsetFeatures.itemByName Method

Parent Object: [OffsetFeatures](OffsetFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatures.h>

## Description

Function that returns the specified offset feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object.```` ``` returnValue = offsetFeatures_var.itemByName(name) ``` ```` |

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFeature](OffsetFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |