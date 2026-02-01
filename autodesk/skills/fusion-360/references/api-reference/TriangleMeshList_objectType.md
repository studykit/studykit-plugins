# TriangleMeshList.objectType Property

Parent Object: [TriangleMeshList](TriangleMeshList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object.  ```` ``` # Get the value of the property. propertyValue = triangleMeshList_var.objectType ``` ```` |

"triangleMeshList\_var" is a variable referencing a TriangleMeshList object. ```` ``` #include <Fusion/MeshData/TriangleMeshList.h>  // Get the value of the property. string propertyValue = triangleMeshList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |