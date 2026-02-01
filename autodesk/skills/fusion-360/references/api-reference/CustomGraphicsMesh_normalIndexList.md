# CustomGraphicsMesh.normalIndexList Property

Parent Object: [CustomGraphicsMesh](CustomGraphicsMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsMesh.h>

## Description

Gets and sets an array of indices that define which normal is associated with each vertex in the mesh. This is used to look-up the normal in the normalVectors array.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. |

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. ```` ``` #include <Fusion/Graphics/CustomGraphicsMesh.h>  // Get the value of the property. std::vector<integer> propertyValue = customGraphicsMesh_var->normalIndexList();  // Set the value of the property, where value_var is an integer. bool returnValue = customGraphicsMesh_var->normalIndexList(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |