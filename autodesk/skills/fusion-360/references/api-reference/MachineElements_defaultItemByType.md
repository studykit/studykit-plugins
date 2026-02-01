# MachineElements.defaultItemByType Method

Parent Object: [MachineElements](MachineElements.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElements.h>

## Description

Returns the default item of the given type. In most cases this will be the element with an element ID of "default".

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object.```` ``` returnValue = machineElements_var.defaultItemByType(typeId) ``` ```` |

"machineElements\_var" is a variable referencing a [MachineElements](MachineElements.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineElement](MachineElement.htm) | Returns the specified Element or null if no matching type ID is found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| typeId | string | Element typeId to get the default for. See staticTypeId for the desired element type. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |