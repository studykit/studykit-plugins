# DataFile.createMilestone Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Makes the version this DataFile represents a milestone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.createMilestone(milestoneName) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Milestone](Milestone.htm) | Returns the created Milestone object or null in the case of failure. One case of failure is if a milestone already exists for this version. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| milestoneName | string | The name of the milestone as seen in the data panel and Fusion web client. If an empty string is provided, a default name will be used. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |