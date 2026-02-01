# BRepVertexDefinition.objectType Property

Parent Object: [BRepVertexDefinition](BRepVertexDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertexDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertexDefinition\_var" is a variable referencing a BRepVertexDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepVertexDefinition_var.objectType ``` ```` |

"bRepVertexDefinition\_var" is a variable referencing a BRepVertexDefinition object. ```` ``` #include <Fusion/BRep/BRepVertexDefinition.h>  // Get the value of the property. string propertyValue = bRepVertexDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |