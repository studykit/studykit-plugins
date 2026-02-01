# MachineAvoidGroups.item Method

Parent Object: [MachineAvoidGroups](MachineAvoidGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidGroups.h>

## Description

Function that returns the specified machine/avoid group selection object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object.```` ``` returnValue = machineAvoidGroups_var.item(index) ``` ```` |

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineAvoidSelectionBase](MachineAvoidSelectionBase.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |