# MeshManager.createMeshCalculator Method

Parent Object: [MeshManager](MeshManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

Creates a new MeshCalculator which is used to calculate new triangular meshes based on various parameters that control the calculation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshManager\_var" is a variable referencing a [MeshManager](MeshManager.htm) object.```` ``` returnValue = meshManager_var.createMeshCalculator() ``` ```` |

"meshManager\_var" is a variable referencing a [MeshManager](MeshManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TriangleMeshCalculator](TriangleMeshCalculator.htm) | Returns the new MeshCalculator object or null if the creation failed. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |