# PolygonMesh.quadNodeIndices Property

Parent Object: [PolygonMesh](PolygonMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

Returns the index values that index into the NodeCoordinates and NormalVectors arrays to define the four coordinates of each quad and the corresponding normal.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object. |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = polygonMesh_var->quadNodeIndices(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |