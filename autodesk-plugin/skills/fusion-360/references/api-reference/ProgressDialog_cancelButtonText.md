# ProgressDialog.cancelButtonText Property

Parent Object: [ProgressDialog](ProgressDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressDialog.h>

## Description

Sets the text label on the Cancel button. The default text label is "Cancel".

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressDialog\_var" is a variable referencing a ProgressDialog object. |

"progressDialog\_var" is a variable referencing a ProgressDialog object. ```` ``` #include <Core/UserInterface/ProgressDialog.h>  // Get the value of the property. string propertyValue = progressDialog_var->cancelButtonText();  // Set the value of the property, where value_var is a string. bool returnValue = progressDialog_var->cancelButtonText(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Progress Dialog API Sample](ProgressDialogSample_Sample.htm) | Demonstrates how to use progress dialog |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |