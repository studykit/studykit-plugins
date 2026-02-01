# BRepWireDefinition.objectType Property

Parent Object: [BRepWireDefinition](BRepWireDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireDefinition\_var" is a variable referencing a BRepWireDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepWireDefinition_var.objectType ``` ```` |

"bRepWireDefinition\_var" is a variable referencing a BRepWireDefinition object. ```` ``` #include <Fusion/BRep/BRepWireDefinition.h>  // Get the value of the property. string propertyValue = bRepWireDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |