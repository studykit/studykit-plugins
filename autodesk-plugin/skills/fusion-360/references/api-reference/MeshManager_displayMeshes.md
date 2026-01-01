# MeshManager.displayMeshes Property

Parent Object: [MeshManager](MeshManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

Returns a collection that provides access to all of the existing display meshes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshManager\_var" is a variable referencing a MeshManager object. |

"meshManager\_var" is a variable referencing a MeshManager object. ```` ``` #include <Fusion/MeshData/MeshManager.h>  // Get the value of the property. Ptr<TriangleMeshList> propertyValue = meshManager_var->displayMeshes(); ``` ```` |

## Property Value

This is a read only property whose value is a [TriangleMeshList](TriangleMeshList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |