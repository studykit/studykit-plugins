# CommandInput.id Property

Parent Object: [CommandInput](CommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInput.h>

## Description

Gets the unique identifier for this input in the command's CommandInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInput\_var" is a variable referencing a CommandInput object. |

"commandInput\_var" is a variable referencing a CommandInput object. ```` ``` #include <Core/UserInterface/CommandInput.h>  // Get the value of the property. string propertyValue = commandInput_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |