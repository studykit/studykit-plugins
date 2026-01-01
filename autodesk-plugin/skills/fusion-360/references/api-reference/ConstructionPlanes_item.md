# ConstructionPlanes.item Method

Parent Object: [ConstructionPlanes](ConstructionPlanes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Function that returns the specified construction plane using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.```` ``` returnValue = constructionPlanes_var.item(index) ``` ```` |

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPlane](ConstructionPlane.htm) | Returns the specified item or null if an invalid index was specified. |

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