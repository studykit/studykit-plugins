# BRepCells.item Method

Parent Object: [BRepCells](BRepCells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCells.h>

## Description

Function that returns the specified BRepCell using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCells\_var" is a variable referencing a [BRepCells](BRepCells.htm) object.```` ``` returnValue = bRepCells_var.item(index) ``` ```` |

"bRepCells\_var" is a variable referencing a [BRepCells](BRepCells.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepCell](BRepCell.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |