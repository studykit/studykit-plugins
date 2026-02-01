# ConstructionPoints.item Method

Parent Object: [ConstructionPoints](ConstructionPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

Function that returns the specified construction point using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.```` ``` returnValue = constructionPoints_var.item(index) ``` ```` |

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPoint](ConstructionPoint.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |