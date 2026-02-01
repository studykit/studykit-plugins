# CloudFileDialog.showOpen Method

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Displays a modal open dialog, allowing the user to select one or more files. The return value can be used to determine if the dialog was canceled without selecting a file. The dataFile and dataFiles properties can be used to get the selected files.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a [CloudFileDialog](CloudFileDialog.htm) object.```` ``` returnValue = cloudFileDialog_var.showOpen() ``` ```` |

"cloudFileDialog\_var" is a variable referencing a [CloudFileDialog](CloudFileDialog.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DialogResults](DialogResults.htm) | Returns an enum value indicating which button was clicked on the dialog. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |