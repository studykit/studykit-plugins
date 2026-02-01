# BRepVertex.faces Property

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

Returns the BRepFaces that uses this vertex through BRepEdge

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a BRepVertex object. |

"bRepVertex\_var" is a variable referencing a BRepVertex object. ```` ``` #include <Fusion/BRep/BRepVertex.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = bRepVertex_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |