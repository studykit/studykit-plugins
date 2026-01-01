# MachineLibrary.childFolderURLs Method

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Get all library folders under given URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.```` ``` returnValue = machineLibrary_var.childFolderURLs(url) ``` ```` |

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm)[] | Returns list of folder URLs at given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the parent folder. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |