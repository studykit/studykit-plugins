# BRepLump.faces Property

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Returns the BRepFaces owned by the lump

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a BRepLump object. |

"bRepLump\_var" is a variable referencing a BRepLump object. ```` ``` #include <Fusion/BRep/BRepLump.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = bRepLump_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |