# BRepLumpDefinitions.objectType Property

Parent Object: [BRepLumpDefinitions](BRepLumpDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLumpDefinitions\_var" is a variable referencing a BRepLumpDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepLumpDefinitions_var.objectType ``` ```` |

"bRepLumpDefinitions\_var" is a variable referencing a BRepLumpDefinitions object. ```` ``` #include <Fusion/BRep/BRepLumpDefinitions.h>  // Get the value of the property. string propertyValue = bRepLumpDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |