# BRepVertices.item Method

Parent Object: [BRepVertices](BRepVertices.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertices.h>

## Description

Function that returns the specified vertex using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertices\_var" is a variable referencing a [BRepVertices](BRepVertices.htm) object.```` ``` returnValue = bRepVertices_var.item(index) ``` ```` |

"bRepVertices\_var" is a variable referencing a [BRepVertices](BRepVertices.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepVertex](BRepVertex.htm) | Returns the specified item or null if an invalid index was specified. |

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