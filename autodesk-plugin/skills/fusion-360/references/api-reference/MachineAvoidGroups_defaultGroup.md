# MachineAvoidGroups.defaultGroup Method

Parent Object: [MachineAvoidGroups](MachineAvoidGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidGroups.h>

## Description

Function that returns the specified machine/avoid default group selection object using the group type. Default groups contain surfaces that have a specific meaning within the toolpath operation, for example Model, Fixture, Drive etc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object.```` ``` returnValue = machineAvoidGroups_var.defaultGroup(type) ``` ```` |

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineAvoidSelectionBase](MachineAvoidSelectionBase.htm) | Returns the specified item or null if there isn't a group of the specified type |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| type | [DefaultGroupType](DefaultGroupType.htm) | The type of the default group within the collection to return. There can be only one default group of a given type |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |