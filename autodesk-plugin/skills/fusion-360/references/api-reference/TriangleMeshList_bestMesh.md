# TriangleMeshList.bestMesh Property

Parent Object: [TriangleMeshList](TriangleMeshList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshList.h>

## Description

Returns the mesh with the tightest surface tolerance. This can return null in the case the list is empty, i.e. Count is 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object. |

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object. ```` ``` #include <Fusion/MeshData/TriangleMeshList.h>  // Get the value of the property. Ptr<TriangleMesh> propertyValue = triangleMeshList_var->bestMesh(); ``` ```` |

## Property Value

This is a read only property whose value is a [TriangleMesh](TriangleMesh.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |