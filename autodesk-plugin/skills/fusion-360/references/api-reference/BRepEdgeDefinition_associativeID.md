# BRepEdgeDefinition.associativeID Property

Parent Object: [BRepEdgeDefinition](BRepEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdgeDefinition.h>

## Description

Gets and sets the associate ID of this edge definition. This ID will be copied to the corresponding edge when the BRepBodyDefinition is used to create a BrepBody. It is used internally by Fusion as the identifier for the edge and is used for tracking this geometry for parametric recomputes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. |

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepEdgeDefinition.h>  // Get the value of the property. integer propertyValue = bRepEdgeDefinition_var->associativeID();  // Set the value of the property, where value_var is an integer. bool returnValue = bRepEdgeDefinition_var->associativeID(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |