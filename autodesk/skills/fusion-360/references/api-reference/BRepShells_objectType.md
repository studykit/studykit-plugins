# BRepShells.objectType Property

Parent Object: [BRepShells](BRepShells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShells.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShells\_var" is a variable referencing a BRepShells object.  ```` ``` # Get the value of the property. propertyValue = bRepShells_var.objectType ``` ```` |

"bRepShells\_var" is a variable referencing a BRepShells object. ```` ``` #include <Fusion/BRep/BRepShells.h>  // Get the value of the property. string propertyValue = bRepShells_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |