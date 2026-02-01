# MeshBody.material Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Gets and sets the physical material assigned to this mesh body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object. |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. Ptr<Material> propertyValue = meshBody_var->material();  // Set the value of the property, where value_var is a Material. bool returnValue = meshBody_var->material(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mesh Body Sample](MeshBodySample_Sample.htm) | Mesh body related functions |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |