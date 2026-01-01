# ProgressDialog.isCancelButtonShown Property

Parent Object: [ProgressDialog](ProgressDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressDialog.h>

## Description

Gets and sets if the cancel button is included in the dialog. This is false by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressDialog\_var" is a variable referencing a ProgressDialog object. |

"progressDialog\_var" is a variable referencing a ProgressDialog object. ```` ``` #include <Core/UserInterface/ProgressDialog.h>  // Get the value of the property. boolean propertyValue = progressDialog_var->isCancelButtonShown();  // Set the value of the property, where value_var is a boolean. bool returnValue = progressDialog_var->isCancelButtonShown(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Progress Dialog API Sample](ProgressDialogSample_Sample.htm) | Demonstrates how to use progress dialog |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |