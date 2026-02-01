# MachineLibrary.deleteAsset Method

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Delete asset by URL from the library. Throw an error if given URL does not point to a valid asset or the URL is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.```` ``` returnValue = machineLibrary_var.deleteAsset(url) ``` ```` |

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if asset was deleted successfully, false otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the asset that should be removed. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |