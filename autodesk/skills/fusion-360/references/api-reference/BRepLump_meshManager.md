# BRepLump.meshManager Property

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Returns the mesh manager object for this lump.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a BRepLump object. |

"bRepLump\_var" is a variable referencing a BRepLump object. ```` ``` #include <Fusion/BRep/BRepLump.h>  // Get the value of the property. Ptr<MeshManager> propertyValue = bRepLump_var->meshManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [MeshManager](MeshManager.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |