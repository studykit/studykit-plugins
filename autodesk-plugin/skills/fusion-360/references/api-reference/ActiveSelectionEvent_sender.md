# ActiveSelectionEvent.sender Property

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. |

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. ```` ``` #include <Core/UserInterface/ActiveSelectionEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = activeSelectionEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |