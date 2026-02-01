# MachineAvoidGroups.sync Method

Parent Object: [MachineAvoidGroups](MachineAvoidGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidGroups.h>

## Description

Function that synchronizes the selections and properties of the default groups from the current operation. This is needed when there are changes made to parameters that drive the default groups (e.g. Setup model or fixture selection changes to be reflected in the MachineAvoidGroups object on the API side). WARNING: This function must not be called before applyMachineAvoidGroups, because temporary group settings and selections will not have been stored in the operation object and will be overwritten.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object.```` ``` returnValue = machineAvoidGroups_var.sync() ``` ```` |

"machineAvoidGroups\_var" is a variable referencing a [MachineAvoidGroups](MachineAvoidGroups.htm) object. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |