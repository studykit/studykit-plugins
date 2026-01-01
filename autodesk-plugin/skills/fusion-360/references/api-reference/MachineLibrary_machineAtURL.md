# MachineLibrary.machineAtURL Method

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Get a specific machine by the given URL. Returns null, if the URL does not exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.```` ``` returnValue = machineLibrary_var.machineAtURL(url) ``` ```` |

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Machine](Machine.htm) | Returns the machine for a valid URL, returns null otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the machine to be loaded. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |