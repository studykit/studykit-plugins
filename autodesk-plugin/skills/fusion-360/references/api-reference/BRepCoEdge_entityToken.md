# BRepCoEdge.entityToken Property

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns a token for the BRepCoEdge object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same co-edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object.  ```` ``` # Get the value of the property. propertyValue = bRepCoEdge_var.entityToken ``` ```` |

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. ```` ``` #include <Fusion/BRep/BRepCoEdge.h>  // Get the value of the property. string propertyValue = bRepCoEdge_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |