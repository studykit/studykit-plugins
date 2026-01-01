# CustomGraphicsMesh.vertexIndexList Property

Parent Object: [CustomGraphicsMesh](CustomGraphicsMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsMesh.h>

## Description

Gets and sets an array of indices that define which coordinate in the coordinate list is used for each vertex in the mesh. Each set of three indices defines a triangle. For example: Indices 0, 1, and 2 define the coordinates to use for the first triangle and indices 3, 4, and 5 define the coordinates for the second triangle, and so on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. |

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. ```` ``` #include <Fusion/Graphics/CustomGraphicsMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = customGraphicsMesh_var->vertexIndexList();  // Set the value of the property, where value_var is an integer. bool returnValue = customGraphicsMesh_var->vertexIndexList(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |