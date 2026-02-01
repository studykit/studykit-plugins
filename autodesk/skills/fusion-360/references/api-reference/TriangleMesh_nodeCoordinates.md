# TriangleMesh.nodeCoordinates Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns the node coordinates as an array of Point3D objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<Ptr<Point3D>> propertyValue = triangleMesh_var->nodeCoordinates(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |