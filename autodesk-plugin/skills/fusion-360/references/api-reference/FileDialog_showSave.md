# FileDialog.showSave Method

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Displays a modal save dialog, allowing the user to specify a file. The return value can be used to determine if the dialog was canceled without selecting a file. The Filename and Filenames properties can be used to get the selected files.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a [FileDialog](FileDialog.htm) object.```` ``` returnValue = fileDialog_var.showSave() ``` ```` |

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
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |