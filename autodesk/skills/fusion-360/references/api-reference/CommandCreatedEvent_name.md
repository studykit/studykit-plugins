# CommandCreatedEvent.name Property

Parent Object: [CommandCreatedEvent](CommandCreatedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object. |

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object. ```` ``` #include <Core/UserInterface/CommandCreatedEvent.h>  // Get the value of the property. string propertyValue = commandCreatedEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |