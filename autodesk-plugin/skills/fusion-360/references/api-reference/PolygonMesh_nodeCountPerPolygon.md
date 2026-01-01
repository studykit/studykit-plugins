# PolygonMesh.nodeCountPerPolygon Property

Parent Object: [PolygonMesh](PolygonMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

Returns the number of nodes that define each polygon. For example, if NodeCountPerPolygon[0] returns 6 it indicates the first polygon is defined using 6 nodes. The first six indices returned by the PolygonNodeIndices properties provide the look-up into the NodeCoordinates array.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object. |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = polygonMesh_var->nodeCountPerPolygon(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |