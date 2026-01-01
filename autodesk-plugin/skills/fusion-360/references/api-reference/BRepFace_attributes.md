# BRepFace.attributes Property

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a BRepFace object. |

"bRepFace\_var" is a variable referencing a BRepFace object. ```` ``` #include <Fusion/BRep/BRepFace.h>  // Get the value of the property. Ptr<Attributes> propertyValue = bRepFace_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |