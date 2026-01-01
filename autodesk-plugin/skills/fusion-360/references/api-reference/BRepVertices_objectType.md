# BRepVertices.objectType Property

Parent Object: [BRepVertices](BRepVertices.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertices.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertices\_var" is a variable referencing a BRepVertices object.  ```` ``` # Get the value of the property. propertyValue = bRepVertices_var.objectType ``` ```` |

"bRepVertices\_var" is a variable referencing a BRepVertices object. ```` ``` #include <Fusion/BRep/BRepVertices.h>  // Get the value of the property. string propertyValue = bRepVertices_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |