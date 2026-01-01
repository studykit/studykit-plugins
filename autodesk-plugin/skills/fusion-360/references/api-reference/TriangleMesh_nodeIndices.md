# TriangleMesh.nodeIndices Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns an array of indices that define which nodes are used for each triangle. This is used to look-up the coordinates in the NodeCoordinates array to get the three coordinates of each triangle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = triangleMesh_var->nodeIndices(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |