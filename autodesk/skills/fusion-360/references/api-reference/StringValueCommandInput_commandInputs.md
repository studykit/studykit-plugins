# StringValueCommandInput.commandInputs Property

Parent Object: [StringValueCommandInput](StringValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/StringValueCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. |

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. ```` ``` #include <Core/UserInterface/StringValueCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = stringValueCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |