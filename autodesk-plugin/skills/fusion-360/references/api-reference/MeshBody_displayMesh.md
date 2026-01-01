# MeshBody.displayMesh Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Returns the associated mesh that is used for the display. This will always be triangles and includes any textures.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object. |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. Ptr<TriangleMesh> propertyValue = meshBody_var->displayMesh(); ``` ```` |

## Property Value

This is a read only property whose value is a [TriangleMesh](TriangleMesh.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |