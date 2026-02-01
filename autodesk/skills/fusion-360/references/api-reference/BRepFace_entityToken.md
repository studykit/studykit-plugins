# BRepFace.entityToken Property

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Returns a token for the BRepFace object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a BRepFace object.  ```` ``` # Get the value of the property. propertyValue = bRepFace_var.entityToken ``` ```` |

"bRepFace\_var" is a variable referencing a BRepFace object. ```` ``` #include <Fusion/BRep/BRepFace.h>  // Get the value of the property. string propertyValue = bRepFace_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |