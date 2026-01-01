# PrintSetting.syncWithMachine Method

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Synchronizes the print setting with the given machine, making extruder parameter options dependent on the available extruders in the machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object.```` ``` returnValue = printSetting_var.syncWithMachine(machine) ``` ```` |

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| machine | [Machine](Machine.htm) |  |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |