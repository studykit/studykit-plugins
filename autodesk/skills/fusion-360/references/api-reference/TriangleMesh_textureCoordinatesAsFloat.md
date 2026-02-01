# TriangleMesh.textureCoordinatesAsFloat Property

Parent Object: [TriangleMesh](TriangleMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

Returns the texture coordinates used when mapping a texture to this face. The coordinates are returned as an array of floats where they are the u and v components of each coordinate as defined in parametric space. There is a texture coordinate for each vertex in the face mesh.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMesh\_var" is a variable referencing a TriangleMesh object. |

"triangleMesh\_var" is a variable referencing a TriangleMesh object. ```` ``` #include <Fusion/MeshData/TriangleMesh.h>  // Get the value of the property. std::vector<float> propertyValue = triangleMesh_var->textureCoordinatesAsFloat(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type float.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |