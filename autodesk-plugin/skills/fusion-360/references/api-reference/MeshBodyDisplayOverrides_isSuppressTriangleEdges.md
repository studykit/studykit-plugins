# MeshBodyDisplayOverrides.isSuppressTriangleEdges Property

Parent Object: [MeshBodyDisplayOverrides](MeshBodyDisplayOverrides.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyDisplayOverrides.h>

## Description

Controls whether the edges of the triangles of the mesh body are shown. If set to true, individual triangles will not be visible, edges of face groups (if any) will be shown instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object. |

"meshBodyDisplayOverrides\_var" is a variable referencing a MeshBodyDisplayOverrides object. ```` ``` #include <Fusion/MeshBody/MeshBodyDisplayOverrides.h>  // Get the value of the property. boolean propertyValue = meshBodyDisplayOverrides_var->isSuppressTriangleEdges();  // Set the value of the property, where value_var is a boolean. bool returnValue = meshBodyDisplayOverrides_var->isSuppressTriangleEdges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |