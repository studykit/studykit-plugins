# SketchLines.item Method

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Function that returns the specified sketch line using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object.```` ``` returnValue = sketchLines_var.item(index) ``` ```` |

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object. |

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