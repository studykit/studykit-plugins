# ApplicationCommandEventArgs.commandDefinition Property

Parent Object: [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

Returns the CommandDefinition object for the command the event is being fired for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. |

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. ```` ``` #include <Core/UserInterface/ApplicationCommandEventArgs.h>  // Get the value of the property. Ptr<CommandDefinition> propertyValue = applicationCommandEventArgs_var->commandDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandDefinition](CommandDefinition.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |