# BRepShellDefinitions.objectType Property

Parent Object: [BRepShellDefinitions](BRepShellDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShellDefinitions\_var" is a variable referencing a BRepShellDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepShellDefinitions_var.objectType ``` ```` |

"bRepShellDefinitions\_var" is a variable referencing a BRepShellDefinitions object. ```` ``` #include <Fusion/BRep/BRepShellDefinitions.h>  // Get the value of the property. string propertyValue = bRepShellDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |