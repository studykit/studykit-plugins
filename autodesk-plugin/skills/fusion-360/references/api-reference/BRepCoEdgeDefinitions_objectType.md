# BRepCoEdgeDefinitions.objectType Property

Parent Object: [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinitions\_var" is a variable referencing a BRepCoEdgeDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepCoEdgeDefinitions_var.objectType ``` ```` |

"bRepCoEdgeDefinitions\_var" is a variable referencing a BRepCoEdgeDefinitions object. ```` ``` #include <Fusion/BRep/BRepCoEdgeDefinitions.h>  // Get the value of the property. string propertyValue = bRepCoEdgeDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |