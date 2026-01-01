# BRepEdge.attributes Property

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a BRepEdge object. |

"bRepEdge\_var" is a variable referencing a BRepEdge object. ```` ``` #include <Fusion/BRep/BRepEdge.h>  // Get the value of the property. Ptr<Attributes> propertyValue = bRepEdge_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |