# SketchEntityList.item Method

Parent Object: [SketchEntityList](SketchEntityList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntityList.h>

## Description

Function that returns the specified sketch entity using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntityList\_var" is a variable referencing a [SketchEntityList](SketchEntityList.htm) object.```` ``` returnValue = sketchEntityList_var.item(index) ``` ```` |

"sketchEntityList\_var" is a variable referencing a [SketchEntityList](SketchEntityList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEntity](SketchEntity.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |