# CloudFileDialog.title Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets or sets the title displayed on the dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. string propertyValue = cloudFileDialog_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = cloudFileDialog_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |