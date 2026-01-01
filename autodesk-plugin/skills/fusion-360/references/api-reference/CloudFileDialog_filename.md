# CloudFileDialog.filename Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets and sets the filename when using the showSave method. If you set this value before using the showSave method, this will display the filename as the default in the dialog, but the user can change it. The default is an empty string, which indicates there is not an initial filename.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object.  ```` ``` # Get the value of the property. propertyValue = cloudFileDialog_var.filename  # Set the value of the property. cloudFileDialog_var.filename = propertyValue ``` ```` |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. string propertyValue = cloudFileDialog_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = cloudFileDialog_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |