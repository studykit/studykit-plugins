# BRepLoop.body Property

Parent Object: [BRepLoop](BRepLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

Returns the parent body of the loop.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoop\_var" is a variable referencing a BRepLoop object. |

"bRepLoop\_var" is a variable referencing a BRepLoop object. ```` ``` #include <Fusion/BRep/BRepLoop.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = bRepLoop_var->body(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |