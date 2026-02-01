# NavigationEvent.sender Property

Parent Object: [NavigationEvent](NavigationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEvent\_var" is a variable referencing a NavigationEvent object. |

"navigationEvent\_var" is a variable referencing a NavigationEvent object. ```` ``` #include <Core/UserInterface/NavigationEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = navigationEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |