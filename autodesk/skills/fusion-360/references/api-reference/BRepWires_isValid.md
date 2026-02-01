# BRepWires.isValid Property

Parent Object: [BRepWires](BRepWires.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWires.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWires\_var" is a variable referencing a BRepWires object. |

"bRepWires\_var" is a variable referencing a BRepWires object. ```` ``` #include <Fusion/BRep/BRepWires.h>  // Get the value of the property. boolean propertyValue = bRepWires_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |