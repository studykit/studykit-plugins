# PolygonMesh.nodeCoordinatesAsFloat Property

Parent Object: [PolygonMesh](PolygonMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

Returns the node coordinates as an array of floats where they are the x, y, z components of each coordinate.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object. |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. std::vector<float> propertyValue = polygonMesh_var->nodeCoordinatesAsFloat(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type float.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |