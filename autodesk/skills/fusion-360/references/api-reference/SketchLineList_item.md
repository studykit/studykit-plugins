# SketchLineList.item Method

Parent Object: [SketchLineList](SketchLineList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLineList.h>

## Description

Function that returns the specified sketch line using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLineList\_var" is a variable referencing a [SketchLineList](SketchLineList.htm) object.```` ``` returnValue = sketchLineList_var.item(index) ``` ```` |

"sketchLineList\_var" is a variable referencing a [SketchLineList](SketchLineList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLine](SketchLine.htm) | Returns the specified item or null if an invalid index was specified. |

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