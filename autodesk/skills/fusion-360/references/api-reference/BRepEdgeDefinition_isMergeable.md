# BRepEdgeDefinition.isMergeable Property

Parent Object: [BRepEdgeDefinition](BRepEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdgeDefinition.h>

## Description

Gets and sets if the two faces that share this edge can be merged along this edge. This property defaults to true so that merging is always done but this can be set to false in cases where you want to preserve the edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepEdgeDefinition_var.isMergeable  # Set the value of the property. bRepEdgeDefinition_var.isMergeable = propertyValue ``` ```` |

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepEdgeDefinition.h>  // Get the value of the property. boolean propertyValue = bRepEdgeDefinition_var->isMergeable();  // Set the value of the property, where value_var is a boolean. bool returnValue = bRepEdgeDefinition_var->isMergeable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |