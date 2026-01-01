# DraftFeatures.item Method

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Function that returns the specified draft feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object.```` ``` returnValue = draftFeatures_var.item(index) ``` ```` |

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftFeature](DraftFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |