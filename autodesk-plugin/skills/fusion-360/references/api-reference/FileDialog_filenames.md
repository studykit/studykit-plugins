# FileDialog.filenames Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Gets the filenames specified by the user in the dialog. This property is used after the ShowOpen or ShowSave methods have been called to retrieve the filenames specified by the user. Each file name includes both the file path and the extension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object.  ```` ``` # Get the value of the property. propertyValue = fileDialog_var.filenames ``` ```` |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. std::vector<string> propertyValue = fileDialog_var->filenames(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

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