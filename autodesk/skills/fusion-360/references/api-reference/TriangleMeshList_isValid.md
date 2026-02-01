# TriangleMeshList.isValid Property

Parent Object: [TriangleMeshList](TriangleMeshList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object. |

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object. ```` ``` #include <Fusion/MeshData/TriangleMeshList.h>  // Get the value of the property. boolean propertyValue = triangleMeshList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |