# CloudFileDialog.dataFiles Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets the DataFiles specified by the user in the dialog. This property is used after the ShowOpen method has been called to retrieve the DataFiles specified by the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object.  ```` ``` # Get the value of the property. propertyValue = cloudFileDialog_var.dataFiles ``` ```` |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. std::vector<Ptr<DataFile>> propertyValue = cloudFileDialog_var->dataFiles(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [DataFile](DataFile.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |