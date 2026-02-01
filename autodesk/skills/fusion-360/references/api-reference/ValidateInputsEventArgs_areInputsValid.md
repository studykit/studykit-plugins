# ValidateInputsEventArgs.areInputsValid Property

Parent Object: [ValidateInputsEventArgs](ValidateInputsEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

Used with AreInputsValid event to specify if the all of the inputs for the command are valid or not. If you set this to false, indicating they are not valid, the OK button for the dialog is disabled forcing the user to correct the inputs before continuing. If you set this to true the OK button will be enabled, as long as the inputs satisfy their own requirements. For example, if a SelectionCommandInput is defined to have at minimum number of entities selected, that requirement must be met, or if a ValueCommandInput has an invalid value specified, the OK button will still be disabled.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. |

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. ```` ``` #include <Core/UserInterface/ValidateInputsEventArgs.h>  // Get the value of the property. boolean propertyValue = validateInputsEventArgs_var->areInputsValid();  // Set the value of the property, where value_var is a boolean. bool returnValue = validateInputsEventArgs_var->areInputsValid(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |