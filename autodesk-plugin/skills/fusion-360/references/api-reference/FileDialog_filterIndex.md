# FileDialog.filterIndex Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Gets or sets the index of the filter currently selected in the file dialog box. Use the FilterIndex property to set which filtering option is shown first to the user. You can also use the value of FilterIndex after showing the file dialog to perform special file operations depending upon the filter chosen. The first item in the filter list is index 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object. |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. integer propertyValue = fileDialog_var->filterIndex();  // Set the value of the property, where value_var is an integer. bool returnValue = fileDialog_var->filterIndex(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |