# TriangleMesh.normalVectors Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns the normal vectors of the mesh where there is a normal vector at each node. The normals are returned as an array of Vector3D objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<Ptr<Vector3D>> propertyValue = triangleMesh_var->normalVectors(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |