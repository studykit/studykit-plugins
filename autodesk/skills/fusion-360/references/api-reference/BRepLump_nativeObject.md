# BRepLump.nativeObject Property

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a BRepLump object. |

"bRepLump\_var" is a variable referencing a BRepLump object. ```` ``` #include <Fusion/BRep/BRepLump.h>  // Get the value of the property. Ptr<BRepLump> propertyValue = bRepLump_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepLump](BRepLump.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |