# SketchArcs.item Method

Parent Object: [SketchArcs](SketchArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArcs.h>

## Description

Function that returns the specified sketch arc using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object.```` ``` returnValue = sketchArcs_var.item(index) ``` ```` |

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchArc](SketchArc.htm) | Returns the specified item or null if an invalid index was specified. |

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