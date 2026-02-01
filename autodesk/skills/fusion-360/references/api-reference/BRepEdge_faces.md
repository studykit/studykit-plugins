# BRepEdge.faces Property

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns the BRepFaces that are associated with this edge through its BRepCoEdges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a BRepEdge object. |

"bRepEdge\_var" is a variable referencing a BRepEdge object. ```` ``` #include <Fusion/BRep/BRepEdge.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = bRepEdge_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |