# ProgressDialog.progressValue Property

Parent Object: [ProgressDialog](ProgressDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressDialog.h>

## Description

Gets and sets the current progress bar value. Progress is determined based on this value relative to the minimum and maximum values. This will update the values displayed in the message string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressDialog\_var" is a variable referencing a ProgressDialog object. |

"progressDialog\_var" is a variable referencing a ProgressDialog object. ```` ``` #include <Core/UserInterface/ProgressDialog.h>  // Get the value of the property. integer propertyValue = progressDialog_var->progressValue();  // Set the value of the property, where value_var is an integer. bool returnValue = progressDialog_var->progressValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

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