# ProgressDialog.message Property

Parent Object: [ProgressDialog](ProgressDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressDialog.h>

## Description

Gets and sets the message to display along with the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. %m is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1. Specify an empty string ("") for no message to appear along with the progress panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressDialog\_var" is a variable referencing a ProgressDialog object. |

"progressDialog\_var" is a variable referencing a ProgressDialog object. ```` ``` #include <Core/UserInterface/ProgressDialog.h>  // Get the value of the property. string propertyValue = progressDialog_var->message();  // Set the value of the property, where value_var is a string. bool returnValue = progressDialog_var->message(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |