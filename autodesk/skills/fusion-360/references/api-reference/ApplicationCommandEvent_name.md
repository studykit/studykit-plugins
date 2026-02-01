# ApplicationCommandEvent.name Property

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. |

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. ```` ``` #include <Core/UserInterface/ApplicationCommandEvent.h>  // Get the value of the property. string propertyValue = applicationCommandEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |