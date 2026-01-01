# CommandEventArgs.terminationReason Property

Parent Object: [CommandEventArgs](CommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

Gets the termination reason of the command. It's only valid on the destroy event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. |

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. ```` ``` #include <Core/UserInterface/CommandEventArgs.h>  // Get the value of the property. CommandTerminationReason propertyValue = commandEventArgs_var->terminationReason(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandTerminationReason](CommandTerminationReason.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |