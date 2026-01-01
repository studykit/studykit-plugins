# BRepWireEdgeDefinition.associativeID Property

Parent Object: [BRepWireEdgeDefinition](BRepWireEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinition.h>

## Description

Gets and sets the associate ID of this B-Rep wire definition. This ID will be copied to the corresponding edge when the BRepBodyDefinition is used to create a BrepBody. It is used by Fusion as the identifier for the edge and is used for tracking this geometry for parametric recomputes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. |

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepWireEdgeDefinition.h>  // Get the value of the property. integer propertyValue = bRepWireEdgeDefinition_var->associativeID();  // Set the value of the property, where value_var is an integer. bool returnValue = bRepWireEdgeDefinition_var->associativeID(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |