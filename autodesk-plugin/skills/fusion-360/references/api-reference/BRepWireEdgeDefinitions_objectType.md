# BRepWireEdgeDefinitions.objectType Property

Parent Object: [BRepWireEdgeDefinitions](BRepWireEdgeDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinitions\_var" is a variable referencing a BRepWireEdgeDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepWireEdgeDefinitions_var.objectType ``` ```` |

"bRepWireEdgeDefinitions\_var" is a variable referencing a BRepWireEdgeDefinitions object. ```` ``` #include <Fusion/BRep/BRepWireEdgeDefinitions.h>  // Get the value of the property. string propertyValue = bRepWireEdgeDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |