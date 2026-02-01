# CloudFileDialog.isMultiSelectEnabled Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Gets or sets a value indicating whether the dialog allows multiple files to be selected. This defaults to False when a new CloudFileDialog is created. It is only used when using the showOpen method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. boolean propertyValue = cloudFileDialog_var->isMultiSelectEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = cloudFileDialog_var->isMultiSelectEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |