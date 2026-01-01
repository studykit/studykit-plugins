# CurveSelections.item Method

Parent Object: [CurveSelections](CurveSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelections.h>

## Description

Function that returns the specified curve selection object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object.```` ``` returnValue = curveSelections_var.item(index) ``` ```` |

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurveSelection](CurveSelection.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |