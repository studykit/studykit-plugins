# SketchPoints.item Method

Parent Object: [SketchPoints](SketchPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoints.h>

## Description

Function that returns the specified sketch using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoints\_var" is a variable referencing a [SketchPoints](SketchPoints.htm) object.```` ``` returnValue = sketchPoints_var.item(index) ``` ```` |

"sketchPoints\_var" is a variable referencing a [SketchPoints](SketchPoints.htm) object. |

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