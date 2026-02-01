# BRepVertex.shell Property

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

Returns the parent shell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a BRepVertex object. |

"bRepVertex\_var" is a variable referencing a BRepVertex object. ```` ``` #include <Fusion/BRep/BRepVertex.h>  // Get the value of the property. Ptr<BRepShell> propertyValue = bRepVertex_var->shell(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepShell](BRepShell.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |