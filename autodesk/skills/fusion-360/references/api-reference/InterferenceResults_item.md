# InterferenceResults.item Method

Parent Object: [InterferenceResults](InterferenceResults.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResults.h>

## Description

Function that returns the specified interference result using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceResults\_var" is a variable referencing an [InterferenceResults](InterferenceResults.htm) object.```` ``` returnValue = interferenceResults_var.item(index) ``` ```` |

"interferenceResults\_var" is a variable referencing an [InterferenceResults](InterferenceResults.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [InterferenceResult](InterferenceResult.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |