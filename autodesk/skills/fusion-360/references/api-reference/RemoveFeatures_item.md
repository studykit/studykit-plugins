# RemoveFeatures.item Method

Parent Object: [RemoveFeatures](RemoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeatures.h>

## Description

Function that returns the specified Remove feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object.```` ``` returnValue = removeFeatures_var.item(index) ``` ```` |

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RemoveFeature](RemoveFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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