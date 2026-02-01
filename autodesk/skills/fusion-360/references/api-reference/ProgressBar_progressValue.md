# ProgressBar.progressValue Property

Parent Object: [ProgressBar](ProgressBar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressBar.h>

## Description

Gets and sets the current progress value. This value determines the progress based on this value relative to the minimum and maximum values specified when the progress bar was created. This will also update the values displayed in the message string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressBar\_var" is a variable referencing a ProgressBar object.  ```` ``` # Get the value of the property. propertyValue = progressBar_var.progressValue  # Set the value of the property. progressBar_var.progressValue = propertyValue ``` ```` |

"progressBar\_var" is a variable referencing a ProgressBar object. ```` ``` #include <Core/UserInterface/ProgressBar.h>  // Get the value of the property. integer propertyValue = progressBar_var->progressValue();  // Set the value of the property, where value_var is an integer. bool returnValue = progressBar_var->progressValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |