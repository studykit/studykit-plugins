# SplitBodyFeatures.item Method

Parent Object: [SplitBodyFeatures](SplitBodyFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatures.h>

## Description

Function that returns the specified split body feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object.```` ``` returnValue = splitBodyFeatures_var.item(index) ``` ```` |

"splitBodyFeatures\_var" is a variable referencing a [SplitBodyFeatures](SplitBodyFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitBodyFeature](SplitBodyFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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