# BRepShell.entityToken Property

Parent Object: [BRepShell](BRepShell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Returns a token for the BRepShell object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same shell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShell\_var" is a variable referencing a BRepShell object.  ```` ``` # Get the value of the property. propertyValue = bRepShell_var.entityToken ``` ```` |

"bRepShell\_var" is a variable referencing a BRepShell object. ```` ``` #include <Fusion/BRep/BRepShell.h>  // Get the value of the property. string propertyValue = bRepShell_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |