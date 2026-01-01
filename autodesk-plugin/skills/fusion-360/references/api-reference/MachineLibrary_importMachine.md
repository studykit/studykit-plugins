# MachineLibrary.importMachine Method

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Import a given machine at a specific location. The machine will be stored in the library. Throws an error, if the given URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.```` ``` returnValue = machineLibrary_var.importMachine(machine, destinationUrl, machineName) ``` ```` |

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL of the newly imported machine, or null if the import failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| machine | [Machine](Machine.htm) | The machine that should be imported. |
| destinationUrl | [URL](URL.htm) | The URL to the folder where to save the machine. |
| machineName | string | The name of the machine that should be created due to the import. The name can be extended if the asset already exists at given location to ensure a unique name. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |