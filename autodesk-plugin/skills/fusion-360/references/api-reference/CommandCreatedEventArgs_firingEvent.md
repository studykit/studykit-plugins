# CommandCreatedEventArgs.firingEvent Property

Parent Object: [CommandCreatedEventArgs](CommandCreatedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object. |

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object. ```` ``` #include <Core/UserInterface/CommandCreatedEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = commandCreatedEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |