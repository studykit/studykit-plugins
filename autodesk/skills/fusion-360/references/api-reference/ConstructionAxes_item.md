# ConstructionAxes.item Method

Parent Object: [ConstructionAxes](ConstructionAxes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

Function that returns the specified construction axis using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object.```` ``` returnValue = constructionAxes_var.item(index) ``` ```` |

"constructionAxes\_var" is a variable referencing a [ConstructionAxes](ConstructionAxes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionAxis](ConstructionAxis.htm) | Returns the specified item or null if an invalid index was specified. |

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