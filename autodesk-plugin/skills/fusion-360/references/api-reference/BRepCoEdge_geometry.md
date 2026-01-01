# BRepCoEdge.geometry Property

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns a geometry object that represents the shape of this co-edge in parameter space of the parent face's surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. |

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. ```` ``` #include <Fusion/BRep/BRepCoEdge.h>  // Get the value of the property. Ptr<Curve2D> propertyValue = bRepCoEdge_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve2D](Curve2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |