# SketchFittedSplines.item Method

Parent Object: [SketchFittedSplines](SketchFittedSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSplines.h>

## Description

Function that returns the specified sketch fitted spline using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSplines\_var" is a variable referencing a [SketchFittedSplines](SketchFittedSplines.htm) object.```` ``` returnValue = sketchFittedSplines_var.item(index) ``` ```` |

"sketchFittedSplines\_var" is a variable referencing a [SketchFittedSplines](SketchFittedSplines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchFittedSpline](SketchFittedSpline.htm) | Returns the specified item or null if an invalid index was specified. |

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