# BRepWires.objectType Property

Parent Object: [BRepWires](BRepWires.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWires.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWires\_var" is a variable referencing a BRepWires object.  ```` ``` # Get the value of the property. propertyValue = bRepWires_var.objectType ``` ```` |

"bRepWires\_var" is a variable referencing a BRepWires object. ```` ``` #include <Fusion/BRep/BRepWires.h>  // Get the value of the property. string propertyValue = bRepWires_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |