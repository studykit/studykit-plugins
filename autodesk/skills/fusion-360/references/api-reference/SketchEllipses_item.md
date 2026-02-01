# SketchEllipses.item Method

Parent Object: [SketchEllipses](SketchEllipses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipses.h>

## Description

Function that returns the specified sketch ellipse using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipses\_var" is a variable referencing a [SketchEllipses](SketchEllipses.htm) object.```` ``` returnValue = sketchEllipses_var.item(index) ``` ```` |

"sketchEllipses\_var" is a variable referencing a [SketchEllipses](SketchEllipses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEllipse](SketchEllipse.htm) | Returns the specified item or null if an invalid index was specified. |

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