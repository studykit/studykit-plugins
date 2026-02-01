# ApplicationCommandEvent.sender Property

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. |

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. ```` ``` #include <Core/UserInterface/ApplicationCommandEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = applicationCommandEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |