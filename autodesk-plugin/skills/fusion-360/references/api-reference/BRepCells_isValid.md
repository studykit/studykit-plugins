# BRepCells.isValid Property

Parent Object: [BRepCells](BRepCells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCells.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCells\_var" is a variable referencing a BRepCells object. |

"bRepCells\_var" is a variable referencing a BRepCells object. ```` ``` #include <Fusion/Features/BRepCells.h>  // Get the value of the property. boolean propertyValue = bRepCells_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |