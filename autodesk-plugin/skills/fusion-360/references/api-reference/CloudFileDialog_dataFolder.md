# CloudFileDialog.dataFolder Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets or sets the initial DataFolder displayed in the dialog. The DataFolder should be in current project. If null, this defaults to the DataFolder that is currently active in the Data Panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object.  ```` ``` # Get the value of the property. propertyValue = cloudFileDialog_var.dataFolder  # Set the value of the property. cloudFileDialog_var.dataFolder = propertyValue ``` ```` |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = cloudFileDialog_var->dataFolder();  // Set the value of the property, where value_var is a DataFolder. bool returnValue = cloudFileDialog_var->dataFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |