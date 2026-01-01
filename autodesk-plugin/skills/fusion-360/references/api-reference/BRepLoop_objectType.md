# BRepLoop.objectType Property

Parent Object: [BRepLoop](BRepLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoop\_var" is a variable referencing a BRepLoop object.  ```` ``` # Get the value of the property. propertyValue = bRepLoop_var.objectType ``` ```` |

"bRepLoop\_var" is a variable referencing a BRepLoop object. ```` ``` #include <Fusion/BRep/BRepLoop.h>  // Get the value of the property. string propertyValue = bRepLoop_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |