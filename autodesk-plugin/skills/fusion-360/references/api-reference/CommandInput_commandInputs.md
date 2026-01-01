# CommandInput.commandInputs Property

Parent Object: [CommandInput](CommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInput\_var" is a variable referencing a CommandInput object. |

"commandInput\_var" is a variable referencing a CommandInput object. ```` ``` #include <Core/UserInterface/CommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = commandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |