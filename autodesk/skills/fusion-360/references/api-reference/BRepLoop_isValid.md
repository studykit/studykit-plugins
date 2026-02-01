# BRepLoop.isValid Property

Parent Object: [BRepLoop](BRepLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoop\_var" is a variable referencing a BRepLoop object. |

"bRepLoop\_var" is a variable referencing a BRepLoop object. ```` ``` #include <Fusion/BRep/BRepLoop.h>  // Get the value of the property. boolean propertyValue = bRepLoop_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |