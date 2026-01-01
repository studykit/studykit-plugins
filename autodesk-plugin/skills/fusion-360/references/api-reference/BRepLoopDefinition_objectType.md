# BRepLoopDefinition.objectType Property

Parent Object: [BRepLoopDefinition](BRepLoopDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoopDefinition\_var" is a variable referencing a BRepLoopDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepLoopDefinition_var.objectType ``` ```` |

"bRepLoopDefinition\_var" is a variable referencing a BRepLoopDefinition object. ```` ``` #include <Fusion/BRep/BRepLoopDefinition.h>  // Get the value of the property. string propertyValue = bRepLoopDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |