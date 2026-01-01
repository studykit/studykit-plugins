# BRepLump.body Property

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Returns the immediate owner BRepBody of the lump

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a BRepLump object. |

"bRepLump\_var" is a variable referencing a BRepLump object. ```` ``` #include <Fusion/BRep/BRepLump.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = bRepLump_var->body(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |