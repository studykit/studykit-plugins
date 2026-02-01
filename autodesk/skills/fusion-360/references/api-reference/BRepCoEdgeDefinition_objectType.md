# BRepCoEdgeDefinition.objectType Property

Parent Object: [BRepCoEdgeDefinition](BRepCoEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepCoEdgeDefinition_var.objectType ``` ```` |

"bRepCoEdgeDefinition\_var" is a variable referencing a BRepCoEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepCoEdgeDefinition.h>  // Get the value of the property. string propertyValue = bRepCoEdgeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |