# BRepWireEdgeDefinition.objectType Property

Parent Object: [BRepWireEdgeDefinition](BRepWireEdgeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepWireEdgeDefinition_var.objectType ``` ```` |

"bRepWireEdgeDefinition\_var" is a variable referencing a BRepWireEdgeDefinition object. ```` ``` #include <Fusion/BRep/BRepWireEdgeDefinition.h>  // Get the value of the property. string propertyValue = bRepWireEdgeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |