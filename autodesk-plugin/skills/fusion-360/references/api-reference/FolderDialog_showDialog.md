# FolderDialog.showDialog Method

Parent Object: [FolderDialog](FolderDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FolderDialog.h>

## Description

Displays a modal dialog allowing the user to select a folder. The return value can be used to determine if the dialog was canceled without selecting a folder. the folder property can be used to get the selected folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"folderDialog\_var" is a variable referencing a [FolderDialog](FolderDialog.htm) object.```` ``` returnValue = folderDialog_var.showDialog() ``` ```` |

"folderDialog\_var" is a variable referencing a [FolderDialog](FolderDialog.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DialogResults](DialogResults.htm) | Returns an enum value indicating which button was clicked on the dialog. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [File Dialog Sample](FileDialogSample_Sample.htm) | Demonstrating how to pop up a file dialog and a folder dialog. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |