# BRepEdgeDefinition.objectType Property

Parent Object: [BRepEdgeDefinition](BRepEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdgeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepEdgeDefinition_var.objectType ``` ```` |

"bRepEdgeDefinition\_var" is a variable referencing a BRepEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepEdgeDefinition.h>  // Get the value of the property. string propertyValue = bRepEdgeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |