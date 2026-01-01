# DirectionCommandInput.commandInputs Property

Parent Object: [DirectionCommandInput](DirectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DirectionCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. |

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. ```` ``` #include <Core/UserInterface/DirectionCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = directionCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |