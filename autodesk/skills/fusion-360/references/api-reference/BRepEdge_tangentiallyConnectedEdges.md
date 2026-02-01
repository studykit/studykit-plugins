# BRepEdge.tangentiallyConnectedEdges Property

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns a collection of edges that includes all of the edges tangentially connected to this edge. The result includes this edge. The edges are in the collection in their connected order.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a BRepEdge object. |

"bRepEdge\_var" is a variable referencing a BRepEdge object. ```` ``` #include <Fusion/BRep/BRepEdge.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = bRepEdge_var->tangentiallyConnectedEdges(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |