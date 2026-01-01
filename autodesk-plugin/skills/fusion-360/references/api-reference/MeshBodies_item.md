# MeshBodies.item Method

Parent Object: [MeshBodies](MeshBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodies.h>

## Description

Provides access to a mesh body within the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodies\_var" is a variable referencing a [MeshBodies](MeshBodies.htm) object.```` ``` returnValue = meshBodies_var.item(index) ``` ```` |

"meshBodies\_var" is a variable referencing a [MeshBodies](MeshBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshBody](MeshBody.htm) | Returns the specified mesh body or null in the case of a invalid index. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the mesh body to return, where an index of 0 is the first mesh body in the collection. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |