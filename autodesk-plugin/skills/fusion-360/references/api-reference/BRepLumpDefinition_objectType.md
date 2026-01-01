# BRepLumpDefinition.objectType Property

Parent Object: [BRepLumpDefinition](BRepLumpDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLumpDefinition\_var" is a variable referencing a BRepLumpDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepLumpDefinition_var.objectType ``` ```` |

"bRepLumpDefinition\_var" is a variable referencing a BRepLumpDefinition object. ```` ``` #include <Fusion/BRep/BRepLumpDefinition.h>  // Get the value of the property. string propertyValue = bRepLumpDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |