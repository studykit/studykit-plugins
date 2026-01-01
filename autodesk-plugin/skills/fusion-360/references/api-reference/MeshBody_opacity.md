# MeshBody.opacity Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Gets and sets the opacity override assigned to this body. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object.  ```` ``` # Get the value of the property. propertyValue = meshBody_var.opacity  # Set the value of the property. meshBody_var.opacity = propertyValue ``` ```` |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. double propertyValue = meshBody_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = meshBody_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mesh Body Sample](MeshBodySample_Sample.htm) | Mesh body related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |