# MachineAxisConfigurations.itemById Method

Parent Object: [MachineAxisConfigurations](MachineAxisConfigurations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfigurations.h>

## Description

Get the configuration with the given ID

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAxisConfigurations\_var" is a variable referencing a [MachineAxisConfigurations](MachineAxisConfigurations.htm) object.```` ``` returnValue = machineAxisConfigurations_var.itemById(id) ``` ```` |

"machineAxisConfigurations\_var" is a variable referencing a [MachineAxisConfigurations](MachineAxisConfigurations.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineAxisConfiguration](MachineAxisConfiguration.htm) | Return the MachineAxisConfiguration with the given ID, or null if the given ID does not match any configuration in the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID for the configuration to get. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |