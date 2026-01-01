# TriangleMeshCalculator.parentMeshManager Property

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

Returns the parent MeshManager object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. |

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  // Get the value of the property. Ptr<MeshManager> propertyValue = triangleMeshCalculator_var->parentMeshManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [MeshManager](MeshManager.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |