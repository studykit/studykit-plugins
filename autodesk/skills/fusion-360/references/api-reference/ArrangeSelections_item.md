# ArrangeSelections.item Method

Parent Object: [ArrangeSelections](ArrangeSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelections.h>

## Description

Function that returns the specified arrange selection object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelections\_var" is a variable referencing an [ArrangeSelections](ArrangeSelections.htm) object.```` ``` returnValue = arrangeSelections_var.item(index) ``` ```` |

"arrangeSelections\_var" is a variable referencing an [ArrangeSelections](ArrangeSelections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeSelection](ArrangeSelection.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |