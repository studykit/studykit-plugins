# CustomGraphicsMesh.normalVectors Property

Parent Object: [CustomGraphicsMesh](CustomGraphicsMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsMesh.h>

## Description

Gets and sets the normal vectors of the mesh where there is a normal vector at each node. The normals are defined as an array of floats where they are the x, y, z components of each vector.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. |

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. ```` ``` #include <Fusion/Graphics/CustomGraphicsMesh.h>  // Get the value of the property. std::vector<double> propertyValue = customGraphicsMesh_var->normalVectors();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsMesh_var->normalVectors(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |