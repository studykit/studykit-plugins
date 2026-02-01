# SketchDimensionList.item Method

Parent Object: [SketchDimensionList](SketchDimensionList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensionList.h>

## Description

Function that returns the specified sketch dimension using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensionList\_var" is a variable referencing a [SketchDimensionList](SketchDimensionList.htm) object.```` ``` returnValue = sketchDimensionList_var.item(index) ``` ```` |

"sketchDimensionList\_var" is a variable referencing a [SketchDimensionList](SketchDimensionList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchDimension](SketchDimension.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |