# BRepShellDefinition.objectType Property

Parent Object: [BRepShellDefinition](BRepShellDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepShellDefinition_var.objectType ``` ```` |

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object. ```` ``` #include <Fusion/BRep/BRepShellDefinition.h>  // Get the value of the property. string propertyValue = bRepShellDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |