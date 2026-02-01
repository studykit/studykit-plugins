# BRepLoopDefinitions.objectType Property

Parent Object: [BRepLoopDefinitions](BRepLoopDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoopDefinitions\_var" is a variable referencing a BRepLoopDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepLoopDefinitions_var.objectType ``` ```` |

"bRepLoopDefinitions\_var" is a variable referencing a BRepLoopDefinitions object. ```` ``` #include <Fusion/BRep/BRepLoopDefinitions.h>  // Get the value of the property. string propertyValue = bRepLoopDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |