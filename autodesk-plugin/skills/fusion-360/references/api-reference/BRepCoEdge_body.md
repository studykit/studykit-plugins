# BRepCoEdge.body Property

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns the body this co-edge is part of.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. |

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. ```` ``` #include <Fusion/BRep/BRepCoEdge.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = bRepCoEdge_var->body(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |