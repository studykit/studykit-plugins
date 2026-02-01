# InputChangedEvent.sender Property

Parent Object: [InputChangedEvent](InputChangedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object. |

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object. ```` ``` #include <Core/UserInterface/InputChangedEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = inputChangedEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |