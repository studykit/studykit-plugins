# CommandEvent.name Property

Parent Object: [CommandEvent](CommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEvent\_var" is a variable referencing a CommandEvent object. |

"commandEvent\_var" is a variable referencing a CommandEvent object. ```` ``` #include <Core/UserInterface/CommandEvent.h>  // Get the value of the property. string propertyValue = commandEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |