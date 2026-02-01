# ValidateInputsEventArgs.inputs Property

Parent Object: [ValidateInputsEventArgs](ValidateInputsEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

Returns the collection of command inputs that are associated with the command this event is being fired for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. |

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. ```` ``` #include <Core/UserInterface/ValidateInputsEventArgs.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = validateInputsEventArgs_var->inputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |