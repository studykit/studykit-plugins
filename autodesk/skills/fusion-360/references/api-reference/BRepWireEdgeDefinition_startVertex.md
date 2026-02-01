# BRepWireEdgeDefinition.startVertex Property

Parent Object: [BRepWireEdgeDefinition](BRepWireEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinition.h>

## Description

Gets and sets the start vertex of the wire edge definition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. |

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepWireEdgeDefinition.h>  // Get the value of the property. Ptr<BRepVertexDefinition> propertyValue = bRepWireEdgeDefinition_var->startVertex();  // Set the value of the property, where value_var is a BRepVertexDefinition. bool returnValue = bRepWireEdgeDefinition_var->startVertex(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepVertexDefinition](BRepVertexDefinition.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |