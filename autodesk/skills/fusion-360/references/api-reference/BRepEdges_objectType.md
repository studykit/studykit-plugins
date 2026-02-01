# BRepEdges.objectType Property

Parent Object: [BRepEdges](BRepEdges.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdges.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdges\_var" is a variable referencing a BRepEdges object.  ```` ``` # Get the value of the property. propertyValue = bRepEdges_var.objectType ``` ```` |

"bRepEdges\_var" is a variable referencing a BRepEdges object. ```` ``` #include <Fusion/BRep/BRepEdges.h>  // Get the value of the property. string propertyValue = bRepEdges_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |