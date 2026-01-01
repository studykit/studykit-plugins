# CommandControl.commandDefinition Property

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

Gets the command definition associated with this button. The command definition defines all of the resource information used to display this button and receives the event when the button is clicked.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a CommandControl object. |

"commandControl\_var" is a variable referencing a CommandControl object. ```` ``` #include <Core/UserInterface/CommandControl.h>  // Get the value of the property. Ptr<CommandDefinition> propertyValue = commandControl_var->commandDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandDefinition](CommandDefinition.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |