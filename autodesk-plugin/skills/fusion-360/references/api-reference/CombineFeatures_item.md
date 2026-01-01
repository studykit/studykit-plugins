# CombineFeatures.item Method

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

Function that returns the specified combine feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object.```` ``` returnValue = combineFeatures_var.item(index) ``` ```` |

"combineFeatures\_var" is a variable referencing a [CombineFeatures](CombineFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CombineFeature](CombineFeature.htm) | Returns the specified item or null if an invalid index was specified. This property returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |