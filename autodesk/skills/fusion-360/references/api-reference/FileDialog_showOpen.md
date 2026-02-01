# FileDialog.showOpen Method

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Displays a modal open dialog, allowing the user to select one or more files. The return value can be used to determine if the dialog was canceled without selecting a file. The Filename and Filenames properties can be used to get the selected files.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a [FileDialog](FileDialog.htm) object.```` ``` returnValue = fileDialog_var.showOpen() ``` ```` |

"fileDialog\_var" is a variable referencing a [FileDialog](FileDialog.htm) object. |

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

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |