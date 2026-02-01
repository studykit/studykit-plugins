# CloudFileDialog.filter Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets or sets the current file type filter. This controls the types of files displayed in the dialog. The filter consists of file extensions separated by a semi-colon. The string below is an example of the filter used by Fusion for the Open command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object.  ```` ``` # Get the value of the property. propertyValue = cloudFileDialog_var.filter  # Set the value of the property. cloudFileDialog_var.filter = propertyValue ``` ```` |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. string propertyValue = cloudFileDialog_var->filter();  // Set the value of the property, where value_var is a string. bool returnValue = cloudFileDialog_var->filter(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |