# MeshBody.name Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Gets and sets the name of the mesh body as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object. |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. string propertyValue = meshBody_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = meshBody_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mesh Body Sample](MeshBodySample_Sample.htm) | Mesh body related functions |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |