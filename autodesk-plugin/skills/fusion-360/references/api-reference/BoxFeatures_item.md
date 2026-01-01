# BoxFeatures.item Method

Parent Object: [BoxFeatures](BoxFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeatures.h>

## Description

Function that returns the specified box feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeatures\_var" is a variable referencing a [BoxFeatures](BoxFeatures.htm) object.```` ``` returnValue = boxFeatures_var.item(index) ``` ```` |

"boxFeatures\_var" is a variable referencing a [BoxFeatures](BoxFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoxFeature](BoxFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |