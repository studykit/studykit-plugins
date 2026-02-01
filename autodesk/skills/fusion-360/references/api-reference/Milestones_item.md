# Milestones.item Method

Parent Object: [Milestones](Milestones.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestones.h>

## Description

Returns the specified milestone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestones\_var" is a variable referencing a [Milestones](Milestones.htm) object.```` ``` returnValue = milestones_var.item(index) ``` ```` |

"milestones\_var" is a variable referencing a [Milestones](Milestones.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Milestone](Milestone.htm) | Returns the specified file or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the milestone to return. The first milestone in the list has an index of 0. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |