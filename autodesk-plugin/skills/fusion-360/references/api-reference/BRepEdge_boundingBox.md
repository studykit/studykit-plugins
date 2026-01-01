# BRepEdge.boundingBox Property

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns the bounding box of this edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a BRepEdge object. |

"bRepEdge\_var" is a variable referencing a BRepEdge object. ```` ``` #include <Fusion/BRep/BRepEdge.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = bRepEdge_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |