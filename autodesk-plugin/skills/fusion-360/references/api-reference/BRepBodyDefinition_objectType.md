# BRepBodyDefinition.objectType Property

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepBodyDefinition_var.objectType ``` ```` |

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. ```` ``` #include <Fusion/BRep/BRepBodyDefinition.h>  // Get the value of the property. string propertyValue = bRepBodyDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |