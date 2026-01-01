# FolderDialog.folder Property

Parent Object: [FolderDialog](FolderDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FolderDialog.h>

## Description

Gets the folder selected by the user in the dialog. This property is used after the ShowDialog method has been called to retrieve the folder specified by the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"folderDialog\_var" is a variable referencing a FolderDialog object. |

"folderDialog\_var" is a variable referencing a FolderDialog object. ```` ``` #include <Core/UserInterface/FolderDialog.h>  // Get the value of the property. string propertyValue = folderDialog_var->folder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

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