# OffsetFeatures.item Method

Parent Object: [OffsetFeatures](OffsetFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatures.h>

## Description

Function that returns the specified offset feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object.```` ``` returnValue = offsetFeatures_var.item(index) ``` ```` |

"offsetFeatures\_var" is a variable referencing an [OffsetFeatures](OffsetFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFeature](OffsetFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |