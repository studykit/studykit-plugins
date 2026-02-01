# MeshManager.parent Property

Parent Object: [MeshManager](MeshManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

Returns the parent BRepBody, BRepFace, BRepLump, BRepShell, SculptBody, or SculptFace object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshManager\_var" is a variable referencing a MeshManager object. |

"meshManager\_var" is a variable referencing a MeshManager object. ```` ``` #include <Fusion/MeshData/MeshManager.h>  // Get the value of the property. Ptr<Base> propertyValue = meshManager_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |