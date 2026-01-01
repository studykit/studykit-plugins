# PolygonMesh.objectType Property

Parent Object: [PolygonMesh](PolygonMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonMesh\_var" is a variable referencing a PolygonMesh object.  ```` ``` # Get the value of the property. propertyValue = polygonMesh_var.objectType ``` ```` |

"polygonMesh\_var" is a variable referencing a PolygonMesh object. ```` ``` #include <Fusion/MeshData/PolygonMesh.h>  // Get the value of the property. string propertyValue = polygonMesh_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |