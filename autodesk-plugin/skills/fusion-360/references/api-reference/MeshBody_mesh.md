# MeshBody.mesh Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Returns the original mesh data that was imported. This can include triangles, quads, and polygons.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object. |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. Ptr<PolygonMesh> propertyValue = meshBody_var->mesh(); ``` ```` |

## Property Value

This is a read only property whose value is a [PolygonMesh](PolygonMesh.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |