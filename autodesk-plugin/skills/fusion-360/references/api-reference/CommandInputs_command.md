# CommandInputs.command Property

Parent Object: [CommandInputs](CommandInputs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInputs.h>

## Description

Gets the parent Command object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInputs\_var" is a variable referencing a CommandInputs object. |

"commandInputs\_var" is a variable referencing a CommandInputs object. ```` ``` #include <Core/UserInterface/CommandInputs.h>  // Get the value of the property. Ptr<Command> propertyValue = commandInputs_var->command(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |