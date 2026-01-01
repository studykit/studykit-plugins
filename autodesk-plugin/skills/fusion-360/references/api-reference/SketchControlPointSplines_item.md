# SketchControlPointSplines.item Method

Parent Object: [SketchControlPointSplines](SketchControlPointSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSplines.h>

## Description

Function that returns the specified sketch control point spline using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSplines\_var" is a variable referencing a [SketchControlPointSplines](SketchControlPointSplines.htm) object.```` ``` returnValue = sketchControlPointSplines_var.item(index) ``` ```` |

"sketchControlPointSplines\_var" is a variable referencing a [SketchControlPointSplines](SketchControlPointSplines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchControlPointSpline](SketchControlPointSpline.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |