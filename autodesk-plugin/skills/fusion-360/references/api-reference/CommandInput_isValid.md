# CommandInput.isValid Property

Parent Object: [CommandInput](CommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInput\_var" is a variable referencing a CommandInput object. |

"commandInput\_var" is a variable referencing a CommandInput object. ```` ``` #include <Core/UserInterface/CommandInput.h>  // Get the value of the property. boolean propertyValue = commandInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |