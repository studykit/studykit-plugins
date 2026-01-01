# FileDialog.filter Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Gets or sets the current file name filter string, which determines the choices that appear in the "Save as file type" or "Files of type" box in the dialog box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object.  ```` ``` # Get the value of the property. propertyValue = fileDialog_var.filter  # Set the value of the property. fileDialog_var.filter = propertyValue ``` ```` |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. string propertyValue = fileDialog_var->filter();  // Set the value of the property, where value_var is a string. bool returnValue = fileDialog_var->filter(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

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