# TrimFeatures.item Method

Parent Object: [TrimFeatures](TrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

Function that returns the specified trim feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object.```` ``` returnValue = trimFeatures_var.item(index) ``` ```` |

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TrimFeature](TrimFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |