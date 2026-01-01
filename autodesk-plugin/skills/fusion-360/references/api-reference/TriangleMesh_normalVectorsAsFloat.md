# TriangleMesh.normalVectorsAsFloat Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns the normal vectors of the mesh where there is a normal vector at each node. The normals are returned as an array of floats where they are the x, y, z components of each vector.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<float> propertyValue = triangleMesh_var->normalVectorsAsFloat(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type float.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |