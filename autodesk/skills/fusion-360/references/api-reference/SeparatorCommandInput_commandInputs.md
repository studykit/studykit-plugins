# SeparatorCommandInput.commandInputs Property

Parent Object: [SeparatorCommandInput](SeparatorCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. |

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. ```` ``` #include <Core/UserInterface/SeparatorCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = separatorCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |