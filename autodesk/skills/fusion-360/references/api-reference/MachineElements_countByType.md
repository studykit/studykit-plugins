# MachineElements.countByType Method

Parent Object: [MachineElements](MachineElements.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElements.h>

## Description

Number of elements of specified type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object.```` ``` returnValue = machineElements_var.countByType(typeId) ``` ```` |

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| uinteger | Returns the number of elements of the requested type. Returns zero if no elements match the specified type ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| typeId | string | Element typeId to filter. See staticTypeId for the desired element type. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |