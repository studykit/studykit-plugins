# MarkingMenuEvent.sender Property

Parent Object: [MarkingMenuEvent](MarkingMenuEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object. |

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object. ```` ``` #include <Core/UserInterface/MarkingMenuEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = markingMenuEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |