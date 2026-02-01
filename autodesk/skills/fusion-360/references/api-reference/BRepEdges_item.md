# BRepEdges.item Method

Parent Object: [BRepEdges](BRepEdges.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdges.h>

## Description

Function that returns the specified edge using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdges\_var" is a variable referencing a [BRepEdges](BRepEdges.htm) object.```` ``` returnValue = bRepEdges_var.item(index) ``` ```` |

"bRepEdges\_var" is a variable referencing a [BRepEdges](BRepEdges.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepEdge](BRepEdge.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extendFeatures.add](extendFeatures_add_Sample.htm) | Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |