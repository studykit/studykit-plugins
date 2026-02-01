# CurveSelections.removeByObject Method

Parent Object: [CurveSelections](CurveSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelections.h>

## Description

Function that removes the specified curve selection object from the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object.```` ``` returnValue = curveSelections_var.removeByObject(selection) ``` ```` |

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selection | [CurveSelection](CurveSelection.htm) | The item within the collection to remove. Throws an exception if the curve selection is not part of the given selection. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |