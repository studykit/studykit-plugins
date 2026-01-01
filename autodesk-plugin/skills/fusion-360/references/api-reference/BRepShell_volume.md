# BRepShell.volume Property

Parent Object: [BRepShell](BRepShell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Returns the volume in cm ^ 3. Returns 0 in the case the shell is not solid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShell\_var" is a variable referencing a BRepShell object. |

"bRepShell\_var" is a variable referencing a BRepShell object. ```` ``` #include <Fusion/BRep/BRepShell.h>  // Get the value of the property. double propertyValue = bRepShell_var->volume(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |