# BRepShell.boundingBox Property

Parent Object: [BRepShell](BRepShell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Returns the bounding box of this shell

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShell\_var" is a variable referencing a BRepShell object. |

"bRepShell\_var" is a variable referencing a BRepShell object. ```` ``` #include <Fusion/BRep/BRepShell.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = bRepShell_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |