# BRepEdges.isValid Property

Parent Object: [BRepEdges](BRepEdges.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdges.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdges\_var" is a variable referencing a BRepEdges object. |

"bRepEdges\_var" is a variable referencing a BRepEdges object. ```` ``` #include <Fusion/BRep/BRepEdges.h>  // Get the value of the property. boolean propertyValue = bRepEdges_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |