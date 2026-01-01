# BRepFaces.item Method

Parent Object: [BRepFaces](BRepFaces.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaces.h>

## Description

Function that returns the specified face using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaces\_var" is a variable referencing a [BRepFaces](BRepFaces.htm) object.```` ``` returnValue = bRepFaces_var.item(index) ``` ```` |

"bRepFaces\_var" is a variable referencing a [BRepFaces](BRepFaces.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepFace](BRepFace.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |