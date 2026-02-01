# TriangleMesh.nodeCoordinatesAsDouble Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns the node coordinates as an array of doubles where they are the x, y, z components of each coordinate.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<double> propertyValue = triangleMesh_var->nodeCoordinatesAsDouble(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |