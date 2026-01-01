# Scripts.itemByPath Method

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Function that returns the script that is located in the specified folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object.```` ``` returnValue = scripts_var.itemByPath(folderPath) ``` ```` |

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Script](Script.htm) | Returns the specified script or null if there isn't a script at the specified path. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| folderPath | string | The full path to the folder that contains the script. This does not include the name of the script, but only the path. For example "C:\Scripts\MyScript" is valid where "C:\Scripts\MyScripts\MyScript.py" is not. |

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |