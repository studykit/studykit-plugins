# ChamferEdgeSets.item Method

Parent Object: [ChamferEdgeSets](ChamferEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSets.h>

## Description

Function that returns the specified chamfer edge set using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSets\_var" is a variable referencing a [ChamferEdgeSets](ChamferEdgeSets.htm) object.```` ``` returnValue = chamferEdgeSets_var.item(index) ``` ```` |

"chamferEdgeSets\_var" is a variable referencing a [ChamferEdgeSets](ChamferEdgeSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferEdgeSet](ChamferEdgeSet.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |