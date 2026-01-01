# SketchTexts.item Method

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

Function that returns the specified sketch text using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object.```` ``` returnValue = sketchTexts_var.item(index) ``` ```` |

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchText](SketchText.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |