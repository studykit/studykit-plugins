# SketchPointList.item Method

Parent Object: [SketchPointList](SketchPointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPointList.h>

## Description

Function that returns the specified sketch point using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPointList\_var" is a variable referencing a [SketchPointList](SketchPointList.htm) object.```` ``` returnValue = sketchPointList_var.item(index) ``` ```` |

"sketchPointList\_var" is a variable referencing a [SketchPointList](SketchPointList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchPoint](SketchPoint.htm) | Returns the specified item or null if an invalid index was specified. |

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