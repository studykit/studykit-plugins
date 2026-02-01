# Event.name Property

Parent Object: [Event](Event.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Event.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"event\_var" is a variable referencing an Event object. |

"event\_var" is a variable referencing an Event object. ```` ``` #include <Core/Application/Event.h>  // Get the value of the property. string propertyValue = event_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |