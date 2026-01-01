# ArrangeOccurrenceResults.item Method

Parent Object: [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeOccurrenceResults.h>

## Description

Returns the specified Arrange occurrence using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeOccurrenceResults\_var" is a variable referencing an [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm) object.```` ``` returnValue = arrangeOccurrenceResults_var.item(index) ``` ```` |

"arrangeOccurrenceResults\_var" is a variable referencing an [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeOccurrenceResult](ArrangeOccurrenceResult.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |