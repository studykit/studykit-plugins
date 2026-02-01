# SketchCurves.item Method

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Function that returns the specified sketch curve using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a [SketchCurves](SketchCurves.htm) object.```` ``` returnValue = sketchCurves_var.item(index) ``` ```` |

"sketchCurves\_var" is a variable referencing a [SketchCurves](SketchCurves.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchCurve](SketchCurve.htm) | Returns the specified item or null if an invalid index was specified. |

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