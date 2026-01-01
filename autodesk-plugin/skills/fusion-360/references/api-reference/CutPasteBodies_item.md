# CutPasteBodies.item Method

Parent Object: [CutPasteBodies](CutPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBodies.h>

## Description

Function that returns the specified Cut/Paste Body feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object.```` ``` returnValue = cutPasteBodies_var.item(index) ``` ```` |

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CutPasteBody](CutPasteBody.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Cut Paste Bodies API Sample](CutPasteBodiesSample_Sample.htm) | Demonstrates how to use Cut Paste Bodies related API. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |