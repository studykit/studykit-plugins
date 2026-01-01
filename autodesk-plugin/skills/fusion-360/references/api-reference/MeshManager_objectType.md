# MeshManager.objectType Property

Parent Object: [MeshManager](MeshManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshManager\_var" is a variable referencing a MeshManager object.  ```` ``` # Get the value of the property. propertyValue = meshManager_var.objectType ``` ```` |

"meshManager\_var" is a variable referencing a MeshManager object. ```` ``` #include <Fusion/MeshData/MeshManager.h>  // Get the value of the property. string propertyValue = meshManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |