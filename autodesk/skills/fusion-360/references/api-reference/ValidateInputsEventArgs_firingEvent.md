# ValidateInputsEventArgs.firingEvent Property

Parent Object: [ValidateInputsEventArgs](ValidateInputsEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. |

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. ```` ``` #include <Core/UserInterface/ValidateInputsEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = validateInputsEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |