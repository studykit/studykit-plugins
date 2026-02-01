# BRepEdgeDefinition.endVertex Property

Parent Object: [BRepEdgeDefinition](BRepEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdgeDefinition.h>

## Description

Gets and sets the end vertex of the edge definition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. |

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepEdgeDefinition.h>  // Get the value of the property. Ptr<BRepVertexDefinition> propertyValue = bRepEdgeDefinition_var->endVertex();  // Set the value of the property, where value_var is a BRepVertexDefinition. bool returnValue = bRepEdgeDefinition_var->endVertex(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepVertexDefinition](BRepVertexDefinition.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |