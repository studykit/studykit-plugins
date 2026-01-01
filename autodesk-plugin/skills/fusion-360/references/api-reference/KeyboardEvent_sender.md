# KeyboardEvent.sender Property

Parent Object: [KeyboardEvent](KeyboardEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEvent\_var" is a variable referencing a KeyboardEvent object. |

"keyboardEvent\_var" is a variable referencing a KeyboardEvent object. ```` ``` #include <Core/UserInterface/KeyboardEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = keyboardEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |