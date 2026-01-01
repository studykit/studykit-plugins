# BRepWire.coEdges Property

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

Returns the co-edges associated with this wire body. The co-edges record the connections between the edges in the wire body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a BRepWire object. |

"bRepWire\_var" is a variable referencing a BRepWire object. ```` ``` #include <Fusion/BRep/BRepWire.h>  // Get the value of the property. Ptr<BRepCoEdges> propertyValue = bRepWire_var->coEdges(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCoEdges](BRepCoEdges.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BrepWire Sample](BrepWireSample_Sample.htm) | BrepWires and BrepWire related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |