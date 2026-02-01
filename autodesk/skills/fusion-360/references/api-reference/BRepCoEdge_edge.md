# BRepCoEdge.edge Property

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns the edge this co-edge is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. |

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. ```` ``` #include <Fusion/BRep/BRepCoEdge.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = bRepCoEdge_var->edge(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |