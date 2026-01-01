# BRepCoEdgeDefinition.isOpposedToEdge Property

Parent Object: [BRepCoEdgeDefinition](BRepCoEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinition.h>

## Description

Gets and sets if the orientation of this BRepCoEdgeDefinition object is reversed with respect to the associated BRepEdgeDefinition object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object. |

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepCoEdgeDefinition.h>  // Get the value of the property. boolean propertyValue = bRepCoEdgeDefinition_var->isOpposedToEdge();  // Set the value of the property, where value_var is a boolean. bool returnValue = bRepCoEdgeDefinition_var->isOpposedToEdge(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |