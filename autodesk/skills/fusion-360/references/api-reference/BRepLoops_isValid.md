# BRepLoops.isValid Property

Parent Object: [BRepLoops](BRepLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoops.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoops\_var" is a variable referencing a BRepLoops object. |

"bRepLoops\_var" is a variable referencing a BRepLoops object. ```` ``` #include <Fusion/BRep/BRepLoops.h>  // Get the value of the property. boolean propertyValue = bRepLoops_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |