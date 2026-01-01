# BRepVertex.objectType Property

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a BRepVertex object.  ```` ``` # Get the value of the property. propertyValue = bRepVertex_var.objectType ``` ```` |

"bRepVertex\_var" is a variable referencing a BRepVertex object. ```` ``` #include <Fusion/BRep/BRepVertex.h>  // Get the value of the property. string propertyValue = bRepVertex_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |