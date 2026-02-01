# ProgressBar.message Property

Parent Object: [ProgressBar](ProgressBar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressBar.h>

## Description

Gets and sets the message to display in the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. %m is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressBar\_var" is a variable referencing a ProgressBar object.  ```` ``` # Get the value of the property. propertyValue = progressBar_var.message  # Set the value of the property. progressBar_var.message = propertyValue ``` ```` |

"progressBar\_var" is a variable referencing a ProgressBar object. ```` ``` #include <Core/UserInterface/ProgressBar.h>  // Get the value of the property. string propertyValue = progressBar_var->message();  // Set the value of the property, where value_var is a string. bool returnValue = progressBar_var->message(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |