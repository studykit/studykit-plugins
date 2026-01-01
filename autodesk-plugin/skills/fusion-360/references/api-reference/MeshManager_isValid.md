# MeshManager.isValid Property

Parent Object: [MeshManager](MeshManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshManager\_var" is a variable referencing a MeshManager object. |

"meshManager\_var" is a variable referencing a MeshManager object. ```` ``` #include <Fusion/MeshData/MeshManager.h>  // Get the value of the property. boolean propertyValue = meshManager_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |