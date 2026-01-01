# BRepVertex.entityToken Property

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

Returns a token for the BRepVertex object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same vertex.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a BRepVertex object.  ```` ``` # Get the value of the property. propertyValue = bRepVertex_var.entityToken ``` ```` |

"bRepVertex\_var" is a variable referencing a BRepVertex object. ```` ``` #include <Fusion/BRep/BRepVertex.h>  // Get the value of the property. string propertyValue = bRepVertex_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |