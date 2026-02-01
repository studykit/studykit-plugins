# Milestones.itemByName Method

Parent Object: [Milestones](Milestones.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestones.h>

## Description

Returns the milestone specified using its name..

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestones\_var" is a variable referencing a [Milestones](Milestones.htm) object.```` ``` returnValue = milestones_var.itemByName(name) ``` ```` |

"milestones\_var" is a variable referencing a [Milestones](Milestones.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Milestone](Milestone.htm) | Returns the Milestone object or null if a milestone with the specified name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the milestone to return. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |