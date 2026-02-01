# BRepShells.isValid Property

Parent Object: [BRepShells](BRepShells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShells.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShells\_var" is a variable referencing a BRepShells object. |

"bRepShells\_var" is a variable referencing a BRepShells object. ```` ``` #include <Fusion/BRep/BRepShells.h>  // Get the value of the property. boolean propertyValue = bRepShells_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |