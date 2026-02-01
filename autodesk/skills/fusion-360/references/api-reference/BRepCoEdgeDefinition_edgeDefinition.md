# BRepCoEdgeDefinition.edgeDefinition Property

Parent Object: [BRepCoEdgeDefinition](BRepCoEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinition.h>

## Description

Gets and sets the BRepEdgeDefinition object associated with this BrepCoEdgeDefinition object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object. |

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepCoEdgeDefinition.h>  // Get the value of the property. Ptr<BRepEdgeDefinition> propertyValue = bRepCoEdgeDefinition_var->edgeDefinition();  // Set the value of the property, where value_var is a BRepEdgeDefinition. bool returnValue = bRepCoEdgeDefinition_var->edgeDefinition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepEdgeDefinition](BRepEdgeDefinition.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |