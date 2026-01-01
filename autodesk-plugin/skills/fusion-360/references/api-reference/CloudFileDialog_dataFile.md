# CloudFileDialog.dataFile Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets the DataFile selected by the user in the dialog. This property is used after the ShowOpen method has been called to retrieve the filename specified by the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object.  ```` ``` # Get the value of the property. propertyValue = cloudFileDialog_var.dataFile ``` ```` |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. Ptr<DataFile> propertyValue = cloudFileDialog_var->dataFile(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |