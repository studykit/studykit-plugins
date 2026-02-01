# BRepLoops.item Method

Parent Object: [BRepLoops](BRepLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoops.h>

## Description

Function that returns the specified loop using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoops\_var" is a variable referencing a [BRepLoops](BRepLoops.htm) object.```` ``` returnValue = bRepLoops_var.item(index) ``` ```` |

"bRepLoops\_var" is a variable referencing a [BRepLoops](BRepLoops.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLoop](BRepLoop.htm) | Returns the specified item or null if an invalid index was specified. |

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