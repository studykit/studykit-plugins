# ProgressDialog.minimumValue Property

Parent Object: [ProgressDialog](ProgressDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressDialog.h>

## Description

The minimum value of the progress bar. This is used along with the maximum value and the progress value to compute the current percentage complete. This is also the initial progress value when the progress bar is first displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressDialog\_var" is a variable referencing a ProgressDialog object. |

"progressDialog\_var" is a variable referencing a ProgressDialog object. ```` ``` #include <Core/UserInterface/ProgressDialog.h>  // Get the value of the property. integer propertyValue = progressDialog_var->minimumValue();  // Set the value of the property, where value_var is an integer. bool returnValue = progressDialog_var->minimumValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |