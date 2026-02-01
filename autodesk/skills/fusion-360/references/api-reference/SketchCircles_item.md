# SketchCircles.item Method

Parent Object: [SketchCircles](SketchCircles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircles.h>

## Description

Function that returns the specified sketch circle using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircles\_var" is a variable referencing a [SketchCircles](SketchCircles.htm) object.```` ``` returnValue = sketchCircles_var.item(index) ``` ```` |

"sketchCircles\_var" is a variable referencing a [SketchCircles](SketchCircles.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchCircle](SketchCircle.htm) | Returns the specified item or null if an invalid index was specified. |

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