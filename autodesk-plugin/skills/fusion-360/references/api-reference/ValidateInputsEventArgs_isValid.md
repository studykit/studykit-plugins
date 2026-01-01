# ValidateInputsEventArgs.isValid Property

Parent Object: [ValidateInputsEventArgs](ValidateInputsEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. |

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. ```` ``` #include <Core/UserInterface/ValidateInputsEventArgs.h>  // Get the value of the property. boolean propertyValue = validateInputsEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |