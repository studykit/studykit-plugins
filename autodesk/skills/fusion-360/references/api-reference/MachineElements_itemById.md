# MachineElements.itemById Method

Parent Object: [MachineElements](MachineElements.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElements.h>

## Description

Gets an element of a specific type by ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object.```` ``` returnValue = machineElements_var.itemById(typeId, elementId) ``` ```` |

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineElement](MachineElement.htm) | Returns an element of the desired type with the specified ID or null in the case where no match is found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| typeId | string | Element typeId to filter. See staticTypeId for the desired element type. |
| elementId | string | Element ID to select. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |