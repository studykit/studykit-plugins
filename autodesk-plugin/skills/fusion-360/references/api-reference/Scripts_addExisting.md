# Scripts.addExisting Method

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Fusion looks in specific folders for scripts and add-ins, but you can manually add other scripts and add-ins to the list of known scripts and add-ins so they will be listed in the "Scripts and Add-ins" dialog. This method does that.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object.```` ``` returnValue = scripts_var.addExisting(scriptFolderPath) ``` ```` |

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Script](Script.htm) | Returns the Script object that represents the script or add-in just added. Returns null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| scriptFolderPath | string | The full path to the folder that contains the script or add-in. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |