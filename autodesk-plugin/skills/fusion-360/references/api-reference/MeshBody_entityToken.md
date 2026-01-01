# MeshBody.entityToken Property

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Returns a token for the MeshBody object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same mesh body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a MeshBody object.  ```` ``` # Get the value of the property. propertyValue = meshBody_var.entityToken ``` ```` |

"meshBody\_var" is a variable referencing a MeshBody object. ```` ``` #include <Fusion/MeshBody/MeshBody.h>  // Get the value of the property. string propertyValue = meshBody_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |