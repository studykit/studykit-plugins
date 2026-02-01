# ValidateInputsEvent.isValid Property

Parent Object: [ValidateInputsEvent](ValidateInputsEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEvent\_var" is a variable referencing a ValidateInputsEvent object. |

"validateInputsEvent\_var" is a variable referencing a ValidateInputsEvent object. ```` ``` #include <Core/UserInterface/ValidateInputsEvent.h>  // Get the value of the property. boolean propertyValue = validateInputsEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |