# PolygonMesh.normalVectors Property

Parent Object: [PolygonMesh](PolygonMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

Returns the normal vectors as an array of Vector 3D objects. There is one normal vector for each index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object. |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. std::vector<Ptr<Vector3D>> propertyValue = polygonMesh_var->normalVectors(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |