# PolygonMesh.triangleFaceGroupTempIds Property![](../images/TestTubeLarge.png)

Parent Object: [PolygonMesh](PolygonMesh.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

Returns the face groups tempId values for every triangle of the mesh. The tempId corresponds to the triangles, which are defined in triangleNodeIndices.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object. |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = polygonMesh_var->triangleFaceGroupTempIds(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type integer.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |