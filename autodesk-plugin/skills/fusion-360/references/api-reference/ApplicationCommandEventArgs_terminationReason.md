# ApplicationCommandEventArgs.terminationReason Property

Parent Object: [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

Returns the reason the command is being terminated. This property should be ignored for all events besides the commandTerminated event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. |

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. ```` ``` #include <Core/UserInterface/ApplicationCommandEventArgs.h>  // Get the value of the property. CommandTerminationReason propertyValue = applicationCommandEventArgs_var->terminationReason(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandTerminationReason](CommandTerminationReason.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |