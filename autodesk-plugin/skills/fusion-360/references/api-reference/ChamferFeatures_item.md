# ChamferFeatures.item Method

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

Function that returns the specified chamfer feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.```` ``` returnValue = chamferFeatures_var.item(index) ``` ```` |

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeature](ChamferFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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