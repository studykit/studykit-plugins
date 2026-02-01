# ArrangeSelections.removeByObject Method

Parent Object: [ArrangeSelections](ArrangeSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelections.h>

## Description

Function that removes the specified arrange selection object from the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelections\_var" is a variable referencing an [ArrangeSelections](ArrangeSelections.htm) object.```` ``` returnValue = arrangeSelections_var.removeByObject(selection) ``` ```` |

"arrangeSelections\_var" is a variable referencing an [ArrangeSelections](ArrangeSelections.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selection | [ArrangeSelection](ArrangeSelection.htm) | The item within the collection to remove. Throws an exception if the arrange selection is not part of the given selection. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |