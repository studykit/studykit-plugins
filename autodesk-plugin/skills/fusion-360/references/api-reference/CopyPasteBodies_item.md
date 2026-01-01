# CopyPasteBodies.item Method

Parent Object: [CopyPasteBodies](CopyPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBodies.h>

## Description

Function that returns the specified Copy/Paste Body feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object.```` ``` returnValue = copyPasteBodies_var.item(index) ``` ```` |

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CopyPasteBody](CopyPasteBody.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copy Paste Bodies API Sample](CopyPasteBodiesSample_Sample.htm) | Demonstrates how to use Copy Paste Bodies related API. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |