# BRepWire.objectType Property

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a BRepWire object.  ```` ``` # Get the value of the property. propertyValue = bRepWire_var.objectType ``` ```` |

"bRepWire\_var" is a variable referencing a BRepWire object. ```` ``` #include <Fusion/BRep/BRepWire.h>  // Get the value of the property. string propertyValue = bRepWire_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |