# BRepFace.tangentiallyConnectedFaces Property

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Returns the set of faces that are tangentially adjacent to this face. In other words, it is the set of faces that are adjacent to this face's edges and have a smooth transition across those edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a BRepFace object. |

"bRepFace\_var" is a variable referencing a BRepFace object. ```` ``` #include <Fusion/BRep/BRepFace.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = bRepFace_var->tangentiallyConnectedFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |