# SketchConicCurves.item Method

Parent Object: [SketchConicCurves](SketchConicCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurves.h>

## Description

Function that returns the specified conic curve using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurves\_var" is a variable referencing a [SketchConicCurves](SketchConicCurves.htm) object.```` ``` returnValue = sketchConicCurves_var.item(index) ``` ```` |

"sketchConicCurves\_var" is a variable referencing a [SketchConicCurves](SketchConicCurves.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchConicCurve](SketchConicCurve.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |