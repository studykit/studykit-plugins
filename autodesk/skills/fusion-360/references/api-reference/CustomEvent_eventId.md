# CustomEvent.eventId Property

Parent Object: [CustomEvent](CustomEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEvent.h>

## Description

Returns the id that was assigned to this event when it was registered. Each custom event has it's own unique id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEvent\_var" is a variable referencing a CustomEvent object. |

"customEvent\_var" is a variable referencing a CustomEvent object. ```` ``` #include <Core/Application/CustomEvent.h>  // Get the value of the property. string propertyValue = customEvent_var->eventId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |