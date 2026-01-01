# BRepCoEdges.item Method

Parent Object: [BRepCoEdges](BRepCoEdges.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdges.h>

## Description

Function that returns the specified co-edge using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdges\_var" is a variable referencing a [BRepCoEdges](BRepCoEdges.htm) object.```` ``` returnValue = bRepCoEdges_var.item(index) ``` ```` |

"bRepCoEdges\_var" is a variable referencing a [BRepCoEdges](BRepCoEdges.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepCoEdge](BRepCoEdge.htm) | Returns the specified item or null if an invalid index was specified. |

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