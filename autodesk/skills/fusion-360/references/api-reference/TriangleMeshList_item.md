# TriangleMeshList.item Method

Parent Object: [TriangleMeshList](TriangleMeshList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshList.h>

## Description

Returns the specified triangle meshes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshList\_var" is a variable referencing a [TriangleMeshList](TriangleMeshList.htm) object.```` ``` returnValue = triangleMeshList_var.item(index) ``` ```` |

"triangleMeshList\_var" is a variable referencing a [TriangleMeshList](TriangleMeshList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TriangleMesh](TriangleMesh.htm) | Returns the specified mesh or null in the case of invalid index. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the mesh to return where the first item has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |